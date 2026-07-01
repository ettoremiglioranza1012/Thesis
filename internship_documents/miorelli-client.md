# Miorelli Client Layer — `MiorelliClient/`

**Location:** `Antares_AI_McpServer/MiorelliClient/`  
**Role:** Abstraction layer between the MCP tools and the Miorelli workforce management platform. All tool code depends exclusively on the `IMiorelliService` interface — the concrete implementation (stub or real) is swapped in `program.cs` with no other changes required.

---

## Design Intent

The Miorelli tenant (real Antares/Miorelli API) was not yet provisioned when this system was built. Rather than blocking development:

- All tools code against `IMiorelliService` — an interface that expresses the exact data contract needed.
- `MiorelliServiceStub` implements the interface by **throwing `MiorelliClientNotAvailableException`** on every call.
- Every tool that calls into Miorelli catches `MiorelliClientNotAvailableException` and falls back to static mock data from `MiorelliMockDataProvider`.
- When the real tenant is ready, only one line in `program.cs` changes; no tool code is touched.

---

## `IMiorelliService` — The Contract

```csharp
public interface IMiorelliService
{
    // Identity
    Task<MiorelliCallerIdentity> GetCallerIdentityAsync(string? username = null);

    // Assets (Cantieri)
    Task<List<MiorelliCantiere>> GetAuthorizedCantieriAsync(Guid personId, Guid? itemCategoryId = null);
    Task<List<MiorelliRelation>> GetPeopleByRelationOnAssetAsync(Guid assetId, Guid? relationTypeId = null);
    Task<List<MiorelliCantiere>> GetAssetsNearCoordinatesAsync(double latitude, double longitude, double maxDistanceMeters);

    // Persons
    Task<MiorelliPerson?> GetPersonByIdAsync(Guid personId);
    Task<List<MiorelliPerson>> SearchPersonByNameAsync(string name);
    Task<List<MiorelliColleague>> GetColleaguesOfPersonAsync(Guid personId, Guid relationTypeId, bool includeDetails = false);
    Task<List<MiorelliPerson>> GetPersonsUnderRelationAsync(Guid managerId, Guid relationTypeId);

    // Absences
    Task<List<MiorelliTicket>> GetAbsencesForPersonAsync(Guid personId, long? category = null, DateTimeOffset? from = null, DateTimeOffset? to = null);

    // Lookups
    Task<List<MiorelliRelationType>> GetRelationTypesAsync(string? shortNameFilter = null);
    Task<List<MiorelliItemCategory>> GetItemCategoriesAsync(string? shortNameFilter = null);
    Task<List<MiorelliRole>> GetRolesAsync(string? shortNameFilter = null);
}
```

---

## `MiorelliServiceStub`

Implements `IMiorelliService` by throwing `MiorelliClientNotAvailableException` on every method:

```csharp
public class MiorelliServiceStub : IMiorelliService
{
    public Task<MiorelliCallerIdentity> GetCallerIdentityAsync(string? username = null)
        => throw new MiorelliClientNotAvailableException();

    // ... same for all other methods
}
```

This makes the stub useful as a compile-time proof that all tools handle the unavailable-service case. If a tool fails to catch the exception, it will propagate and be visible in testing.

---

## `MiorelliClientNotAvailableException`

```csharp
public class MiorelliClientNotAvailableException : Exception
{
    public MiorelliClientNotAvailableException()
        : base("The Miorelli client is not available. Using mock data.") { }
}
```

A simple marker exception. Every tool catches it specifically (not the general `Exception`) to avoid accidentally swallowing real errors.

---

## Mock Data — `Mock/`

### `MiorelliMockConstants.cs`

Defines placeholder GUIDs for all tenant concepts. These are stable across runs (not randomly generated), so tests and logs are reproducible.

| Concept | ID format | Notes |
|---------|----------|-------|
| Person IdP001–IdP010 | `1111000N-0000-0000-0000-000000000000` | N = 1–10 |
| Cantiere IdC001–IdC003 | `2222000N-0000-...` | N = 1–3 |
| Ticket IdT001–IdT005 | `3333000N-0000-...` | N = 1–5 |
| PULITO_DA relation type | `aaaa0001-0000-...` | Worker assigned to a site |
| RESPONSABILE_DI_RIFERIMENTO | `aaaa0002-0000-...` | Manager relationship |
| AUTORIZZATORE | `aaaa0003-0000-...` | Authorization relationship |
| SedePrincipale item category | `bbbb0001-0000-...` | Main-site category |
| Roles (5 types) | `cccc000N-0000-...` | Capocantiere, CapoServizioEvoluto, ServiceManager, ResponsabileRif, Autorizzatore |

**When real tenant is provisioned:** replace the constants in `MiorelliMockConstants.cs` with real GUIDs from the Miorelli admin panel.

---

### `MiorelliMockDataProvider.cs`

Static readonly collections that simulate a real Miorelli tenant dataset. All data is in the Lombardy region of Italy (realistic GPS coordinates).

#### Persons (10)

| ID | Name | Active | Has GPS | Notes |
|----|------|--------|---------|-------|
| IdP001 | Marco Ferretti | yes | yes | — |
| IdP002 | Luca Sartori | yes | yes | — |
| IdP003 | Giulia Conti | yes | yes | Test subject for UC-B/C |
| IdP004 | Roberto Mazza | yes | yes | — |
| IdP005 | Elena Bruni | yes | yes | — |
| IdP006 | Antonio Neri | no | yes | Inactive worker |
| IdP007 | Carla Galli | yes | yes | — |
| IdP008 | Paolo Ricci | yes | yes | **Fixed caller identity** |
| IdP009 | Federica Sala | yes | yes | — |
| IdP010 | Davide Lombardi | yes | yes | — |

