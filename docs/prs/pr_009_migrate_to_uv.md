## Summary

Migrate the project's dependency management from pip with requirements.txt files to [uv](https://docs.astral.sh/uv/), a fast Python package installer and resolver. This modernizes the development workflow while also changing the default installation method from source compilation to package-based installation.

---

## Purpose

- **Simplify dependency management**: Replace scattered `test-requirements.txt` files with a single `pyproject.toml` and lockfile
- **Faster CI**: uv is significantly faster than pip for dependency resolution and installation
- **Modern tooling**: Align with current Python ecosystem best practices
- **Reduce maintenance burden**: Remove support for deprecated platforms (CentOS 7, RHEL 7/8, Ubuntu 20.04)
- **Improve default behavior**: Package installation is simpler and more appropriate for most use cases

---

## Testing

* [x] Added/updated tests
* [x] Ran `uv run ansible-lint`
* Notes: Linting passes with 0 failures and 0 warnings. Molecule tests updated for new workflow.

---

## Related Issues

N/A

---

## Changes

**Dependency Management**
* Add `pyproject.toml` with uv-managed dev dependencies
* Add `uv.lock` for reproducible builds
* Remove all `test-requirements.txt` files
* Add `ansible.cfg` for proper role path configuration

**CI/CD Updates**
* Update GitHub Actions to use `astral-sh/setup-uv@v4` instead of pip
* Change all `molecule` commands to `uv run molecule`
* Pin CI runner to `ubuntu-22.04` for consistency
* Remove deprecated distros from test matrix (centos7, rhel7, rhel8, ubuntu2004, rockylinux8)

**Default Behavior Change**
* Change `sox_install_from_source` default from `true` to `false`
* Rename `install-from-package` scenario to `install-from-source` (flipping the default)
* Update tests to verify `/usr/bin/sox` for package installs

**Platform Support Updates**
* Add CRB (CodeReady Builder) repository enablement for EL8+ package installation
* Fix ARM architecture (aarch64) builds by copying config.guess/config.sub from system automake
* Remove CentOS 7 and RHEL 7/8 from supported platforms
* Update platform versions in `meta/main.yml`

**Code Quality**
* Fix Ansible facts access pattern (`ansible_os_family` -> `ansible_facts['os_family']`)
* Fix file mode strings (octal `0644` -> string `"0644"`)
* Rename `configure_libmad.yml` to `patch_libmad.yml` for clarity
* Remove `.yamllint` (using ansible-lint's built-in YAML linting)
* Add CLAUDE.md and AGENTS.md for AI agent guidance

**Documentation**
* Rewrite README examples to use role parameters instead of pre_tasks
* Add Testing section to README with uv commands
* Update molecule/README.md with new commands and distro list

---

## Notes for Reviewers

**Breaking Changes:**
- Default installation method changed from source to package
- Dropped support for CentOS 7, RHEL 7, RHEL 8, Rocky Linux 8, and Ubuntu 20.04
- Users who relied on `sox_install_from_source: true` as the default will need to explicitly set it

**Migration:**
- Existing playbooks using this role with default settings will now install Sox from packages instead of compiling from source
- CentOS 7/RHEL 7 users must upgrade to supported platforms

---

## Docs

* [x] Updated relevant documentation
