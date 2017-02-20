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

# Color using for the plots
colors = {'purple' : '#78037F',
          'orange' : '#F55D3E',
          'magenta': '#A4243B',
          'gray'   : '#454545',
          'blue'   : '#1781AA',
          'green'  : '#6DA34D',
         }

def main():
    data = pd.DataFrame.from_csv("dataC12X3.csv") # Load the data with the initial mining.

    # Delete column sale price before get dummies
    resultList = data['SalePrice']
    data = data.drop('SalePrice', 1)
    # Make dummies variables for nominal attributes.
    processedData = pd.get_dummies(data)
    #  Add column sale price at the end of the dummies
    processedData = processedData.assign(SalePrice=resultList.values)

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
    twentyPDataFile.write(str(twentyPData.shape[1] + 1) + ' columns\n') # Add the number of columns.
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
    result = lr.gradientDescent(alpha, ds_80.varList, ds_80.resultList, ds_80.thetas, ds_80.rows, ds_80.columns)
    print(result['converge']) # Let you know if the function converge.

    #------------------------------- plots -----------------------------------#

    # Simple plot: iterations vs cost function
    iterations = np.arange(0, result['nIterations'] + 1, 1)
    makeSimplePlot(iterations, result['costFunction'], 'Ames Housing', alpha, colors['magenta'])

    # Use the test data set with the predicting model
    ds_20 = lr.DataSet('twentyPData.txt')
    hypothesis = np.dot(ds_20.varList, result['thetas'])
    makeBiasPlot(ds_20.resultList, hypothesis)
    makeMaxDeviationPlot(ds_20.resultList, hypothesis)
    makeMeanDeviationPlot(ds_20.resultList, hypothesis)
    makeMeanSquarePlot(ds_20.resultList, hypothesis)

"""
    Descripction: plot of the cost function against number of iterations
    Parameters:
        @param iterations   : position of the theta to use.
        @param costFunction : array that contains the values for every cost
        @param dsName       : name of dataset
        @param label        : label of the legend plot
        @param color        : color of the line on the plot
"""
def makeSimplePlot(iterations, costFunction, dsName, label, color):
    plt.plot(iterations, costFunction, label='alpha= ' + str(label), c=color, linewidth=1.5)
    plt.xlabel("numero de iteraciones")
    plt.ylabel("Funcion de costo (J)")
    plt.title(dsName)
    plt.grid(True)
    plt.legend()
    plt.savefig(dsName + ".png")
    plt.show()

"""
    Descripction: plot of bias estimate
    Parameters:
        @param real      : actual value of the feature to be predicted
        @param predicted : values predicted by linear regression
"""
def makeBiasPlot(real, predicted):

    index = np.arange(2)
    bias = np.average(real - predicted)
    print(bias)
    dsName = "Sesgado - Ames Housing"
    plt.bar(index, [0, bias], width=0.35, color=colors['blue'] )
    plt.xlabel("promedio(valor real - valor estimado)")
    plt.title(dsName)
    plt.xticks( index + 0.35/2,('', 'A'))
    plt.legend()
    plt.savefig(dsName + ".png")
    plt.show()

"""
    Descripction: plot of maximum deviation estimate
    Parameters:
        @param real      : actual value of the feature to be predicted
        @param predicted : values predicted by linear regression
"""
def makeMaxDeviationPlot(real, predicted):

    index = np.arange(2)
    maxi = np.max(np.abs(real - predicted))
    print(maxi)
    dsName = "Desviacion Maxima - Ames Housing"
    plt.bar(index, [0, maxi], width=0.35, color=colors['purple'] )
    plt.xlabel("max(abs(valor real - valor estimado))")
    plt.title(dsName)
    plt.xticks( index + 0.35/2,('', 'A'))
    plt.legend()
    plt.savefig(dsName + ".png")
    plt.show()

"""
    Descripction: plot of mena deviation estimate
    Parameters:
        @param real      : actual value of the feature to be predicted
        @param predicted : values predicted by linear regression
"""
def makeMeanDeviationPlot(real, predicted):

    index = np.arange(2)
    mean = np.average(abs(real - predicted))
    print(mean)
    dsName = "Desviacion Media Absoluta  - Ames Housing"
    plt.bar(index, [0, mean], width=0.35, color=colors['orange'] )
    plt.xlabel("promedio(abs(valor real - valor estimado))")
    plt.title(dsName)
    plt.xticks( index + 0.35/2,('', 'A'))
    plt.legend()
    plt.savefig(dsName + ".png")
    plt.show()

"""
    Descripction: plot of mean square error estimate
    Parameters:
        @param real      : actual value of the feature to be predicted
        @param predicted : values predicted by linear regression
"""
def makeMeanSquarePlot(real, predicted):

    index = np.arange(2)
    mean2 = np.mean((real - predicted)**2)
    print(mean2)
    dsName = "Error cuadratico medio  - Ames Housing"
    plt.bar(index, [0, mean2], width=0.35, color=colors['green'] )
    plt.xlabel("media(valor real - valor estimado ^ 2)")
    plt.title(dsName)
    plt.xticks( index + 0.35/2,('', 'A'))
    plt.legend()
    plt.savefig(dsName + ".png")
    plt.show()

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
