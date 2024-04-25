'''
Implementation of a butterworth Filter for the ppg data filtering

'''
# using a butterworth filter
from scipy.signal import butter, lfilter, lfilter_zi

def butter_bandpass(lowcut = 0.5, highcut = 12, fs = 25, order=5):
    return butter(order, [lowcut, highcut], fs=fs, btype='band')

def butter_bandpass_filter_zi(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    zi = lfilter_zi(b, a)
    y,zo = lfilter(b, a, data, zi=zi*data[0])
    return y
