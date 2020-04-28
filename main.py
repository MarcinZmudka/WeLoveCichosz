import scipy.fftpack
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from scipy.fft import fftshift
from scipy import signal
import numpy as np
import ecg as ecg
import ftt as ftt
import pandas as pd


[ts, samples] = ecg.import_from_txt("./ekg100.txt", 360)

ftt.fft(360, ts, samples)
