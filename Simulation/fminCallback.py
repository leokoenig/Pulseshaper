import numpy as np

def fminCallback(x, optimValues, itCount, plotFunc):
    if np.mod(optimValues.iteration, itCount) == 0:
        plotFunc(x, optimValues)

    return False