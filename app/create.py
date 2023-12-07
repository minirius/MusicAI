import math
import wave
import struct
import random

if __name__ == '__main__':
    # http://stackoverflow.com/questions/3637350/how-to-write-stereo-wav-files-in-python
    # http://www.sonicspot.com/guide/wavefiles.html
    data_size = 10000
    fname = "test3.wav"
    frate = 11025.0
    amp = 64000.0
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes = data_size
    comptype = "NONE"
    compname = "not compressed"
    notes_freq = [random.randint(0, 1000) for i in range(5)]
    print(notes_freq)
    data = []
    i = 0
    for x in range(data_size):
        freq = notes_freq[i]
        data.append(math.sin(2 * math.pi * freq * (x / frate)))
        if(x%2000 == 0 and x!=0):
            i+=1
    
    wav_file = wave.open(fname, 'w')
    wav_file.setparams(
        (nchannels, sampwidth, framerate, nframes, comptype, compname))
    for v in data:
        wav_file.writeframes(struct.pack('h', int(v * amp / 2)))
    wav_file.close()