#------------------------------------------------------------------------------
#   Comparing the analytical solution with the LBM solution 
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

def read_lbm_file(  f_name : str, nx : int, intervals : int) -> np.array:
    # This function reads the *.dat file that Palabos writes on the
    with open(f_name,'r') as f:
        text = f.read().split(" ")
    temp = np.array([float(j) for j in text[0:-1]]).reshape(intervals,nx)
    return(temp)

def color(x : int) -> str: return 'rbgmcyk'[x%7]             # color cycler

def main(plot_interval : int = 1) -> None:
    nx : int = 1000
    ny : int = 1000
    dpi : float = 300
    extension : str = 'png'
    D : float = 1.0/6.0
    times = range(0,1000,50)
    boundary = 500
    M0 : float = 1000
    intervals : int = 21
    f_name = 'concentrationProfiles.dat'
    lbm_values = read_lbm_file( f_name, nx, intervals)
    rad = np.linspace(-boundary,boundary,nx)
    plt.figure(0, figsize = (8,8))
    for i,t in enumerate(times):
        if i % plot_interval == 0 and i != 0:
            analytical = np.array([(M0/(4*np.pi*D*t))*np.exp(-r**2/(4*D*t)) for r in rad])
            plt.plot(rad,analytical,'{}--'.format(color(i)), linewidth = .75, label = "{} s".format(t))
            plt.plot(rad-.5,lbm_values[i],'ko', markerfacecolor = color(i), markersize = 3)

    plt.title(r"C(r,t) = $\frac{M_0}{4 \pi Dt}$exp($\frac{-r^2}{4Dt}$)"+"; Domain = {}x{} lu$^2$; M$_0$ = {} mu".format(2*boundary,2*boundary,M0))
    plt.grid(True)
    plt.legend()
    plt.xlim(-75,75)
    plt.xlabel("Lattice Units")
    plt.ylabel("Concentration mu lu$^{-2}$")
    plt.savefig('.comparisonD2Q5.png',dpi = dpi)
    plt.show()

if __name__ == "__main__":
    main(2)
