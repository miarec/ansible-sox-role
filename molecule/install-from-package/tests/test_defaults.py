import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_libs(host):
    if host.system_info.distribution == "centos":
        libs = [
            "/lib64/libogg.so.0",
            "/lib64/libmad.so.0",
            "/lib64/libmp3lame.so.0"
        ]

    if host.system_info.distribution == "ubuntu":
        libs = [
            "/lib/x86_64-linux-gnu/libogg.so.0",
            "/lib/x86_64-linux-gnu/libmad.so.0",
            "/lib/x86_64-linux-gnu/libmp3lame.so.0"
        ]

    for lib in libs:
        f = host.file(lib)
        assert f.exists
        assert f.is_file

def test_bins(host):
    bins = [
        "/usr/bin/sox"
    ]

    for bin in bins:
        b = host.file(bin)
        assert b.exists
        assert b.is_file
