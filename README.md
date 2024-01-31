# PIRD - INSA Lyon - GCU - 2024

RESULTS NOT VERIFIED

The repository presents the implementation of a new multi-criteria analysis procedure. This new procedure allows to consider the variability of the reference profiles (intervals) for the definition of the categories in the ELECTRE-Tri method. The multi-criteria analysis method used in this report is thus the probabilistic ELECTRE-Tri (Basser, 2023. This new procedure is applied to a case study of energy renovation of a building (Gauthier et Viala, 2023).

The repository contains:

Notebooks:
- **"MainElectreTri.ipynb" is the main Notebook file. Run this file to initiate the ELECTRE-Tri method on the provided dataset.**
- "PreProcess.ipynb" is the Notebook for the implementation of the Monte Carlo principle to the perfomances of the studied alternatives and the implementation of the intervals for the reference profiles.
- "Process.ipynb" is the Notebook for the implementation of all the calculations of the ELECTRE-Tri method (Gauthier et Viala, 2023).

Python codes:
- "MainElectreTri.py" is the main execution file.
- "PreProcess.py" is the implementation of the Monte Carlo principle to the perfomances of the studied alternatives and the implementation of the intervals for the reference profiles. It uses the "Input_Data.csv".
- "Process.py" is the implementation of all the calculations of the ELECTRE-Tri method.
- "Test.py" is the test of all methods from the python files above.

Data:
- "Input_Data.csv" is a csv file containing all the data necesaary for the project. These data were retrieved by Souleymane Daniel as part of his thesis where he applied ELECTRE-Tri individually to this project (Daniel, 2023).

Other:
- "Figures" is the folder which contains all the figures used in the Notebooks.
- "environment.yml" is the environment of the implementation.

**Reading order:**
1) "PreProcess.ipynb" for the explanations of the Monte Carlo method (Gauthier et Viala, 2023) and of the method for the implementation of the intervals for the reference profiles.
2) "Process.ipynb" for the explainations of all the calculation of the ELECTRE-Tri method (Gauthier et Viala, 2023).
3) "MainElectreTri.ipynb" for the compilation of all methods to obtain the results (optimisitic and pessimistic sorting of the alternatives into categories).

*Gauthier, N. & Viala, R., 2023. A New Procedure for Handling Input Data Uncertainty in the ELECTRE Tri Method: The Monte Carlo-ELECTRE Tri Approach, s.l.: s.n.*

*Daniel, S.; Ghiaus, C. Multi-Criteria Decision Analysis for Energy Retrofit of Residential Buildings: Methodology and Feedback from Real Application. Energies 2023, 16, 902. https://doi.org/10.3390/en16020902*

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/liloudeboulard/PIRD_ELECTRE-Tri/HEAD)
