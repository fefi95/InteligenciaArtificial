"""
    Universidad Simon Bolivar
    CI-5437
    Edward Fernandez 10-11121
    Stefani Castellanos 11-11394
    Carlos <insert last name> <insert ID>

    Description:
        This file contains the Gradient Descent implementation to solve an multiple
        linear regression.
"""

# .----------------------------------------------------------------------------.
# Import libraries to use.

import sys          # This provides access to some variables used or maintained
                    # by the interpreter.
import numpy as np  # This provides access to an efficient multi-dimensional
                    # container of generic data.

# .----------------------------------------------------------------------------.

def main():

    init = False    # This let you know if it store the dataset information.
    att  = []       # List of dataset attribute.
    varList = []    # Matrix of all the variables in our model.
    resultList = [] # Array with the data result.

    maxIter = 1000  # Number of maximal iterations for the function to converge.
    alpha = float(sys.argv[2]) # learning rate to use.

    dataSetFile = open(sys.argv[1], 'r'); # Get the dataset.

    for line in dataSetFile:
        wordList = line.split()

        # If the first word on the line isn't a '#', we have a data vector.
        if wordList[0][0] != '#':

            # The file with the dataset has the next rows: columns length, rows
            # length, the attributes name and the data.

            # Initialize the dataset information (rows length, columns length, names)
            # if it not store.
            if not(init):
                columms = int(wordList[0])                # We obtain the columns length.
                wordList = next(dataSetFile).split()  # We obtain the next line to obtain the rows length.
                rows = int(wordList[0])

                # Store the name of the dataset atributes.
                for i in range(columms):
                    line = next(dataSetFile)
                    att.append(line)
                thetas = [0] * (columms-1) # Se inicializan los thetas.

                init = True # We have all the data information and now we can store the data itself.
            else:
                wordList[0] = 1
                varList.append(wordList[:-1])
                resultList.append(wordList[-1])
        else:
            pass

    thetas = np.asarray(thetas, dtype=float)
    varList    = np.array(varList, dtype=float)
    resultList = np.array(resultList, dtype=float)
    conv = False  # Let you know if the function converge.

    # Calculate the initial cost.
    cos = cost(varList,resultList,thetas,rows)

    i = 0 # Initialize the counter of iterations.
    while (not(conv) and (i <= maxIter)):
        # Update of theta's
        auxtheta = [0] * (columms - 1)  # Store the new theta's value.

        for j in range(columms-1):
            auxtheta[j] = dcost(alpha, varList, resultList, thetas, rows, j)

        thetas = np.array(auxtheta, dtype=float) # Update the thetas value.
        newcost = cost(varList , resultList, thetas, rows)

        i = i + 1 # Update the actual number of iterations.
        if (abs(newcost - cos) <= 0.001):
            conv = True
    print(conv) # Let you know if the function converge.

"""
    Descripction: Calcule the cost function.
    Parameters:
        @param varList   : all variables in the model.
        @param resultList: store the result of the data.
        @param thetas    : array with the parameters to use.
        @param m         : number of rows.
"""
def cost(varList, resultList, theta, m):
    cost = 0
    for i in range(m):
        aux = np.dot(varList[i], theta)- resultList[i]
        cost = cost + (aux * aux)
    return(cost / (2*m))

"""
    Descripction: calculate the derived cost function.
    Parameters:
        @param alpha: this is the learning rate to use.
        @param varList   : all variables in the model.
        @param resultList: store the result of the data.
        @param theta     : array with the parameters to use.
        @param m         : number of rows.
        @param j         : position of the theta to use.
"""
def dcost(alpha, varList, resultList, thetas, m, j):
    dcost = 0
    for i in range(m):
        aux = (np.dot(varList[i], thetas)-resultList[i]) * varList[i][j]
        dcost = dcost + aux
    return(thetas[j] - alpha * dcost / (2*m))

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
            main()

# .----------------------------------------------------------------------------.
