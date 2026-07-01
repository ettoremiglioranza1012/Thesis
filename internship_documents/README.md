# Antares AI — MCP Architecture

An AI-powered workforce management system built on the **Model Context Protocol (MCP)**. It combines a .NET 10 MCP server with a Python NER microservice to enable **privacy-first, Claude-routed workforce queries** — finding substitute workers, listing colleagues, and processing holiday requests — all without exposing personal data to the client.

---

## How It Works (at a glance)

The client anonymizes any PII in the user's prompt before sending it to the server. The MCP server uses **Claude as a semantic router** (`ask_antares`) to pick the right tool and execute it. All real personal data (names, phones, distances) is processed and logged server-side only. The client receives a single hardcoded confirmation string.

![Runtime Flow](Assets/final_runtime_flow.png)

---

## Project Structure

```
MCP_Architecture_.NET_CSharp/
│
├── run_services.sh                  # One-shot script: starts all 3 services
│
├── Antares_AI_McpServer/            # MCP Server — Claude router + Miorelli tools (port 5001)
│   ├── program.cs                   # DI setup, MCP registration
│   ├── appsettings.json             # API endpoints, Claude model params
│   ├── Tools/                       # MCP tool implementations (ask_antares, UC-A/B/C, ...)
│   ├── MiorelliClient/              # Miorelli service abstraction + mock data
│   └── Anonymization_Client/        # NSwag-generated client for the Anonymization API
│
├── AnonymizationServiceAPI/         # Anonymization microservice (port 5292)
│   ├── Program.cs                   # Minimal API: /anonymize, /anonymize-into-context, /deanonymize-known
│   ├── Services/                    # GLiNER-based anonymizer + Redis context store
│   └── Contracts/                   # ITextAnonymizer, IAnonymizationContextStore
│
├── Antares_AI_McpClient/            # Console client — runs UC-A, UC-B, UC-C scenarios
│   ├── Program.cs                   # MCP client bootstrap
│   └── App/AppRunner.cs             # Test scenarios (anonymize → ask_antares → print response)
│
├── GLiNERService/                   # Python FastAPI NER service (port 5100)
│   ├── app.py                       # POST /analyze — entity extraction via GLiNER
│   └── gliner_service.py            # CLI entry point
│
├── Assets/
│   └── final_runtime_flow.png       # Architecture diagram
│
└── Docs/                            # Detailed per-component documentation
    ├── mcp-server.md
    ├── anonymization-service.md
    ├── gliner-service.md
    ├── mcp-client.md
    └── miorelli-client.md
```

---

## Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| `.NET SDK` | 10.0+ | Build and run the two C# services |
| `uv` | any recent | Run the Python GLiNER service |
| `Redis` | 7+ | Context store for anonymization (port `55000`) |
| `nc` (netcat) | system | Port-readiness checks in `run_services.sh` |

---

## How to Run

### 0. Restore NuGet packages

`dotnet restore` is called automatically by `dotnet build` and `dotnet run`, so you do not need to run it manually. All package references are declared in the `.csproj` files and will be pulled from NuGet.org on first build. If you want to pre-fetch them explicitly:

```bash
dotnet restore
```

### 1. Set required secrets

The MCP Server needs three secrets. Set them with .NET user-secrets:

```bash
cd Antares_AI_McpServer
dotnet user-secrets init
dotnet user-secrets set "Anthropic:ApiKey"      "<your-claude-api-key>"
dotnet user-secrets set "ApiSettings:ApiKey"    "<antares-basic-auth-key>"
dotnet user-secrets set "ApiSettings:ApiSecret" "<antares-basic-auth-secret>"
```

### 2. Start Redis

Redis must be reachable at `localhost:55000`. If you use Docker:

```bash
docker run -d -p 55000:6379 redis:7
```

### 3. Start all services (recommended)

```bash
./run_services.sh
```

This starts all three services in order, waits for each port to be ready, and tails logs to `.run-logs/`. Press `Ctrl+C` to stop all.

| Service | Port | Log file |
|---------|------|---------|
| MCP Server | 5001 | `.run-logs/mcp-server.log` |
| Anonymization API | 5292 | `.run-logs/anonymization-api.log` |
| GLiNER NER | 5100 | `.run-logs/gliner.log` |

### 4. Run the client (separate terminal)

```bash
dotnet run --project Antares_AI_McpClient
```

This executes the three demo use cases (UC-A, UC-B, UC-C) in sequence and prints results to the console. Full reports with real data are saved to `Antares_AI_McpServer/bin/Debug/net10.0/logs/`.

### Manual startup (3 terminals)

```bash
# Terminal 1 — MCP Server
ASPNETCORE_URLS="http://localhost:5001" dotnet run --project Antares_AI_McpServer

# Terminal 2 — Anonymization API
ASPNETCORE_URLS="http://localhost:5292" dotnet run --project AnonymizationServiceAPI

# Terminal 3 — GLiNER
cd GLiNERService && uv run uvicorn app:app --host 0.0.0.0 --port 5100
```

---

## Use Cases

| ID | Name | Tool | Description |
|----|------|------|-------------|
| UC-A | Nearest workers to cantiere | `get_nearest_workers_to_cantiere` | Finds PULITO_DA workers for a cantiere, ranks by Haversine distance |
| UC-B | Colleagues of person | `get_colleagues_of_person` | Lists colleagues (shared cantiere) + top-5 nearest non-colleagues |
| UC-C | Holiday request | `report_holiday_request` | On a ferie ticket: lists absent colleagues + nearby substitute pool |

---

## Switching to Real Miorelli Data

Currently all Miorelli calls fall back to static mock data. When the real Miorelli tenant is provisioned, only one line in `program.cs` needs to change:

```csharp
// Before (mock):
builder.Services.AddScoped<IMiorelliService, MiorelliServiceStub>();

// After (real):
builder.Services.AddScoped<IMiorelliService, AntaresMiorelliClient>();
```

No tool code changes are required. See [Miorelli Client Layer](Docs/miorelli-client.md) for details.

---

## Documentation Index

### [MCP Server](Docs/mcp-server.md)
The core of the system. Covers `program.cs` DI setup, all registered MCP tools (`ask_antares`, `get_nearest_workers_to_cantiere`, `get_colleagues_of_person`, `report_holiday_request`, and the lower-level Miorelli wrappers), Claude retry logic, and how UC-A/B/C reports are built and saved to disk.

### [Anonymization Service](Docs/anonymization-service.md)
The PII gateway. Covers the three REST endpoints (`/anonymize`, `/anonymize-into-context`, `/deanonymize-known`), the token generation pipeline (`<PERSON_0001>`, `<LOCATION_0001>`, …), and the Redis-backed context store that enables server-side deanonymization.

### [GLiNER Service](Docs/gliner-service.md)
The Python NER microservice. Covers the GLiNER model (`urchade/gliner_multi-v2.1`), the `/analyze` endpoint, and the three-stage filtering pipeline: normalization → low-quality filtering → overlap deduplication.

### [MCP Client](Docs/mcp-client.md)
The reference client and test harness. Covers the four-step pattern every use case follows (build prompt → anonymize → call `ask_antares` → print response), the three UC scenarios wired in `AppRunner`, and what a production client would do differently.

### [Miorelli Client Layer](Docs/miorelli-client.md)
The data abstraction layer. Covers `IMiorelliService`, the stub/mock-fallback pattern, the full mock dataset (10 persons, 3 cantieri, PULITO_DA relations, absence tickets), all DTOs, and the step-by-step checklist for switching to the real Miorelli API.
