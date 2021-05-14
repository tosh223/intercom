import numpy as np
import pyaudio
import wave
 
WAVE_FILE = "sample.wav"
INDEX = 0
NUM_FRAMES = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def make_wav_file(file="sample.wav", sec=2):
    pa = pyaudio.PyAudio()
    stream = pa.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = NUM_FRAMES)
    
    print("Now Recording...")
    chunked_waves = []
    for _ in range(0, int(RATE / NUM_FRAMES * sec)):
        chunked_waves.append(stream.read(NUM_FRAMES))
    stream.close()
    pa.terminate()
    print("Recording Finished.")

    wavFile = wave.open(WAVE_FILE, 'wb')
    wavFile.setnchannels(CHANNELS)
    wavFile.setsampwidth(pa.get_sample_size(FORMAT))
    wavFile.setframerate(RATE)
    wavFile.writeframes(b"".join(chunked_waves))
    wavFile.close()

if __name__ == "__main__":
    make_wav_file(file="sample.wav", sec=2) 