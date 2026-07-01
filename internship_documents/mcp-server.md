# MCP Server — `Antares_AI_McpServer`

**Port:** `5001`  
**Framework:** .NET 10 / ASP.NET Core  
**Role:** Central intelligence layer. Exposes MCP tools over HTTP/SSE. Uses Claude as a semantic router to dispatch user requests to the correct workforce-management tool.

---

## Entry Point — `program.cs`

Bootstraps the application with ASP.NET Core's `WebApplication` builder. Key responsibilities:

### Named HTTP Clients

| Name | Target URL | Auth |
|------|-----------|------|
| `ExternalApi` | `https://demo.goantares.uno/public/api/v1/` | Basic (key:secret from secrets) |
| `AntaresGeneratedClient` | configurable via `ApiSettings:GeneratedClientBaseUrl` | Basic |
| `AnonymizationClient` | `http://localhost:5292` | none |

### DI Registrations

All tool classes are registered as **scoped** services so they can be injected into one another and into the MCP framework:

```
IMiorelliService          → MiorelliServiceStub   (swap here for real client)
AntaresAPIClient          (NSwag-generated)
DepartmentsTools
IdentityTools
AssetTools
PersonTools
AbsenceTools
LookupTools
JobTools
AntaresTools
```

`AntaresTools` and `JobTools` are also registered as **MCP tool types** via `.WithTools<T>()`.

### Configuration Validation

On startup, `ClaudeOptions` is validated:
- `MaxTokens > 0`
- `Temperature ∈ [0.0, 1.0]`
- `Model` is non-empty

### MCP Transport

The server mounts MCP over HTTP/SSE at the default `/` path via `.MapMcp()`.

---

## Configuration — `appsettings.json`

```json
{
  "ApiSettings": {
    "BaseUrl": "https://demo.goantares.uno/public/api/v1",
    "GeneratedClientBaseUrl": "https://demo.goantares.uno/public/api/",
    "TimeoutSeconds": 30
  },
  "MessagesParams": {
    "MaxTokens": 1024,
    "Temperature": 1.0,
    "Model": "claude-sonnet-4-6"
  }
}
```

**Required secrets** (via `dotnet user-secrets` or environment variables):

| Secret key | Purpose |
|-----------|---------|
| `Anthropic:ApiKey` | Claude API authentication |
| `ApiSettings:ApiKey` | Antares Basic auth username |
| `ApiSettings:ApiSecret` | Antares Basic auth password |

---

## MCP Tools — `Tools/`

All tool classes are decorated with `[McpServerToolType]` (except `NotificationTools`, which is intentionally disabled). Individual methods are decorated with `[McpServerTool(Name = "...")]`.

---

### `AntaresTools.cs` — `ask_antares`

**The entry point for all use cases.** This is the only tool the MCP client ever calls directly.

```csharp
[McpServerTool(Name = "ask_antares")]
public async Task<string> AskAntares(string user_input, string? context_id = null)
```

**Parameters:**
- `user_input` — the user's natural language request (may contain anonymized tokens like `<PERSON_0001>`)
- `context_id` — the anonymization session ID returned by the Anonymization API; forwarded to sub-tools for server-side deanonymization

**How it works:**

1. Builds a system prompt in Italian that defines Claude's role as a "semantic router": pick exactly one sub-tool, never reveal PII, always forward `context_id`, always include the tool's hardcoded result string in the response.
2. Calls `IChatClient.GetResponseAsync()` with `UseFunctionInvocation` and the `SubTools` list.
3. Returns `response.Text` — Claude's response, which will include the sub-tool's hardcoded confirmation string.

**Sub-tools available to Claude inside `ask_antares`:**

| Sub-tool | Source class |
|---------|-------------|
| `GetDepartments` | `DepartmentsTools` |
| `GetDepartement` | `DepartmentsTools` |
| `GetNearestWorkersToCantiere` | `JobTools` |
| `GetColleaguesOfPerson` | `JobTools` |
| `ReportHolidayRequest` | `JobTools` |

Note: the lower-level Miorelli tools (`AssetTools`, `PersonTools`, etc.) are **not** exposed as sub-tools to Claude. They are called internally by `JobTools`. The DepartmentsTools are leftovers from the first prototyping phase.

**Retry logic:** On `overloaded_error` from the Claude API, the tool retries up to 4 times with exponential backoff (2s → 4s → 8s). After all retries fail, it returns an Italian error string.

**Privacy enforcement:** The system prompt instructs Claude to keep anonymized tokens intact in its response and to never mention real names or contact details.

---

### `DepartmentsTools.cs`

Thin HTTP wrappers over the Antares REST API using the `ExternalApi` named client.

```csharp
[McpServerTool(Name = "get_departments")]
public async Task<string> GetDepartments()

[McpServerTool(Name = "get_department")]
public async Task<string> GetDepartement(string department_name)
```

