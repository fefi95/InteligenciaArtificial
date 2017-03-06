import matplotlib.pyplot as plt

"""
    Descripction: clasifies the data set into points thet are in the circle
                and the ones that are on the square
    Parameters:
        @param dataset : data set
"""

def getPoints(dataset):
    inCircleX  = []
    inCircleY  = []
    outCircleX = []
    outCircleY = []

    for row in dataset:
        if row[-1] == 1:
            inCircleX.append(row[0])
            inCircleY.append(row[1])
        else:
            outCircleX.append(row[0])
            outCircleY.append(row[1])

    return {'inCircleX': inCircleX, 'inCircleY': inCircleY, 'outCircleX': outCircleX, 'outCircleY': outCircleY}

"""
    Descripction: draws a scatter plot for the circle and square data
    Parameters:
        @param dataset : data set
        @param dsName  : name of the data set
        @param nNeuron : number of neurons
"""

def drawPoints(dataset, dsName, nNeuron):
    points = getPoints(dataset)

    # Draw the figure.
    fig = plt.figure()
    ax  = fig.add_subplot()

    #plot points inside circle
    p1 = plt.scatter(points['inCircleX'], points['inCircleY'], c='r', marker='.', label = "Points inside circle.")
    p2 = plt.scatter(points['outCircleX'], points['outCircleY'], c='c', marker='.', label = "Points outside circle.")
    #plt.axis((0,20,0,20))
    plt.title(dsName + " con " + str(nNeuron) + " neuronas")
    plt.legend(loc=2)
    plt.savefig(dsName + "_" + str(nNeuron) +"_neuronas.png")
    plt.show()

"""
    Descripction: plot of the error against number of iterations
    Parameters:
        @param iterations   : position of the theta to use.
        @param error        : array that contains the values of every error
        @param dsName       : name of dataset
        @param label        : label of the legend plot
        @param color        : color of the line on the plot
"""
def makeSimplePlot(iterations, error, dsName, label, color):
    plt.plot(iterations, error, label='#neuronas= ' + str(label), c=color, linewidth=1.5)
    plt.xlabel("numero de iteraciones")
    plt.ylabel("error")
    plt.title(dsName)
    plt.grid(True)
    plt.legend()
    plt.savefig(dsName + ".png")
