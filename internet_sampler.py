#! /usr/bin/python

import extract_samples
import os

if __name__ == '__main__' :

    # Delete Samples directory and files inside it if it already exists
    if os.path.exists("Samples"):
        for file in os.listdir("Samples"):
            os.remove("Samples/" + file)
        os.rmdir("Samples")

    drum_samples = extract_samples.extract_drum_samples("Data/Birthday.wav")
    print("Found " + str(len(drum_samples)) + " drum samples")

    # drum_samples = extract_samples.extract_drum_samples("Data/Standup.wav")
    # print("Found " + str(len(drum_samples)) + " drum samples")
    
    print("Done!")