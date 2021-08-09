import subprocess
from os import listdir, makedirs, walk
from os.path import join, isdir, isfile, dirname
from uuid import uuid4
# this script splits big noise files into smaller chunks of N seconds more
# similar to the duration of a wake word


def split_into_chunks(SOURCE_DIR, DEST_DIR, seconds=3):
    if not isdir(DEST_DIR):
        makedirs(DEST_DIR)

    exts = ["wav"]
    for wav in listdir(SOURCE_DIR):
        if wav.split(".")[-1] not in exts:
            # non audio file, skip
            if isdir(join(SOURCE_DIR, wav)):
                # TODO recursive
                print("skipping directory", wav)
            else:
                print("unrecognized format, skipping", wav)
            continue
        print("converting ", wav)

        converted = join(DEST_DIR, str(uuid4()))
        wav = join(SOURCE_DIR, wav)

        cmd = ["ffmpeg", "-i", wav, "-f", "segment", "-segment_time",
               str(seconds), "-c", "copy", converted + "%03d.wav"]

        subprocess.call(cmd)


src = "/home/user/Downloads/building_106_kitchen/building_106_kitchen/test"
dst = "/home/user/Downloads/building_106_kitchen/building_106_kitchen/crops"
for root, dirs, files in walk(src, topdown=False):
    path = root
    dest = path.replace(src, dst)
    split_into_chunks(root, dest)
