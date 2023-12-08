# ansible-sox-role
![CI](https://github.com/miarec/ansible-role-sox/actions/workflows/ci.yml/badge.svg?event=push)

Ansible role for installation of [sox](https://sourceforge.net/projects/sox/) - sound processing utilities


## Role Variables

### Installation varaiables
  - `sox_install_from_source` when true, libraries and Sox will be installed from source, default = `true`
  > **_NOTE:_** package installation is not supported on centos7 hosts.  Sox has to be compiled to support mp3 on Centos7

### Install from Source variables

Sox variables
  - `sox_version` default `14.4.2`

Optional Format variables:

 - `sox_compile_optional_library_config` defines information about

```yaml
sox_compile_optional_library_config:
  flac:
    version: 1.3.2
    download_url: "https://ftp.osuosl.org/pub/xiph/releases/flac/flac-1.3.2.tar.xz"
    download_dir: "{{ compile_default_download_dir }}"
    download_checksum: "sha1:2bdbb56b128a780a5d998e230f2f4f6eb98f33ee"
    download_cleanup: true
    configure_args:
    install_dir: "{{ compile_default_install_dir }}"
    library_file: "libFLAC.so"
```

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

Install from pacakage with optional formats
```yaml
- name: Install Sox
  hosts:
    - all
  pre_tasks:
    - set_fact:
        sox_install_from_source: false
        sox_package_optional_formats_config:
          oss:
            packages: [libsox-fmt-oss]
  become: true
  roles:
    - role: 'sox'
  tags: 'sox'
```


sox_package_optional_formats_config: {}
  # oss:
  #   packages: [libsox-fmt-oss]

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

Install from source with optional formats
```yaml
- name: Install Sox
  hosts:
    - all
  pre_tasks:
    - set_fact:
        sox_install_from_source: true
        sox_version: 14.4.2
        sox_compile_optional_formats_config:
          ogg:
            configure_args: "--with-oggvorbis"
            libraries: [libogg, libvorbis]
        sox_compile_optional_library_config:
          libogg:
            version: 1.3.3
            download_url: "http://ftp.osuosl.org/pub/xiph/releases/ogg/libogg-1.3.3.tar.gz"
            download_dir: "{{ compile_default_download_dir }}"
            download_checksum: "sha1:28ba40fd2e2d41988f658a0016fa7b534e509bc0"
            download_cleanup: "{{ compile_default_download_cleanup }}"
            configure_args:
            install_dir: "{{ compile_default_install_dir }}"
            library_file: "libogg.a"
          libvorbis:
            version: 1.3.6
            download_url: "https://ftp.osuosl.org/pub/xiph/releases/vorbis/libvorbis-1.3.6.tar.xz"
            download_dir: "{{ compile_default_download_dir }}"
            download_checksum: "sha1:237e3d1c66452734fd9b32f494f44238b4f0185e"
            download_cleanup: "{{ compile_default_download_cleanup }}"
            configure_args: "--bindir={{ compile_default_install_dir }} --libdir={{ compile_default_install_dir }}"
            install_dir: "{{ compile_default_install_dir }}"
            library_file: "libvorbis.a"
  become: true
  roles:
    - role: 'sox'
  tags: 'sox'

```