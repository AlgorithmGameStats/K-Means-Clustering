import os

import itertools

from math import sqrt

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

	def __init__(self, level):
		self.labels=['speed', 'achiever', 'killer']
		# predefine centroid extremes
		self.centroids= [[0.0, 0.0, 0.0], [1000.0, 1000.0, 0.0], [1000.0, 0.0, 1000.0]]
		self.clusters = [[], [], []]
		self.current_level=level 

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
		self.clusters[2].extend(items)


		oldCentroids=[[], [], []]
		newCentroids = [[0.0, 0.0, 0.0], [1000.0, 1000.0, 0.0], [1000.0, 0.0, 1000.0]]
		newClusters=[[], [], []]
		iterations=0
		
		#continue converging dataset points until max iteration
		while not (self.__shouldStop(oldCentroids, newCentroids, iterations)):
			iterations+=1 
			newClusters=[[], [], []]
			oldCentroids=newCentroids[:]	#copies old centroids into new centroids
			dataSet=itertools.chain(self.clusters[0], self.clusters[1], self.clusters[2])
			for item in dataSet:

				centroid_index= self.__closestcentroid(item, newCentroids) 
				newClusters[centroid_index].append(item)
				newCentroids[centroid_index]=self.__recalculate(newClusters[centroid_index])


		self.centroids=newCentroids
	 	self.clusters=newClusters

	 	return label
	#recalculate centroids as the new mean of each cluster dataset

	def __recalculate(self, cluster):

		return map(lambda x:sum(x)/float(len(x)), zip(*cluster))


	def __closestcentroid(self, item, centroids):


		return min([(i[0], sqrt(((item[0] - centroids[i[0]][0])**2) + ((item[1] - centroids[i[0]][1])**2)) + ((item[2] - centroids[i[0]][2])**2))) for i in enumerate(centroids)], key=lambda t:t[1])[0]

	def __shouldStop(self, oldCentroids, centroids, iterations):
		if iterations> self.MAX_ITERATIONS:
			return True
		return oldCentroids==centroids


	def __getLabel(self, index):
		return self.labels[index] 


	def getlabel(self,item):

		index=self.__closestcentroid(item, self.centroids)
		profile= self.__getlabel(index) 

		return profile
