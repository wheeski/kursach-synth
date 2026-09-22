import tkinter as tk
import numpy as np
import sounddevice as sd

freq = 440
sample_rate = 44100
phase = 0
playing = False

def callback(outdata, frames, time, status):
    global phase
    if playing:
        t = (np.arange(frames) + phase) / sample_rate
        outdata[:, 0] = 0.3 * np.sin(2 * np.pi * freq * t)
        phase += frames
    else:
        outdata[:, 0] = 0

stream = sd.OutputStream(samplerate=sample_rate, channels=1, callback=callback, blocksize=256)
stream.start()

def start_sound(event):
    global playing
    playing = True
    
def stop_sound(event):
    global playing
    playing = False
    
root = tk.Tk()
root.title('Синусоида')

button = tk.Button(root, text="Жми")
button.pack(padx=50, pady=50)

button.bind("<ButtonPress-1>", start_sound)
button.bind("<ButtonRelease-1>", stop_sound)

root.mainloop()