import numpy as np
from numpy import linalg
import math
import matplotlib.pyplot as plt

def AA(kx, ky, n):
    t=2.8
    v=3.16*3*1.42/2
    h = np.zeros((2*n, 2*n), dtype=complex)
    
    for i in range(0,2*n-2,2):
        h[i,i+1] =  v*(kx + 1j*ky)
        h[i,i+2] = t
        h[i+1,i+3] = t
    h[2*n-2,2*n-1] = v*(kx + 1j*ky)

    for i in range(0, 2*n):
        for j in range(0,i):
            h[i,j] = h[j,i].conjugate()
        
    energy, states = linalg.eig(h)
    return energy

def bandstructure_AA(n):    
    ky = np.linspace(-2, +2, 100)
    # ky = np.linspace(-2*math.pi /(3*math.sqrt(3))-2, 2*math.pi /(3*math.sqrt(3))+2, 100)

    H = np.zeros((100, 2*n))
    for i in range(0, 100):
        # H[i,:] = AA(2*math.pi /3,ky[i],n)
        H[i,:] = AA(0,ky[i],n)
    return H


def AB(kx, ky, n):
    t=2.8
    v=3.16*3*1.42/2
    h = np.zeros((2*n, 2*n), dtype=complex)
    k=0
    i=0
  
    if (n==2):
        h[i,i+1] =  v*(kx + 1j*ky)
        h[i+1,i+2] = t
        h[i+2,i+3] = v*(kx + 1j*ky)
        h[i+2,i+3] = v*(kx + 1j*ky)
    else:
        while(n!=2 and k<2*n-4):
            h[i,i+1] =  v*(kx + 1j*ky)
            h[i+1,i+2] = t
            h[i+2,i+3] = v*(kx + 1j*ky)
            h[i+2,i+3] = v*(kx + 1j*ky)
            h[i+2,i+5] = t
            k+=4
            i+=4   
        if (n%2 != 0):
            h[i,i+1] = v*(kx + 1j*ky)
        
    
        

    for i in range(0, 2*n):
        for j in range(0,i):
            h[i,j] = h[j,i].conjugate()
        
    energy, states = linalg.eig(h)
    return energy


def bandstructure_AB(n):    
    ky = np.linspace(-2, +2, 100)
    H = np.zeros((100, 2*n))
    for i in range(0, 100):
        H[i,:] = AB(0,ky[i],n)
    return H


h_AA_2 = bs_AA(2)
h_AA_3 = bs_AA(3)
h_AB_2 = bs_AB(2)
h_AB_3 = bs_AB(3)

x = np.linspace(-2, 2, 100)
fig1 = plt.figure()

ax1 = fig1.add_axes([0, 0, 1, 1])
ax2 = fig1.add_axes([1.3, 0, 1, 1])
ax3 = fig1.add_axes([0, 1.3, 1, 1])
ax4 = fig1.add_axes([1.3, 1.3, 1, 1])

for i in range (0,4):
    ax1.scatter(x, h_AA_2[:,i], c="black", s=13)
    ax2.scatter(x, h_AB_2[:,i], c="black", s=13)

for i in range (0,6):
    ax3.scatter(x, h_AA_3[:,i], c="black", s=13)
    ax4.scatter(x, h_AB_3[:,i], c="black", s=13)
    
ax1.set_title("AA, N=2", fontsize = 25)
ax2.set_title("AB, N=2", fontsize = 25)
ax3.set_title("AA, N=3", fontsize = 25)
ax4.set_title("AB, N=3", fontsize = 25)

ax1.set_xlabel('K', fontsize=20)
ax1.set_ylabel('E (eV)', fontsize=20)
ax2.set_xlabel('K', fontsize=20)
ax2.set_ylabel('E (eV)', fontsize=20)
ax3.set_xlabel('K', fontsize=20)
ax3.set_ylabel('E (eV)', fontsize=20)
ax4.set_xlabel('K', fontsize=20)
ax4.set_ylabel('E (eV)', fontsize=20)



plt.rc('xtick', labelsize=0) 
plt.rc('ytick', labelsize=30)
    
fig1.savefig('multi.pdf',bbox_inches='tight', dpi=1200)
