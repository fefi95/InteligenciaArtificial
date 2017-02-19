"""
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-11121
    Stefani Castellanos 11-11394
    Carlos Ferreira <insert ID>

    Description:
        This file contains the awnser for question 2 of the project.
"""

# .----------------------------------------------------------------------------.
# Import libraries to use.

import sys                      # This provides access to some variables used
                                # or maintained by the interpreter.
import numpy as np              # This provides access to an efficient
                                # multi-dimensional container of generic data.
import matplotlib.pyplot as plt # This provides functions for making plots
import pandas as pd
from attributes import *
# .----------------------------------------------------------------------------.

data = pd.read_csv("dataC12.csv") # Load the data with the initial mining.
atrributeNames = list(data)       # Get the attribute's name.

# Hash table to replace the atributes with nominal values for numeric values.
attributeNewValues = attributeTransformation

print(data.ix[1][1])
