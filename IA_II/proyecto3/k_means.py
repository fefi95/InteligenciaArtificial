"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Description:
        This file contains the implementation of k-means algorithm
"""
# .----------------------------------------------------------------------------.
# Import libraries to use.

import numpy as np              # This provides access to an efficient
                                # multi-dimensional container of generic data.
import random as rm
# .----------------------------------------------------------------------------.

np.random.seed(1)

"""
    Description:
        Makes k new clusters given the data
    Params:
        @param X         : all examples of the problem
        @param centroids : k centroids of the clusters
        @param K         : number of clusters
"""
def makeCluster(X, centroids, K):
    # Store every created cluster
    clusters = []
    # Store the index of every example on the cluster
    clusters_index = []
    clusters_tags = []

    for k in range(0, K):
        clusters.append([])
        clusters_index.append([])

    for i in range(0, len(X)):
        best_cluster = 0
        old_distance = np.linalg.norm(X[i] - centroids[0])
        # get best cluster for the example
        for k in range(1, K):
            distance = np.linalg.norm(X[i] - centroids[k])
            if (old_distance > distance):
                best_cluster = k
                old_distance = distance

        clusters[best_cluster].append(X[i])
        clusters_tags.append(centroids[best_cluster])
        clusters_index[best_cluster].append(i)
    clusters = np.asarray(clusters)
    return [clusters, clusters_index, clusters_tags]

"""
    Description:
        Calculates the new centroids of a k given cluster
    Params:
        @param clusters : K clusters
        @param centroids : K centroids
"""

def getNewCentroid(clusters, centroids):
    newCentroids = []
    # print clusters
    # print clusters.shape
    for i in range(len(clusters)):
        if len(clusters[i]) == 0:
            newCentroids.append(centroids[i])
        else:
            newCentroids.append(np.mean(clusters[i], axis = 0))
    return newCentroids

"""
    Description:
        Test whether the algorithm has converge
    Params:
        @param old_centroids : K old centroids
        @param centroids     : K new centroids
"""
def converge(old_centroids, centroids):
    converge = True
    for i in range(0, len(centroids)):
        if np.any(old_centroids[i] != centroids[i]):
            converge = False
            break
    # print converge
    return converge

"""
    Description:
        Calculates the new centroids of a k given cluster
    Params:
        @param X : orginal examples
        @param K : number of clusters
"""
def k_means(X,k):
    # Initialize centroids
    centroids = rm.sample(X, k)
    # print centroids
    old_centroids = rm.sample(X, k)

    i = 1
    while (not converge(old_centroids, centroids)) and (i < 21):
        old_centroids = centroids
        aux = makeCluster(X, centroids, k)
        clusters = aux[0]
        clusters_index = aux[1]
        clusters_tags = aux[2]
        # print clusters
        centroids = getNewCentroid(clusters,centroids)
        # print i
        i += 1
    return {'centroids' : centroids, 'clusters' : clusters, 'clusters_index' : clusters_index, 'clusters_tags' : clusters_tags}
