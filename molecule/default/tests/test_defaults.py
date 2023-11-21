import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# def test_libs(host):
#     libs = [
#         "/usr/local/lib/libmp3lame.a",
#         "/usr/local/lib/libmad.a",
#         "/usr/local/lib/libogg.a",
#     ]

#     for lib in libs:
#         f = host.file(lib)
#         assert f.exists
#         assert f.is_file

def test_bins(host):
    bins = [
        "/usr/local/bin/sox"
    ]

    for bin in bins:
        b = host.file(bin)
        assert b.exists
        assert b.is_file

# def test_supported_formats(host):

#     help_output = host.run('/usr/local/bin/sox --help | grep "AUDIO FILE FORMATS:"')

#     assert help_output.rc == 0 , "AUDIO_FILE_FORMATS is missing in sox --help output"

#     # parse the supported formats into a list
#     supported_formats = help_output.stdout.split(":")[1].split()

#     assert "mp3" in supported_formats
#     # assert "ogg" in supported_formats
#     assert "wav" in supported_formats


def test_supported_formats(host):
    # Define list of formats
    formats = [
        "mp3",
        "wav"
        # "ogg"
    ]

    # Generate a file to be converted
    generated_file = host.run('sox -n -r 16000 sample.wav synth 3 sine 500')

    for format in formats:
        c = host.run('sox -r 8000 sample.wav output.{}'.format(format))
        assert c.succeeded