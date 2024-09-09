#import
import numpy as np
from numpy import linalg
import math
import matplotlib.pyplot as plt

N=300
a=1.42 # Lattice Parameter in Angstroms (set to 1 for the time-being, will be updated later)
t=2.7 #hopping energy to nearest neighbor (set to 1 for the time-being, will be updated later)
    
def hamiltonian(k):
    #Below are the nearest neighbor vectors in the Honey-Comb lattice for 2D Graphene
    del_1 = a/2 * np.array([1, math.sqrt(3)]) 
    del_2 = a/2 * np.array([1, -1*math.sqrt(3)])
    del_3 = -1*a * np.array([1, 0])
    
    # Here we initialize the Tight Binding Hamiltonian
    h = np.zeros((2, 2), dtype=complex)
    
    h[0, 1] = -t*(np.exp(1j*np.dot(del_1, k)) + np.exp(1j*np.dot(del_2, k)) + np.exp(1j*np.dot(del_3, k)))
    h[1, 0] = h[0,1].conjugate()
    
    # We have a singular unique point, so we only need 1 matrix, here we find the eigenvalues
    energy, states = linalg.eig(h)
    return energy
  
# The following function returns the band structure along a set k-vector path 
def band_structure_2D():
    #Here, we find the k-vector path and the band structure
    k_list = np.zeros((N, 2))
    e_list1 = np.zeros(N)
    e_list2 = np.zeros(N)
  
    # Path: G M K G
    k_x = np.zeros(N)
    k_x[0:100] = np.linspace(0, 2*math.pi /(a*3),100)
    k_x[100:200] = np.full(100,2*math.pi /(a*3) )
    k_x[200:] = np.linspace(2*math.pi /(a*3),0,100)
    
    k_y = np.zeros(N)
    k_y[100:200] = np.linspace(0, 2*math.pi/(a*3*math.sqrt(3)), 100)
    k_y[200:] = np.linspace(2*math.pi/(a*3*math.sqrt(3)),0, 100)

    for i in range(0, N):
        k_list[i] = np.array([k_x[i], k_y[i]])
    
        h = hamiltonian(k_list[i])
        e_list1[i] = h[0]
        e_list2[i] = h[1]

    return e_list1, e_list2


e1, e2 = band_structure_2D()
X = np.linspace(-2*math.pi /(a*3) -0.5,2*math.pi /(a*3) +0.5,N)

#plot figure
fig, ax = plt.subplots(figsize = (5, 2.5))
ax.set_title("2D Graphene Bandstructure" ,fontsize=12)
ax.set(xlabel=' ', ylabel='Energy (eV)')

#markers and ticks for x axis
ticks = np.full(N,"")
ticks[0]="G"
ticks[100]='M'
ticks[200]="K"
ticks[-1]='G'
ax.axvline(x=X[100], c='black', linewidth=0.5)
ax.axvline(x=X[200], c='black', linewidth=0.5)
ax.set_xticks(X[:N])
ax.set_xticklabels(ticks)
ax.tick_params(bottom = False)

ax.plot(X, e1)
ax.plot(X, e2)
