import numpy as np
import matplotlib.pyplot as plt

# XCORRSPECTROGRAM create cross corellation spectrogram matrix
#     Arguments: 
#     timeVec1: first signal vector in time domain
#     timeVec2: second signal vector in time domain, same length as timeVec2
#     Ts: sample time of first two arguments
#     tauVec: vector of time delays. 
#     showPlot (default=false): show plots as timeVec2 slides across timeVec1
#     Return value
#     specMat: spectrogram matrix of dimension length(timeVec1) x length(tauVec)
#     wVec: the frequency axis of the spectrogram matrix

def xcorrSpectrogram(timeVec1, timeVec2, Ts, tauVec, showPlot = False):
    Nw = len(timeVec1)
    if len(timeVec1) != len(timeVec2):
        raise ValueError('timeVec1 und timeVec2 muessen die gleiche Laenge haben')
    Ntau = len(tauVec)

    #specMat = complex(np.zeros([Nw, Ntau]))
    specMat = np.zeros([Nw, Ntau]).astype(complex)
    wVec = np.arange(0,(Nw)) * 2*np.pi/(Ts*Nw)

    for k in range(len(tauVec)):
        tau = tauVec[k]
        # Now, timeVec2 has to be shifted by tau
        timeVec2Shift = np.zeros(np.size(timeVec2))
        nShift = abs(round(tau / Ts))   # number of values to be shifted
        if nShift < Nw:
            if tau < 0:
                # shift to right
                timeVec2Shift[1:len(timeVec2Shift)-nShift] = timeVec2[1+nShift:len(timeVec2Shift)]
            else:
                # shift to left
                timeVec2Shift[1+nShift:len(timeVec2Shift)] = timeVec2[1:len(timeVec2Shift)-nShift]

        if showPlot:
            # this is just for illustration
            tt = np.arange(0,(Nw))* Ts
            plt.plot(tt, timeVec1, tt, timeVec2Shift)
            plt.pause(1)

        zft = Ts * np.fft.fft(timeVec1 * timeVec2Shift)
        specMat[:, k] = zft

    return specMat, wVec