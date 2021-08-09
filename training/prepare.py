# this will take the data from an organized folder and symlink it in a ready
# for training format
import os
from os.path import isdir, join
from os import makedirs
import random

hotwords = ["android"]

noise_folders = ["eltocino", # eltocino noise from precise community repo
                 "cropped_bg", # google commands, background noises cropped in 3 second chunks
                 "false_activations",  # false activations collected over time
                 "cropped_sounds", # public domain sounds cropped in 3 second chunks
                 "bg_noise" # "poluted silence"
                 ]

RAW_DATA_PATH = "/opt/precise/wake-words/wake-words"
COMMANDS_DATA_PATH = "/opt/precise/wake-words/commands"
NOT_WW_DATA_PATH = "/opt/precise/wake-words/not-wake-words"
NOISE_DATA_PATH = "/opt/precise/wake-words/noise"
TRAINING_PATH = "/opt/precise/training"


def create_dirs():
    # create training dirs
    for w in hotwords:
        p = join(TRAINING_PATH, w)
        if not isdir(p):
            makedirs(p)
        p = join(TRAINING_PATH, w, "wake-word")
        if not isdir(p):
            makedirs(p)
        p = join(TRAINING_PATH, w, "not-wake-word")
        if not isdir(p):
            makedirs(p)
        p = join(TRAINING_PATH, w, "test")
        if not isdir(p):
            makedirs(p)
        p = join(TRAINING_PATH, w, "test/wake-word")
        if not isdir(p):
            makedirs(p)
        p = join(TRAINING_PATH, w, "test/not-wake-word")
        if not isdir(p):
            makedirs(p)


def symlink_noises():
    # symlink files
    for word in hotwords:
        out_folder = join(TRAINING_PATH, word)

        for fold in noise_folders:

            w_path = join(NOISE_DATA_PATH, fold)

            wav_files = os.listdir(w_path)
            random.shuffle(wav_files)
            random.shuffle(wav_files)
            total_files = len(wav_files)
            train = wav_files[:int(total_files / 2)]
            test = wav_files[int(total_files / 2):]
            for f in train:
                src = join(w_path, f)
                dst = join(out_folder, "not-wake-word", f)
                try:
                    print("symlink", src, dst)
                    os.symlink(src, dst)
                except:
                    pass

            for f in test:
                src = join(w_path, f)
                dst = join(out_folder, "test", "not-wake-word", f)
                try:
                    print("symlink", src, dst)
                    os.symlink(src, dst)
                except:
                    pass


def symlink_data():
    for word in hotwords:
        out_folder = join(TRAINING_PATH, word)
        w_path = join(RAW_DATA_PATH, word)

        wav_files = os.listdir(w_path)
        random.shuffle(wav_files)
        random.shuffle(wav_files)
        total_files = len(wav_files)
        train = wav_files[:3 * int(total_files / 4)]
        test = wav_files[3 * int(total_files / 4):]

        for w in train:
            src = join(w_path, w)
            dst = join(out_folder, "wake-word", w)
            try:
                print("symlink", src, dst)
                os.symlink(src, dst)
            except:
                pass

        for w in test:
            src = join(w_path, w)
            dst = join(out_folder, "test", "wake-word", w)
            try:
                print("symlink", src, dst)
                os.symlink(src, dst)
            except:
                pass


def symlink_not_ww():
    # symlink files
    for word in hotwords:
        out_folder = join(TRAINING_PATH, word)
        wav_files = os.listdir(NOT_WW_DATA_PATH)
        random.shuffle(wav_files)
        random.shuffle(wav_files)
        total_files = len(wav_files)
        train = wav_files[:int(total_files / 2)]
        test = wav_files[int(total_files / 2):]
        for f in train:
            src = join(NOT_WW_DATA_PATH, f)
            dst = join(out_folder, "not-wake-word", f)
            try:
                print("symlink", src, dst)
                os.symlink(src, dst)
            except:
                pass

        for f in test:
            src = join(NOT_WW_DATA_PATH, f)
            dst = join(out_folder, "test", "not-wake-word", f)
            try:
                print("symlink", src, dst)
                os.symlink(src, dst)
            except:
                pass


def symlink_commands():
    # symlink files

    cmd_folders = os.listdir(COMMANDS_DATA_PATH)

    for word in hotwords:
        out_folder = join(TRAINING_PATH, word)

        for fold in cmd_folders:

            w_path = join(COMMANDS_DATA_PATH, fold)

            wav_files = os.listdir(w_path)
            random.shuffle(wav_files)
            random.shuffle(wav_files)
            total_files = len(wav_files)
            train = wav_files[:int(total_files / 2)]
            test = wav_files[int(total_files / 2):]
            for f in train:
                src = join(w_path, f)
                dst = join(out_folder, "not-wake-word", f)
                try:
                    print("symlink", src, dst)
                    os.symlink(src, dst)
                except:
                    pass

            for f in test:
                src = join(w_path, f)
                dst = join(out_folder, "test", "not-wake-word", f)
                try:
                    print("symlink", src, dst)
                    os.symlink(src, dst)
                except:
                    pass


def symlink_other_words():
    # symlink files

    word_folders = os.listdir(RAW_DATA_PATH)

    for word in hotwords:
        out_folder = join(TRAINING_PATH, word)

        for fold in [w for w in word_folders if w != word]:

            w_path = join(RAW_DATA_PATH, fold)

            wav_files = os.listdir(w_path)
            random.shuffle(wav_files)
            random.shuffle(wav_files)
            total_files = len(wav_files)
            train = wav_files[:int(total_files / 2)]
            test = wav_files[int(total_files / 2):]
            for f in train:
                src = join(w_path, f)
                dst = join(out_folder, "not-wake-word", f)
                try:
                    print("symlink", src, dst)
                    os.symlink(src, dst)
                except:
                    pass

            for f in test:
                src = join(w_path, f)
                dst = join(out_folder, "test", "not-wake-word", f)
                try:
                    print("symlink", src, dst)
                    os.symlink(src, dst)
                except:
                    pass


create_dirs()
symlink_noises()  # background noises (no speech)
symlink_not_ww()  # random speech that is not a wake word (false activations)
symlink_commands()     # google speech commands (not a wake word)
symlink_other_words()  # each wake word is a not-wake-word for the others
symlink_data()
