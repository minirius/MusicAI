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

rate, data = wavfile.read('Married-Life-piano.wav')

temp_data = data
data = data[:,0]
#data = np.expand_dims(data, np.full(temp_data.shape, np.mean(data[196000: 200000])))
print(data.shape, data.size, data.size)
#for i in range(1.81e5, 160010):
#    print(data[i])

pl.plot(data[196000: 200000])
pl.axis
pl.show()
