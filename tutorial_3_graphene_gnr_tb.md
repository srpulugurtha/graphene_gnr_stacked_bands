We can characterize the geometries of graphene nanoribbons into 2 main categories determined by their edge type, namely zig-zag and armchair nanoribbons (AGNRs). We see that AGNRs with a width of $n$ atoms where $n=3p+2, p=0,1,2...$ are semimetallic. We can understand these properties by studying the band structure of AGNRs by developing a tight-binding model. See the appendix of [this paper](https://iopscience.iop.org/article/10.1088/1468-6996/11/5/054504/pdf) for analytical solutions and a more thorough derivation. 

![image](https://github.com/user-attachments/assets/bec9e747-1467-4541-88be-7c24926385a9)


Using the same formalism as before with creation and annihilation operators, we define the following as our tight-binding Hamiltonian.


$$H = -\gamma_0 \sum_l{\sum_{m \in odd}{a_l^\dagger(m)b_{l-1}(m)+a_l^\dagger(m)b_{l}(m)}}$$

$$\pm \gamma_0 \sum_l{\sum_m^{N-1}{b_l^\dagger(m+1)a_l(m)+a_l^\dagger(m+1)b_l(m)}}$$

The creation and annihilation operators $a_l^\dagger(m)$ and $b_l^\dagger(m)$ indicate the $m$th site of the A or B sublattice within the $l$th unit cell (See Fig. 6 for tight-binding Hamiltonian). Using a similar method as given in the 2D graphene tight-binding model, we can define our wave functions as the following:

$$
\vec{\boldsymbol{\Psi}}_x=\begin{bmatrix} a_1 \\\ b_1 \\\ a_2 \\\ b_2 \\\ \dots \\\ a_N \\\ b_N  \end{bmatrix}
$$

where $N$ is the number of carbon atoms across the width of the nano-ribbon. With the defined wavefunction and Hamiltonian, we can develop the matrix representation of the Hamiltonian:

$$H=
\begin{bmatrix}
 & t &  & -1 &  &  &  &  &  & \\
t^* &  & -1 &  &  &  &  &  &  & \\
 & -1 &  & t &  & -1 &  &  &  & \\
-1 &  & t^* &  & -1 &  &  &  &  & \\
 &  &  & -1 &  & t &  & -1 &  & \\
 &  & -1 &  & t^* &  & -1 &  &  & \\
 &  &  &  &  & \dots &  & \dots &  & \dots\\
 &  &  &  & \dots &  & \dots &  & \dots & \\
 &  &  &  &  &  &  & -1 &  & t\\
 &  &  &  &  &  & -1 &  & t^* & \\
\end{bmatrix} 
$$

Where $t=e^{-ik/2}$. This matrix is given by the following equations of motion:

$$E\psi_{m,A} = -e^{-ik/2}\psi_{m,B} - \psi_{m-1,B}- \psi_{m+1,B}$$
$$E\psi_{m,B} = -e^{ik/2}\psi_{m,A} - \psi_{m-1,A}- \psi_{m+1,A}$$

The most notable difference between our 2D graphene and GNR tight-binding model is the necessity for boundary conditions due to infinite versus finite geometries. We inherently assume the finite nature of the GNR through the development of the Hamiltonian matrix, but we can qualitatively describe these boundaries:

We first attempt to use the equations of motion for the 1st and Nth atoms:

$$E\psi_{1,A} = -e^{-ik/2}\psi_{1,B} - \psi_{0,B}- \psi_{2,B}$$

$$E\psi_{1,B} = -e^{ik/2}\psi_{1,A} - \psi_{0,A}- \psi_{2,A}$$

$$E\psi_{N,A} = -e^{-ik/2}\psi_{N,B} - \psi_{N-1,B}- \psi_{N+1,B}$$

$$E\psi_{N,B} = -e^{ik/2}\psi_{N,A} - \psi_{N-1,A}- \psi_{N+1,A}$$

The immediate issue we see here is that $\psi_{0,A}, \psi_{N+1,A}, \psi_{0,B},$ and $\psi_{N+1,B}$ don't exist. To correct this, we state the following:

$$
\psi_{0,A}=\psi_{N+1,A}=\psi_{0,B}= \psi_{N+1,B}=0
$$

We can then restate our boundary conditions as the following:

$$E\psi_{1,A} = -e^{-ik/2}\psi_{1,B} - \psi_{2,B}$$

$$E\psi_{1,B} = -e^{ik/2}\psi_{1,A} - \psi_{2,A}$$

$$E\psi_{N,A} = -e^{-ik/2}\psi_{N,B} - \psi_{N-1,B}$$

$$E\psi_{N,B} = -e^{ik/2}\psi_{N,A} - \psi_{N-1,A}$$

After solving for the eigenvalues of the above-described matrix, we can solve for the eigenvalues and plot them as a function of the k-vector.
