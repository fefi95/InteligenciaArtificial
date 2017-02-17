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

# Tiene 2 parametros de entreda el archivo y el alpha(gradiante creo)
def main():

    init = False
    #list of attributes
    att = []
    #matrix of all the variables in our model
    x = []
    #array of the result of the data
    y = []

    with open(sys.argv[1], 'r') as f:
        for line in f:
            word = line.split()
            if word[0][0] != '#':
                #initialize the rows and columms
                if not(init):
                    columms = int(word[0])
                    word = next(f).split()
                    rows = int(word[0])
                    for i in range(columms):
                        line = next(f)
                        att.append(line)
                    theta = [0] * (columms-1)
                    init = True
                else:
                    #initialize x and y
                    word[0] = 1
                    x.append(word[:-1])
                    y.append(word[-1])
            else:
                pass
        theta = np.asarray(theta,dtype=float)
        x = np.array(x,dtype=float)
        y = np.array(y,dtype=float)
        conv = False
        #function cost (J)
        cos = cost(x,y,theta,rows)
        i = 0
        while (not(conv) and (i <= 1000)):
            #update of theta's
            auxtheta = [0] * (columms - 1)
            for j in range(columms-1):
                auxtheta[j] = dcost(float(sys.argv[2]),x,y,theta,rows,j)
            theta = np.array(auxtheta,dtype=float)
            newcost = cost(x,y,theta,rows)
            i = i+1
            if (abs(newcost - cos) <= 0.001):
                conv = True
        print(conv)

def cost(x,y,theta,m):
    cost = 0
    for i in range(m):
        aux = np.dot(x[i],theta)-y[i]
        cost = cost + (aux * aux)
    return(cost/(2*m))

def dcost(alpha,x,y,theta,m,j):
    dcost = 0
    for i in range(m):
        aux = (np.dot(x[i],theta)-y[i]) * x[i][j]
        dcost = dcost + aux
    return(theta[j] - alpha * dcost / (2*m))

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
            main()

# .----------------------------------------------------------------------------.
