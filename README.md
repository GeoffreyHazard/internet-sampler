This is a python script to be run locally by typing `python my-script.py` into a Terminal.

It will generate samples for you in the `/Samples` folder provided.

## Requirements
You will need to download the following python modules, using `pip` or `pip3` etc. depending on python version.

`pip install scipy #python`

`pip install scipy #python`

## How to use
Use command line arguments to pass additional information to the script, such as the radio station ID or the filename for the audio file. For example, you could run the script with the following command:

`python radio_listener.py --station-id 123456 --filename "my-drum-sample"`

This will execute the script and run the program, capturing a drum hit or drum beat from the radio station with ID 123456 and storing it in the "Samples" folder with the specified filename. You will need to update the script to handle these command line arguments and use them to capture the audio and create the text file with the appropriate information


## Common audio formats that should be supported include:
    .wav
    .mp3
    .m4a
    .flac
    .aif

created w/ help from GTPChat!