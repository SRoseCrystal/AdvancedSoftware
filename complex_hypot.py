import numpy as np

def complex_hypot(x1, x2):
    return np.sqrt(np.abs(x1)**2 + np.abs(x2)**2 + 2 * np.real(x1 * np.conj(x2)))
