import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy
from scipy import fftpack
import matplotlib.pyplot as plt

# transformata fouriera


def fft(fs, ts, data):
    fs = fs/1000
    sp = np.fft.fft(flat(data.to_numpy()))
    freq = np.fft.fftfreq(len(ts))
    plt.plot(freq, sp)  # .real, freq, sp.imag
    plt.xlim(0, fs / 2)
    plt.show()

# odwortna transformata fouriera


def ifft(fs, ts, data):
    fs = fs/1000
    sp = np.fft.ifft(flat(data.to_numpy()))
    # freq = np.fft.fftfreq(len(ts))
    freq = ts
    plt.plot(freq, sp)
    plt.xlim(0, fs / 2)
    plt.show()


# służy do spłaszczania zagnieżdżonych list
def flat(listOfLists):
    newList = []
    for list in listOfLists:
        newList.append(list[0])
    return newList
