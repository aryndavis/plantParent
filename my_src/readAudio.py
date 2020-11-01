from scipy.io.wavfile import write
import sounddevice as sd


def read_audio():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    filename = 'output.wav'

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write(filename, fs, myrecording)  # Save as WAV file
    return filename
