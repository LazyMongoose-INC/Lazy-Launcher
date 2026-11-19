# Development Roadmap

## Phase 1 — Audit and Architecture
- [x] Inspect repository metadata, files, branches, history, releases and issues
- [x] Document baseline audit
- [x] Propose architecture and stack
- [x] Identify blockers and risks
- [ ] Review architecture document and approve scope before broad implementation

## Phase 2 — Application Skeleton
- [ ] Create package structure and application entry point
- [ ] PySide6 main window and theme
- [ ] Validated settings and local profile persistence
- [ ] Logging and diagnostics
- [ ] Unit tests and CI baseline

## Phase 3 — Download/Manifest
- [ ] Manifest schema/version validation
- [ ] HTTP streaming, timeouts, progress, retry/backoff
- [ ] Resume support where safe
- [ ] SHA-256/size verification
- [ ] Safe destination paths
- [ ] Test coverage

## Phase 4 — Minecraft Runtime
- [ ] Version metadata handling for 1.12.2
- [ ] Libraries/assets/natives resolver
- [ ] Java 8 discovery and managed runtime
- [ ] Launch argument builder
- [ ] Real vanilla 1.12.2 smoke test

## Phase 5 — Forge
- [ ] Identify exact Forge build from pack input
- [ ] Install/resolve Forge client files
- [ ] Forge launch metadata and classpath
- [ ] Real Forge launch smoke test

## Phase 6 — Modpack Integration
- [ ] Obtain legally distributable pack files or user-provided source
- [ ] Inventory and dependency review
- [ ] Build versioned manifest
- [ ] Install mods/configs/resources
- [ ] Verify complete pack startup and mod loading

## Phase 7 — Offline Profiles and Networking
- [ ] Nickname validation and persistence
- [ ] Offline UUID handling
- [ ] Singleplayer and LAN validation
- [ ] Server IP/port helper
- [ ] Clearly communicate online-auth server limitation

## Phase 8 — Updates
- [ ] Pack manifest/version check
- [ ] Incremental file updates
- [ ] Staging, rollback and repair
- [ ] Preserve worlds and user files

## Phase 9 — Stabilization
- [ ] Unit and integration test expansion
- [ ] Windows smoke tests
- [ ] Crash/error diagnostics
- [ ] Performance and UX checks

## Phase 10 — Release
- [ ] Windows build
- [ ] Installer, shortcuts and uninstall
- [ ] Clean Windows install verification
- [ ] Full pack launch verification
- [ ] Documentation and changelog
- [ ] GitHub Release

## Completion policy
A phase is marked complete only after its implementation and tests are recorded. A CI-only launch simulation does not count as a real Minecraft launch test.
