#! /usr/bin/python

import extract_samples

if __name__ == '__main__' :
    drum_samples = extract_samples.extract_drum_samples("Data/Birthday.wav")
    print("Found " + str(len(drum_samples)) + " drum samples")

    drum_samples = extract_samples.extract_drum_samples("Data/Standup.wav")
    print("Found " + str(len(drum_samples)) + " drum samples")
    
    print("Done!")