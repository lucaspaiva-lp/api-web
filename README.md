
# API_Web

## Overview

API_Web is a backend-focused project designed to explore and apply clean architectural principles using a simple and well-defined domain.

The project prioritizes **clarity, correctness, and maintainability** over feature breadth, serving as an educational and evolvable foundation for backend development.

---

## Problem Statement

Many small backend projects grow without clear structure, leading to tightly coupled code, unclear responsibilities, and fragile tests.

This project was created to address those issues by:

* Applying a clear architectural pattern (MVC)
* Enforcing separation of concerns
* Treating the database as an explicit and controlled dependency
* Encouraging deterministic and understandable behavior

---

## Project Purpose

The purpose of this project is to provide a **structured backend API** that:

* Demonstrates clean separation between layers
* Uses explicit contracts between components
* Remains easy to reason about, test, and extend
* Serves as a learning vehicle for real-world backend practices

Correctness and architectural integrity are prioritized over rapid feature expansion.

---

## Architectural Style

The project follows the **MVC (Model–View–Controller)** architectural pattern, adapted for a backend API context.

### MVC Mapping in This Project

* **Model**
  * Domain entities (`models/entities`)
  * Database connection and ORM base (`models/connection`)
  * Repositories (`models/repositories`)
* **Controller**
  * Route handlers and request orchestration (`main/routes`)
* **View**
  * JSON responses returned by the API (no UI rendering)

This structure ensures that business logic, persistence, and request handling remain clearly separated.

---

## Project Structure

<pre class="overflow-visible! px-0!" data-start="2046" data-end="2408"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible! px-0!" data-start="2046" data-end="2408"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-text"><span><span>src/
├── database/
│   └── init/
│       └── schema.sql
├── main/
│   ├── routes/
│   │   └── user_route.py
│   └── server/
│       └── server.py
├── models/
│   ├── connection/
│   │   ├── base.py
│   │   └── db_connection_handler.py
│   ├── entities/
│   │   └── users.py
│   └── repositories/
│       └── users_repository.py
├── __init__.py
run.py
</span></span></code></div></div></pre>

Additional documentation lives in the `docs/` directory.

---

## Scope

The system focuses on a  **small and controlled domain** .

### In Scope

* Handling HTTP requests via Flask
* Managing user data through a repository layer
* Interacting with a relational database (SQLite)
* Applying automated tests to persistence logic
* Enforcing architectural boundaries

### Out of Scope

* Frontend or UI rendering
* Authentication and authorization
* Distributed systems or messaging
* Performance optimization beyond correctness
* Production-scale deployment concerns

For more detail, see `docs/scope.md`.

---

## Database

* **SQLite** is used for simplicity and transparency
* Database schema is defined explicitly (`schema.sql`)
* The database is treated as an external dependency, not implicit state
* Tests may use either in-memory or file-based databases depending on intent

---

## Testing Strategy

* Repository behavior is validated via automated tests
* Tests are written to highlight the importance of data isolation and state control
* Both isolated and persistent-database scenarios are intentionally explored

Testing decisions are documented and aligned with the project’s educational goals.

---

## Documentation

* `docs/architecture.md` — Architectural decisions and layer responsibilities
* `docs/scope.md` — Explicit definition of system scope
* `CHANGELOG.md` — Versioned record of changes
* `SECURITY.md` — Security-related considerations

---

## Non-Goals

This project does **not** aim to:

* Be a production-ready system
* Replace full-featured frameworks
* Hide infrastructure complexity behind abstractions
* Optimize prematurely for scalability

---

## Role of This Repository

This repository serves as:

* A learning artifact
* A reference for clean backend structure
* A controlled environment to explore architectural trade-offs

Any significant change in intent or scope **must be reflected in the documentation** .

## Learning Context

This project was initially developed following the *Clean Code* course by Rocketseat as a learning reference.

At this stage, the structure and patterns closely align with the course material, with minor adaptations applied intentionally.

Future iterations of this project may diverge from the original course approach as architectural decisions evolve independently.
