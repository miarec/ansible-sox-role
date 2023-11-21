import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# def test_libs(host):
#     if host.system_info.distribution == "centos":
#         libs = [
#             "/lib64/libogg.so.0",
#             "/lib64/libmad.so.0",
#             "/lib64/libmp3lame.so.0"
#         ]

#     if host.system_info.distribution == "ubuntu":
#         libs = [
#             "/lib/x86_64-linux-gnu/libogg.so.0",
#             "/lib/x86_64-linux-gnu/libmad.so.0",
#             "/lib/x86_64-linux-gnu/libmp3lame.so.0"
#         ]

#     for lib in libs:
#         f = host.file(lib)
#         assert f.exists
#         assert f.is_file

def test_bins(host):
    bins = [
        "/usr/bin/sox"
    ]

    for bin in bins:
        b = host.file(bin)
        assert b.exists
        assert b.is_file

# Move this to testing files by generating and then converting files
# def test_supported_formats(host):

#     help_output = host.run('/usr/bin/sox --help | grep "AUDIO FILE FORMATS:"')

#     assert help_output.rc == 0 , "AUDIO_FILE_FORMATS is missing in sox --help output"

#     # parse the supported formats into a list
#     supported_formats = help_output.stdout.split(":")[1].split()

#     assert "mp3" in supported_formats
#     assert "ogg" in supported_formats
#     assert "wav" in supported_formats

def test_supported_formats(host):
    # Define list of formats
    formats = [
        "mp3",
        "wav",
        "ogg"
    ]

    # Generate a file to be converted
    generated_file = host.run('sox -n -r 16000 sample.wav synth 3 sine 500')

    for format in formats:
        c = host.run('sox -r 8000 sample.wav output.{}'.format(format))
        assert c.succeeded