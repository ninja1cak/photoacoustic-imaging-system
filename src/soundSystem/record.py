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


def getPeakSignalAroundFreqLaser(frequencyLaser, signalAudioInFrequency):
    BOUND_FREQUENCY = 500
    lowerBoundFrequency = frequencyLaser - BOUND_FREQUENCY
    upperBoundFrequency = frequencyLaser + BOUND_FREQUENCY

    indexLowerBoundFrequency = lowerBoundFrequency * 2
    indexUpperBoundFrequency = upperBoundFrequency * 2

    peakSignal, indexPeakSignal = _getMaxValueWithIndex(signalAudioInFrequency[indexLowerBoundFrequency:indexUpperBoundFrequency])
    frequencyPeakSignal = (indexPeakSignal/2) + lowerBoundFrequency
    return frequencyPeakSignal, peakSignal

def _getMaxValueWithIndex(signal):
    value = numpy.max(signal)
    index = numpy.argmax(signal)

    return value, index
