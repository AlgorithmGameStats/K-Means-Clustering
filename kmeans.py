import os
import numpy as np

import matplotlib.pyplot as plt 
# 1) randomnly assign 3 centroids
# 2) add data and determine distance from each data point to closest centroid
# 3) shift new centroids by averaging data points of each cluster 
# 4) convergence stops when centroids approach fixed values (i.e. centroid-data distance minimizes) 

# player 1: Speed Runners(time, level, coins=0, murders=0); player 2: Achievers (coins, levels); player 3: Killers (murders, levels)

# k= # of clusters (3 : one for each player profile)
# c= # of initial clusters 


def kmeans(dataSet, k):

	centroids= []
	centroids=getRandomCentroids(dataSet, centroids, k)
	oldCentroids = [[] for i in range(k)]
	iterations=0
	oldCentroids=None
	counter=0 


# predefine centroid extremes


	#continue converging dataset points until max iteration
	while not (shouldStop(oldCentroids, centroids, iterations)):
		iterations+=1 
		clusters = [[] for i in range(k)]

		#assign datapoint to cluster type
		clusters= distance(dataSet,centroids,clusters)
		
		#recalculate centroids as the new mean of each cluster dataset
		index=0
		
		#axis=0 flatten array
		#redefine means
		for cluster in clusters:
			oldCentroids[index]=centroids[index]
			centroids[index]= map(lambda x:sum(x)/float(len(x)), zip(*dataSet)) 
			index+=1

		labels=getLabels(centroids)
		

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

def distance(dataSet, centroids, clusters):
	for data in dataSet:
		mu_index=array[]
		for i in centroids:
			mu_index.append(sqrt((data-i)**2)) 

		mu_index= min(mu_index)
		
		clusters[mu_index].append(data)
		
	return clusters 
	
	#need to get index


def getLabels(centroids): 

	for i in centroids:






