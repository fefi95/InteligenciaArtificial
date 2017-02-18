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
import linearRegression as lr   # linear regresion library
# .----------------------------------------------------------------------------.

colors = {'purple' : '#78037F',
          'orange' : '#F55D3E',
          'magenta': '#A4243B',
          'gray'   : '#454545',
          'blue'   : '#1781AA',
          'green'  : '#6DA34D', #23CE6B
         }

# Two parameters: input file with data and learning rate (alpha)
def main():

    # ------------------------------------------------------------------------#
    #                             dataset_x01                                 #
    # ------------------------------------------------------------------------#
    alpha = float(0.1) # learning rate to use.
    dataSetName = 'dataset_x01'

    ds_01 = lr.DataSet(dataSetName + '.txt')
    result = lr.gradientDescent(alpha, ds_01.varList, ds_01.resultList, ds_01.thetas, ds_01.rows, ds_01.columns)
    print(result['converge']) # Let you know if the function converge.

    #------------------------------- plots -----------------------------------#

    # Simple plot: iterations vs cost function
    iterations = np.arange(0, result['nIterations'] + 1, 1)
    makeSimplePlot(iterations, result['costFunction'], dataSetName, alpha, colors['blue'])
    plt.show()

    # Scatter plot: feature xi vs result and hypothesis
    x1 = [] # feature x1
    h = [] # hypothesis
    for xi in ds_01.varList:
        x1.append(xi[1])
        h.append(result['thetas'][0] + result['thetas'][1]*xi[1])

    makeScatterPlot(x1, ds_01.resultList, h, ds_01.att[1], ds_01.att[2], dataSetName)
    plt.show()

    #-------------------------------------------------------------------------#
    #                             dataset_x08                                 #
    #-------------------------------------------------------------------------#
    alpha = float(0.1) # learning rate to use.
    dataSetName = 'dataset_x08'

    #------------------------------- question a ------------------------------#
    ds_08 = lr.DataSet(dataSetName + '.txt')
    result = lr.gradientDescent(alpha, ds_08.varList, ds_08.resultList, ds_08.thetas, ds_08.rows, ds_08.columns)
    print(result['converge']) # Let you know if the function converge.

    #------------------------------- plots -----------------------------------#

    # Simple plot: iterations vs cost function
    iterations = np.arange(0, result['nIterations'] + 1, 1)
    makeSimplePlot(iterations, result['costFunction'], dataSetName, alpha, colors['purple'])
    plt.show()

    #------------------------------ end question a ---------------------------#


    #------------------------------- question b ------------------------------#
    alphas = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]

    ds_08 = lr.DataSet(dataSetName + '.txt')
    colorsKeys = colors.keys()
    color = 0;
    for alpha in alphas :
        result = lr.gradientDescent(alpha, ds_08.varList, ds_08.resultList, ds_08.thetas, ds_08.rows, ds_08.columns)
        print(result['converge']) # Let you know if the function converge.

        #----------------------------- plots ---------------------------------#

        # Simple plot: iterations vs cost function
        iterations = np.arange(0, result['nIterations'] + 1, 1)
        makeSimplePlot(iterations, result['costFunction'], dataSetName + '_multiple', alpha, colors[colorsKeys[color]])
        color = color + 1

    plt.show()
    #------------------------------ end question b ---------------------------#

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

"""
    Descripction: scatter plot of the cost function against number of iterations
    Parameters:
        @param feature     : position of the theta to use.
        @param result      : results. Column to be predicted (y)
        @param linearReg   : linear regresion that fits into the data
        @param featureName : name of the feature (xi)
        @param resultName  : name of result (y)
        @param dsName      : name of dataset
"""
def makeScatterPlot(feature, result, linearReg, featureName, resultName, dsName):

    plt.scatter(feature, result, c=colors['orange'], edgecolor = colors['gray'])
    plt.plot(feature, linearReg, label='regresion lineal', c=colors['gray'])
    plt.xlabel(featureName)
    plt.ylabel(resultName)
    plt.title(dsName)
    plt.legend()
    plt.savefig(dsName + "_scatter.png")

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
