import numpy as np
import scipy
from scipy import interpolate
import matplotlib.pyplot as plt
from xcorrSpectrogram import xcorrSpectrogram

def plotOptimState(pSupp, optimValues, cfg, refValue, pulseFormer):
    wws = np.linspace(cfg.shaperLims[0], cfg.shaperLims[1], cfg.nPix)
    wSupp = np.linspace(cfg.shaperLims[0], cfg.shaperLims[1], cfg.S)
    Tp = 2*np.pi/cfg.wp
    w0 = (cfg.shaperLims[1] - cfg.shaperLims[0]) / cfg.nPix     # frequency resolution
    NN = np.ceil(2*np.pi/(Tp*w0)*cfg.samplesPerPeriod)
    ww = np.arange(0,NN)*w0   # Frequency axis
    ws = NN * w0    # sample rate
    Ts = 2*np.pi / ws  # sample time
    T0 = 2*np.pi/w0    # duration in time domain
    tt = -T0/2 + np.arange(0,NN)*Ts   # time axis shifted so that it centers around 0
    ttMask = abs(tt) < cfg.tLim

    pp = scipy.interpolate.CubicSpline(wSupp, pSupp)
    phaseOffsets = pp(wws)  # hier checken ob es sich wie ppval (Matlab) verhält
    AwShaped = pulseFormer(phaseOffsets)
    #AwShaped = np.reshape(AwShaped,(1,8000))
    atShaped = np.fft.fftshift(np.fft.ifft(AwShaped))

    # the rest of the loop is just plotting to observe optimization progress
    fig = plt.figure(figsize=(10, 7), layout="constrained")
    spec = fig.add_gridspec(2, 2)
    #t = plt.tiledlayout(2,3, "TileSpacing","compact", "Padding","compact")
    fig.suptitle('Iteration {}, Value={:.3f} (Ref={:.3f})'.format(optimValues.iteration,abs(optimValues.fval), refValue))

    ax1 = fig.add_subplot(spec[0, 0])
    #plt.plot(wws, (-cfg.phaseFunc(wws)), linewidth = 2, label = 'True phase')  # Hier kommi weg nehmen eventuell
    plt.plot(wws, phaseOffsets, label = 'Offset Phasenfunktion')                       # Hier neu eventuell rausnhemen
    plt.ylim(np.pi*-2, np.pi*6)
    plt.scatter(wSupp, pSupp, label = 'Support points')
    plt.title('Phase Offset')
    ax1.set_ylabel('Radians')
    plt.xlabel('Frequency $\omega$')
    ax1.legend()
    
    ax2 = ax1.twinx()
    ax2.plot(ww, abs(AwShaped), linestyle = '--', linewidth = 1, label = 'Magnitude')
    ax2.set_ylabel('Magnitude')
    plt.xlim(wws[0], wws[-1])
    ax2.legend()

    fig.add_subplot(spec[1, 0])
    plt.plot(tt, abs(atShaped), linewidth = 2, label = 'Magnitude')
    plt.xlabel('Time t')
    plt.title('Time domain')
    plt.xlim(4*(-4/cfg.sigma), 4*(4/cfg.sigma))
    plt.plot(tt, np.real(atShaped), label = 'Real part', linewidth = 1)
    plt.plot(tt, abs(cfg.atRef), label = '0 phase', linewidth = 1)
    plt.legend()

    #Spectrogramm
    fig.add_subplot(spec[0, 1])

    def extents(f):
        delta = f[1] - f[0]
        return [f[0] - delta/2, f[-1] + delta/2]

    timeVec1 = np.real(atShaped[ttMask])/Ts
    timeVec2 = (np.power(abs(atShaped[ttMask]),2))/Ts
    SM, wVec = xcorrSpectrogram(timeVec1, timeVec2, Ts, cfg.tauVec)
    wMask = (wVec > 0) & (wVec <  2*cfg.wp)
    im1 = plt.imshow(abs(SM[wMask,:]), extent=extents(cfg.tauVec) + extents(wVec[wMask]))
    #plt.imshow(cfg.tauVec, wVec[wMask], abs(SM[wMask,:]))
    plt.xlabel('Time shift $\\tau$')
    plt.ylabel('Frequency $\omega$')
    plt.title('Spectrogramm')
    plt.colorbar(im1)
    #plt.drawnow
    plt.pause(0.1)






