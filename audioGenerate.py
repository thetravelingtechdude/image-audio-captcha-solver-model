#!/usr/bin/env python3

import os
import random
import argparse
from gtts import gTTS
from sys import exit

def scramble_audio_name(audio_name):
    import hashlib
    m = hashlib.sha1()
    m.update(audio_name.encode('utf-8'))
    return m.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', help='Length of captchas in characters', type=int)
    parser.add_argument('--count', help='How many captchas to generate', type=int)
    parser.add_argument('--scramble', help='Whether to scramble image names', default=False, action='store_true')
    parser.add_argument('--output-dir', help='Where to store the generated captchas', type=str)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    args = parser.parse_args()

    if args.length is None:
        print("Please specify the captcha length")
        exit(1)

    if args.count is None:
        print("Please specify the captcha count to generate")
        exit(1)

    if args.output_dir is None:
        print("Please specify the captcha output directory")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    symbols_file.close()

    print("Generating audio file captchas with symbol set {" + captcha_symbols + "}")

    if not os.path.exists(args.output_dir):
        print("Creating output directory " + args.output_dir)
        os.makedirs(args.output_dir)

    for i in range(args.count):
        captcha_text = ''.join([random.choice(captcha_symbols) for j in range(args.length)])
        audio_name_scrambled = captcha_text
        if args.scramble:
            audio_name_scrambled = scramble_audio_name(captcha_text)
        tts = gTTS(text=captcha_text, lang='en')

        audio_path = os.path.join(args.output_dir, audio_name_scrambled+'.mp3')
        if os.path.exists(audio_path):
            version = 1
            while os.path.exists(os.path.join(args.output_dir, audio_name_scrambled + '_' + str(version) + '.mp3')):
                version += 1
            audio_path = os.path.join(args.output_dir, audio_name_scrambled + '_' + str(version) + '.mp3')

        tts.save(audio_path)

    print("Audio file captchas generated successfully!")

if __name__ == '__main__':
    main()
