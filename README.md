# DarkCapPy

Written by: Adam Green (agree019@ucr.edu) and Philip Tanedo (flip.tanedo@ucr.edu)

DarkCapPy is a Python 3/Jupyter package for calculating rates associated with dark matter capture in the Earth, annihilation into light mediators, and the subsequent observable decay of the light mediators near the surface of the Earth. The package includes a calculation of the Sommerfeld enhancement at the center of the Earth and the timescale for capture--annihilation equilibrium. The code is open source and can be modified for other compact astronomical objects and mediator spins. The reference paper can be found at: https://arxiv.org/abs/1509.07525v3. Along with being included in the package, the manual can be found at https://arxiv.org/abs/1808.03700.

## DarkCapPy Dependencies

Python 3.6.2

__Python Packages__
 - Numpy 1.14.3
 - Scipy 0.19.1
 - Pandas 0.22.0


## Installation with PIP

`pip install git+https://github.com/agree019/DarkCapPy`

## Package Structure
```
DarkCapPy/
||DarkPhoton.py
||Configure/
||--AtomicData.py
||--Constants.py
||--PlanetData.py
||--PREM500.csv
||Template_Calculation/
||--DarkCapPy_Template.ipynb
||--Branching_Ratio/
||----Branching_Ratio.READ_ME.txt
||----brtoe.csv
||--Signal/
||----Signal_READ_ME.txt
||----100GeVSignal.csv
||----Signal_Backups/
||------Signal_Backups_Read_ME.txt
||--Sommerfeld/
||----Sommerfeld_READ_ME.txt
||----100GeVSommerfeld.csv
```

## File Descriptions
#### DarkPhoton.py
This file contains all the function definitions to calculate the "Earthshine" scenario.

#### AtomicData.py
This file contains information about elements, eg: atomic mass, number of protons.

#### Constants.py
This file initializes all constants used in this calculation.

#### PlanetData.py
This file initializes the planet-dependent quantities, eg: enclosed mass, escape velocity. The input comma separated file (csv) file defines the planet.

#### PREM500.csv
This csv file contains radius and density information about Earth.

#### DarkCapPy_Template.ipynb
This Jupyter notebook contains an example implementation of DarkCapPy

#### brtoe.csv
This file stores the branching ratio to electron-positron pairs as a function of mediator mass.

#### 100GeVSignal.csv
This file is a completed Signal file for dark matter with a mass of 100 GeV.

#### 100GeVSommerfeld.csv
This file is a completed Sommerfeld file for dark matter with a mass of 100 GeV.

## Example use
```python
import numpy as np
import pandas as pd
from scipy.interpolate import interpolate

from DarkCapPy import *
import DarkCapPy.DarkPhoton as DP

mx = 1000
ma = 1
epsilon = 1e-8
alpha = 1/137
alphax = 0.035
tauCross = DP.tauCross

cap1 = DP.cCap(mx, ma, epsilon, alpha, alphax)
kappa0 = DP.kappa_0(mx, alpha)
cap2 = DP.cCapQuick(mx, ma, epsilon, alphax, kappa0)


sommerfeld = DP.thermAvgSommerfeld(mx, ma, alphax)
sigma = DP.sigmaVtree(mx, ma, alphax)
ann = DP.cAnn(mx, sigma, sommerfeld)

tau = DP.tau(cap1, ann)

gammaAnn = DP.gammaAnn(cap1, ann)
L = DP.decayLength(mx, ma, epsilon, 1)
Edecay = DP.epsilonDecay(L)

signal = DP.iceCubeSignal(gammaAnn, Edecay, DP.yr2s(10))
```
## Output
    Capture_1            : 110079473.7575132
    Kappa_0              : 3.1452272427969017e+25
    Capture_2            : 110082953.49789158
    Therm Avg Sommerfeld : 238.71863691039448
    Sigma V              : 3.8484490764205524e-09
    Annihilation         : 1.8311290915841913e-46
    EQ Time              : 7.04348098392085e+18
    Gamma_ann            : 22336.873085842682
    Decay Length         : 87324480.0
    Epsilon_decay        : 5.100088114082073e-07
    N_signal             : 0.012594031678514129
