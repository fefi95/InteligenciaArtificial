import matplotlib.pyplot as plt

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

def drawPoints(dataset):
    points = getPoints(dataset)

    # Draw the figure.
    fig = plt.figure()
    ax  = fig.add_subplot()

    #plot points inside circle
    p1 = plt.scatter(points['inCircleX'], points['inCircleY'], c='r', marker='.', label = "Points inside circle.")
    p2 = plt.scatter(points['outCircleX'], points['outCircleY'], c='c', marker='.', label = "Points outside circle.")
    #plt.axis((0,20,0,20))
    plt.legend(loc=2)

    plt.show()