- `GetDepartments()` — returns a JSON list of all departments from `GET /departments`
- `GetDepartement(name)` — filters by `ShortName` (case-insensitive substring match)

The `Department` record is defined inline: `record Department(string? Id, string? ShortName, string? Description, ...)`.

---

### `IdentityTools.cs` — `resolve_caller_identity`

```csharp
[McpServerTool(Name = "resolve_caller_identity")]
public async Task<MiorelliCallerIdentity> ResolveCallerIdentity(string? username = null)
```

Resolves who is calling (the logged-in user). Falls back to mock data (Paolo Ricci, Service Manager) when `MiorelliClientNotAvailableException` is thrown by the stub.

---

### `AssetTools.cs`

```csharp
[McpServerTool(Name = "get_authorized_cantieri")]
public async Task<List<MiorelliCantiere>> GetAuthorizedCantieri(Guid personId, Guid? itemCategoryId = null)

[McpServerTool(Name = "get_people_by_relation_on_asset")]
public async Task<List<MiorelliRelation>> GetPeopleByRelationOnAsset(Guid assetId, Guid? relationTypeId = null)

[McpServerTool(Name = "get_assets_near_coordinates")]
public async Task<List<MiorelliCantiere>> GetAssetsNearCoordinates(double latitude, double longitude, double maxDistanceMeters)
```

- `GetAuthorizedCantieri` — returns the cantieri (job sites) a person is authorized to manage. Used in all three use cases to build the working scope.
- `GetPeopleByRelationOnAsset` — returns all `MiorelliRelation` records linking persons to a cantiere via a specific relation type (e.g., `PULITO_DA`).
- `GetAssetsNearCoordinates` — geo-proximity search; returns cantieri within `maxDistanceMeters` meters.

---

### `PersonTools.cs`

```csharp
public async Task<MiorelliPerson> GetPersonDetails(Guid personId)
public async Task<List<MiorelliPerson>> SearchPersonByName(string name)
public async Task<List<MiorelliColleague>> GetColleaguesOfPerson(Guid personId, Guid relationTypeId, bool includeDetails = false)
public async Task<List<MiorelliPerson>> GetPersonsUnderRelation(Guid managerId, Guid relationTypeId)
public List<MiorelliRankedPerson> CalculateDistanceAndRank(double refLat, double refLon, List<MiorelliPerson> persons, int? topN = null)
public List<MiorelliRankedPerson> FilterByRadiusKm(List<MiorelliRankedPerson> ranked, double radiusKm)
```

- `GetPersonDetails` — fetches a single person by GUID. Throws `KeyNotFoundException` if not found (propagates fatally — a real data integrity issue).
- `SearchPersonByName` — case-insensitive name search across the mock dataset.
- `GetColleaguesOfPerson` — finds all persons sharing at least one cantiere via `PULITO_DA`.
- `GetPersonsUnderRelation` — finds all persons subordinate to a manager via a given relation type (used in UC-C authorization check).
- `CalculateDistanceAndRank` — **pure computation, no service call**. Applies the Haversine formula to rank persons by distance from a reference point. Persons without coordinates are sorted last. Optionally returns only top-N.
- `FilterByRadiusKm` — filters an already-ranked list to only include persons within the given radius.

---

### `AbsenceTools.cs` — `get_absences_for_person`

```csharp
[McpServerTool(Name = "get_absences_for_person")]
public async Task<List<MiorelliTicket>> GetAbsencesForPerson(
    Guid personId,
    long? unavailabilityCategory = null,
    string? from = null,
    string? to = null)
```

Returns all `MiorelliTicket` records where `UnavailabilityGenerated = true`. Optional filters: category (`1 = FERIE`, `2 = MALATTIA`), date range (ISO 8601 strings).

---

### `LookupTools.cs`

```csharp
[McpServerTool(Name = "get_relation_types")]
public async Task<List<MiorelliRelationType>> GetRelationTypes(string? shortNameFilter = null)

[McpServerTool(Name = "get_item_categories")]
public async Task<List<MiorelliItemCategory>> GetItemCategories(string? shortNameFilter = null)

[McpServerTool(Name = "get_roles")]
public async Task<List<MiorelliRole>> GetRoles(string? shortNameFilter = null)
```

Resolves tenant-specific GUIDs before they are needed by other tools. The typical bootstrap sequence:

```
GetRelationTypes("PULITO_DA")        → Guid pulitoDaId
GetItemCategories("SedePrincipale")  → Guid sedePrincipaleId
GetRoles("Capocantiere")             → Guid capochantiereRoleId
```

---

### `JobTools.cs` — Use Cases UC-A, UC-B, UC-C

High-level orchestration. Each method: deanonymizes its parameter → resolves GUIDs → queries Miorelli tools → logs a full real-data report server-side → returns a hardcoded Italian string.

