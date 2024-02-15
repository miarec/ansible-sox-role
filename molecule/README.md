# Molecule test this role

## Scenario - `default`
This will test the role installing a specific version of Sox from source

Run Molecule test
```
molecule test
```

Run test with variable example
```
MOLECULE_DISTRO=centos7 MOLECULE_SOX_VERSION=14.4.2 molecule test
```

### Molecule variables
 - `MOLECULE_DISTRO` OS of docker container to test, default `ubuntu2204`
   - Tested distros;
    - `ubuntu2204`
    - `ubuntu2004`
    - `centos7`
    - `rockylinux8`
    - `rockylinx9`
    - `rhel7`
    - `rhel8`
    - `rhel9`
 - `MOLECULE_SOX_VERSION` defines variable `sox_version`, default `14.4.2`
 - `MOLECULE_LIBMAD_VERSION` defines variable `libmad_version`, default `0.15.1b`
 - `MOLECULE_LIBOGG_VERSION` defines variable `libogg_version`, default `1.3.3`
 - `MOLECULE_LAME_VERSION` defines variable `lame_version`, default `3.99.5`


## Scenario - `install-from-package`
This will test installing Sox from package

Run Molecule test
```
molecule test -s install-from-package
```

Run test with variable example
```
MOLECULE_DISTR0=centos7 molecule test -s install-from-package
```

### Molecule variables
 - `MOLECULE_DISTRO` OS of docker container to test, default `ubuntu2204`
   - Tested distros
    - `ubuntu2204`
    - `ubuntu2004`
    - `centos7`
    - `rockylinux8`
    - `rockylinx9`
    - `rhel7`
    - `rhel8`
    - `rhel9`