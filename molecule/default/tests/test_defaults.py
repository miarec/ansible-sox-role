import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_bins(host):
    bins = [
        "/usr/local/bin/sox"
    ]

    for bin in bins:
        b = host.file(bin)
        assert b.exists
        assert b.is_file

def test_supported_formats(host):

    help_output = host.run('/usr/local/bin/sox --help | grep "AUDIO FILE FORMATS:"')

    assert help_output.rc == 0 , "AUDIO_FILE_FORMATS is missing in sox --help output"

    # parse the supported formats into a list
    supported_formats = help_output.stdout.split(":")[1].split()

    assert "mp3" in supported_formats
    assert "wav" in supported_formats
