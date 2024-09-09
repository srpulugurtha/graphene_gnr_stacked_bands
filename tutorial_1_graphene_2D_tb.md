# Tight-Binding Model for 2D Graphene

Graphene is made of up a single layer of carbon atoms arranged in a hexagonal lattice structure where each carbon atom is bonded to three neighboring carbon atoms. Its crystal structure can be described as the combination of two triangular sublattices A and B.

[(INSERT PNG OF 2D GRAPHENE BELOW FIG 1 IN PAPER)]

The A and B sublattices are given in blue and orange colors. The unit cell is shaded in gray and defined by the lattice vectors in black. The nearest neighbor vectors are given in green.

We can define the lattice vectors and nearest neighbor vectors for graphene as the following:

$$\boldsymbol{a_1} = \frac{a}{2}(3, \sqrt{3}),\quad \boldsymbol{a_2} =\frac{a}{2}(3, -\sqrt{3})$$

$$\boldsymbol{\delta_1} = \frac{a}{2}(1, \sqrt{3}),\quad \boldsymbol{\delta_2} =\frac{a}{2}(1, -\sqrt{3}),\boldsymbol{\delta_3} = -a(1, 0)$$

When considering the electronic structure of a given system, the electronic band structure is quintessential to understanding electron behavior. An effective model that we can use to calculate the band structure for graphene is the tight-binding model. 

The tight-binding model considers the energy required for an electron to hop to the nearest neighbors of a given atom. Because of the lack of isotropy resulting in the 2 sublattices mentioned earlier, the nearest neighbors of any carbon atom in a sublattice will be 3 atoms from the other sublattice. To express the hopping energy of electrons from A (B) sublattice atoms to the nearest neighbor atoms in the B (A) sublattice, we can use creation and annihilation operators:

$$H=-\gamma_0\sum_{i,j}{a^\dagger_ib_j + b^\dagger_ja_i}$$

In the above Hamiltonian, we are summing over the energy it takes to create and annihilate an electron in sublattice A at position $r_i$ and sublattice B at position $r_j$ respectively. $\gamma_0$ is the hopping energy or tight-binding coefficient that is determined experimentally or via first principles (discussed later in this section). We can now incorporate our nearest neighbor vectors to rewrite all the position vectors in terms of $r_i$.

$$H=-\gamma_0\sum_{i}{\sum_{\delta}{{a^\dagger_ib_j + b^\dagger_ja_i}}}$$

Using the following definition:

$$a^\dagger_i=\frac{1}{\sqrt{N/2}}\sum_k{a^\dagger_ke^{i\boldsymbol{kr_i}}}$$

We can rewrite the tight-binding Hamiltonian as the following:

$$H=\frac{-\gamma_0}{N/2}\sum_{i}{\sum_{\boldsymbol{\delta, k, k'}}{a^\dagger_kb_{k'}e^{i\boldsymbol{(k-k')r_i}}e^{-i\boldsymbol{(k')\delta}}}}.$$

Since

$$\sum_i{e^{i\boldsymbol{(k-k')r_i}}}=\frac{N}{2}\delta_\boldsymbol{k,k'},$$

we can simplify our Hamiltonian to the following:

$$H=\-\gamma_0{\sum_{\boldsymbol{\delta, k}}{a^\dagger_kb_{k}e^{-i\boldsymbol{k\delta}}+a_kb^\dagger_{k}e^{i\boldsymbol{k\delta}}}}.$$

We can now define our wavefunctions which need 2 elements due to the 2 sublattices that wholly describe the graphene structure:

$$\vec{\boldsymbol{\Psi}}_x=\begin{bmatrix} a_k \\\ b_k  \end{bmatrix}$$

Upon expressing our Hamiltonian in the following form:

$$\sum_k{\boldsymbol{\Psi^\dagger h(k) \Psi}},$$

we can express the 2 x 2 matrix representation of the Hamiltonian as:

$$\boldsymbol{h(k)}=-\gamma_0\begin{bmatrix}0 & \Delta_k\Delta_k^* & 0 \end{bmatrix}$$

where 
$$\Delta_k = \sum_{\boldsymbol\delta}{e^{i\boldsymbol{k\delta}}}.$$

Upon solving for the eigenvalues of $\boldsymbol{h(k)}$, we can find the energies of our tight-binding model as a function of the k-vector. Analytically, this yields

$$E=\pm \gamma_0\sqrt{3 + 2cos(\sqrt{3}k_y a)+4cos(\frac{\sqrt{3}}{2}k_y a)cos(\frac{3}{2}k_x a)}.$$

Above: The band structure has been plotted as function of $k_x$ and $k_y$ in 3D. The valence band is shown in orange and the conduction band is shown in orange. The zoomed in area shows the Dirac point. Below: A 2D cross section has been taken to show the Dirac Points labelled K and K'.

The remarkable characteristic of graphene's band structure is the presence of Dirac points within the lattice seen at the K and K' points. These points can be seen in the reciprocal lattice of graphene, shown in Fig. 2. The reciprocal lattice is defined with reciprocal lattice vectors:

$$\boldsymbol{b_1} = \frac{2 \pi}{3a}(1, -\sqrt{3}), \boldsymbol{b_2} =\frac{2 \pi}{3a}(1, \sqrt{3})$$

$$\boldsymbol{K} = \frac{2 \pi}{3\sqrt{3}a}(\sqrt{3}, 1), \boldsymbol{K'} =\frac{2 \pi}{3\sqrt{3}a}(\sqrt{3}, -1)$$

The Dirac points can be seen in the reciprocal lattice of graphene in red. The reciprocal lattice vectors are in black, labeled $b_1$ and $b_2$.

We can quantify this linear relationship by calibrating k-vectors such that the origin is at the K point:

$$E=\pm \gamma_0\sqrt{\frac{9}{4}k_y^2a^2+\frac{9}{4}k_x^2 a^2)}=\pm\frac{3}{2}at|\boldsymbol{k}|=\pm \hbar v_fk$$

where $v_f$ is the Fermi velocity which is approximately $c/300$.

The linear relation between the momentum (k point) and energy is seen in the massless Dirac equation:

$$E^2=p^2c^2+m_0^2c^4$$

The first term yields the linear relationship that we see whereas the second term resembles parabolic band behavior. We can see that electrons near the Dirac point are effectively mass-less. These quickly moving, light electrons allow for the unique semi-metallic properties seen in graphene. 

It is important to carefully consider the hopping energy constant, $\gamma_0$. This value is the only quantitative aspect of the above-described tight-binding model and is therefore determined by fitting the tight-binding model to first-principles calculations or experimental results. However, a standard value used commonly in literature is given as $t=2.7eV$. The above-described tight binding model is the basis of all other tight binding models given for graphene nanoribbons and bilayer graphene. More complex tight binding models can also be generated that consider beyond nearest-neighbor interactions. However, the hopping energy for these interactions is relatively low. We can affirm the accuracy of our simple tight-binding model by comparing results with first-principles calculations.
