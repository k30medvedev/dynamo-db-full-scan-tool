# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] - Unreleased
### Added
- ✨ New page: **Execution Link Checker**.
- View full DynamoDB item for a given correlation ID.
- Extract and display all Step Function execution links.
- Session-based checkbox tracking per correlation ID.

---

## [0.2.1] - 2025-05-22
### ⚠️ Important
- AWS session now uses **temporary credentials only**, avoiding local credential storage in `~/.aws`.
- Solves conflict with existing `login-sso` setup.
- Runtime credentials fetching was removed for compatibility with future cloud deployments.

### Added
- Custom **CSS support** via `styles.css`.
- UI styling improvements, custom fonts, and layout padding.
- Input field added next to the DynamoDB table selector — allows filtering tables by substring (e.g. typing `1023` filters matching names).
- Docker & Podman support:
  - `Dockerfile` and `docker-compose.yml` included.
  - Compatible with `podman compose up / down`.

### Changed
- Font sizes adjusted to be more consistent and less oversized.
- CloudWatch query now supports selecting a larger number of days (limit lifted).
- Some `selectbox` UI elements were replaced with `radio` buttons for better UX.
- Version number is now read from a standalone `VERSION` file and injected both into the UI and Docker image.

