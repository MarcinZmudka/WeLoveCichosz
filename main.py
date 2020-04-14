import ecg as ecg

[ts, samples] = ecg.import_from_txt("./ekg100.txt", 360.)
# ts - timestamp
# samples - wartość próbki
ecg.make_chart(ts, samples, "czas", "wartość sygnału")

# x = ecg.spectrum(samples)
# ecg.make_chart(ts, x, "czas", "wartość sygnału")
