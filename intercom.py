from typing import List
from pyaudio import paInt16, PyAudio
import wave

FORMAT = paInt16
CHANNELS = 2    # 1:Monaural, 2:Stereo
RATE = 44100    # 441.kHz
CHUNK = 1024

def make_wav_file(frames: List, wav_file: str='intercom.wav'):
    with wave.open(wav_file, 'wb') as wavFile:
        wavFile.setnchannels(CHANNELS)
        wavFile.setsampwidth(PyAudio.get_sample_size(FORMAT))
        wavFile.setframerate(RATE)
        wavFile.writeframes(b''.join(frames))

def listen(sec: int=2) -> list:
    try:
        frames = []
        p = PyAudio()

        with p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK) as stream:
            print("Now Recording...")

            max_range = int(RATE / CHUNK * sec)
            for _ in range(max_range):
                frames.append(stream.read(CHUNK))
            print("Recording Finished.")
        
        return frames

    except Exception as e:
        print(e)

    finally:
        p.terminate()

if __name__ == "__main__":
    make_wav_file(frames=listen(), wav_file="test.wav") 