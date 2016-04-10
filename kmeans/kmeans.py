import os, itertools, random
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
	'time' == time take to beat stage
	'coins' == percentage of coins collected in stage
	'murders' == number of cubes killed on the stage
	"""


	def __init__(self, class_name, k=1, max_iterations=300):
		
		# predefine random centroids
		self.centroids = self.__random_centroid(k)
		
		# predefine empty clusters
		self.clusters = [ [] for i in range(k) ]
		
		# Store k-means variables and constants
		self.__class_name = class_name
		self.__k = k
		self.__max_iterations = max_iterations


	def put(self, items):
		"""
		Put new entries in the dataSet,
		Recalculate KMeans

		Parameters
   		----------
    	items : array_ofarrays
    		[item, item, item, ....]
    		item == [time, coins, murders]
		"""

		# Add item to the last cluster before we begin
		self.clusters[self.__k-1].extend(items)

		# Create list of old/new centroids and clusters before re-calculation
		old_centroids = [ [] for i in range(self.__k) ]
		new_centroids = self.__random_centroid(self.__k)
		new_clusters = [ [] for i in range(self.__k) ]

		# Keep track of iterations of moving centroids
		iterations = 0
		
		# Continue converging data points until __max_iterations is reached
		while not (self.__should_stop(old_centroids, new_centroids, iterations)):
			iterations += 1 # increase iterations count
			new_clusters = [ [] for i in range(self.__k) ] # Empty the 'new_clusters' for this iteration
			old_centroids = new_centroids[:]	# Copies new_centroids into old_centroids

			# chain together all clusters (old ones) instead of copying, 
			# this way we don't waste soo much memory
			data_set = itertools.chain( *(self.clusters[i] for i in range(self.__k)) )
			
			# For each item in the data_set, we: 
			# 1) find the closest centroid to the data item
			# 2) add data item to the cluster it belongs to
			# 3) recalculate the centroid for that cluster
			for item in data_set:
				centroid_index = self.__closest_centroid(item, new_centroids) 
				new_clusters[centroid_index].append(item)
				new_centroids[centroid_index] = self.__recalculate(new_clusters[centroid_index])
		
		# Once we have converged (or reached max_iterations)
		# Re-assign centroids and clusters to the new values
		self.centroids = new_centroids
	 	self.clusters = new_clusters


	def __random_centroid(self, k):
		"""
		Generate a list of 'k' random centroids
		"""
		return [[random.uniform(0, 200), random.uniform(0, 1), random.uniform(0, 25)] for i in range(k)]


	def __recalculate(self, cluster):
		"""
		Recalculate centroid as the new mean of the cluster
		"""
		return map(lambda x:sum(x)/float(len(x)), zip(*cluster))


	def __closest_centroid(self, item, centroids):
		"""
		Return the index of the centroid the 'item' is closer to
		"""
		return min([(i[0], sqrt(((item[0] - centroids[i[0]][0])**2) + ((item[1] - centroids[i[0]][1])**2)) + ((item[2] - centroids[i[0]][2])**2)) for i in enumerate(centroids)], key=lambda t:t[1])[0]

	def __should_stop(self, old_centroids, centroids, iterations):
		"""
		Verify if we should stop recalculating centroids
		"""
		if iterations > self.__max_iterations:
			return True
		return old_centroids == centroids
		return profile


		#calculate dot product of each item to each centroid 
		#calculate the dot product per centroid 

	def dot_product(self, item):

		for j in range(len(self.centroids)):
			print sum( [ item[i]* self.centroids[j][0] for i in range (len(item))]) 

