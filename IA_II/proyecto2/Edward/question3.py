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
import random as rm             # To use random functions.
# .----------------------------------------------------------------------------.

# Colors used for the plots

# Max number of iterations.
maxIter = 1000

# Co-relation between the class and number.
binaryClass  = {"Iris-setosa": 1, "Iris-versicolor": 0, "Iris-virginica": 0}
numericClass = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}

"""
    Description:
        Read the dataset and transform the data class.
    Params:
        @param dataSetName: file's name of the dataset to use.
        @param isBinary   : the data class will be a binary o numeric class.
"""
def readData(dataSetName, isBinary, frac):
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
    return { 'train': trainList, 'test': testList }

"""
    Description:
        Gets the confusion matrix for the data
    Params:
        @param predictedValue: the value predicted for the network
        @param originalValue : the orginal value of the data set
"""

def getConfusionMatrix(predictedValue, originalValue):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    correct = 0
    incorrect = 0
    lastpos = len(originalValue[0]) - 1
    nP = 0
    nF = 0
    for i in range(0, len(predictedValue)):
        if (abs(predictedValue[i] - originalValue[i][lastpos]) < 0.01):
            correct += 1
        else:
            incorrect += 1
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

    error = float(incorrect)/len(predictedValue)
    print "correct " + str(correct) + " incorrect "  + str(incorrect) + " error " + str(error)
    # print "TP: " + str(TP) + ", FP: " + str(FP) + ", TN: " + str(TN) + ", FN: " + str(FN)
    return [error, correct, incorrect]

def main():

    statsFB = open("datosP2EM2017/data_iris_stats_binary.csv", 'w')
    statsFC = open("datosP2EM2017/data_iris_stats_class.csv", 'w')
    statsFB.write("% \datos de entrenamiento, numero de neuronas, error en prueba, aciertos, fallos\n")
    statsFC.write("% \datos de entrenamiento, numero de neuronas, error en prueba, aciertos, fallos\n")

    alpha = 0.1 # Learning rate to use.
    print "--------------------------------------------------------------------------------"
    # For split the data into i*10% for training and (100 - i*10) for test.
    for i in range(5,10):

        dataIrisBinary  = readData('datosP2EM2017/data_iris.txt', True, float(i)/10)
        dataIrisNumeric = readData('datosP2EM2017/data_iris.txt', False, float(i)/10)

        # Total of neuron to use in the hidden layers.
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

            cm = getConfusionMatrix(newData, dataIrisBinary['test'])
            statsFB.write(str(i*10) + ", " + str(j) + ", " + str(cm[0]) + ", " + str(cm[1]) + ", " + str(cm[2])+ "\n")

            cm = getConfusionMatrix(newData3out, dataIrisNumeric['test'])
            statsFC.write(str(i*10) + ", " + str(j) + ", " + str(cm[0]) + ", " + str(cm[1]) + ", " + str(cm[2])+ "\n")

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
