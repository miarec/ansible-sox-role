import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_bin(host):
    bins = [
        "/usr/local/bin/sox",
        "/usr/local/bin/flac",
        "/usr/local/bin/metaflac",
    ]
    for bin in bins:
        b = host.file(bin)
        assert b.exists
        assert b.is_file

def test_command(host):
    # Run and check specific status codes in one step
    host.run_expect([0], "sox --version")

