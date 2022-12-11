#!/usr/bin/python
# extractsamples.py

import wave
from scipy.io import wavfile
from scipy import signal
import numpy as np

def extract_drum_samples(audio_file):
  #print "Extracting drum samples from " + audio_file
  print("Extracting drum samples from " + audio_file)

  # Read the audio file and get the sample rate and data
  sample_rate, data = wavfile.read(audio_file)

  # Use a bandpass filter to isolate the frequency range of drums
  filtered_data = bandpass_filter(data, sample_rate, [100, 1000])

  # Use a thresholding algorithm to identify segments of the audio that only contain drums
  drum_segments = detect_drum_segments(filtered_data, sample_rate)

  # Create .wav files for each drum sample and return the file paths
  drum_samples = []
  for segment in drum_segments:
    sample_data = segment[1]
    sample_file = wave.open("drum_sample.wav", "wb")
    sample_file.setnchannels(1)
    sample_file.setsampwidth(2)
    sample_file.setframerate(sample_rate)
    sample_file.writeframes(sample_data)
    drum_samples.append("drum_sample.wav")

  return drum_samples

def detect_drum_segments(audio_data, sample_rate):
  # Set the threshold value for identifying drum segments
  threshold = 0.5

  # Initialize variables to track the start and end of a drum segment
  start_time = None
  end_time = None

  # Initialize a list to store the detected drum segments
  drum_segments = []

  # Iterate through the audio data and detect drum segments
  for i, sample in enumerate(audio_data):
    if sample > threshold:
      # If this is the start of a drum segment, record the start time
      if start_time is None:
        start_time = i / sample_rate
      
      # If this is the end of a drum segment, record the end time and add the segment to the list
      elif end_time is None:
        end_time = i / sample_rate
        drum_segments.append((start_time, end_time))

        # Reset the start and end times for the next segment
        start_time = None
        end_time = None

  return drum_segments

def bandpass_filter(audio_data, sample_rate, frequency_range):

  # Calculate the Nyquist frequency
  nyquist_frequency = sample_rate / 2

  # Calculate the lower and upper bounds of the frequency range
  lower_bound = frequency_range[0] / nyquist_frequency
  upper_bound = frequency_range[1] / nyquist_frequency

  # Calculate the filter coefficients
  b, a = signal.butter(5, [lower_bound, upper_bound], btype='bandpass')

  # Apply the filter to the audio data
  filtered_data = signal.filtfilt(b, a, audio_data)

  return filtered_data
