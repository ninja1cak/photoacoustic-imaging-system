from scipy.io.wavfile import write
import sounddevice 
import scipy.fft
import numpy


def recordAudio(duration, frequency = 44100):
    frames = frequency * duration
    recording = sounddevice.rec(int(frames), samplerate=frequency, channels=1)

    sounddevice.wait()
    
    return recording
  

def saveAudio(audio, frequency = 44100,path=".", filename="recording"):
    saveAudioLocation = f"{path}/{filename}.wav"

    write(saveAudioLocation, frequency, audio)


def transformSignalAudioToFrequency(signalAudio, frequency=44100):
    lengthSignal = len(signalAudio) 
    frequencies = scipy.fft.fftfreq(lengthSignal, d=1/frequency)

    signalAudioInFrequency = scipy.fft.fft(signalAudio)
    signalAudioInFrequencyAbsolute = numpy.abs(signalAudioInFrequency)

    halfIndex = lengthSignal//2

    return frequencies[:halfIndex], signalAudioInFrequencyAbsolute[:halfIndex]


