# Anonymization Service — `AnonymizationServiceAPI`

**Port:** `5292`  
**Framework:** .NET 10 / ASP.NET Core Minimal API  
**Role:** PII anonymization and deanonymization gateway. Detects named entities in text using the GLiNER NER service, replaces them with reversible tokens, and stores the token-to-value mapping in Redis so the server can later deanonymize parameters.

---

## Purpose in the Architecture

The Anonymization Service sits between the MCP client and the MCP server:

1. The **client** sends raw user input to `/anonymize` before forwarding anything to the MCP server.
2. The service detects PII (names, locations, phone numbers, etc.) and replaces each with a stable token like `<PERSON_0001>` or `<LOCATION_0001>`.
3. The token-to-value mapping is persisted under a `contextId` in Redis.
4. The client passes the anonymized text and the `contextId` to `ask_antares`.
5. Inside `JobTools`, just before real data operations begin, the server calls `/deanonymize-known` to restore the original values — entirely server-side.

**Result:** The client never sees real names, phones, or addresses. The server sees them only long enough to process the request and write the report to a local file.

---

## REST Endpoints — `Program.cs`

### `GET /anonymize`

```
GET /anonymize?input=<text>
→ 200 AnonymizationResult
```

Detects PII in `input`, replaces entities with tokens, generates a new `contextId`, stores the mapping in Redis.

**Response shape:**

```json
{
  "text": "Trova i lavoratori più vicini a <LOCATION_0001> entro 15 km.",
  "contextId": "abc123",
  "knownFieldCount": 1
}
```

Used by the MCP client for the one-shot anonymization flow (UC-A/B/C).

### `POST /anonymize-into-context`

```
POST /anonymize-into-context
{ "text": "...", "contextId": "existing-id" }
→ 200 AnonymizeIntoContextResponse
```

Anonymizes text and **appends** the new token mappings into an **existing** context. Used when multiple prompts share the same session (e.g., a follow-up question that introduces a new name).

Returns:
```json
{ "text": "<anonymized text>" }
```

Returns `400` if `contextId` is empty.

### `POST /deanonymize-known`

```
POST /deanonymize-known
{ "text": "<PERSON_0001> vuole ferie", "contextId": "abc123" }
→ 200 DeanonymizeResponse
```

Replaces all tokens in `text` with the real values from the Redis context for `contextId`.

Returns:
```json
{ "text": "Giulia Conti vuole ferie" }
```

Returns `400` if `contextId` is empty, `404` if the context is not found in Redis.

---

## Services

### `GlinerTextAnonymizer` — `Services/GlinerTextAnonymizer.cs`

Implements `ITextAnonymizer`. Orchestrates the full anonymization pipeline.

**Dependencies:**
- `IHttpClientFactory` (named client `"GlinerAnalyzerClient"` → `http://localhost:5100`)
- `IAnonymizationContextStore` (Redis)
- `IOptions<GlinerOptions>` — configures `MinScore`, `Labels`, `BaseUrl`, `TimeoutSeconds`

**Pipeline:**

```
Analyze(text)
  → POST http://localhost:5100/analyze { text, labels, threshold, language: "it" }
  ← List<Entity> (start, end, label, score, text)

Anonymize(entities, originalText)
  → sort entities by position
  → for each entity: generate token (e.g. <PERSON_0001>)
  → replace in text (right-to-left to preserve offsets)
  → build contextId + token map
  → Store(contextId, tokenMap)
  ← AnonymizationResult { Text, ContextId, KnownFieldCount }

AnonymizeIntoContext(text, contextId)
  → Analyze + Anonymize as above
  → Append(contextId, newTokenMap)   ← merges into existing context
  ← anonymized text

Deanonymize(text, contextId)
  → Pop(contextId) from Redis
  → for each (token, realValue): text.Replace(token, realValue)
  ← restored text
```

