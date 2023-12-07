#########################################################################################
#   Author : Marius Nerantzakis
#   Project : Music AI
#   Page : Main.py
#
#   This is the Main app for the Music AI project
#########################################################################################
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as pl
import time

def showGraphic(data):
    pl.plot(data)
    pl.show()

def get_freq(bit, chunk, offset, data, rate):
    # start position of the current bit
    strt = (chunk * bit) 
    
    # remove the delimiting 1600hz tone
    end = (strt + chunk) - offset
    
    # slice the array for each bit
    sliced = data[strt:end]

    w = np.fft.fft(sliced)
    freqs = np.fft.fftfreq(len(w))

    idx = np.argmax(np.abs(w))
    if(idx <= len(freqs)):
        freq = freqs[idx]
        freq_in_hertz = abs(freq * rate)
        return freq_in_hertz


def detection(show):
    rate, data = wavfile.read('flute.wav')


    #data = np.expand_dims(data, np.full(temp_data.shape, np.mean(data[196000: 200000])))
    # 15ms chunk includes delimiting 5ms 1600hz tone
    duration = 0.015
    # calculate the length of our chunk in the np.array using sample rate
    chunk = int(rate * duration)
    # length of delimiting 1600hz tone
    offset = int(rate * 0.005)
    # number of bits in the audio data to decode
    bits = int(len(data) / chunk)

    decoded_freqs = []
    for bit in range(bits):
        freqq = get_freq(bit, chunk, offset, data, rate)
        if freqq is not None :decoded_freqs.append(freqq)
        else: decoded_freqs.append(decoded_freqs[-1])
    mean_freq = []

    joined_array = np.zeros(shape=(2, data.size))

    precision = 60
    for i in range(precision, bits, precision):
        for j in range(precision):
            mean_freq.append(np.mean(decoded_freqs[(i-precision) : i]))

    '''for bit in range(bits):
        print(get_freq(bit, chunk, offset, data, rate))
        time.sleep(0.05)'''
    #print(decoded_freqs)

    if show:
        pl.figure(0)
        pl.plot(decoded_freqs)
        pl.figure(1)
        pl.plot(mean_freq)
        pl.figure(2)
        pl.plot(data)


        pl.show()

    print(data.size, len(decoded_freqs), data.shape)
    return data

if __name__ == "__main__":
    detection(True)