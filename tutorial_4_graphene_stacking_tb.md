We can develop a tight-binding model for multilayer graphene by considering interactions within a single layer and between neighboring layers. We consider interactions from the nearest-neighbors within a single layer of graphene, along with the non-negligible second nearest-neighbors from adjacent layers of graphene. For the simplest models that neglect twisting and other complex stacking arrangements, we can categorize multilayer graphene into AB and AA stacking orders. 

AB stacking is characterized by the z-direction interactions between A and B sublattice atoms, while AA stacking is characterized by z-direction interactions between 2 A or 2 B sublattice atoms.


We can characterize the energy-hopping interactions in the z-direction (second nearest neighbor) as $\gamma_1$ and in nearest neighbor directions as $\gamma_\pm = \hbar v_f (k_x \pm ik_y)$.

We can define an eigenvector basis that corresponds to the A or B sublattices of the nth layer:

$$\psi = \begin{bmatrix} A_1 \\ B_1 \\ A_2 \\ B_2 \\ \dots \\ A_N \\ B_N  \end{bmatrix}$$

We can then use our energy-hopping interactions based on the AB and AA stacking structures and determine the coupled equations that describe the hopping:

For AB stacking, we can separate our equations into even and odd layers for both sublattices:

For odd $n$:
$$EA_n = \gamma_- B_n$$

$$EB_n = \gamma_1(A_{n-1} + A_{n+1}) + \gamma_+A_n$$

For even $n$:
$$EB_n = \gamma_+ A_n$$

$$EA_n = \gamma_1(B_{n-1} + B_{n+1}) + \gamma_-B_n$$

The resulting tight-binding Hamiltonian for AB stacking is then:

$$H=\begin{bmatrix} 0&\gamma_- & 0 &0&0&0&\\ \gamma_+&0&\gamma_1&0&0&0&\\
0&\gamma_1&0\gamma_-&0&\gamma_1\\
0&0&\gamma_+&0&0&0&\dots\\
0 & 0 &0&0&0&\gamma_-&\\
0&0&\gamma_1&0&\gamma_+&0&
\\&&&\dots&&&&\\ \end{bmatrix} 
$$

For AA stacking, we can write the following coupled equations:

$$EA_n = \gamma_1(A_{n-1} + A_{n+1}) + \gamma_-A_n$$

$$EB_n = \gamma_1(B_{n-1} + B_{n+1}) + \gamma_-B_n$$

The resulting tight-binding Hamiltonian for AA stacking is then:

$$ H= \begin{bmatrix}
0&\gamma_- & \gamma_1 &0&0&0&\\
\gamma_+&0&0&\gamma_1&0&0&\\
\gamma_1&0&0&\gamma_-&\gamma_1&0&\dots\\
0&\gamma_1&\gamma_+&0&0&\gamma_0&\\
0 & 0 &\gamma_1&0&0&\gamma_-&\\
0&0&0&\gamma_1&\gamma_+&0&
\\&&&\dots&&&\\ \end{bmatrix} 
$$

The band structures for $N=2$ and $N=3$ for AA and AB stacking orders were computed.
