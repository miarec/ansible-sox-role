# ansible-sox-role
![CI](https://github.com/miarec/ansible-role-sox/actions/workflows/ci.yml/badge.svg?event=push)

Ansible role for installation of the following

   - [sox](https://sourceforge.net/projects/sox/) - sound processing utilities
   - [libmad](https://github.com/markjeee/libmad) - MPEG audio decoder library
   - [lame](https://lame.sourceforge.io/) - MPEG Audio Layer III (MP3) encoder.
   - [libogg](https://www.xiph.org/ogg/) - Library of media codecs

## Role Variables

Installation varaiables
  - `sox_install_from_source` when true, libraries and Sox will be installed from source, default = `true`

Version varaiables (when `sox_install_from_source` = true )
  - `sox_version` default `14.4.2`
  - `libmad_version`default `0.15.1b`
  - `lame_version` default `3.99.5`
  - `libogg_version` default `1.3.3`

## Example Playbook

Install from package
```yaml
- name: Install Sox
  hosts:
    - all
  pre_tasks:
    - set_fact:
        sox_install_from_source: false
  become: true
  roles:
    - role: 'sox'
  tags: 'sox'
```

Install from source
```yaml
- name: Install Sox
  hosts:
    - all
  pre_tasks:
    - set_fact:
        sox_install_from_source: true
        sox_version: 14.4.2
  become: true
  roles:
    - role: 'sox'
  tags: 'sox'
```