# Spanish Translation

Spanish Translation of DK64

## Installation
1. Download the latest `translation_spanish.nrm` from Releases.
2. Put the file in your DK64 Recompiled mods folder.
   - Example (Windows): `C:\Users\<YourUser>\AppData\Local\DK64Recompiled\mods`
3. Launch DK64 Recompiled and enable the mod from the mods menu.

## Build Requirements
- `clang`
- `ld.lld`
- `make`
- `RecompModTool` from [N64Recomp](https://github.com/N64Recomp/N64Recomp)

Notes:
- On macOS, Apple Clang is not enough for this target. Use an LLVM toolchain that supports MIPS and point `CC`/`LD` to it if needed.
- On Linux/macOS, ensure `zip` is installed for packaging workflows.

## Building from Source
From the repository root:

```bash
make
```

This builds `build/mod.elf`.

Then package the mod:

```bash
RecompModTool mod.toml C:/path/to/DK64Recompiled/mods
```

PowerShell example:

```powershell
.\RecompModTool.exe .\mod.toml C:\Users\<YourUser>\AppData\Local\DK64Recompiled\mods
```

The produced mod file is named `translation_spanish.nrm`.

## Project Layout
- `src/tag_anywhere.c`: Main gameplay patch logic.
- `mod.toml`: Mod metadata, target game id, and packaging inputs.
- `dk64_decomp/`: Decompiled DK64 source and headers used by the build.
- `Dk64Syms/`: Symbol files used by RecompModTool.

## Credits
See `authors` in `mod.toml` for the full contributor list included in the mod manifest.
