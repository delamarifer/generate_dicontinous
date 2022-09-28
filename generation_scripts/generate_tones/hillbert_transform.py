def getEnvelope (inputSignal):
    
    # Taking the absolute value
    
    absoluteSignal = []
    for sample in inputSignal:
        absoluteSignal.append (abs (sample))
    
    # Peak detection
    
    intervalLength = 800 # Experiment with this number, it depends on your sample frequency and highest "whistle" frequency
    outputSignal = []
    
    for baseIndex in range (intervalLength, len (absoluteSignal)):
        maximum = 0
        for lookbackIndex in range (intervalLength):
            maximum = max (absoluteSignal [baseIndex - lookbackIndex], maximum)
        outputSignal.append (maximum)
    
    return outputSignal


import numpy as np
import librosa
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
import librosa.display
# duration = 1.0
from scipy import signal
import os
# fs = 400.0
# samples = int(fs*duration)
# t = np.arange(samples) / fs

# signal = chirp(t, 20.0, t[-1], 100.0)
# signal *= (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t) )
directory = 'output_stimuli/original_sounds'
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        filen = f = os.path.join(directory, filename)
    
        signal0, fs = librosa.load(filen, sr=None)
        duration = librosa.get_duration(filename=filen)
        print(duration)

        envelope = getEnvelope(signal0)
        tone = librosa.tone(400, sr=fs, length=duration*fs)

        y = envelope
        f = signal.resample(np.asarray(y), np.size(tone))
        fig, (ax0, ax1) = plt.subplots(nrows=2)
        ax0.plot(signal0, label='signal')
        y3 = tone*(0.3*f)
        ax0.plot(y3, label='envelope')
        ax0.set_xlabel("time in seconds")
        ax0.legend()

        fig.tight_layout()



        print(np.asarray(f).size)
        print(np.asarray(tone).size)

        # plt.show()
        import soundfile as sf
        filen = f = os.path.join('output_stimuli/new_tones', filename)
        sf.write(filen.replace('.wav','') + "_tone.wav", y3, fs, subtype='PCM_24')