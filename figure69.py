#!/Users/cyrus/miniconda3/bin/python3
import matplotlib.pyplot as plt
from numpy import meshgrid,linspace,array,sqrt,pi,exp
#------------------------------------------------------------------------------
#   Comparing the analytical solution with the LBM solution 
#------------------------------------------------------------------------------
def read_lbm_file(  f_name,
                    nx,
                    intervals):
    # This function reads the *.dat file that Palabos writes on the
    with open(f_name,'r') as f:
        text = f.read().split(" ")
    temp = array([float(j) for j in text[0:-1]]).reshape(intervals,nx)
    return(temp)

color = 'rbgmcy'*1000
nx = 1000
dpi = 300
extension = 'png'
times = list(range(0,1000,50))
D = 1/6
boundary = 500
M0 = 1000
intervals = 21
f_name = 'concentrationProfiles.dat'
lbm_values = read_lbm_file( f_name, nx, intervals)
rad = linspace(-boundary,boundary,nx)
plt.figure(0, figsize = (8,8))
for i,t in enumerate(times):
    if i % 2 == 0 and i != 0:
        analytical = array([(M0/(4*pi*D*t))*exp(-r**2/(4*D*t)) for r in rad])
        plt.plot(rad,analytical,'{}--'.format(color[i]), linewidth = .75, label =
                "{} s".format(t))
        plt.plot(rad-.5,lbm_values[i],'ko', markerfacecolor = color[i], markersize = 3)

plt.title(r"C(r,t) = $\frac{M_0}{4 \pi Dt}$exp($\frac{-r^2}{4Dt}$)"+"; Domain = {}x{} lu$^2$; M$_0$ = {} mu".format(2*boundary,2*boundary,M0))
plt.grid(True)
plt.legend()
plt.xlim(-75,75)
plt.xlabel("Lattice Units")
plt.ylabel("Concentration mu lu$^{-2}$")
plt.savefig('comparisonD2Q5.png',dpi = dpi)
plt.show()
