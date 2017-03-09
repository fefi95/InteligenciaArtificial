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

def main():

    data = readData("datasets/data_iris.txt")
    for k in range(2, 3):
        print "--------------------------------------------------------------------------------"
        result = km.k_means(data['x'], k)
        print result['clusters']
        print "--------------------------------------------------------------------------------"


# .----------------------------------------------------------------------------.

if __name__ == '__main__':
    main()

# .----------------------------------------------------------------------------.
