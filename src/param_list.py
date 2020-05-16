#!python3
"""
Population parameters for a Wright-Fisher process
in a Stepping Stone spatial lattice.
"""
numgens = 1e3 # Number of simulated generations 
L = 1 # Number of demes
popsize = 1e4 # Population size N
mu = 1e-4 # Symmetric mutation rate
m = 1e-2 # Symmetric migration rate
s = 1e-2 # Selection coefficient
f0 = 1/popsize # Initial allele frequency