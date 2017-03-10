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

import k_means as km   # Neural Network library
import numpy as np     # This provides access to an efficient
                       # multi-dimensional container of generic data.
import pandas as pd    # This provides access to function for data manipulation
                       # and analysis.
# .----------------------------------------------------------------------------.

statsF = statsF = open("datasets/data_iris.txt_stats.csv", 'w')
statsF.write("# de clusters, Etiqueta del cluster, Aciertos, Fallos\n")

"""
    Description:
        Read the dataset and transform the data class.
    Params:
        @param dataSetName: file's name of the dataset to use.
"""
def readData(dataSetName):
    # Open the file.
    data = pd.read_csv(dataSetName, sep=",", header = None)

    # Get the min and max values for each column.
    minValues = []
    maxValues = []
    for i in range(0, len(data.columns)-1):
        mini = data[i].min()
        maxi = data[i].max()
        data[i] = (data[i] - mini) / (maxi - mini)

    df = data.values
    x = []
    y = []
    for index, row in data.iterrows():
        x.append(row.values.tolist()[:-1])
        y.append(row.values.tolist()[-1])

    x = np.asarray(x)
    y = np.array(y)

    return { 'x': x, 'y' : y}

"""
    Description:
        Caculates wich tag appears the must in a cluster
    Params:
        @param cluster_tags: all of the tags within a cluster
"""
def mode(cluster_tags):
    mode, indices = np.unique(cluster_tags, return_inverse=True)
    # print mode
    # print mode[np.argmax(np.bincount(indices))]
    return mode[np.argmax(np.bincount(indices))]

"""
    Description:
        Gets the confusion matrix for the data
    Params:
        @param data           : the original dataset
        @param clusters       : the cluster of the dataset
        @param clusters_index : the index of every example in the dataset
        @param K              : the numer of clusters
"""
def getConfusionMatrix(data, clusters, clusters_index, K):
    clusters_tags = []
    for k in range(0, K):
        clusters_tags.append([])
        for index in clusters_index[k]:
            clusters_tags[k].append(data['y'][index])
    # print clusters_tags

    # matrix = []
    error = 0
    print "\tnumero de clusters: " + str(K)
    for k in range(0, K):
        correct = 0
        incorrect = 0
        md = mode(clusters_tags[k])
        # print mode(clusters_tags[k])
        for tag in clusters_tags[k]:
            if tag == md:
                correct += 1
            else:
                incorrect += 1
        error += incorrect
        # matrix.append([correct, incorrect])
        print "\t\t" + "etiqueta del cluster " + str(k) + ": " + md
        print "\t\t" + str(correct) + " aciertos y " + str(incorrect) + " fallos"
        statsF.write(str(K) + ", " + md + ", " + str(correct) + ", " + str(incorrect) + "\n")

    error = float(error)/len(data['x'])
    print "\t\t" + "error total: " + str(error)
    statsF.write(str(K) + ", " + "error total, " + str(error) + "\n")

    # return matrix

def main():

    data = readData("datasets/data_iris.txt")
    for k in range(2, 6):
        print "--------------------------------------------------------------------------------"
        result = km.k_means(data['x'], k)
        getConfusionMatrix(data, result['clusters'], result['clusters_index'], k)
        print "--------------------------------------------------------------------------------"

    statsF.close()

# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