**Token format:** `<LABEL_NNNN>` where:
- `LABEL` is the uppercase entity label (e.g., `PERSON`, `LOCATION`, `PHONE_NUMBER`)
- `NNNN` is a zero-padded 4-digit counter, per label, per context

Example tokens: `<PERSON_0001>`, `<LOCATION_0001>`, `<PERSON_0002>`

**GlinerOptions** (from `appsettings.json` under `"GLiNER"`):

```json
{
  "BaseUrl": "http://localhost:5100",
  "TimeoutSeconds": 30,
  "MinScore": 0.45,
  "Labels": ["person", "organization", "location", "address", "email", "phone number", "date", "time"]
}
```

---

### `RedisAnonymizationContextStore` — `Services/RedisAnonymizationContextStore.cs`

Implements `IAnonymizationContextStore`. Wraps `CachingFramework.Redis` for token-map persistence.

**Interface:**

```csharp
Task Store(string contextId, Dictionary<string, string> tokenMap);
Task<Dictionary<string, string>> Get(string contextId);
Task Append(string contextId, Dictionary<string, string> newTokens);
Task<Dictionary<string, string>> Pop(string contextId);
```

- `Store` — writes a new context. Overwrites if it already exists.
- `Get` — reads without removing. Throws `KeyNotFoundException` if not found.
- `Append` — merges new token entries into an existing context (used by `AnonymizeIntoContext`).
- `Pop` — reads and **deletes** the context (used by `Deanonymize` to ensure one-time use).

**Redis connection:** `localhost:55000` (hardcoded in `Program.cs` — move to config if needed).

**Storage key format:** `anon:context:{contextId}` (each key holds a serialized `Dictionary<string, string>`).

No TTL is currently set — contexts persist until `Pop` is called or Redis is restarted.

---

## Contracts — `Contracts/`

```csharp
// ITextAnonymizer.cs
interface ITextAnonymizer
{
    Task<IEnumerable<Entity>> Analyze(string text);
    Task<AnonymizationResult> Anonymize(IEnumerable<Entity> entities, string originalText);
    Task<string> AnonymizeIntoContext(string text, string contextId);
    Task<string> Deanonymize(string text, string contextId);
}

// IAnonymizationContextStore.cs
interface IAnonymizationContextStore
{
    Task Store(string contextId, Dictionary<string, string> tokenMap);
    Task<Dictionary<string, string>> Get(string contextId);
    Task Append(string contextId, Dictionary<string, string> newTokens);
    Task<Dictionary<string, string>> Pop(string contextId);
}
```

---

## OpenAPI / Swagger

In `Development` mode the service exposes:
- `GET /swagger` — Swagger UI
- `GET /swagger/api-docs.yaml` — OpenAPI YAML spec

The YAML spec at `Anonymization_Client/api-docs.yml` is used by NSwag to regenerate the C# client in both `Antares_AI_McpServer` and `Antares_AI_McpClient`.

To regenerate the client after an API change:
```bash
# From Antares_AI_McpServer:
nswag run Anonymization_Client/nswag.json

# From Antares_AI_McpClient:
nswag run Clients/nswag.json
```

---

## NuGet Dependencies

All packages are declared in `AnonymizationServiceAPI.csproj`. **`dotnet restore` runs automatically on `dotnet build` or `dotnet run`** — no manual install step is needed. ASP.NET Core itself and `System.Net.Http.Json` are part of the `Microsoft.NET.Sdk.Web` SDK and require no separate package reference.

| Package | Version | Purpose |
|---------|---------|---------|
| `NSwag.AspNetCore` | 14.6.3 | OpenAPI document generation + Swagger UI (`/swagger`) |
| `NSwag.Core.Yaml` | 14.6.3 | YAML serialization of the OpenAPI spec (required for `api-docs.yml` output) |
| `CachingFramework.Redis` | 17.1.0 | `IContext` / Redis client used by `RedisAnonymizationContextStore` |
