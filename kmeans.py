import os
import numpy as np

import matplotlib.pyplot as plt 
# 1) randomnly assign 3 centroids
# 2) add data and determine distance from each data point to closest centroid
# 3) shift new centroids by averaging data points of each cluster 
# 4) convergence stops when centroids approach fixed values (i.e. centroid-data distance minimizes) 

# player 1: Speed Runners; player 2: Achievers; player 3: Killers

# k= # of clusters (3 : one for each player profile)
# c= # of initial clusters 


def kmeans(dataSet, k, c):

	centroids= []
	centroids=getRandomCentroids(dataSet, centroids, k)
	oldCentroids = [[] for i in range(k)]
	iterations=0
	oldCentroids=None
	counter=0 

	#continue converging dataset points until max iteration
	while not (shouldStop(oldCentroids, centroids, iterations)):
		iterations+=1 
		clusters = [[] for i in range(k)]

		#assign datapoint to cluster type
		clusters= distance(dataSet,centroids,clusters)
		
		#recalculate centroids as the new mean of each cluster dataset
		index=0
		for cluster in clusters:
			oldCentroids[index]=centroids[index]
			centroids[index]= np.mean(cluster, axis=0).tolist()
			index+=1

		labels=getLabels(dataSet,centroids)
		

	return centroids
MAX_ITERATIONS=300 
def shouldStop(oldCentroids, centroids, iterations):
	if iterations> MAX_ITERATIONS:
		return True
		return oldCentroids=centroids
		iterations++ 

def getRandomCentroids(dataSet, centroids, k):
	for cluster in range(0,k):
	centroids.append(data[np.random.randint(0, len(data), size=1].flatten(). tolist())
	return centroids 

def distance(data,centroids,clusters):
	for d in data:
	#find closest centroid to datapoint
	mu_index= min([i[0], np.linalg.norm(d-centroids[i[0]])) \ for i in enumerate(centroids)], key=lambda t:t[1])[0]
	
	try:
		clusters[mu_index].append(instance)
		
	except KeyError:
	
		clusters[mu_index]= [d]
		
	return clusters 
	
def getLabels(dataSet, centroids):




