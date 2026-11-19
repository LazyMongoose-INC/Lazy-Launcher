<div align="center">

# Lazy Launcher

### Launcher for LazyMongoose Modpack · Minecraft Java Edition 1.12.2

**Install, launch, and maintain your Minecraft modpack from one application.**

<p>
  <strong>English</strong> · <a href="README.md">Русский</a>
</p>

<p>
  <a href="https://github.com/LazyMongoose-INC/Lazy-Launcher"><img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub repository"></a>
  <a href="https://github.com/LazyMongoose-INC/Lazy-Launcher/releases"><img src="https://img.shields.io/badge/Download-Releases-2ea44f?style=for-the-badge&logo=windows" alt="Releases"></a>
  <a href="docs/ROADMAP.md"><img src="https://img.shields.io/badge/Project-Roadmap-59636e?style=for-the-badge" alt="Roadmap"></a>
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Early%20Development-orange?style=flat-square" alt="Early development">
  <img src="https://img.shields.io/badge/Platform-Windows-0078D4?style=flat-square&logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/Minecraft-1.12.2-62B47A?style=flat-square" alt="Minecraft 1.12.2">
  <img src="https://img.shields.io/badge/Forge-Planned-orange?style=flat-square" alt="Forge planned">
</p>

</div>

---

## About

**Lazy Launcher** is a dedicated Windows launcher being developed to install and run the custom **LazyMongoose Modpack** for Minecraft Java Edition 1.12.2.

The user experience is designed around a clear home screen, player profile, game version management, component setup, and a straightforward launch flow.

The goal is to do more than start Minecraft. The launcher is intended to prepare and maintain the complete modpack environment: Minecraft, Forge, Java, mods, configuration files, and additional resources.


## Planned features

The following is the target feature set. Features will be implemented incrementally; the application has not been released yet.

| Feature | Planned functionality |
|---|---|
| Modpack installation | Download and prepare Minecraft 1.12.2 and modpack files |
| Forge | Install and configure the compatible Forge version |
| Java Runtime | Compatible system Java 8 x64 first; managed Java is installed only when needed |
| Player profile | Local player profile with an offline-mode nickname |
| Game launch | Resolve launch arguments and start Minecraft from the launcher |
| Updates | Check the modpack version and download changed files only |
| File verification | Size and SHA-256 checks, detect corrupted files |
| Repair | Re-download missing or corrupted files |
| Save protection | Preserve worlds and user data during updates |
| Diagnostics | Launcher and game logs with actionable error messages |

### User experience

The planned interface follows the familiar workflow of modern Minecraft launchers:

- a home screen with the selected modpack and a Play button;
- installation, update, and verification progress;
- player nickname and launcher settings;
- installation directory selection;
- access to logs and error details;
- background downloads that do not freeze the interface.

## Technology

| Component | Planned technology |
|---|---|
| Language | Python 3.12 |
| UI | PySide6 / Qt Widgets |
| Networking | HTTP(S), streaming downloads, retries |
| File integrity | SHA-256 |
| Settings and profiles | Validated JSON |
| Testing | pytest |
| Windows packaging | PyInstaller; installer technology to be selected for release |
| CI | GitHub Actions |

Technical choices are documented in the architecture proposal and may be adjusted after compatibility testing with the actual modpack.

## Development status

<details>
<summary><strong>Project milestones</strong></summary>

| Phase | Scope | Status |
|---|---|---|
| 1 | Repository audit and architecture | Documentation prepared |
| 2 | Application skeleton and UI | Not started |
| 3 | Downloader, manifest, and file verification | Not started |
| 4 | Minecraft Runtime and Java | Not started |
| 5 | Forge 1.12.2 integration | Not started |
| 6 | LazyMongoose Modpack integration | Waiting for pack files |
| 7 | Local profiles and offline mode | Not started |
| 8 | Updates and repair | Not started |
| 9 | Testing and stabilization | Not started |
| 10 | Windows build and release | Not started |

</details>

**Current status:** project setup and architecture preparation. There is no finished EXE, installer, or public release yet. The exact Forge build and modpack contents must be confirmed from the source pack files.

## Documentation

- [Repository audit](docs/PROJECT_AUDIT.md)
- [Application architecture](docs/ARCHITECTURE.md)
- [Development roadmap](docs/ROADMAP.md)

## Installation

There is no public build available yet. Once a verified release is published, it will be available on the [Releases](https://github.com/LazyMongoose-INC/Lazy-Launcher/releases) page.

Do not download executable files from unofficial sources or treat the source code as a finished launcher before a release is published.

## Important notes

- An offline profile means a local nickname without Microsoft sign-in. It does not replace licensed authentication and cannot access servers that require online-mode authentication.
- Mods and third-party files will only be distributed where permissions and applicable licenses allow it.
- Updates must preserve user worlds and other unmanaged files.
- Java and Forge compatibility will be verified against the actual modpack, not just automated tests.

## Contributing and feedback

Found a bug or have an improvement in mind?

<p>
  <a href="https://github.com/LazyMongoose-INC/Lazy-Launcher/issues"><img src="https://img.shields.io/badge/Report%20a%20Bug-Issues-d73a4a?style=for-the-badge&logo=github" alt="Issues"></a>
  <a href="https://github.com/LazyMongoose-INC/Lazy-Launcher/pulls"><img src="https://img.shields.io/badge/Submit%20a%20Change-Pull%20Requests-8957e5?style=for-the-badge&logo=github" alt="Pull requests"></a>
</p>

Before opening an issue, check whether it has already been reported. When possible, include your Windows version, reproduction steps, and the relevant log.

---

<div align="center">

**Lazy Launcher** · A LazyMongoose project

[Repository](https://github.com/LazyMongoose-INC/Lazy-Launcher) · [Releases](https://github.com/LazyMongoose-INC/Lazy-Launcher/releases) · [Roadmap](docs/ROADMAP.md)

</div>
