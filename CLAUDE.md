This file provides guidance to coding agent when working with code in this repository.

## Repository Overview

This is an Ansible role for installing Sox (Sound eXchange) audio processing tool and its associated libraries. Sox can be installed either from system packages (default) or compiled from source.

## Common Commands

### Linting
```bash
uv run ansible-lint
```

### Testing with Molecule

Run the default test scenario (install from package):
```bash
uv run molecule test
```

Run a specific distro:
```bash
MOLECULE_DISTRO=ubuntu2204 uv run molecule test
```

Run the source installation scenario:
```bash
uv run molecule test -s install-from-source
```

### Molecule Environment Variables
- `MOLECULE_DISTRO`: Target OS (ubuntu2204, ubuntu2404, rockylinux9, rhel9)
- `MOLECULE_SOX_VERSION`: Sox version (default: 14.4.2)
- `MOLECULE_ANSIBLE_VERBOSITY`: 0-3 for ansible output verbosity

## Architecture

### Role Structure
- `tasks/main.yml`: Entry point - routes to either package or source installation based on `sox_install_from_source`
- `tasks/install_from_package.yml`: Package manager installation
- `tasks/install_from_source.yml`: Source compilation workflow
- `tasks/install_libraries_from_source.yml`: Handles library compilation (lame, libmad, and optional libs)
- `tasks/patch_libmad.yml`: Patches libmad for modern compilers
- `defaults/main.yml`: All configurable variables with defaults
- `vars/`: OS-specific variables (Debian.yml, RedHat.yml, Rocky.yml)

### Key Design Decisions
- Default installation method is from package (`sox_install_from_source: false`)
- CentOS/RHEL 7 requires source compilation for MP3 support (package install will fail with error)
- Rocky Linux/AlmaLinux/RHEL 8+ require CRB (CodeReady Builder) repo for libmad dependency
- ARM architecture (aarch64) support: config.guess/config.sub are copied from system automake for lame/libmad
- Libraries are compiled before Sox to ensure format support
- Optional formats (ogg, flac) require both library installation and Sox configure flags
- Library installation order matters (e.g., libvorbis depends on libogg)

### Variable Configuration System
Two main configuration dictionaries control optional format support:
- `sox_compile_optional_formats_config`: Defines formats with their configure args and required libraries
- `sox_compile_optional_library_config`: Defines library download/build details

Base libraries (lame, libmad) are always installed when compiling from source via `sox_compile_base_library_config`.
