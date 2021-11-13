#include "palabos2D.h"
#include "palabos2D.hh"

using namespace plb;

typedef double T;
#define ADESCRIPTOR descriptors::AdvectionDiffusionD2Q5Descriptor
#define ADYNAMICS AdvectionDiffusionBGKdynamics

void centerPointSetup(  MultiBlockLattice2D<T,ADESCRIPTOR>& adLattice, T M_0)
{
    plint nx = adLattice.getNx();
    plint ny = adLattice.getNy();
    plint center_x = nx/2;
    plint center_y = ny/2;
    Box2D centralSquare(center_x, center_x,center_y,center_y);
    T C_init = 0.0;             // Initialized to zero concentration (not density)
    Array<T,2> u0((T)0,(T)0);   // velocity (0,0)
    initializeAtEquilibrium(adLattice, adLattice.getBoundingBox(), C_init, u0);
    initializeAtEquilibrium(adLattice, centralSquare, M_0, u0);
    adLattice.initialize();
}

int main(){
    const plint nx = 1000;            // lattice points in x-direction
    const plint ny = 1000;            // lattice points in y-direction
    const double D = 1.0/6.0;         // Diffusivity
    const plint maxIter = 1000;       // Maximum number of iterations
    T tau = 3.0 * D + 0.5;            // hard coding this for now
    T adOmega = 1.0 / tau;            // omega = 1/tau 
    T M_0 = 1000.0;                   // concentration at the center

    // Instantiate the lattice
    MultiBlockLattice2D<T,ADESCRIPTOR> adLattice(
                                nx,
                                ny,
                                new ADYNAMICS<T, ADESCRIPTOR>(adOmega));
    // Periodic boundary in all directions
    adLattice.periodicity().toggleAll(true);    

    // Initial Condition
    centerPointSetup(adLattice,M_0);

    plb_ofstream successiveProfiles("concentrationProfiles.dat");
    for (plint iT = 0; iT<=maxIter; iT++){
        if (iT%50==0) {
            pcout << "Writing concentration profile  at iT = " << iT << std::endl;
            successiveProfiles << std::setprecision(7)
                << *computeDensity(adLattice, Box2D(0,nx,ny/2,ny/2))
                << std::endl << std::endl;
        }
        adLattice.collideAndStream();
    }
}
