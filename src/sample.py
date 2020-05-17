#!python3
"""
    Performs convolution of frequency matrix
    with Gaussian sampling kernel of width w
    Returns: F matrix of sampled allele frequencies
"""
import numpy as np
from scipy.ndimage import gaussian_filter

def sample_f(f,w):
    F = np.zeros(f.shape)
    ## Need to convolve array along spatial axes
    ## so iterate over time axis
    for i in range(f.shape[0]):
        F[i] = gaussian_filter(f[i],sigma=w,mode = "wrap")
    return F

if __name__ == "__main__":
    sample_f()