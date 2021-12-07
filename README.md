# Validation of 2D Diffusion with Palabos

See page 132-133 from *Lattice Boltzmann Modeling: An Introduction for
Geoscientists and Engineers*
This Palabos program is for validating diffusion in a (infinite) two
dimensional domain agains a known analytic solution.

Analytical solution by Crank in [The Mathematics of Diffusion](http://www-eng.lbl.gov/~shuman/NEXT/MATERIALS&COMPONENTS/Xe_damage/Crank-The-Mathematics-of-Diffusion.pdf) (Chapter 3)

---

![analytic vs numerical](.comparisonD2Q5.png)

Figure 69 from *Lattice Boltzmann Modeling: An Introduction for Geoscientists
and Engineers*

---

This directory houses a 2D implementation of the Lattice Boltzmann equation for
advection/diffusion (pure diffusion i.e. velocity = [0,0]) for a point source
(Concentration = M_0 = 1000) in the center of an infinite (for our instance we
use 1000 x 1000) domain. The concentration does not reach the boundaries by the
end of the time stepping and therefore periodic boundary conditions are used.
The function *centerPointSetup* instantiates the initial conditions and
initializes the lattice.

The analytic solution for this problem is:

![solution to pde](.equation.jpg)

The file *figure69.py* solves the analytical solution for the given conditions
and plots it as dashed lines, while plotting the corresponding *Palabos*
solution with solid circles.

## Values Used

| parameter     | value |
| ---           | ---  |
| C<sub>i</sub> | 0    |
| M<sub>0</sub> | 1000 |
| D             | 1/6  |
| n<sub>x</sub> | 1000 |
| n<sub>y</sub> | 1000 |

## Compiling

Note the path in CmakeLists.txt to the Palabos library is not the same path you
will use (lines 99 - 104). Also you will need to create a build directory in
which you can compile the program like this:

    $ mkdir build && cd build && cmake .. && make && cd ..