# System Architecture

## 1. Architectural Overview

API_Web is structured as a backend service with clear responsibilities and separation of concerns.

The architecture emphasizes  **clarity, maintainability, and scalability** , even in its minimal prototype form.

---

## 2. Architectural Style

The system follows a  **layered architecture** , where each layer has a well-defined responsibility.

Primary layers:

* **Interface Layer** – Flask routes / Blueprints
* **Application Layer** – Future orchestration of business rules
* **Domain Layer** – Core logic and validations (currently minimal)
* **Infrastructure Layer** – Database setup, SQLite persistence, external tools

Communication is  **directional** : Interface → Application → Domain → Infrastructure.

---

## 3. Layer Responsibilities

### 3.1 Interface Layer

Responsible for:

* Exposing API endpoints (`/user`) to clients
* Translating HTTP requests into internal actions
* Validating input and formatting JSON responses

**Notes:**

* No business logic is implemented yet; responses are placeholders.

---

### 3.2 Application Layer

Responsible for:

* Orchestrating use cases (future implementation)
* Coordinating domain operations
* Enforcing workflows

**Notes:**

* Currently minimal; will be added when registration logic is implemented.

---

### 3.3 Domain Layer

Responsible for:

* Core business rules and validations
* Domain invariants (e.g., user age or height constraints)
* Pure logic independent of Flask or database frameworks

**Notes:**

* Domain layer is empty for now, but will encapsulate rules to allow future scalability.

---

### 3.4 Infrastructure Layer

Responsible for:

* Database persistence (`schema.db` via SQLite)
* SQL schema management (`schema.sql`)
* External integrations (Postman, DBeaver for testing)

**Notes:**

* `src/database/__init__.py` handles DB auto-creation
* Infrastructure details are  **isolated from domain logic** .

---

## 4. Data Flow

1. HTTP requests hit the **Interface Layer** (Flask route / Blueprint).
2. Interface delegates to **Application Layer** for business workflow.
3. Application Layer interacts with **Domain Layer** for rules and validations.
4. Domain logic requests persistence via the  **Infrastructure Layer** .
5. Responses flow in the **opposite direction** to the client.

**Rule:** no layer bypasses another; dependencies point inward.

---

## 5. Technical Constraints

* No business logic in Interface or Infrastructure layers
* Domain logic must remain independent of external frameworks
* SQLite DB is used for local development only
* Project must remain testable without external dependencies

---

## 6. Key Architectural Decisions

* Layered architecture chosen for clarity and maintainability
* Initial phase uses **stateless endpoints** and in-memory data placeholders
* Database persistence isolated to Infrastructure Layer
* Explicit contracts between layers allow future scalability

---

## 7. Architectural Evolution

* New features must follow the layer boundaries
* Major changes must update this document or be recorded in **Decision Records**
* Future enhancements may include:
  * Application Layer orchestration
  * Service and repository separation
  * Additional entities and tables
