import numpy as np
import matplotlib.pyplot as plt
from biosppy import storage
from biosppy.signals import ecg
from math import ceil
import librosa
import pandas as pd


def import_from_txt(path_to_file, fs):
    try:
        data = pd.read_csv(f"{path_to_file}", sep=" ", header=None)
    except:
        data = pd.read_csv(f"{path_to_file}", sep="  ", header=None)

    rows, number_of_columns = data.shape
    if number_of_columns == 2:  # if second column is time
        return [data[0], [data[1]]]
    data = data[:5000]
    N = rows  # number of samples
    T = (N - 1) / fs  # duration
    ts = np.linspace(0, T, N, endpoint=False)  # relative timestamps
    return [ts[:5000], data]


def make_chart(x, y, xlabel, ylabel):
    try:
        rows, number_of_charts = y.shape
    except:
        number_of_charts = 1
    rows = ceil(number_of_charts/2)
    fig, axs = plt.subplots(rows, 2)
    if rows == 1:
        axs = [axs]
    index_of_plot = 0
    for i in range(0, rows):
        if i == (rows - 1) and number_of_charts % 2 == 1:
            axs[i][0].plot(x, y[index_of_plot], lw=1)
            axs[i][0].set_title(f"kanał: {index_of_plot}")
            axs[i][0].set_xlabel("T[s]")
            index_of_plot += 1
            axs[i][0].grid()
        else:
            for j in range(0, 2):
                print(axs)
                axs[i][j].plot(x, y[index_of_plot], lw=1)
                axs[i][j].set_title(f"kanał: {index_of_plot}")
                axs[i][j].set_xlabel("T[s]")
                index_of_plot += 1
                axs[i][j].grid()
    plt.show()
