# ansible-sox-role
![CI](https://github.com/miarec/ansible-role-sox/actions/workflows/ci.yml/badge.svg?event=push)

Ansible role for installation of Sox, and associated libraries.   Sox can be installed from package or from source.

## Role Variables

### Installation varaiables
  - `sox_install_from_source` when true, libraries and sox will be installed from source, `default = true`
  > **_NOTE:_** package installation is not supported on centos7 hosts.  Sox has to be compiled to support mp3 on Centos7



### `install from source` variables

#### Sox variables
  - `sox_version` default `14.4.2`

  - `sox_download_url` URL where sox should be downloaded from.
  - `sox_verify_checksum` when true, download checksum will be verified, `default = true`
  - `sox_download_dir` directory where files will be downloaded and extracted to, `default = /tmp`
  - `sox_install_dir` directory where sox will be installed, `default = /usr/local/bin`
  - `sox_cleanup_downloads` when true, all downloaded and extracted files will be removed


#### Optional format variables
Optional Formats can be used by installing additonal libraries and compiling sox with configuration flags.
> Define optional format's required libraries and configure argument

Example: `ogg` format requires libraries `libogg` and `libvorbis` and sox must be configured with the `--with-oggvorbis` Configure this with variable `sox_compile_optional_formats_config`

```yaml
sox_compile_optional_formats_config:
  ogg:
    configure_args: "--with-oggvorbis"
    libraries: [libogg, libvorbis]
```

 - `sox_compile_optional_formats_config` dictionary that defines optional formats that sox should be compiled to support
    - `key` unique name for the optional format
      - `configure_args` String of any specific arguements that need to be passed at the configure step of Sox
      - `libraries` list of libraries that need to be installed, this must match a key in `sox_compile_optional_library_config`



> Define addtional libraries

For any additional libraries, information must be supplied

Example: libraries `libogg` and `libvorbis` installation information

```yaml
sox_compile_optional_library_config:
  libogg:
    version: 1.3.3
    download_url: "http://ftp.osuosl.org/pub/xiph/releases/ogg/libogg-1.3.3.tar.gz"
    download_dir: "{{ sox_compile_default_library_download_dir }}"
    download_checksum: "sha1:28ba40fd2e2d41988f658a0016fa7b534e509bc0"
    download_cleanup: "{{ sox_compile_default_library_download_cleanup }}"
    configure_args:
    install_dir: "{{ sox_compile_default_library_install_dir }}"
    library_file: "libogg.a"
  libvorbis:
    version: 1.3.6
    download_url: "https://ftp.osuosl.org/pub/xiph/releases/vorbis/libvorbis-1.3.6.tar.xz"
    download_dir: "{{ sox_compile_default_library_download_dir }}"
    download_checksum: "sha1:237e3d1c66452734fd9b32f494f44238b4f0185e"
    download_cleanup: "{{ sox_compile_default_library_download_cleanup }}"
    configure_args: "--bindir={{ sox_compile_default_library_install_dir }} --libdir={{ sox_compile_default_library_install_dir }}"
    install_dir: "{{ sox_compile_default_library_install_dir }}"
    library_file: "libvorbis.a"
```

 - `sox_compile_optional_library_config` dictionary that defines information about needed to install libraies to support additonal formats
    - `key` unique name, this must match value libraries defined in `sox_compile_optional_formats_config`
        - `version` version of library that will be donwloaded
        - `donload_url` url where library will be downloaded from.
        - `download_dir` path where binlibrary will be donloaded and extracted.
        - `download_checksum` *Optional* `[method]:[checksum]`, if no checksum is supplied, it will not be verified
        - `download_cleanup` *Optional* if true downloaded and extracted files will be removed after installation
        - `configure_args` String of any specific arguements that need to be passed at the configure step of the library.
        - `install_dir` path where library will be installed
        - `library_file` library file name, this is used to verify installation on subsequent runs.



### `install from pacakge`` variables
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

### Install from package
```yaml
- name: Install Sox from package
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

### Install from pacakage with optional formats
```yaml
- name: Install Sox from package with OSS format
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

### Install from source
```yaml
- name: Install Sox from source.
  hosts:
    - all
  pre_tasks:
    - set_fact:
        sox_install_from_source: true
  become: true
  roles:
    - role: 'sox'
  tags: 'sox'
```

### Install from source with optional formats
```yaml
- name: Install Sox from source with OGG format.
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
            download_dir: "{{ sox_compile_default_library_download_dir }}"
            download_checksum: "sha1:28ba40fd2e2d41988f658a0016fa7b534e509bc0"
            download_cleanup: "{{ sox_compile_default_library_download_cleanup }}"
            configure_args:
            install_dir: "{{ sox_compile_default_library_install_dir }}"
            library_file: "libogg.a"
          libvorbis:
            version: 1.3.6
            download_url: "https://ftp.osuosl.org/pub/xiph/releases/vorbis/libvorbis-1.3.6.tar.xz"
            download_dir: "{{ sox_compile_default_library_download_dir }}"
            download_checksum: "sha1:237e3d1c66452734fd9b32f494f44238b4f0185e"
            download_cleanup: "{{ sox_compile_default_library_download_cleanup }}"
            configure_args: "--bindir={{ sox_compile_default_library_install_dir }} --libdir={{ sox_compile_default_library_install_dir }}"
            install_dir: "{{ sox_compile_default_library_install_dir }}"
            library_file: "libvorbis.a"
  become: true
  roles:
    - role: 'sox'
  tags: 'sox'

```