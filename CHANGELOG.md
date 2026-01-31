# Changelog

All notable changes to this project will be documented in this file.

This project follows a pragmatic versioning approach during its early development stages.

---

## [Unreleased]

### Planned

- Introduce an explicit Application Layer
- Add domain-level validations
- Improve test isolation and database lifecycle handling
- Expand API endpoints beyond basic user operations

---

## [0.1.0] – Initial Architecture and Persistence Setup

### Added

- Initial project structure following a layered, MVC-inspired architecture
- Flask server setup with Blueprint-based routing
- SQLite database integration
- SQLAlchemy base configuration
- User entity definition
- User repository with insert and select operations
- Database connection handler abstraction
- Initial database schema definition (`schema.sql`)
- Repository-level tests interacting with the database
- Project documentation:
  - README with project intent and boundaries
  - Architecture documentation
  - Scope definition

### Changed

- Adjusted database connection handling to support testing scenarios
- Refined repository tests to better reflect persistence behavior
- Improved project structure to isolate infrastructure concerns

### Fixed

- Issues related to repeated data insertion during test execution
- Test failures caused by shared database state
- Missing initialization steps in database setup

### Notes

- Business logic is intentionally minimal at this stage
- Routes currently return placeholder responses
- Application Layer is planned but not yet implemented
- Database is treated as a first-class dependency for learning and clarity
