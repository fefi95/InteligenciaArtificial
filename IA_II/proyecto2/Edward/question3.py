"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Description:
        This file contains the answer for question 3
"""

# .----------------------------------------------------------------------------.
# Import libraries to use.

import NeuralNetwork as nn      # Neural Network library
import graphics as gf           # This provides access to plot functions for the data.
import numpy as np              # This provides access to an efficient
                                # multi-dimensional container of generic data.
import pandas as pd             # This provides access to function for data manipulation
                                # and analysis.
import matplotlib.pyplot as plt # This provides functions for making plots
import random as rm             # To use random functions.
# .----------------------------------------------------------------------------.

# Colors used for the plots
colors = {'purple' : '#78037F',
          'orange' : '#F55D3E',
          'magenta': '#A4243B',
          'gray'   : '#454545',
          'blue'   : '#1781AA',
          'green'  : '#23CE6B',
         }

# Max number of iterations.
maxIter = 1500

# Co-relation between the class and number.
binaryClass  = {"Iris-setosa": 1, "Iris-versicolor": 0, "Iris-virginica": 0}
numericClass = {"Iris-setosa": 1, "Iris-versicolor": 2, "Iris-virginica": 3}

"""
    Description:
        Read the dataset and transform the data class.
    Params:
        @param dataSetName: file's name of the dataset to use.
        @param isBinary   : the data class will be a binary o numeric class.
"""
def readData(dataSetName, isBinary, frac):
    # originalList = [] # initialize matrix of features without normalization.
    # varList      = [] # initialize matrix of features with normalization.
    # Open the file.
    trainList = []
    testList = []
    data = pd.read_csv(dataSetName, sep=",", header = None)
    # Get the min and max vlues for each column. 
    minValues = []
    maxValues = []
    for i in range(0, len(data.columns)-1):
        mini = data[i].min()
        maxi = data[i].max()
        data[i] = (data[i] - mini) / (maxi - mini)
        # minValues.append(data[i].min())
        # maxValues.append(data[i].max())
    if (isBinary):
        data[len(data.columns)-1].replace(binaryClass, inplace = True)
    else: 
        data[len(data.columns)-1].replace(numericClass, inplace = True)

    data_train = data.sample(frac = frac)
    data_test = data.drop(data_train.index)
    for index, row in data_train.iterrows():
        trainList.append(row.values.tolist())
        
    for index, row in data_test.iterrows():
        testList.append(row.values.tolist())

    # Normalize the data.
    # for index, row in data.iterrows():
    #     normalRow   = []
    #     rowObtained = []
        
    #     for i in range(0, len(row)-1):
    #         normalize = (row[i] - minValues[i]) / (maxValues[i] - minValues[i])
    #         normalRow.append(normalize) 
    #         rowObtained.append(row[i])

    #     # Transform the data into binary class o numerical class. 
    #     if (isBinary):
    #         normalRow.append(binaryClass[row[len(row)-1]])
    #         rowObtained.append(binaryClass[row[len(row)-1]])    
    #     else:
    #         normalRow.append(numericClass[row[len(row)-1]])
    #         rowObtained.append(numericClass[row[len(row)-1]])
        
    #     varList.append(normalRow)
    #     originalList.append(rowObtained)
    return { 'train': trainList, 'test': testList }

def getConfusionMatrix(predictedValue, originalValue):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    lastpos = len(originalValue[0]) - 1
    nP = 0
    nF = 0
    for i in range(0, len(predictedValue)):
        if (predictedValue[i] == 1 and originalValue[i][lastpos] == 1):
            TP += 1
            nP += 1
        elif (predictedValue[i] == 1 and originalValue[i][lastpos] == 0):
            FP += 1
            nP += 1
        elif (predictedValue[i] == 0 and originalValue[i][lastpos] == 0):
            TN += 1
            nF += 1
        elif (predictedValue[i] == 0 and originalValue[i][lastpos] == 1):
            FN += 1
            nF += 1
        else:
            pass
    print "TP: " + str(TP) + ", FP: " + str(FP) + ", TN: " + str(TN) + ", FN: " + str(FN)

def main():

    alpha = 0.1 # Learning rate to use.
    print "--------------------------------------------------------------------------------"
    # For split the data into i*10% for training and (100 - i*10) for test.

        # Total of neuron to use in the hidden layers.
    for i in range(5,10):

        dataIrisBinary  = readData('datosP2EM2017/data_iris.txt', True, float(i)/10)
        dataIrisNumeric = readData('datosP2EM2017/data_iris.txt', False, float(i)/10)

        for j in range(4, 11):    
            print "\n Calculando thetas para data_iris.txt usando el " + str(float(i)/10) + " de los datos con " + str(j) + " neuronas..."
            print "\n Creo la red. \n"
            neuralNet = nn.NeuralNetwork(len(dataIrisBinary['train'][0]) - 1, j, 2)
            neuralNet3out = nn.NeuralNetwork(len(dataIrisNumeric['train'][0]) - 1, j, 3)

            print "\n Entreno la red. \n"
            nn.trainNetwork(neuralNet, dataIrisBinary['train'], alpha, maxIter, 2)  
            nn.trainNetwork(neuralNet3out, dataIrisNumeric['train'], alpha, maxIter, 3)  

            newData = []
            for row in dataIrisBinary['test'] :
                newData.append(nn.predictNetwork(neuralNet, row))
            newData3out = []
            for row in dataIrisNumeric['test'] :
                newData3out.append(nn.predictNetwork(neuralNet3out, row))

            getConfusionMatrix(newData, dataIrisBinary['test'])
            getConfusionMatrix(newData3out, dataIrisNumeric['test'])

            #gf.drawPoints(newData)
# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
