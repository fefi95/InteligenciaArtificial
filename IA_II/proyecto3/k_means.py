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

"""
    Description:
        Makes k new clusters given the data
    Params:
        @param X         : all examples of the problem
        @param centroids : k centroids of the clusters
"""

def makeCluster(X, centroids, K):
    clusters = []
    for k in range(0, K):
        clusters.append([])
        clusters[k].append(centroids[k])

    for x in X:
        best_cluster = 0
        old_distance = np.linalg.norm(x - centroids[0])
        # get best centroid
        for k in range(1, K):
            distance = np.linalg.norm(x - centroids[k])
            if (old_distance > distance):
                best_cluster = k

        # print "best"
        # print best_cluster
        # print clusters[best_cluster]
        # print x
        clusters[best_cluster].append(x)
        # break
        # Insert new value to the closest centroid for x
    # print "cluster"
    # print clusters
    clusters = np.asarray(clusters)
    return clusters

"""
    Description:
        Calculates the new centroids of a k given cluster
    Params:
        @param clusters : K clusters
"""

def getNewCentroid(clusters):
    newCentroids = []
    # print clusters
    # print clusters.shape
    for cluster in clusters:
        newCentroids.append(np.mean(cluster, axis = 0))
        print 'mean'
        print np.mean(cluster, axis = 0)
    print "new c"
    print newCentroids
    return newCentroids

def converge(old_centroids, centroids):
    converge = True
    for i in range(0, len(centroids)):
        if np.any(old_centroids[i] != centroids[i]):
            converge = False
            break
    print converge
    return converge

def k_means(X, k):
    # Initialize centroids
    centroids = rm.sample(X, k)
    # print centroids
    old_centroids = rm.sample(X, k)

    while not converge(old_centroids, centroids):
        print "old"
        print old_centroids
        print "new"
        print centroids
        old_centroids = centroids
        clusters = makeCluster(X, centroids, k)
        # print clusters
        centroids = getNewCentroid(clusters)
        print "old"
        print old_centroids
        print "new"
        print centroids
        # print len(centroids)
        # break
    return {'centroids' : centroids, 'clusters' : clusters}
