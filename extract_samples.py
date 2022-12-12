#!/usr/bin/python
# extractsamples.py

import wave
from scipy.io import wavfile
from scipy import signal
import numpy as np
import struct
import uuid
import csv
import os


# Set the threshold value for identifying drum segments
threshold = 0.255
freq_range = [100, 1000]

def extract_drum_samples(audio_file):
  #print "Extracting drum samples from " + audio_file
  print("Extracting drum samples from " + audio_file)

  # Create a Samples directory if it doesn't already exist
  if not os.path.exists("Samples"):
    os.makedirs("Samples")

  # Open the csv file for writing and create a csv writer object
  csv_file = open("Samples/samples.csv", "a")
  csv_writer = csv.writer(csv_file)

  # Read the audio file and get the sample rate and data
  sample_rate, data = wavfile.read(audio_file)

  # Use a bandpass filter to isolate the frequency range of drums
  filtered_data = bandpass_filter(data, sample_rate, freq_range)

  # Use a thresholding algorithm to identify segments of the audio that only contain drums
  drum_segments = detect_drum_segments(filtered_data, sample_rate)

  # Create .wav files for each drum sample and return the file paths
  drum_samples = []
  for segment in drum_segments:
    sample_data = segment[1]

    # Make sure sample_data is a sequence of floating-point numbers
    if not isinstance(sample_data, (list, tuple)):
      sample_data = [sample_data]
    
    # Convert the sample data from floating-point numbers to bytes
    byte_data = struct.pack('f' * len(sample_data), *sample_data)

    # Generate a unique number id for the sample
    sample_id = str(uuid.uuid4())

    # Create a .wav file for the sample with the unique id as the file name
    sample_file = wave.open("Samples/" + sample_id + ".wav", "wb")

    sample_file.setnchannels(1)
    sample_file.setsampwidth(2)
    sample_file.setframerate(sample_rate)

    # Write the byte data to the file
    sample_file.writeframes(byte_data)
    drum_samples.append(sample_id + ".wav")

    # Write a row to the csv file with the sample id and the file name
    csv_writer.writerow([sample_id, audio_file])
  
  csv_file.close()
  return drum_samples

def detect_drum_segments(audio_data, sample_rate):

  # Initialize variables to track the start and end of a drum segment
  start_time = None
  end_time = None

  # Initialize a list to store the detected drum segments
  drum_segments = []

  # Iterate through the audio data and detect drum segments
  for i, sample in enumerate(audio_data):
    # Check if any element of the sample is above the threshold
    if np.any(sample > threshold):
      # If this is the start of a drum segment, record the start time
      if start_time is None:
        start_time = i / sample_rate
      
      # If this is the end of a drum segment, record the end time and add the segment to the list
      elif end_time is not None:
        drum_segments.append((start_time, end_time))

        # Reset the start and end times for the next segment
        start_time = None
        end_time = None

    # If we are in the middle of a drum segment, update the end time
    elif start_time is not None:
      end_time = i / sample_rate

  return drum_segments

def bandpass_filter(data, sample_rate, freq_range):
  b, a = signal.butter(5, freq_range, btype='bandpass', fs=sample_rate)
  return signal.lfilter(b, a, data)
