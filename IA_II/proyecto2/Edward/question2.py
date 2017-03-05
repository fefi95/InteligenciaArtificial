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
# colors = {'purple' : '#78037F',
#           'orange' : '#F55D3E',
#           'magenta': '#A4243B',
#           'gray'   : '#454545',
#           'blue'   : '#1781AA',
#           'green'  : '#23CE6B',
#          }

colors = ['#78037F',
          '#F55D3E',
          '#A4243B',
          '#454545',
          '#1781AA',
          '#23CE6B',
          '#FFC857',
          '#101010',
          '#FF2020'
          ]

maxIter = 1000

"""
    Description:
        reads the data of a given datset and outputs its attributes and
        result
    Params:
        @param dataSetName: name of the file where the dataset is
"""

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

"""
    Description:
        reads the data of a given datset and outputs its attributes and
        result
    Params:
        @param dataSetName: name of the file where the dataset is
"""

def getConfusionMatrix(predictedValue, originalValue):
    TP = 0 # True positive
    FP = 0 # False positive
    TN = 0 # True negative
    FN = 0 # False negative

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
    return [TP, FP, TN, FN]


def calculate(dataFileName, dataPredict, alpha):
    data = readData("datosP2EM2017/" + dataFileName +".txt")
    statsF = open("datosP2EM2017/" + dataFileName + "_stats.csv", 'w')
    statsF.write("numero de neuronas, error en entrenamiento, error en prueba, falsos positivos, falsos negativos\n")
    results = []
    print "--------------------------------------------------------------------------------"
    for i in range(2, 11):
        print "\t calculando thetas para" + dataFileName + " con " + str(i) + " neuronas..."
        print "\t Creando la red."
        neuralNet = nn.NeuralNetwork(len(data['normalized'][0]) - 1, i, 2)
        print "\t Entrenando la red."
        result = nn.trainNetwork(neuralNet, data['normalized'], alpha, maxIter, 2)
        results.append(result)
        newData = []
        for row in dataPredict['normalized']:
            newData.append([row[0], row[1], nn.predictNetwork(neuralNet, row)])

        cm = getConfusionMatrix(newData, dataPredict['original'])
        errorE = result[maxIter-1]
        errorP = 0
        # average(false positive + false negative )
        errorP = (float(cm[1]) + float(cm[3]))/10000

        statsF.write(str(i) + ", " + str(errorE) + ", " + str(errorP) + ", " + str(cm[1]) + ", " + str(cm[3])+ "\n")
        gf.drawPoints(newData, dataFileName, i)

    statsF.close()

    # Making plots
    j = 2
    for result in results:
        # Simple plot: iterations vs error
        iterations = np.arange(0, maxIter, 1)
        gf.makeSimplePlot(iterations, result, dataFileName, j, colors[j-2])
        j += 1
    plt.show()


def main():

    alpha = 0.1
    dataPredict = readData('datosP2EM2017/dataset_test_circle.txt')

    # calculate("datos_P2_EM2017_N500", dataPredict, alpha)
    # calculate("datos_P2_Gen_500", dataPredict, alpha)
    # calculate("datos_P2_EM2017_N1000", dataPredict, alpha)
    # calculate("datos_P2_Gen_1000", dataPredict, alpha)
    calculate("datos_P2_EM2017_N2000", dataPredict, alpha)
    calculate("datos_P2_Gen_2000", dataPredict, alpha)

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
