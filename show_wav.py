"""Combining pyaudio_ex1.py and spec_analyze.py"""

# pyaudio example imports
import wave
import sys
import pyaudio

# youtube spect an imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import time
from tkinter import TclError

# create matplotlib figure and axes
fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))

CHUNK = 1024 * 2             # samples per frame
RATE = 44100                 # samples per second


# variable for plotting
x = np.arange(0, 4*CHUNK, 2)       # samples (waveform)
xf = np.linspace(0, RATE, CHUNK)     # frequencies (spectrum)

# create a line object with random data
line, = ax1.plot(x, np.random.rand(2*CHUNK), '-', lw=2)

# create semilogx line for spectrum
line_fft, = ax2.semilogx(xf, np.random.rand(CHUNK), '-', lw=2)

# Signal range is -32k to 32k
# limiting amplitude to +/- 4k
AMPLITUDE_LIMIT = 40000

# format waveform axes
ax1.set_title('AUDIO WAVEFORM')
ax1.set_xlabel('samples')
ax1.set_ylabel('volume')
ax1.set_ylim(-AMPLITUDE_LIMIT, AMPLITUDE_LIMIT)
ax1.set_xlim(0, 2 * CHUNK)
plt.setp(ax1, xticks=[0, CHUNK, 2 * CHUNK], yticks=[-AMPLITUDE_LIMIT, 0, AMPLITUDE_LIMIT])

# format spectrum axes
ax2.set_xlim(20, RATE / 2)


sys.argv.append(r"C:\Users\zolse\VSCode Projects\Projects\spec_anlyz\SAINt JHN - Still Mine.wav")

if len(sys.argv) < 2:
    print(f'Plays a wave file. Usage: {sys.argv[0]} filename.wav')
    sys.exit(-1)

with wave.open(sys.argv[1], 'rb') as wf:
    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()

    # Open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)



    print('stream started')

    # for measuring frame rate
    frame_count = 0
    start_time = time.time()

    # Play samples from the wave file (3)
    while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
        stream.write(data)

        # binary data
        #data = stream.read(CHUNK)    

        data_np = np.frombuffer(data, dtype='h')
        
        line.set_ydata(data_np)
        
        # compute FFT and update line
        yf = fft(data_np)
        line_fft.set_ydata(np.abs(yf[0:CHUNK])  / (512 * CHUNK))

        # update figure canvas
        try:
            fig.canvas.draw()
            fig.canvas.flush_events()
            frame_count += 1
            
        except TclError:
            
            # calculate average frame rate
            frame_rate = frame_count / (time.time() - start_time)
            
            print('stream stopped')
            print('average frame rate = {:.0f} FPS'.format(frame_rate))
            break

    # Close stream (4)
    stream.close()

    # Release PortAudio system resources (5)
    p.terminate()