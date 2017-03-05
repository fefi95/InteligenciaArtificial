"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Description:
        This file contains the answer for question 2
"""

# .----------------------------------------------------------------------------.
# Import libraries to use.

import NeuralNetwork as nn      # Neural Network library
import numpy as np              # This provides access to an efficient
                                # multi-dimensional container of generic data.
import matplotlib.pyplot as plt # This provides functions for making plots
# .----------------------------------------------------------------------------.

# Colors used for the plots
colors = {'purple' : '#78037F',
          'orange' : '#F55D3E',
          'magenta': '#A4243B',
          'gray'   : '#454545',
          'blue'   : '#1781AA',
          'green'  : '#23CE6B',
         }

maxIter = 1000

def readData(dataSetName):
    dataSetFile = open(dataSetName, 'r'); # Get the dataset.
    varList     = [] # initialize matrix of features
    resultList  = [] # initialize matrix of results

    for line in dataSetFile:
        wordList = line.split()
        varList.append(wordList[:-1])
        resultList.append([wordList[-1]])

    varList    = np.array(varList, dtype=np.float128)
    resultList = np.array(resultList, dtype=np.float128)

    # Mean normalization to the varList and resultList.
    transVar = varList.transpose()

    # Update the varList and the resultList.
    for i in range(0, len(varList[0])):
        mean = np.mean(transVar[i])
        std = np.std(transVar[i])
        for j in range(len(varList)):
            if (std != 0):
                varList[j][i] = (varList[j][i] - mean) / std

    return {'x' : varList, 'y': resultList}

def main():

    alpha = 0.001

    data500 = readData('datosP2EM2017/datos_P2_EM2017_N500.txt')
    # statsF500 = open("datos_P2_EM2017_N500_stats", 'w')
    # statsF500.write("error en entrenamiento, error en prueba, falsos positivos, falsos negativos")

    print "--------------------------------------------------------------------------------"
    for i in range(2, 3):
        print "\t Calculando thetas para datos_P2_EM2017_N500 con " + str(i) + " neuronas..."
        print "\n Creo la red. \n"
        print data500['x']
        neuralNet = nn.NeuralNetwork(len(data500['x'][0]), i, 2)
        print "\n Entreno la red. \n"
        nn.trainNetwork(neuralNet, data500, alpha, maxIter, 2)
        print "\n Muestro la red. \n"
        for layer in neuralNet:
        	print layer
        # actualizo los pesos
        #neural.gradientChecking(data500['x'], data500['y'])
        #result = neural.gradientDescent(alpha, data500['x'], data500['y'])

        # Statistics
        # errorE = 0
        # errorP = 0
        # falseP = 0
        # flaseN = 0
        # statsF500.write(str(errorE) + ", " + str(errorP) + ", " + str(falseP) + ", " + str(flaseN))
        # Simple plot: iterations vs cost function
        #iterations = np.arange(0, result['nIterations'] + 1, 1)
        #makeSimplePlot(iterations, result['costFunction'], "datos_P2_EM2017_N500", i, colors['blue'])
    #print "--------------------------------------------------------------------------------"
    #plt.show()

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
