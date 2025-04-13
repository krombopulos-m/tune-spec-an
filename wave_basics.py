# https://www.youtube.com/watch?v=n2FKsPt83_A&t=940s 

import wave
import matplotlib.pyplot as plt
import numpy as np

song = wave.open(r'C:\Users\zolse\VSCode Projects\Projects\spec_anlyz\SAINt JHN - Still Mine.wav', 'r')

# read wav

sample_freq = song.getframerate()            # frame rate
n_samples = song.getnframes()                # no. of frames in .wav
signal_wave = song.readframes(-1)            # -1 reads all frames. number >0 reads selected frame

print('CHANNELS:', song.getnchannels())      # audio source
print("Sample Width:", song.getsampwidth())  # bytes per sample    
print('Frame Rate:', sample_freq)    
print('No. Frames:', n_samples)      
print('Parameters:', song.getparams())

t_audio = song.getnframes() / sample_freq
print('Wav time (s):', t_audio)

print(type(signal_wave), type(signal_wave[0]))
print('Frames:', len(signal_wave)/2)


# plot wav

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
time = np.linspace(0,t_audio, num=n_samples*2)

plt.figure(figsize=(15,5))
plt.plot(time, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0,t_audio)
plt.show()



# my code playing around with wave
print('\n\n')

nchannels = song.getnchannels()
sampwidth = song.getsampwidth()
framerate = song.getframerate()
nframes = song.getnframes()
compressiontype = song.getcomptype()
compressionname = song.getcompname()
params = song.getparams()
markers = song.getmarkers()
readframes = song.readframes(nframes)
rewind = song.rewind()
setpos = song.setpos()
currentposition = song.tell()

print(song)









song.close()








