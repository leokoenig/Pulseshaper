import numpy as np

# FWHM Berechnung der Breite als 'full width at half maximum' einer
# Funktion func innerhalb des Intervals lims. 
# Die Funktion ist mit einer Gauss-artigen Funktion im Hinterkopf
# geschrieben (ein Max. und zu den Seiten abfallend). Für andere
# Funktionen (z.B. Sinus) macht der FHWM-Wert nicht unbedingt Sinn. 
 
# #### Argumente: 
# * func: Vektorisierte Funktion-Handle einer Variablen
# * lims: Vektor mit Intervallgrenzen, innerhalb derer die Berechnun läuft
# * N: Anzahl der Punkte, die abgetastet werden. 
# #### Rückgabe: 
# * fwhm: 'full width at half maximum'
# * x1: linke Grenze des FWHM-Bereichs
# * x2: rechte Grenze des FWHM-Bereichs
# * maxVal: Maximum der Funktion

def berechneFWHM(func, lims, N=1000):
    xx = np.linspace(lims[0],lims[1],N)
    funcVals = abs(func(xx))
    maxVal = max(funcVals)
    mask = funcVals > maxVal/2
    x1 = min(xx[mask])
    x2 = max(xx[mask])
    fwhm = x2-x1

    return fwhm, x1, x2, maxVal