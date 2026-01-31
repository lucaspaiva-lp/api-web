
# System Architecture

## 1. Architectural Overview

API_Web is a backend API structured with explicit separation of concerns and clear responsibility boundaries.

Even in its early stage, the architecture prioritizes **clarity, maintainability, and controlled evolution**, avoiding hidden coupling and implicit behavior.

The system is intentionally minimal, but architecturally prepared for growth.

---

## 2. Architectural Style

The project follows a **layered architecture**, inspired by MVC principles and adapted to a backend API context.

Each layer has a single, well-defined responsibility, and dependencies are strictly directional.

### Logical Layers

- **Interface Layer** – HTTP handling (Flask routes / Blueprints)
- **Application Layer** – Use case orchestration (planned)
- **Domain Layer** – Core business rules and entities
- **Infrastructure Layer** – Database access and external tooling

Communication flows inward:

**Interface → Application → Domain → Infrastructure**

---

## 3. Layer Responsibilities

### 3.1 Interface Layer

**Location**

- `src/main/routes`
- `src/main/server`

**Responsibilities**

- Expose HTTP endpoints
- Handle request/response lifecycle
- Translate HTTP input into internal calls
- Return JSON responses

**Constraints**

- No business rules
- No persistence logic
- No domain decisions

**Current State**

- Routes are defined using Flask Blueprints
- Responses are currently simple and illustrative

---

### 3.2 Application Layer

**Location**

- Planned (to be introduced between routes and repositories)

**Responsibilities**

- Orchestrate use cases
- Coordinate domain operations
- Control application flow

**Current State**

- Not implemented yet
- Responsibilities are temporarily handled by routes
- This is an intentional transitional decision

---

### 3.3 Domain Layer

**Location**

- `src/models/entities`

**Responsibilities**

- Represent domain entities
- Encapsulate domain rules and invariants
- Remain independent of frameworks and infrastructure

**Current State**

- Domain entities are defined using SQLAlchemy models
- Business rules are minimal and will evolve incrementally

---

### 3.4 Infrastructure Layer

**Location**

- `src/models/connection`
- `src/database`

**Responsibilities**

- Database connection management
- ORM configuration and persistence
- SQL schema definition
- External tooling support

**Current State**

- SQLite is used as the persistence mechanism
- Database schema is explicitly defined in `schema.sql`
- Connection handling is isolated from domain and interface layers

---

## 4. Data Flow

1. An HTTP request reaches the **Interface Layer** (Flask route).
2. The route delegates processing (currently directly) to repository or future application logic.
3. Domain entities are created or queried.
4. Persistence is handled by the **Infrastructure Layer**.
5. A response is returned to the client.

**Architectural Rule**

- No layer may bypass another intentionally.
- Dependencies must always point inward.

---

## 5. Technical Constraints

- Business logic must not live in routes or database handlers
- Infrastructure details must not leak into domain logic
- SQLite is used for local development and learning purposes
- The system must remain testable with controlled state

---

## 6. Key Architectural Decisions

- Use of layered architecture for clarity and testability
- MVC-inspired structure adapted for backend APIs
- Database treated as an explicit dependency
- Tests may interact with real or isolated databases depending on intent

---

## 7. Architectural Evolution

This architecture is expected to evolve gradually.

Planned evolutions include:

- Introduction of an explicit Application Layer
- Clear separation between services and repositories
- Expansion of domain rules and validations
- Support for additional entities and use cases

All significant architectural changes must be reflected in this document.
