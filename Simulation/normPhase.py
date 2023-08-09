import numpy as np

def normPhase(p):
    pn = np.mod(p, (2*np.pi))
    pn[pn<0] = pn[pn<0] + 2*np.pi

    return pn