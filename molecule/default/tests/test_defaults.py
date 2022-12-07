import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/usr/local/bin/sox",
        "/usr/local/bin/libFLAC.so",
        "/usr/local/bin/libmp3lame.a",
        "/usr/local/bin/libmad.a",
        "/usr/local/bin/libogg.a",
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists

