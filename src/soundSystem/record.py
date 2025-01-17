from scipy.io.wavfile import write
import sounddevice 


def recordAudio(duration, frequency = 44100):
    frames = frequency * duration
    recording = sounddevice.rec(int(frames), samplerate=frequency, channels=1)

    sounddevice.wait()
    
    return recording
  

def saveAudio(audio, frequency = 44100,path=".", filename="recording"):
    saveAudioLocation = f"{path}/{filename}.wav"

    write(saveAudioLocation, frequency, audio)