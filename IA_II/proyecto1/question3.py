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

data = pd.DataFrame.from_csv("dataC12X.csv") # Load the data with the initial mining.
# atrributeNames = list(data)       # Get the attribute's name.

# Hash table to replace the atributes with nominal values for numeric values.
# attributeNewValues = attributeTransformation

# Make dummies variables for nominal attributes.
processedData = pd.get_dummies(data, dummy_na=True)

# Get the 80% of the data.
eightyP = int(processedData.shape[0] * 0.8);
eightyPData = processedData[0:eightyP]
# Add the text format.
eightyPDataFile = open('eightyPData.txt','w')
eightyPDataFile.write(str(eightyPData.shape[1] + 1) + ' columns\n') # Add the number of columns.
eightyPDataFile.write(str(eightyPData.shape[0]) + ' rows\n')    # Add the number of rows.
eightyPDataFile.write('Order\n')    # Add the number of rows.

# Add the attributes name.
for attribute in list(processedData):
    eightyPDataFile.write(attribute +'\n')
eightyPDataFile.close()
# Add the values.
eightyPData.to_csv('eightyPData.txt', sep=' ', header=False, encoding='utf-8', mode='a')

# Get the remaining 20% of the data.
twentyPData = processedData[eightyPData.shape[0] + 1: processedData.shape[0] + 1]
# Add the text format.
twentyPDataFile = open('twentyPData.txt','w')
twentyPDataFile.write(str(twentyPData.shape[1]) + ' columns\n') # Add the number of columns.
twentyPDataFile.write(str(twentyPData.shape[0]) + ' rows\n')    # Add the number of rows.
twentyPDataFile.write('Order\n')
# Add the attributes name.
for attribute in list(processedData):
    twentyPDataFile.write(attribute +'\n')
twentyPDataFile.close()
# Add the values.
twentyPData.to_csv('twentyPData.txt', sep=' ', header=False, encoding='utf-8', mode='a')

alpha = float(0.1) # learning rate to use.
ds_80 = lr.DataSet('eightyPData.txt')
print(ds_80.varList)
result = lr.gradientDescent(alpha, ds_80.varList, ds_80.resultList, ds_80.thetas, ds_80.rows, ds_80.columns)
print(result['converge']) # Let you know if the function converge.

# processedData.to_csv('data2.csv')
