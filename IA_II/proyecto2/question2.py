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

def readData(dataSetName):
    dataSetFile = open(dataSetName, 'r'); # Get the dataset.
    varList = [] #initialize matrix of features
    resultList = [] # initialize matrix of results

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
    plt.plot(iterations, costFunction, label='#neuronas= ' + str(label), linewidth=1.5)
    plt.xlabel("numero de iteraciones")
    plt.ylabel("Funcion de costo (J)")
    plt.title(dsName)
    plt.grid(True)
    plt.legend()
    plt.savefig(dsName + ".png")

def main():

    # print data500['x']
    # print data500['y']
    # neural = nn.NeuralNetwork(2, 2, 1)
    # h = neural.forwardPropagation(np.array([[0,0]]))
    # print h
    # b = neural.backPropagation(np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[1],[0], [0], [1]]))
    # print "ahhhhh"
    # print b
    alpha = 0.001
    # g = neural.gradientDescent(alpha, np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[1],[0], [0], [1]]))
    dataTest = readData('datosP2EM2017/dataset_test_circle.txt')
    n = 10000
    data500 = readData('datosP2EM2017/datos_P2_EM2017_N500.txt')
    statsF500 = open("datosP2EM2017/datos_P2_EM2017_N500_stats.csv", 'w')
    statsF500.write("numero de neuronas, error en entrenamiento, error en prueba, falsos positivos, falsos negativos\n")

    print "--------------------------------------------------------------------------------"
    for i in range(2, 11):
        print "\t calculando thetas para datos_P2_EM2017_N500 con " + str(i) + " neuronas..."
        neural = nn.NeuralNetwork(len(data500['x'][0]), i, 1)
        result = neural.gradientDescent(alpha, data500['x'], data500['y'])

        # Statistics
        errorE = 0
        errorAux = 0
        falseP = 0
        falseN = 0
        errorP = 0
        for j in range(0, n):
            hyp = neural.forwardPropagation(dataTest['x'][j])
            predicted = hyp[0]
            real = dataTest['y'][j]
            errorAux += abs(predicted - real )
            if (predicted > 0.5 and real < 0.01):
                falseP += 1
            elif (predicted < 0.5 and abs(real - 1) < 0.01):
                falseN += 1

        errorP = errorAux[0]/n
        statsF500.write(str(i) + ", " + str(errorE) + ", " + str(errorP) + ", " + str(falseP) + ", " + str(falseN)+ "\n")

        # Simple plot: iterations vs cost function
        iterations = np.arange(0, result['nIterations'] + 1, 1)
        makeSimplePlot(iterations, result['costFunction'], "datos_P2_EM2017_N500", i, colors['blue'])
    print "--------------------------------------------------------------------------------"
    plt.show()


    dataG500 = readData('datosP2EM2017/datos_P2_Gen_500.txt')
    statsFG500 = open("datosP2EM2017/datos_P2_Gen_500_stats.csv", 'w')
    statsFG500.write("numero de neuronas, error en entrenamiento, error en prueba, falsos positivos, falsos negativos\n")

    print "--------------------------------------------------------------------------------"
    for i in range(2, 11):
        print "\t calculando thetas para datos_P2_Gen_500 con " + str(i) + " neuronas..."
        neural = nn.NeuralNetwork(len(dataG500['x'][0]), i, 1)
        result = neural.gradientDescent(alpha, dataG500['x'], dataG500['y'])

        # Statistics
        errorE = 0
        errorAux = 0
        falseP = 0
        falseN = 0
        errorP = 0
        for j in range(0, n):
            hyp = neural.forwardPropagation(dataTest['x'][j])
            predicted = hyp[0]
            real = dataTest['y'][j]
            errorAux += abs(predicted - real )
            if (predicted > 0.5 and real < 0.01):
                falseP += 1
            elif (predicted < 0.5 and abs(real - 1) < 0.01):
                falseN += 1

        errorP = errorAux[0]/n
        statsFG500.write(str(i) + ", " + str(errorE) + ", " + str(errorP) + ", " + str(falseP) + ", " + str(falseN)+ "\n")

        # Simple plot: iterations vs cost function
        iterations = np.arange(0, result['nIterations'] + 1, 1)
        makeSimplePlot(iterations, result['costFunction'], "datos_P2_Gen_500", i, colors['blue'])

    print "--------------------------------------------------------------------------------"
    plt.show()


    data1000 = readData('datosP2EM2017/datos_P2_EM2017_N1000.txt')
    statsF1000 = open("datosP2EM2017/datos_P2_EM2017_N1000_stats.csv", 'w')
    statsF1000.write("numero de neuronas, error en entrenamiento, error en prueba, falsos positivos, falsos negativos\n")

    print "--------------------------------------------------------------------------------"
    for i in range(2, 11):
        print "\t calculando thetas para datos_P2_EM2017_N1000 con " + str(i) + " neuronas..."
        neural = nn.NeuralNetwork(len(data1000['x'][0]), i, 1)
        result = neural.gradientDescent(alpha, data1000['x'], data1000['y'])

        # Statistics
        errorE = 0
        errorAux = 0
        falseP = 0
        falseN = 0
        errorP = 0
        for j in range(0, n):
            hyp = neural.forwardPropagation(dataTest['x'][j])
            predicted = hyp[0]
            real = dataTest['y'][j]
            errorAux += abs(predicted - real )
            if (predicted > 0.5 and real < 0.01):
                falseP += 1
            elif (predicted < 0.5 and abs(real - 1) < 0.01):
                falseN += 1

        errorP = errorAux[0]/n
        statsF1000.write(str(i) + ", " + str(errorE) + ", " + str(errorP) + ", " + str(falseP) + ", " + str(falseN)+ "\n")

        # Simple plot: iterations vs cost function
        iterations = np.arange(0, result['nIterations'] + 1, 1)
        makeSimplePlot(iterations, result['costFunction'], "datos_P2_EM2017_N1000", i, colors['blue'])
    print "--------------------------------------------------------------------------------"
    plt.show()

    dataG1000 = readData('datosP2EM2017/datos_P2_Gen_1000.txt')
    statsFG1000 = open("datosP2EM2017/datos_P2_Gen_1000_stats.csv", 'w')
    statsFG1000.write("numero de neuronas, error en entrenamiento, error en prueba, falsos positivos, falsos negativos\n")

    print "--------------------------------------------------------------------------------"
    for i in range(2, 11):
        print "\t calculando thetas para datos_P2_Gen_1000 con " + str(i) + " neuronas..."
        neural = nn.NeuralNetwork(len(dataG1000['x'][0]), i, 1)
        result = neural.gradientDescent(alpha, dataG1000['x'], dataG1000['y'])

        # Statistics
        errorE = 0
        errorAux = 0
        falseP = 0
        falseN = 0
        errorP = 0
        for j in range(0, n):
            hyp = neural.forwardPropagation(dataTest['x'][j])
            predicted = hyp[0]
            real = dataTest['y'][j]
            errorAux += abs(predicted - real )
            if (predicted > 0.5 and real < 0.01):
                falseP += 1
            elif (predicted < 0.5 and abs(real - 1) < 0.01):
                falseN += 1

        errorP = errorAux[0]/n
        statsFG1000.write(str(i) + ", " + str(errorE) + ", " + str(errorP) + ", " + str(falseP) + ", " + str(falseN)+ "\n")

        # Simple plot: iterations vs cost function
        iterations = np.arange(0, result['nIterations'] + 1, 1)
        makeSimplePlot(iterations, result['costFunction'], "datos_P2_Gen_1000", i, colors['blue'])
    print "--------------------------------------------------------------------------------"
    plt.show()


    data2000 = readData('datosP2EM2017/datos_P2_EM2017_N2000.txt')
    statsF2000 = open("datosP2EM2017/datos_P2_EM2017_N2000.csv", 'w')
    statsF2000.write("numero de neuronas, error en entrenamiento, error en prueba, falsos positivos, falsos negativos\n")

    print "--------------------------------------------------------------------------------"
    for i in range(2, 11):
        print "\t calculando thetas para datos_P2_EM2017_N2000 con " + str(i) + " neuronas..."
        neural = nn.NeuralNetwork(len(data2000['x'][0]), i, 1)
        result = neural.gradientDescent(alpha, data2000['x'], data2000['y'])

        # Statistics
        errorE = 0
        errorAux = 0
        falseP = 0
        falseN = 0
        errorP = 0
        for j in range(0, n):
            hyp = neural.forwardPropagation(dataTest['x'][j])
            predicted = hyp[0]
            real = dataTest['y'][j]
            errorAux += abs(predicted - real )
            if (predicted > 0.5 and real < 0.01):
                falseP += 1
            elif (predicted < 0.5 and abs(real - 1) < 0.01):
                falseN += 1

        errorP = errorAux[0]/n
        statsF2000.write(str(i) + ", " + str(errorE) + ", " + str(errorP) + ", " + str(falseP) + ", " + str(falseN)+ "\n")

        # Simple plot: iterations vs cost function
        iterations = np.arange(0, result['nIterations'] + 1, 1)
        makeSimplePlot(iterations, result['costFunction'], "datos_P2_EM2017_N2000", i, colors['blue'])
    print "--------------------------------------------------------------------------------"
    plt.show()

    dataG2000 = readData('datosP2EM2017/datos_P2_Gen_2000.txt')
    statsFG2000 = open("datosP2EM2017/datos_P2_Gen_2000.csv", 'w')
    statsFG2000.write("numero de neuronas, error en entrenamiento, error en prueba, falsos positivos, falsos negativos\n")

    print "--------------------------------------------------------------------------------"
    for i in range(2, 11):
        print "\t calculando thetas para datos_P2_Gen_2000 con " + str(i) + " neuronas..."
        neural = nn.NeuralNetwork(len(dataG2000['x'][0]), i, 1)
        result = neural.gradientDescent(alpha, dataG2000['x'], dataG2000['y'])

        # Statistics
        errorE = 0
        errorAux = 0
        falseP = 0
        falseN = 0
        errorP = 0
        for j in range(0, n):
            hyp = neural.forwardPropagation(dataTest['x'][j])
            predicted = hyp[0]
            real = dataTest['y'][j]
            errorAux += abs(predicted - real )
            if (predicted > 0.5 and real < 0.01):
                falseP += 1
            elif (predicted < 0.5 and abs(real - 1) < 0.01):
                falseN += 1

        errorP = errorAux[0]/n
        statsFG2000.write(str(i) + ", " + str(errorE) + ", " + str(errorP) + ", " + str(falseP) + ", " + str(falseN)+ "\n")

        # Simple plot: iterations vs cost function
        iterations = np.arange(0, result['nIterations'] + 1, 1)
        makeSimplePlot(iterations, result['costFunction'], "datos_P2_Gen_2000", i, colors['blue'])
    print "--------------------------------------------------------------------------------"
    plt.show()
# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
