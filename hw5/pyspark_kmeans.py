import sys
from pyspark import SparkConf, SparkContext
import numpy as np

conf = SparkConf()
sc = SparkContext(conf=conf)


def pyspark_kmeans(file1, file2):
    """
    The kmeans algorithm, split data into k clusters
    :param file1: Data file
    :param file2: Centroids file
    :return: A txt file including the centroids of each cluster
    """

    # load data
    data = sc.textFile(file1).map(lambda l: l.split(" ")).map(lambda l: np.array([float(x) for x in l]))
    centroids = sc.textFile(file2).map(lambda l: l.split(" "))
    centroids = np.array(centroids.map(lambda l: np.array([float(x) for x in l])).collect())

    max_itr = 100
    itr = 0
    converged = False
    while (itr < max_itr) & (converged is False):
        itr = itr + 1
        # assign each point a custer id, return cluster id as the key
        # and (data point, 1) as value to count number of points in the cluster in the next step
        assigned = data.map(lambda x: (np.argmin([np.linalg.norm(x - c) for c in centroids]), (x, 1)))
        # save a temp centroid
        prev_centroids = centroids
        # group by key, add all data points and counts, divide each other to get mean value
        centroids = np.array(assigned.reduceByKey(lambda x, n: (x[0] + n[0], x[1] + n[1])).sortByKey()
                             .map(lambda c: c[1][0] / c[1][1]).collect())
        if np.array_equal(prev_centroids, centroids):  # when already converged
            converged = True

    return centroids


if __name__ == "__main__":

    seeds = pyspark_kmeans("data.txt", 'c1.txt')
    np.savetxt("answer.txt", seeds)
    sc.stop()
