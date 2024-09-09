#import
import numpy as np
from numpy import linalg
import math
import matplotlib.pyplot as plt

#hopping parameter
t = 2.7

def hamiltonian(k,n):
    h = np.zeros((2*n, 2*n), dtype=complex)
    
    for i in range(2, 2*n-3, 2):
        h[i,i+1] = -np.exp(1j*k)
        h[i,i+3] = -1
        h[i,i-1] = -1
        
        h[i+1,i] = -np.exp(1j*k)
        h[i+1,i-1] = -1
        h[i+1,i+2]= -1  
        
    h[0,1] = -np.exp(1j*k)
    h[0,3] = -1
    h[1,0] = -np.exp(-1j*k)
    h[1,2] = -1
    h[2*n-2,2*n-1]=-np.exp(1j*k)
    h[2*n-2,2*n-3]=-1
    h[2*n-1,2*n-2]=-np.exp(-1j*k)
    h[2*n-1,2*n-3]=-1
    
    for i in range (1,2*n-1):
        for j in range(0,i):
            h[i,j] = h[j,i].conjugate()
          
    energy, states = linalg.eig(h)
    return energy*t

def bandstructure(n):
    k = np.linspace(-5, 5, 500)
    E = np.zeros((500,2*n))
    
    for i in range(0, 500):
        E[i,:]=hamiltonian(k[i],n)
        
    return E
  
# Example
k_axis = np.linspace(-5, 5, 500)
h11 = bandstructure(11)

fig11, ax11 = plt.subplots()
ax11.set_title("Armchair GNR: n=11 (~ 2 nm) ")
ax11.set(xlabel='k', ylabel='E')
for i in range(0,22):
    ax11.scatter(k, h11[:,i], c="black", s=0.4)
  
