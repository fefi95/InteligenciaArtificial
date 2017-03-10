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


numericClass = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}

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
    # minValues = []
    # maxValues = []
    # for i in range(0, len(data.columns)-1):
    #     mini = data[i].min()
    #     maxi = data[i].max()
    #     data[i] = (data[i] - mini) / (maxi - mini)

    df = data.values
    x = []
    y = []
    for index, row in data.iterrows():
        x.append(row.values.tolist()[:-1])
        y.append(row.values.tolist()[-1])

    x = np.asarray(x)
    y = np.array(y)

    return { 'x': x, 'y' : y}

def find(data, example):
    for i in range(0, len(data)):
        print "find"
        print data[i]
        print example
        # if np.all(abs(data[i] - example) < 0.1):
        # found = True
        for j in range(0, len(data[0])):
            if (abs(data[i][j] - example[j]) > 0.1):
                found = False
        if found:
            return i
    return len(data) + 1

def mode(cluster_tags):
    mode, indices = np.unique(cluster_tags, return_inverse=True)
    # print mode
    # print mode[np.argmax(np.bincount(indices))]
    return mode[np.argmax(np.bincount(indices))]

def getConfusionMatrix(data, clusters, clusters_index, K):
    clusters_tags = []
    for k in range(0, K):
        clusters_tags.append([])
        for index in clusters_index[k]:
            clusters_tags[k].append(data['y'][index])
    print clusters_tags

    matrix = []
    for k in range(0, K):
        correct = 0
        incorrect = 0
        md = mode(clusters_tags[k])
        print mode(clusters_tags[k])
        for tag in clusters_tags[k]:
            if tag == md:
                correct += 1
            else:
                incorrect += 1
        matrix.append([correct, incorrect])

    print matrix
    return matrix




    # Tag each cluster
    # clusters_tags = []
    # for k in range(0, K):
    #     cluster = clusters[k]
    #     clusters_tags.append([])
    #     for example in cluster:
    #         index = find(data['x'], example)
    #         print index
    #         tag = data['y'][index]
    #         clusters_tags[k].append(tag)
    # print clusters_tags


def main():

    data = readData("datasets/data_iris.txt")
    for k in range(3, 4):
        print "--------------------------------------------------------------------------------"
        result = km.k_means(data['x'], k)
        print "sol"
        print result['clusters']
        print result['clusters_index']
        getConfusionMatrix(data, result['clusters'], result['clusters_index'], k)
        # para comparar que los resultados cuadren iba a asignar a cada cluster la
        # etiqueta del centroide, luego buscar en la data original cada punto y ver
        # su etiqueta en el vector "y" luego chequear si lo clasifico correctamente
        # pero eso implica varias busquedas y es medio ineficiente.
        # Si se les ocurre una mejor manera...
        print "--------------------------------------------------------------------------------"


# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
