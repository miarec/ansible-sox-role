import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_libs(host):
    libs = [
        "/usr/local/lib/libmp3lame.a",
        "/usr/local/lib/libmad.a",
        "/usr/local/lib/libogg.a",
    ]

    for lib in libs:
        f = host.file(lib)
        assert f.exists
        assert f.is_file

def test_bins(host):
    bins = [
        "/usr/local/bin/sox"
    ]

    for bin in bins:
        b = host.file(bin)
        assert b.exists
        assert b.is_file

