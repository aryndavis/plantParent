from scipy.io.wavfile import write
import sounddevice as sd
import wavio


def read_audio():
    fs = 44100  # Sample rate
    seconds = 8  # Duration of recording
    filename = 'output.wav'
    print("Start Audio")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    print('End of audio')
    write(filename, fs, myrecording)  # Save as WAV file
    wavio.write(filename, myrecording, fs, sampwidth=2)
    return filename


read_audio()
