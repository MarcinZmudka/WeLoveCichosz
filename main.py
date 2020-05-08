import scipy.fftpack
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from scipy.fft import fftshift
from scipy import signal
import numpy as np
import ecg as ecg
import ftt as ftt
import pandas as pd


[ts, samples] = ecg.import_from_txt("./ekg_files/ekg100.txt", 360)

ecg.make_chart(ts, samples, "czas", "wartość")
# ftt.fft(360, ts, samples)
# ftt.ifft(360, ts, samples)
