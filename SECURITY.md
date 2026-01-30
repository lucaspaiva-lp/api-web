# Security Policy

## Supported Versions

This project follows a branch-based support model instead of versioned releases at this stage.

- The `main` branch represents the **stable and supported** state of the project.
- The `develop` branch is used for **active development** and is **not security-supported**.
- Other branches are experimental and unsupported.

| Branch | Supported for Security Updates |

|----------|--------------------------------|

| `main` | ✅ Yes |

| `develop` | ❌ No |

| Others | ❌ No |

Users are strongly advised **not to rely on the `develop` branch** for production or sensitive use cases.

---

## Reporting a Vulnerability

If you identify a security vulnerability, please **do not report it via public issues**.

Instead, use one of the following channels:

- Open a **GitHub Security Advisory** (preferred)
- Or contact the project maintainer directly via GitHub

### What to expect

-**Acknowledgment** within 7 days

- If accepted, the issue will be fixed on the `main` branch
- If declined, a brief explanation will be provided when appropriate

---

## Scope of Security Considerations

At its current stage, this project:

- Does not handle authentication or authorization
- Does not process sensitive personal data
- Does not expose network services by default

Security considerations are therefore limited to:

- Input validation
- Data consistency
- Defensive handling of user-provided information

As the project evolves, this policy may be updated accordingly.

---

## Responsible Disclosure

Please allow reasonable time for a fix before publicly disclosing any vulnerability.
