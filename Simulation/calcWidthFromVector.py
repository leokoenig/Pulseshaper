import numpy as np

# calcWidthFromVector calculate width from the sample values of a vector
# returns error falls Vektoren nicht gleich lang

def calcWidthFromVector(yd, tt):
    N = len(yd)
    if len(tt) != N:
        raise ValueError("Vektoren nicht gleich lang!")

    norm_Fac = np.sum(np.power(np.abs(yd),2))

    mom1 = 1 / norm_Fac * np.sum(tt * np.power(np.abs(yd),2))
    mom2 = 1 / norm_Fac * np.sum(np.power(tt,2) * np.power(np.abs(yd),2))
    return np.sqrt(mom2 - np.power(mom1,2))
