#!python3
"""
    Simulates a Wright-Fisher process in a Stepping-Stone
    spatial lattice. Takes the following parameters:
    pop_size = 'Number of individuals within each deme'
    mu = 'Symmetric mutation rate'
    s = 'Selection coefficient')
    m = 'Symmetric migration rate across demes'
    num_reps = 'Number of independent replicates'
    num_gen = 'Number of generations simulated'
    dims = 'Dimensions of spatial lattice as tuple'
    out = 'Path and filename for output'
"""
import numpy as np
from scipy.ndimage.filters import laplace

def SS_WF_sim(pop_size,mu,s,m,num_reps,num_gen,dims,out):
    #Pre-allocate and initialize
    f = np.zeros((num_gen,num_reps)+dims)
    f[0] = 1/pop_size
    for j in range(num_gen-1):
        #Wright-Fisher diffusion w/Stepping Stone migration
        df = mu*(1-2*f[j])-s*f[j]*(1-f[j]) \
        +m*laplace(f[j],mode='wrap')
        #bounds allele frequencies between 0 and 1
        p = np.clip(a= f[j] + df ,a_min=0,a_max=1)
        #genetic drift binomial sampling
        f[j+1]= np.random.binomial(pop_size,p)/pop_size
    # Write freqmat as .npy
    np.save(out,f)

if __name__ == "__main__":
    SS_WF_sim()