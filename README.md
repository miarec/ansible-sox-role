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

 - `sox_compile_optional_formats_config` dictionary that defines optional formats that sox should be compiled to support
    - `key` unique name,
      - `configure_args` String of any specific arguements that need to be passed at the configure step of Sox
      - `libraries` list of libraies that need to be installed, this must match a key in `sox_compile_optional_library_config`

    Example `sox_compile_optional_formats_config`
    ```yaml
    sox_compile_optional_formats_config:
      ogg:
        configure_args: "--with-oggvorbis"
        libraries: [libogg, libvorbis]
    ```

 - `sox_compile_optional_library_config` dictionary that defines information about needed to install libraies to support additonal formats
    - `key` unique name, this must match value libraries defined in `sox_compile_optional_formats_config`
        - `version` version of library that will be donwloaded
        - `donload_url` url where library will be downloaded from
        - `download_dir` path where binary will be donloaded to, preference would to be use the same dir for all directories
        - `download_checksum` Optional `[method]:[checksum]`, if no checksum is supplied, it will not be verified
        - `download_cleanup` Optional, if true downloaded and extracted files will be removed after installation
        - `configure_args` String of any specific arguements that need to be passed at the configure step
        - `install_dir` path where binary will be installed to, preference would to be use the same dir for all directories
        - `library_file` library file name, this is used to verify installation

      Example `sox_compile_optional_library_config`
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

### Install from pacakge variables
 - `sox_package_optional_formats_config` Dictionary of optional formats, and associated configuration
    - `key` unique name,
      - `packages` list of any addtional packages that need to be installed

    Example `sox_package_optional_formats_config`
    ```yaml
    sox_package_optional_formats_config: {}
      oss:
        packages: [libsox-fmt-oss]
    ```


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