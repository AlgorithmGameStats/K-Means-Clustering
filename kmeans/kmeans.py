import os

import itertools

from math import sqrt
import random

# 1) randomnly assign 3 centroids
# 2) add data and determine distance from each data point to closest centroid
# 3) shift new centroids by averaging data points of each cluster 
# 4) convergence stops when centroids approach fixed values (i.e. centroid-data distance minimizes) 

# player 1: Speed Runners(time=0, level=all levels, coins=0, murders=0); player 2: Achievers (coins=~, levels, time=~, murders=0); player 3: Killers (murders=~, levels, time=~, coins=0)

# k= # of clusters (3 : one for each player profile)
# c= # of initial clusters 


class KMeans(object):
	"""
	Defines the Kmeans class for our game server
	Each point is: [time, coins, murders]
	"""

	def __init__(self, class_name, k=1):
		self.labels=['speed', 'achiever', 'killer']
		# predefine centroid extremes
		self.centroids= self.__randomcentroid(k)
		self.clusters = [[] for i in range(k)]

		self.class_name=class_name
		self.k=k 
		# Constants
		self.MAX_ITERATIONS=300

	def put(self, items):
		"""
		Put a new entry in the dataSet,
		Recalculate KMeans

		Parameters
   		----------
    	items : array_ofarrays
    		[items]
    		item=[time, coins, murders]
		"""
		# Add item to a cluster before we begin
		self.clusters[self.k-1].extend(items)


		oldCentroids=[[] for i in range(self.k)]
		newCentroids = self.__randomcentroid(self.k)
		newClusters=[[] for i in range(self.k)]
		iterations=0
		
		#continue converging dataset points until max iteration
		while not (self.__shouldStop(oldCentroids, newCentroids, iterations)):
			iterations+=1 
			newClusters=[[] for i in range(self.k)]
			oldCentroids=newCentroids[:]	#copies old centroids into new centroids
			dataSet=itertools.chain(*(self.clusters[i] for i in range(self.k)))
 
			
			for item in dataSet:

				centroid_index= self.__closestcentroid(item, newCentroids) 
				newClusters[centroid_index].append(item)
				newCentroids[centroid_index]=self.__recalculate(newClusters[centroid_index])


		self.centroids=newCentroids
	 	self.clusters=newClusters

	#recalculate centroids as the new mean of each cluster dataset


	def __randomcentroid(self, k):
		return [[random.uniform(0, 200), random.uniform(0, 1), random.uniform(0, 25)] for i in range(k)]


	def __recalculate(self, cluster):

		return map(lambda x:sum(x)/float(len(x)), zip(*cluster))


	def __closestcentroid(self, item, centroids):



		return min([(i[0], sqrt(((item[0] - centroids[i[0]][0])**2) + ((item[1] - centroids[i[0]][1])**2)) + ((item[2] - centroids[i[0]][2])**2)) for i in enumerate(centroids)], key=lambda t:t[1])[0]

	def __shouldStop(self, oldCentroids, centroids, iterations):
		if iterations> self.MAX_ITERATIONS:
			return True
		return oldCentroids==centroids


	

		return profile
