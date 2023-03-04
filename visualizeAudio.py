import wave
import numpy as np

#WAVE AUDIO SETUP
wav_obj = wave.open('WAVE FILE NAME HERE WITH .WAV ENDING', 'rb')

sample_freq = wav_obj.getframerate()
sample_freq

n_samples = wav_obj.getnframes()
n_samples

t_audio = n_samples/sample_freq
t_audio

n_channels = wav_obj.getnchannels()
n_channels

signal_wave = wav_obj.readframes(n_samples)

#NUMPY STUFF
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

times = np.linspace(0, n_samples/sample_freq, num=n_samples)

import matplotlib.pyplot as plt

#PLOT ONE
plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Left Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()

#PLOT TWO
plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()