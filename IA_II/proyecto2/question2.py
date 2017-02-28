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
# .----------------------------------------------------------------------------.


def readData(dataSetName):
    dataSetFile = open(dataSetName, 'r'); # Get the dataset.
    varList = [] #initialize matrix of features
    resultList = [] # initialize matrix of results

    for line in dataSetFile:
        wordList = line.split()
        varList.append(wordList[:-1])
        resultList.append(wordList[-1])

    varList    = np.array(varList, dtype=np.float128)
    resultList = np.array(resultList, dtype=np.float128)

    return {'x' : varList, 'y': resultList}

def main():
    data = readData('datosP2EM2017/datos_P2_EM2017_N500.txt')
    print data['x']
    print data['y']

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
