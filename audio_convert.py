import re
from pydub import AudioSegment


def convert(filename):

    file = AudioSegment.from_file(filename)

    filepath = replace_extension(filename)

    file.export(filepath, format="mp3")

    return filepath


def replace_extension(filename):
    return re.sub(r'\.[a-z0-9]+$', '.mp3', filename)
