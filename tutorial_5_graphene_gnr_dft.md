We can perform first-principles band structure calculations using Quantum Espresso for AGNRs as well.

A self-consistent calculation was performed where the AGNR structure was defined with a unit cell shown below.

![image](https://github.com/user-attachments/assets/ae12c4f9-477b-4896-8b3a-c9a1adda84ec)

The red, blue, and green dots represent the positions of graphene carbon atoms given in angstroms on the axes. The Cyan, Magenta, and Yellow dots represent the hydrogen atoms that latch onto the dangling bonds of the AGNRs. The crystalline structures were defined in this way for all first-principles calculations.

It is important to understand that Hydrogen atoms must be included at the dangling bonds of the AGNR edge as that can cause instabilities and inaccuracies in the final band structure results. A non-self-consistent calculation was done to get a more accurate Fermi energy, followed by a band calculation. The same pseudopotentials were used as the 2D graphene Quantum Espresso calculation. Band structures were computed for $N=2$ and $N=5$ AGNRs.
