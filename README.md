# ansible-sox-role
![CI](https://github.com/miarec/ansible-role-sox/actions/workflows/ci.yml/badge.svg?event=push)

Ansible role for installation of Sox

## Role Variables


- `sox_install_from_source` when true, libraries and Sox will be installed from source, default = `true`

- `sox_version` default `14.4.2`
- `libmad_version`default `0.15.1b`
- `lame_version` default `3.99.5`
- `libogg_version` default `1.3.3`
- `flac_version` default `1.3.2`

## Example Playbook

Install from package
```yaml
- name: Install Sox
  hosts:
    - all
  pre_tasks:
    - set_fact:
        sox_install_from_source: false
      failed_when: false
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