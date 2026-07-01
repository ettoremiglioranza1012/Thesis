# GLiNER Service — `GLiNERService`

**Port:** `5100`  
**Framework:** Python / FastAPI + Uvicorn  
**Role:** Named Entity Recognition (NER) microservice. Given a piece of text, it identifies spans that match a set of entity labels (person, location, phone number, etc.) and returns their positions and scores. The Anonymization Service calls this to decide which parts of a prompt to replace with tokens.

---

## Technology

- **GLiNER** — a zero-shot NER model that accepts arbitrary label sets at inference time (no fine-tuning needed per entity type). The default model is `urchade/gliner_multi-v2.1`, a multilingual model that works well with Italian text.
- **FastAPI** — async HTTP framework; the app is served by **Uvicorn**.
- Model weights are downloaded from HuggingFace on first startup and cached locally.

---

## Startup — `app.py`

```python
@app.on_event("startup")
def load_model() -> None:
    global _model
    _model = GLiNER.from_pretrained(MODEL_NAME)
```

The model is loaded once into a module-level global `_model`. Subsequent requests reuse the already-loaded model — no per-request loading. If the `gliner` package fails to import (e.g., missing dependency), the startup raises immediately with a descriptive error.

**Environment variables:**

| Variable | Default | Purpose |
|----------|---------|---------|
| `GLINER_MODEL` | `urchade/gliner_multi-v2.1` | HuggingFace model identifier |
| `GLINER_MIN_SPAN_LEN` | `3` | Minimum character length for a valid entity span |

---

## Endpoints

### `GET /health`

```json
{ "status": "ok", "model": "urchade/gliner_multi-v2.1", "loaded": true }
```

Returns `loaded: false` if the model is not yet initialized. Use this to check readiness before routing traffic.

### `POST /analyze`

```json
// Request
{
  "text": "Chiedi a Giulia Conti di andare al cantiere di Bergamo.",
  "labels": ["person", "location"],
  "threshold": 0.45,
  "language": "it"
}

// Response
{
  "entities": [
    { "start": 9,  "end": 21, "label": "person",   "score": 0.92, "text": "Giulia Conti" },
    { "start": 46, "end": 53, "label": "location",  "score": 0.87, "text": "Bergamo" }
  ]
}
```

**Request fields:**

| Field | Type | Default | Notes |
|-------|------|---------|-------|
| `text` | `str` | required | Input text to analyze |
| `labels` | `list[str]` | `DEFAULT_LABELS` | Entity types to look for |
| `threshold` | `float` | `0.45` | Minimum confidence score; clamped to `[0.0, 1.0]` |
| `language` | `str` | `"it"` | Language hint (informational; GLiNER is multilingual) |

**Default labels** (when `labels` is not provided):
```python
["person", "organization", "location", "address", "email", "phone number", "date", "time"]
```

**Response:** A list of `Entity` objects ordered by position (start offset ascending).

---

## Entity Filtering Pipeline

Raw predictions from GLiNER go through three stages before being returned:

### 1. Normalize — `_normalize_predictions()`

Validates and cleans each raw prediction dict:
- Checks that `start` and `end` are integers with `end > start`
- Checks that `label` is a non-empty string
- Checks that offsets are within the source text bounds
- Reconstructs `text` from `source_text[start:end]` if missing

Invalid predictions are silently dropped.

### 2. Filter low-quality entities — `_is_low_quality_entity()`

An entity is discarded if any of the following is true:
- `score < threshold` (default `0.45`, set by the caller)
- `len(text.strip()) < MIN_SPAN_LEN` (default `3` characters)
- The normalized text is an Italian stopword from the built-in blocklist

**Italian stopword blocklist** (partial, relevant examples):
```python
{"il", "lo", "la", "i", "gli", "le", "di", "a", "da", "in", "con", "su",
 "lista", "risolvi", "ritorna", "internamente", "lavoratori", "assegnati", "risultati"}
```

These are words that GLiNER sometimes misclassifies as entities in Italian operational prompts.

### 3. Deduplicate overlapping spans — `_dedupe_overlaps()`

When two entity predictions overlap (e.g., "Giulia" and "Giulia Conti"), the pipeline keeps the best one:
- Sort by `(score DESC, span_length DESC)` — prefer higher confidence and longer span
- Greedily select non-overlapping entities
- Re-sort the result by position ascending

---

## Error Handling

| Condition | HTTP status | Detail |
|-----------|------------|--------|
| Model not loaded | `503` | `"GLiNER model is not loaded"` |
| GLiNER prediction throws | `500` | `"GLiNER prediction failed: <exception>"` |
| Empty or whitespace input | `200` | Returns empty `entities: []` (no error) |

---

## Installation & Running

The service uses [`uv`](https://docs.astral.sh/uv/) for dependency management:

```bash
cd GLiNERService

# Install dependencies (first time)
uv sync

# Run
uv run uvicorn app:app --host 0.0.0.0 --port 5100
```

Dependencies are declared in `pyproject.toml` and mirrored in `requirements.txt`. `uv sync` (called by `uv run`) resolves and installs them automatically — no manual `pip install` needed.

| Package | Version | Purpose |
|---------|---------|---------|
| `gliner` | 0.2.16 | Zero-shot NER model — entity prediction via `GLiNER.from_pretrained()` and `predict_entities()` |
| `fastapi` | 0.115.12 | HTTP framework — provides the `/health` and `/analyze` endpoints |
| `uvicorn[standard]` | 0.34.0 | ASGI server that runs the FastAPI app |
| `huggingface-hub` | 0.27.1 | Model download and local caching from HuggingFace (`urchade/gliner_multi-v2.1`) |

> `pydantic` is **not** a direct dependency — it is pulled in transitively by FastAPI and used implicitly for request/response model validation (`BaseModel`).

On first run, GLiNER will download the `urchade/gliner_multi-v2.1` weights (~500 MB) from HuggingFace. Subsequent starts load from the local cache.

---

## Relationship with the Anonymization Service

The GLiNER Service is a **dumb NER oracle** — it only detects and scores spans. It has no knowledge of tokens, contexts, or Redis. All anonymization logic (token generation, context storage, deanonymization) lives in the `AnonymizationServiceAPI`.

Call flow:
```
AnonymizationServiceAPI
  → POST http://localhost:5100/analyze { text, labels, threshold }
  ← List<Entity> { start, end, label, score, text }
  → generate tokens, store in Redis
```

The Anonymization Service configures the `threshold` and `labels` it sends via its own `appsettings.json` (`GLiNER:MinScore`, `GLiNER:Labels`), so you can tune entity sensitivity without touching the GLiNER service itself.
