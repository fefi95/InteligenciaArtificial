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
# colors = {'purple' : '#78037F',
#           'orange' : '#F55D3E',
#           'magenta': '#A4243B',
#           'gray'   : '#454545',
#           'blue'   : '#1781AA',
#           'green'  : '#23CE6B',
#           'yellow' : '#FFC857',
#           'black'  : '#101010',
#           'red'    : '#FF3030'
#          }
colors = ['#78037F',
          '#F55D3E',
          '#A4243B',
          '#454545',
          '#1781AA',
          '#23CE6B',
          '#FFC857',
          '#101010',
          '#FF3030'
          ]

alpha = 0.001

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
    plt.plot(iterations, costFunction, label='#neuronas= ' + str(label), c=color, linewidth=1.5)
    plt.xlabel("numero de iteraciones")
    plt.ylabel("Funcion de costo (J)")
    plt.title(dsName)
    plt.grid(True)
    plt.legend()
    plt.savefig(dsName + ".png")

"""
    Descripction: scatter plot of the cost function against number of iterations
    Parameters:
        @param circle : position of the theta to use.
        @param square : position of the theta to use.
        @param dsName : name of dataset
"""
def makeScatterPlot(circleX, circleY, squareX, squareY, dsName):

    plt.scatter(circleX, circleY, c=colors[0], edgecolor = colors[0])
    plt.scatter(squareX, squareY, c=colors[1], edgecolor = colors[1])
    plt.title(dsName)
    plt.legend()
    plt.savefig(dsName + "_scatter.png")
    plt.show()

def calculate(dataFileName, dataTest):
    n = 10000
    data = readData("datosP2EM2017/" + dataFileName +".txt")
    statsF = open("datosP2EM2017/" + dataFileName + "_stats.csv", 'w')
    statsF.write("numero de neuronas, error en entrenamiento, error en prueba, falsos positivos, falsos negativos\n")

    print "--------------------------------------------------------------------------------"
    for i in range(2, 11):
        print "\t calculando thetas para" + dataFileName + " con " + str(i) + " neuronas..."
        neural = nn.NeuralNetwork(len(data['x'][0]), i, 1)
        result = neural.gradientDescent(alpha, data['x'], data['y'])
        circleX = []
        circleY = []
        squareX = []
        squareY = []
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
            if predicted > 0.5:
                circleX.append(dataTest['x'][j][0])
                circleY.append(dataTest['x'][j][1])
            else:
                squareX.append(dataTest['x'][j][0])
                squareY.append(dataTest['x'][j][1])
            if (predicted > 0.5 and real < 0.01):
                falseP += 1
            elif (predicted < 0.5 and abs(real - 1) < 0.01):
                falseN += 1

        errorP = errorAux[0]/n
        statsF.write(str(i) + ", " + str(errorE) + ", " + str(errorP) + ", " + str(falseP) + ", " + str(falseN)+ "\n")

        # Simple plot: iterations vs cost function
        iterations = np.arange(0, result['nIterations'] + 1, 1)
        makeSimplePlot(iterations, result['costFunction'], dataFileName, i, colors[i-2])
        # makeScatterPlot(circleX, circleY, squareX, squareY, dataFileName)
    print "--------------------------------------------------------------------------------"
    plt.show()

def main():

    # print data500['x']
    # print data500['y']
    # neural = nn.NeuralNetwork(2, 2, 1)
    # h = neural.forwardPropagation(np.array([[0,0]]))
    # print h
    # b = neural.backPropagation(np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[1],[0], [0], [1]]))
    # print "ahhhhh"
    # print b
    # g = neural.gradientDescent(alpha, np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[1],[0], [0], [1]]))
    dataTest = readData('datosP2EM2017/dataset_test_circle.txt')
    calculate("datos_P2_EM2017_N500", dataTest)
    # calculate("datos_P2_Gen_500", dataTest)
    # calculate("datos_P2_EM2017_N1000", dataTest)
    # calculate("datos_P2_Gen_1000", dataTest)
    # calculate("datos_P2_EM2017_N2000", dataTest)
    # calculate("datos_P2_Gen_2000", dataTest)

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
