# Lazy Launcher — Architecture

## 1. Project goals

Build a maintainable Windows launcher for LazyMongoose Modpack on Minecraft Java Edition 1.12.2. The launcher should install, verify, repair, update, and start the complete game instance; provide local offline nickname profiles; preserve user data; and expose useful diagnostics through a clear desktop interface.

The user experience may take inspiration from established Minecraft launchers, including Legacy Launcher. This is a UX reference only: Lazy Launcher remains an independent implementation and must not copy third-party source code, assets, trademarks, or proprietary design elements.

## 2. Proposed technology stack

- Python 3.12 for launcher logic. Pin the exact interpreter and dependencies after compatibility checks.
- PySide6 / Qt Widgets for the Windows desktop interface.
- One centralized HTTP client (Requests or the standard library); select one during implementation. It must support streaming, timeouts, retries, and controlled redirects.
- Validated JSON for settings and local profiles. Introduce SQLite only if real requirements exceed simple configuration persistence.
- pytest for unit and integration tests.
- GitHub Actions, including Windows runners, for automated checks.
- PyInstaller for the initial Windows executable; choose and validate the installer technology during the release phase.

## 3. High-level module boundaries

- `ui/`: windows, views, widgets, visual state, and user interaction. No network, installation, or process-management logic.
- `core/config/`: settings schema, validation, migration, and profile persistence.
- `core/installer/`: install orchestration, manifest validation, progress, repair, and install state.
- `core/downloads/`: HTTP transport, queues, progress events, retries, safe resume, and integrity checks.
- `core/minecraft/`: version metadata, libraries, assets, natives, classpath, and argument resolution.
- `core/forge/`: Forge-specific metadata and launch integration for the exact selected 1.12.2 build.
- `core/java/`: system Java discovery, compatibility checks, managed-runtime fallback, and runtime selection.
- `core/pack/`: LazyMongoose manifest, pack version, and file ownership policy.
- `core/updates/`: launcher and pack update checks, staging, activation, and rollback.
- `core/logging/`: rotating launcher logs, game output capture, and diagnostic export.
- `tests/`: unit, integration, and Windows smoke tests.

Keep the UI responsive: network, disk-intensive, and process operations run outside the UI thread and report progress through Qt signals or an equivalent event boundary.

## 4. Java runtime policy

### 4.1 Priority: compatible system Java first

The default policy is **System Java first; managed Java only when needed**. The launcher must not download or bundle a private runtime unconditionally.

For the Minecraft 1.12.2 / Forge target, Java 8 x64 is the expected baseline, but the final compatibility requirement must be confirmed against the actual modpack and exact Forge build.

At launch time, the runtime resolver should use this order:

1. A Java executable explicitly selected by the user in launcher settings, if it passes compatibility checks.
2. A compatible system Java 8 x64 discovered on Windows. Discovery should consider supported sources such as `JAVA_HOME`, the executable available on `PATH`, and standard Windows Java installation registrations/locations. Discovery must not execute arbitrary files found by an unrestricted filesystem scan.
3. A previously installed Lazy Launcher-managed Java runtime, if it is valid and compatible.
4. If no usable runtime is found, offer or automatically initiate installation of the managed Java runtime according to the user's installation settings.

A newer system Java must not be assumed compatible merely because it is installed. The resolver must inspect the actual executable, vendor/version output, and architecture, then apply the compatibility policy for the selected Minecraft/Forge instance.

### 4.2 Compatibility validation

Before selecting a runtime, validate at least:

- executable exists and can be started for a version probe;
- Java major version is supported by the selected instance;
- runtime architecture is 64-bit for the target pack;
- executable is not a broken link or unusable installation;
- the version probe completes within a timeout and its output can be parsed.

The compatibility policy must be instance-aware rather than hard-coded globally. If the actual modpack proves to require a different Java build or vendor, record that requirement in pack metadata and tests.

### 4.3 Managed Java fallback

When no compatible system runtime is available:

- download a supported 64-bit Java 8 runtime from a documented, trusted distribution source;
- verify the download using a pinned checksum or a trusted vendor-provided integrity mechanism;
- install it in a launcher-managed runtime directory, separate from Windows system locations and game saves;
- keep the runtime associated with the relevant game instance or runtime identifier;
- support re-verification and repair if files are missing or corrupted;
- never modify `JAVA_HOME`, the system `PATH`, registry settings, or an existing system Java installation.

The launcher must clearly show whether it selected system Java or its managed runtime, and provide the resolved executable path and version in diagnostics.

### 4.4 Settings and failure behavior

Provide an automatic mode as the default. Where useful, expose an advanced option to select a Java executable or choose a managed runtime. Do not make users configure Java manually for a normal first launch.

If a selected custom Java is incompatible, explain why and offer the next valid option. Do not silently switch runtimes after a launch failure without recording the reason. A user must be able to see and change the selected runtime.