#### UC-A — `get_nearest_workers_to_cantiere`

```csharp
public async Task<string> GetNearestWorkersToCantiere(
    string cantiereName, double radiusKm = 15.0, string? context_id = null)
```

**Flow:**
1. Deanonymize `cantiereName` via `/deanonymize-known` (if `context_id` is set)
2. `ResolveCallerIdentity()` → `GetRelationTypes("PULITO_DA")` → `GetItemCategories("SedePrincipale")`
3. `GetAuthorizedCantieri()` → find the target cantiere by name
4. `GetPeopleByRelationOnAsset(cantiereId, pulitoDaId)` → fetch each worker's details
5. `CalculateDistanceAndRank()` → `FilterByRadiusKm(radiusKm)`
6. Split into `Attivi` / `NonAttivi`, log full report (names, phones, distances)
7. Return `"Operazione completata con successo."`

The log report also includes demo email template stubs for three edge cases: cantiere not recognized, neither cantiere nor service recognized, cantiere recognized but outside caller's perimeter.

#### UC-B — `get_colleagues_of_person`

```csharp
public async Task<string> GetColleaguesOfPerson(string personName, string? context_id = null)
```

**Flow:**
1. Deanonymize `personName`
2. `SearchPersonByName()` → resolve target person
3. `GetColleaguesOfPerson(person.Id, pulitoDaId)` → direct colleagues
4. Scan all authorized cantieri for non-colleagues (workers not sharing any cantiere with the person)
5. `CalculateDistanceAndRank()` from person's residence → take top 5 non-colleagues
6. Log report, return success string

#### UC-C — `report_holiday_request`

```csharp
public async Task<string> ReportHolidayRequest(string personName, string? context_id = null)
```

**Flow:**
1. Deanonymize `personName`
2. `SearchPersonByName()` → resolve target person
3. Resolve `RESPONSABILE_DI_RIFERIMENTO` and `AUTORIZZATORE` relation types
4. Check authorization: caller must manage the person via `PULITO_DA` perimeter, or be their Responsabile, or be their Autorizzatore
5. Build the full worker pool across all authorized cantieri
6. Identify person's cantieri (those where the person is a PULITO_DA worker)
7. For each cantiere:
   - Check all workers for absences today (via `GetAbsencesForPerson`)
   - Identify absent colleagues
   - Find non-colleagues within 15 km, mark which are absent
8. Log per-cantiere report, return success string

#### Deanonymization helper

```csharp
private async Task<string> DeanonymizeAsync(string text, string? contextId)
```

Calls `POST /deanonymize-known` on the Anonymization API. If `contextId` is null or the call fails, returns the original text unchanged — so the function degrades gracefully when anonymization was not used.

#### Report file saving

All three use cases write their reports to timestamped `.txt` files in `AppContext.BaseDirectory/logs/`:

```
logs/20260409_143000_UC-A_nearest_workers.txt
logs/20260409_143001_UC-B_colleagues_of_person.txt
logs/20260409_143002_UC-C_holiday_request.txt
```

---

### `NotificationTools.cs` — (Disabled)

Intentionally not decorated with `[McpServerToolType]` and not registered in `program.cs`. Requires a provisioned Miorelli event template and a working notification endpoint — both pending tenant setup.

---

## Generated Client — `Anonymization_Client/`

`AnonymizationServiceClient.g.cs` is auto-generated by NSwag from `api-docs.yml`. **Do not edit manually.** To regenerate after an API spec update:

```bash
cd Antares_AI_McpServer
nswag run Anonymization_Client/nswag.json
```

The client provides:
- `AnonymizeAsync(string input)` → `AnonymizationResult` (anonymized text + contextId)
- `AnonymizeIntoContextAsync(AnonymizeIntoContextRequest)` → reuse an existing context
- `DeanonymizeKnownAsync(DeanonymizeRequest)` → restore tokens to real values

---

## NuGet Dependencies

All packages are declared in `Antares_AI_McpServer.csproj`. **`dotnet restore` runs automatically on `dotnet build` or `dotnet run`** — no manual install step is needed.

| Package | Version | Purpose |
|---------|---------|---------|
| `Anthropic.SDK` | 5.10.0 | Claude API client — used by `AntaresTools` to call `GetResponseAsync` with function invocation |
| `Microsoft.Extensions.AI` | 9.5.0 | `IChatClient`, `AIFunctionFactory`, `ChatOptions` — unified AI abstraction layer |
| `ModelContextProtocol.AspNetCore` | 0.7.0-preview.1 | MCP server transport over HTTP/SSE; provides `[McpServerToolType]`, `[McpServerTool]`, `.MapMcp()` |
| `Spectre.Console` | 0.54.0 | Rich console output (used for startup/debug logging) |
