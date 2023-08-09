import numpy as np
import scipy
from scipy import interpolate
import matplotlib.pyplot as plt
from calcWidthFromVector import calcWidthFromVector
from shgValue import shgValue

def targetFunc(pSupp, wSupp, wws, pulseFormer, tt):
   pp = scipy.interpolate.CubicSpline(wSupp, pSupp)
   phaseOffsets = pp(wws)  # hier checken ob es sich wie ppval (Matlab) verhält
   AwShaped = pulseFormer(phaseOffsets)
   #AwShaped = np.reshape(AwShaped,(1,8000))
   atShaped = np.fft.ifft(AwShaped)
   value = calcWidthFromVector(abs(np.fft.fftshift(atShaped)), tt)
   #value = - shgValue(atShaped)

   return value