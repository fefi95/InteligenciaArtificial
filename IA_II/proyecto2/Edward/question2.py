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
import graphics as gf
import numpy as np              # This provides access to an efficient
                                # multi-dimensional container of generic data.
import pandas as pd
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

maxIter = 15000

def readData(dataSetName):
    originalList = [] # initialize matrix of features without normalization.
    varList      = [] # initialize matrix of features with normalization.
    # Open the file.
    data = pd.read_csv(dataSetName, sep=" ", header = None)
    # Get the min and max vlues for each column. 
    minValues = []
    maxValues = []
    for i in range(0, len(data.columns)-1):
        minValues.append(data[i].min())
        maxValues.append(data[i].max())

    # Normalize the data.
    for index, row in data.iterrows():
        normalRow   = []
        rowObtained = []
        
        for i in range(0, len(row)-1):
            normalize = (row[i] - minValues[i]) / (maxValues[i] - minValues[i])
            normalRow.append(normalize) 
            rowObtained.append(row[i])

        normalRow.append(row[len(row)-1])
        rowObtained.append(row[len(row)-1])
        varList.append(normalRow)
        originalList.append(rowObtained)
    return { 'normalized': varList, 'original': originalList }

def getConfusionMatrix(predictedValue, originalValue):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    lastpos = len(predictedValue[0]) - 1
    nP = 0
    nF = 0
    for i in range(0, len(predictedValue)):
        if (predictedValue[i][lastpos] == 1 and originalValue[i][lastpos] == 1):
            TP += 1
            nP += 1
        elif (predictedValue[i][lastpos] == 1 and originalValue[i][lastpos] == 0):
            FP += 1
            nP += 1
        elif (predictedValue[i][lastpos] == 0 and originalValue[i][lastpos] == 0):
            TN += 1
            nF += 1
        else:
            FN += 1
            nF += 1

    print "TP: " + str(TP) + ", FP: " + str(FP) + ", TN: " + str(TN) + ", FN: " + str(FN)

def main():

    alpha = 0.1

    data500   = readData('datosP2EM2017/datos_P2_EM2017_N500.txt')
    dataG500  = readData('datosP2EM2017/datos_P2_Gen_500.txt')
    data1000  = readData('datosP2EM2017/datos_P2_EM2017_N1000.txt')
    dataG1000 = readData('datosP2EM2017/datos_P2_Gen_1000.txt')
    data2000  = readData('datosP2EM2017/datos_P2_EM2017_N2000.txt')
    dataG2000 = readData('datosP2EM2017/datos_P2_Gen_2000.txt')

    dataPredict = readData('datosP2EM2017/dataset_test_circle.txt')

    # statsF500 = open("datos_P2_EM2017_N500_stats", 'w')
    # statsF500.write("error en entrenamiento, error en prueba, falsos positivos, falsos negativos")
    print "--------------------------------------------------------------------------------"
    for i in range(5, 6):
        print "\t Calculando thetas para datos_P2_EM2017_N500 con " + str(i) + " neuronas..."
        print "\n Creo la red. \n"
        neuralNet = nn.NeuralNetwork(len(data500['normalized'][0]) - 1, i, 2)
        print "\n Entreno la red. \n"
        #print data500['x']
        nn.trainNetwork(neuralNet, data500['normalized'], alpha, maxIter, 2)
        #nn.trainNetwork(neuralNet, dataG500['normalized'], alpha, maxIter, 2)
        #nn.trainNetwork(neuralNet, data1000['normalized'], alpha, maxIter, 2)
        #nn.trainNetwork(neuralNet, dataG1000['normalized'], alpha, maxIter, 2)
        #nn.trainNetwork(neuralNet, data2000['normalized'], alpha, maxIter, 2)
        #nn.trainNetwork(neuralNet, dataG2000['normalized'], alpha, maxIter, 2)

        newData = []
        for row in dataPredict['normalized']:
            newData.append([row[0], row[1], nn.predictNetwork(neuralNet, row)])

        getConfusionMatrix(newData, dataPredict['original'])
        gf.drawPoints(newData)
        #print "\n Muestro la red. \n"
        #for layer in neuralNet:
        #   print layer
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
