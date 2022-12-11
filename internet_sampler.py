#! /usr/bin/python

import extract_samples

if __name__ == '__main__' :
    print("Extracting drum samples from audio files...")
    drum_samples = extract_samples.extract_drum_samples("Data/Birthday.wav")
    for sample in drum_samples:
        print("Drum sample: " + sample) 
    print("Done!")