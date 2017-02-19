"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Stefani Castellanos 11-11394
    Carlos Ferreira 11-10323

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
import linearRegression as lr   # linear regresion library
from attributes import *
# .----------------------------------------------------------------------------.

data = pd.DataFrame.from_csv("dataC12.csv") # Load the data with the initial mining.
# atrributeNames = list(data)       # Get the attribute's name.

# Hash table to replace the atributes with nominal values for numeric values.
# attributeNewValues = attributeTransformation

processedData = pd.get_dummies(data, dummy_na=True)
# processedData.to_csv('data2.csv')
print(len(list(processedData)))
# processedData.to_csv('data3.txt', sep=' ')
