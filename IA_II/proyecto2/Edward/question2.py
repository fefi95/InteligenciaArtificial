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

maxIter = 25000

def draw_dataset(dataset):

    inCircleX, inCircleY, outCircleX, outCircleY = split(dataset)

    #draw figure
    fig = plt.figure()
    ax = fig.add_subplot()

    #plot points inside circle
    p1 = plt.scatter(inCircleX, inCircleY, c='r', marker='.', label = "Points inside circle.")
    p2 = plt.scatter(outCircleX, outCircleY, c='c', marker='.', label = "Points outside circle.")
    plt.legend(loc=2)

    plt.show()

def readData(dataSetName):
    varList     = [] # initialize matrix of features
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
    	normalRow = []

    	for i in range(0, len(row)-1):
    		normalize = (row[i] - minValues[i]) / (maxValues[i] - minValues[i])
    		normalRow.append(normalize) 
    	varList.append(normalRow)
    return varList

def main():

    alpha = 0.01

    data500 = readData('datosP2EM2017/datos_P2_EM2017_N500.txt')
    # statsF500 = open("datos_P2_EM2017_N500_stats", 'w')
    # statsF500.write("error en entrenamiento, error en prueba, falsos positivos, falsos negativos")
    
    print "--------------------------------------------------------------------------------"
    for i in range(2, 3):
        print "\t Calculando thetas para datos_P2_EM2017_N500 con " + str(i) + " neuronas..."
        print "\n Creo la red. \n"
        neuralNet = nn.NeuralNetwork(len(data500[0]) - 1, i, 2)
        print "\n Entreno la red. \n"
       	#print data500['x']
       	nn.trainNetwork(neuralNet, data500, alpha, maxIter, 2)

       	for row in data500:
 			print nn.predictNetwork(neuralNet, row)
        #print "\n Muestro la red. \n"
        #for layer in neuralNet:
        #	print layer
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