If the runtime download fails, preserve the existing installation and show a recoverable error with the source and log details. Do not launch with an unverified or partially extracted runtime.

## 5. Key design decisions

1. Keep the GUI responsive. All network, installation, verification, and process operations run in worker tasks.
2. Use a versioned manifest. Each managed file has a normalized relative path, size, SHA-256, source URL or source identifier, and file role.
3. Preserve user data. Worlds, screenshots, user-created files, and user-controlled settings are not pack-managed. Stage and verify updates before activation; retain rollback metadata.
4. Do not collect secrets. Offline profiles store a validated nickname and a locally generated stable offline UUID only. Never request or store Microsoft passwords or access tokens.
5. Launch processes safely. Build a structured argument list and start Java without shell interpolation. Capture stdout, stderr, exit code, and log locations.
6. Centralize downloads. Apply HTTPS policy, host allowlists where appropriate, timeouts, retry/backoff, size limits, and safe resume only when the server supports range requests.
7. Resolve Java using the system-first policy in Section 4. Do not alter the user's system Java configuration.
8. Respect third-party licenses. Do not redistribute mods or other files unless the applicable licenses and source permissions allow it. Support a user-provided source or authorized host where required.

## 6. Installation layout

Proposed separation of launcher files, runtime, game instance, and user data:

- Launcher application: under Program Files or a user-selected application directory.
- Launcher state: per-user AppData for settings, profiles, logs, cache, and updater staging.
- Managed Java: a dedicated launcher-managed runtime directory, separate from system Java.
- Game instance: a user-selected directory, separate from launcher binaries and runtime files.
- Pack-managed files: tracked in the manifest and installed under the game instance.
- User data: worlds, screenshots, and other unmanaged user files preserved across updates.

Exact paths should be selected during implementation and documented. The launcher must handle paths containing spaces and non-ASCII characters.

## 7. Manifest model

Each managed entry should include:

- normalized relative path;
- expected file size;
- SHA-256 checksum;
- download URL or source identifier;
- managed role (Minecraft client, library, asset, Forge, mod, config, resource, runtime, etc.);
- optional version and compatibility metadata.

The manifest itself must be versioned, size-limited, validated before use, and rejected safely if malformed or unsupported. A manifest must never provide executable commands or arbitrary shell instructions.

Runtime metadata should identify the supported Java major version, architecture, distribution/source, and integrity data. Secrets must not be embedded in the manifest.

## 8. Launch pipeline

1. Load and validate launcher settings and the selected player profile.
2. Verify the game instance and repair required missing or corrupted managed files.
3. Resolve Java using the system-first policy; use the managed runtime only if no compatible system runtime is available or the user explicitly selects it.
4. Resolve Minecraft 1.12.2 metadata, libraries, assets, and native libraries.
5. Resolve the exact Forge build's metadata and legacy launch requirements.
6. Build the classpath and JVM/game arguments from validated metadata and placeholders.
7. Start the Java process in the game instance directory without invoking a shell.
8. Capture process output, lifecycle, exit code, and relevant launcher/game log paths.
9. Present a useful result and diagnostics if startup fails.

## 9. Security and data integrity

- Reject absolute paths, traversal segments, drive prefixes, UNC paths, and unsafe archive entries.
- Restrict downloads to HTTPS except explicitly justified test-only sources.
- Validate manifest schema, size limits, URL hosts, file sizes, and checksums.
- Never execute commands supplied by a manifest or modpack metadata.
- Apply archive extraction limits and verify destination containment.
- Stage downloads and verify files before making them active.
- Do not overwrite or delete unmanaged user data.
- Do not modify system Java settings or other global Windows configuration.
- Avoid elevated permissions unless a clearly documented installation action requires them.

## 10. Risks and external dependencies

- Modpack source files, mod inventory, exact Forge build, and redistribution permissions are not yet available in the repository.
- Forge 1.12.2 may require legacy-specific launch handling; validate against the actual installed Forge output.
- Java compatibility must be confirmed with the real pack. A generic Java version check alone is insufficient.
- Offline-mode servers may reject local offline profiles.
- Native libraries and mod behavior can vary by Windows version and hardware.
- Large downloads require disk-space estimation, interruption recovery, and robust diagnostics.
- Qt/PyInstaller packaging needs clean-machine Windows verification.

## 11. Decisions still requiring real pack inputs

The following must not be guessed during implementation:

- exact Forge build and its launch metadata;
- exact Java vendor/build requirements, if the pack has constraints beyond Java 8 x64;
- mod/config/resource inventory and file ownership rules;
- authorized download sources and redistribution permissions;
- minimum disk space and final installation defaults.

The architecture can be implemented in layers before the modpack is supplied, but real Forge launch and full-pack compatibility cannot be claimed until tested with the actual files.
