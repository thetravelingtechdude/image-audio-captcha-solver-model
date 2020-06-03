#!/usr/bin/env python3

import argparse
import os
from multiprocessing import Pool
import librosa
import librosa.display
from librosa.feature import melspectrogram
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sg
from sys import exit

def lowpass(signal, cutoff, n=5, sample_freq=44100):
    window = cutoff / (sample_freq / 2)
    b, a = sg.butter(n, window, btype='low', analog=False, output='ba')
    return sg.filtfilt(b, a, signal)


def process(src_fname_path, dest_fname_path):
    if not src_fname_path.endswith('.mp3'):
        return

    try:
        # load and process audio
        audio, sr = librosa.load(src_fname_path)
        # audio = lowpass(audio, cutoff=3000, sample_freq=sr)
        # spec = librosa.stft(np.asfortranarray(audio))
        spec = melspectrogram(audio, sr)
        spec_db = librosa.amplitude_to_db(np.abs(spec))

        # generate plot
        scale = 1
        fig = plt.figure(figsize=(1.28 * scale ,0.64 * scale)) #128x64
        plt.box(False)
        plt.subplots_adjust(left=0, right=1, bottom=0, wspace=0, hspace=0)
        librosa.display.specshow(spec_db, sr=sr, cmap='gray_r', x_axis='time', y_axis='log')
        fig.savefig(dest_fname_path, bbox_inches=None, pad_inches=0)
        plt.close()
        print('{0} -> {1}'.format(src_fname_path, dest_fname_path))
    except Exception as e:
        print('processing {0}: {1}'.format(src_fname_path, e))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src-dir', help='Source directory', type= str)
    parser.add_argument('--dest-dir', help='Destination directory', type = str)
    parser.add_argument('--n', help='Number to processes to run in parallel', type=int, default=4)
    args = parser.parse_args()

    if args.src_dir == args.dest_dir:
        print('source and destination directory must be different!')
        exit(1)

    if not os.path.exists(args.dest_dir):
        os.makedirs(args.dest_dir)

    process_args = []
    for src_fname in os.listdir(args.src_dir):
        src_fname_path = os.path.join(args.src_dir, src_fname)
        dest_fname = src_fname.replace('.mp3', '.png')
        dest_fname_path = os.path.join(args.dest_dir, dest_fname)
        process_args.append((src_fname_path, dest_fname_path))

    with Pool(args.n) as p:
        p.starmap(process, process_args)

    exit(0)

if __name__ == '__main__':
    main()
