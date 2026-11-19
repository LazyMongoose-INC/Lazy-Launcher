# Lazy Launcher — Proposed Architecture

## Goals
A maintainable Windows launcher for LazyMongoose Modpack Minecraft 1.12.2, with install/repair/update, local offline profiles, a real Forge launch, logs, and a clean user interface.

## Proposed stack
- Python 3.12 (launcher implementation; pin exact version after dependency compatibility checks)
- PySide6 / Qt Widgets (desktop UI; mature Windows packaging and event-driven UI)
- Requests or urllib-based HTTP client (choose one and centralize transport; streaming, timeouts, retries)
- SQLite only for durable structured state if settings/profile JSON becomes insufficient; begin with validated JSON for small settings/profile data and avoid unnecessary DB complexity
- PyInstaller for Windows executable packaging; installer technology selected during release phase (evaluate Inno Setup)
- pytest for unit/integration tests
- GitHub Actions for static checks and tests; Windows runner for Windows-specific checks

## Modules
- `ui/`: views, widgets, state presentation; no download or launch logic in UI
- `core/config/`: settings, profile validation and persistence
- `core/installer/`: installation orchestration, manifest validation, install/repair state
- `core/downloads/`: HTTP transport, queues, progress, retries, resume, checksums
- `core/minecraft/`: version metadata, libraries, assets, classpath, argument resolution
- `core/forge/`: Forge metadata/install/launch integration for the selected 1.12.2 build
- `core/java/`: Java discovery, bundled runtime download and verification
- `core/pack/`: LazyMongoose manifest, pack version and file policy
- `core/updates/`: launcher and pack update checks/staging/rollback
- `core/logging/`: rotating launcher logs, game logs and diagnostic export
- `tests/`: unit, integration and Windows smoke tests

## Key design decisions
1. Keep GUI responsive: all network/install/process operations run in worker tasks; UI communicates through signals/events.
2. Manifest-driven installation: versioned file list with relative path, size, SHA-256 (when available), source URL and file role. Validate manifest schema and every target path.
3. Preserve user data: worlds, screenshots, user profile, and user-controlled settings are not pack-managed files. Updates stage files, verify, then replace; rollback metadata retained.
4. No secrets: offline profiles store only validated nickname and locally generated stable offline UUID; no password/token collection.
5. Process launch: build a structured argument list and use process APIs without shell interpolation. Capture stdout/stderr, process exit, and launcher/game log paths.
6. Downloads: HTTPS allowlist policy configurable to documented pack sources; timeouts, retries with backoff, hash verification, safe resume only when server supports range requests.
7. Java: Minecraft 1.12.2/Forge pack compatibility is expected to require Java 8; validate the chosen 64-bit runtime against the actual pack and Forge build. Bundle runtime per-instance rather than modify system Java.
8. Do not redistribute mod files unless licenses and source permissions allow. Provide user-supplied pack source or authorized host with clear provenance.

## Installation layout (proposal)
- Launcher installation: application files under Program Files or user-selected install path
- Launcher state: per-user AppData (settings, profiles, logs, updater staging)
- Game instance: user-selected directory, separate from launcher binaries
- Pack-managed files: tracked in manifest and installed beneath instance
- User data: worlds, screenshots, user configs and profile data preserved across updates

## Manifest model
Each managed entry should include:
- normalized relative path
- file size
- SHA-256
- download URL/source identifier
- managed role (client, config, resource, library, runtime, etc.)
- optional version/compatibility metadata

Manifest schema must be versioned and rejected safely if malformed or unsupported.

## Launch pipeline
1. Validate profile/nickname and settings.
2. Verify installation and repair missing/corrupt files.
3. Resolve compatible Java executable.
4. Resolve Minecraft metadata, libraries, assets and natives.
5. Resolve Forge version-specific launch metadata and required arguments.
6. Build classpath and game/JVM arguments using metadata placeholders.
7. Start Java process in the instance directory (no shell).
8. Capture logs and process lifecycle; report exit code and crash diagnostics.

## Security
- Reject absolute paths, traversal, drive prefixes, UNC paths, and unsafe archive entries.
- Restrict downloads to HTTPS except explicitly justified/test-only sources.
- Validate manifest size/schema and URL hosts.
- Never execute manifest-supplied commands.
- Use archive extraction limits and destination containment checks.
- Use checksums and staged installation before activation.
- Do not overwrite or delete unmanaged user data.

## Risks
- Missing modpack files/source and redistribution rights.
- Forge 1.12.2 launch metadata may require special legacy handling; implementation must be validated against real installed Forge output.
- Offline-mode servers may reject clients.
- Java compatibility and native libraries vary by pack/mods/Windows.
- Large modpack download needs disk-space estimation and robust recovery.
- Qt/PyInstaller packaging can require platform-specific hooks and clean-machine verification.
