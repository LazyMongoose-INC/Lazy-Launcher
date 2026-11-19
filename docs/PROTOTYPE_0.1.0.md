# Lazy Launcher 0.1.0 — scope and verification

## Implemented in this branch
- Windows desktop UI (PySide6).
- Select an existing Minecraft game directory / launcher instance.
- Detect Forge 1.12.2 profile through version JSON.
- Local offline nickname and canonical Minecraft offline UUID.
- Java 8 x64 discovery/validation or manual executable path.
- Parent version metadata and legacy minecraftArguments.
- Library classpath, native extraction with path traversal checks.
- Real Java child process with stdout/stderr merged into launcher log.
- Local profile persistence, RAM selection.

## Not implemented
- Download/installation of Minecraft, Forge, Java, mod JARs, configs or resources.
- Modpack manifest, file hashes, incremental updates, recovery.
- Microsoft authentication (intentionally out of scope).
- Installer, signed executable, automatic updates, server list.
- Verified compatibility with every possible third-party launcher directory layout.

## Test status
Automated unit tests cover nickname validation, offline UUID generation, version-profile discovery and command construction. Windows CI builds a portable folder artifact. These tests do not prove a real Minecraft launch.

## Manual acceptance required
On a Windows PC with the actual LazyMongoose instance installed:
1. Select its game directory.
2. Confirm detected Forge profile is 1.12.2-forge-14.23.5.2860 (or the exact installed folder name).
3. Select Java 8 x64.
4. Launch and verify the Minecraft main menu, all 180 expected mod IDs, and entry into a world.
5. Exit and inspect the launcher log.

Any missing libraries/assets or incompatible Forge JSON must be fixed against the real installation; the launcher intentionally does not fetch unknown files.
