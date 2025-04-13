"""PyAudio Example: Play a wave file."""

import wave
import sys

import pyaudio


CHUNK = 1024
sys.argv.append(r"C:\Users\zolse\VSCode Projects\Projects\spec_anlyz\SAINt JHN - Still Mine.wav")

if len(sys.argv) < 2:
    print(f'Plays a wave file. Usage: {sys.argv[0]} filename.wav')
    sys.exit(-1)

with wave.open(sys.argv[1], 'rb') as wf:
    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()

    #format=p.get_format_from_width(wf.getsampwidth())

    # Open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Play samples from the wave file (3)
    # data = binary data from wav file that is the audio signal
    #data = wf.readframes(CHUNK)
    #while len(data):
    while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
        stream.write(data)
        #j=1

    # Close stream (4)
    stream.close()

    # Release PortAudio system resources (5)
    p.terminate()