import numpy as np

# change the phase of the given frequency vector by the given phase
# offsets starting at startIdx

# find index range on which the pulse shaper acts
def phasePulseFormer(specVec, phaseOffset, startIdx):
   N = len(phaseOffset)
   idxVec = np.arange(startIdx,(N+startIdx))

   # decompose into 
   ampl = abs(specVec[idxVec])
   phase = np.angle(specVec[idxVec])
   ret = specVec.copy()
   ret[idxVec] = ampl * np.exp(1j * (phase + phaseOffset))

   return ret