Paolo Ricci (IdP008) is the hardcoded caller returned by `IdentityTools` when the real identity service is unavailable.

#### Cantieri (3)

| ID | Name | Address | Coordinates |
|----|------|---------|-------------|
| IdC001 | Bergamo | Via della Fonda 5, Bergamo | 45.6983°N, 9.6773°E |
| IdC002 | Brescia | Via Risorgimento 8, Brescia | 45.5416°N, 10.2118°E |
| IdC003 | Mantova | Via Po 34, Mantova | 45.1564°N, 10.7916°E |

#### PULITO_DA Relations (worker → site)

| Person | Cantiere |
|--------|---------|
| IdP002 (Luca Sartori) | IdC001 (Bergamo) |
| IdP006 (Antonio Neri) | IdC001 (Bergamo) |
| IdP007 (Carla Galli) | IdC001 (Bergamo) |
| IdP001 (Marco Ferretti) | IdC002 (Brescia) |
| IdP003 (Giulia Conti) | IdC002 (Brescia) |
| IdP004 (Roberto Mazza) | IdC002 (Brescia) |
| IdP003 (Giulia Conti) | IdC003 (Mantova) |
| IdP004 (Roberto Mazza) | IdC003 (Mantova) |
| IdP009 (Federica Sala) | IdC003 (Mantova) |
| IdP010 (Davide Lombardi)| IdC003 (Mantova) |

#### Person-to-Person Relations (caller = Paolo Ricci, IdP008)

| Type | Caller (manager) | Subordinate |
|------|-----------------|------------|
| RESPONSABILE_DI_RIFERIMENTO | IdP008 | IdP001 (Marco Ferretti) |
| RESPONSABILE_DI_RIFERIMENTO | IdP008 | IdP003 (Giulia Conti) |
| RESPONSABILE_DI_RIFERIMENTO | IdP008 | IdP005 (Elena Bruni) |
| AUTORIZZATORE | IdP008 | IdP002 (Luca Sartori) |
| AUTORIZZATORE | IdP008 | IdP007 (Carla Galli) |

#### Absence Tickets (5)

| ID | Person | Category | Period |
|----|--------|---------|--------|
| IdT001 | IdP003 (Giulia Conti) | FERIE (1) | 2026-04-01 → 2026-04-05 |
| IdT002 | IdP007 (Carla Galli) | MALATTIA (2) | 2026-03-28 → 2026-04-10 |
| IdT003 | IdP001 (Marco Ferretti) | FERIE (1) | 2026-04-07 → 2026-04-14 |
| IdT004 | IdP009 (Federica Sala) | FERIE (1) | 2026-04-06 → 2026-04-08 |
| IdT005 | IdP004 (Roberto Mazza) | MALATTIA (2) | 2026-04-03 → 2026-04-09 |

Tickets T002, T003, T004, T005 overlap with the current date (April 2026), making UC-C non-trivial: multiple workers are absent when a holiday request is filed.

---

## DTOs — `Dtos/`

All DTOs are **C# records** (immutable value types). They represent the internal data contract, independent of the external API format.

```csharp
record MiorelliPerson(
    Guid Id,
    string? FirstName,
    string? LastName,
    string? Phone,
    string? Mobile,
    string? Email,
    double? ResidenceLatitude,
    double? ResidenceLongitude,
    double? WeeklyHours,
    bool IsActive
);

record MiorelliCantiere(
    Guid Id,
    string? Name,
    string? Address,
    double? Latitude,
    double? Longitude,
    bool IsActive
);

record MiorelliRelation(Guid AssetId, Guid PersonId, Guid RelationTypeId);

record MiorelliPersonRelation(Guid ManagerId, Guid SubordinateId, Guid RelationTypeId);

record MiorelliColleague(MiorelliPerson Person, List<MiorelliCantiere> SharedCantieri);

record MiorelliRankedPerson(MiorelliPerson Person, double? DistanceMeters);

record MiorelliCallerIdentity(Guid PersonId, string? Username, List<MiorelliRole> Roles);

record MiorelliTicket(
    Guid Id,
    Guid? ApplicantId,
    bool UnavailabilityGenerated,
    long? UnavailabilityCategory,   // 1 = FERIE, 2 = MALATTIA
    DateTimeOffset? StartDate,
    DateTimeOffset? EndDate
);

record MiorelliRelationType(Guid Id, string? ShortName, string? Description);

record MiorelliItemCategory(Guid Id, string? ShortName, string? Code);

record MiorelliRole(Guid Id, string? ShortName, string? Name);
```

---

## Switching to the Real Miorelli Client

When the Miorelli Antares tenant is provisioned:

1. **Generate the client** from the Miorelli OpenAPI spec using NSwag:
   ```bash
   nswag run MiorelliClient/nswag.json
   ```
   This produces `AntaresMiorelliClient.g.cs`.

2. **Implement the mapping layer** from Miorelli API response types to the internal DTOs above. The mapping should be straightforward — the DTOs were designed to mirror the expected Miorelli schema.

3. **Swap the registration** in `program.cs`:
   ```csharp
   // Before:
   builder.Services.AddScoped<IMiorelliService, MiorelliServiceStub>();

   // After:
   builder.Services.AddScoped<IMiorelliService, AntaresMiorelliClient>();
   ```

4. **Replace GUIDs** in `MiorelliMockConstants.cs` with real tenant GUIDs from the Miorelli admin panel (or load them from configuration).

No changes are needed in any tool class (`AssetTools`, `PersonTools`, `AbsenceTools`, `LookupTools`, `IdentityTools`).
