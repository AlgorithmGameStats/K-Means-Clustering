"""
Class implementing KMeans for our Game Server
"""
import os, itertools, random, time
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


	def __init__(self, class_name, k=1, max_iterations=300, log=False):
		
		# Store k-means variables and constants
		self.__class_name = class_name
		self.__k = k
		self.__max_iterations = max_iterations
		self.__log_enabled = log

		# predefine random centroids
		start = time.clock()
		self.centroids = self.__random_centroid(k)
		self.__log ( 'Initial random centroids generation Time: {0}'.format( (time.clock() - start) ) )

		# predefine empty clusters
		self.clusters = [ [] for i in range(k) ]

		# predefine empty labels
		self.labels = [ '' for i in range(k) ]

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
		start = time.clock()
		self.clusters[self.__k-1] += items
		self.__log ( 'Adding new data Time: {0}'.format( (time.clock() - start) ) )
		
		# Create list of old/new centroids and clusters before re-calculation
		start = time.clock()
		old_centroids = [ [] for i in range(self.__k) ]
		new_centroids = self.__random_centroid(self.__k)
		new_clusters = [ [] for i in range(self.__k) ]
		self.__log ( 'New temp centroids and clusters generation Time: {0}'.format( (time.clock() - start) ) )
		
		# Keep track of iterations of moving centroids
		iterations = 0
		calc_times = list()

		# Continue converging data points until __max_iterations is reached
		self.__log ("*********************************")
		while not (self.__should_stop(old_centroids, new_centroids, iterations)):
			iterations += 1 # increase iterations count
			self.__log("Iteration: {0}".format(iterations))
			start = time.clock()
			new_clusters = [ [] for i in range(self.__k) ] # Empty the 'new_clusters' for this iteration
			old_centroids = new_centroids[:]	# Copies new_centroids into old_centroids
			self.__log ( 'Copy new centroids to old centroids Time: {0}'.format( (time.clock() - start) ) )

			# chain together all clusters (old ones) instead of copying, 
			# this way we don't waste soo much memory
			start = time.clock()
			data_set = itertools.chain( *(self.clusters[i] for i in range(self.__k)) )
			self.__log ( 'Chaining data set Time: {0}'.format( (time.clock() - start) ) )
			
			# For each item in the data_set, we: 
			# 1) find the closest centroid to the data item
			# 2) add data item to the cluster it belongs to
			# 3) recalculate the centroid for that cluster
			start = time.clock()
			c_time = 0
			r_time = 0
			for item in data_set:
				temp = time.clock()
				centroid_index = self.__closest_centroid(item, new_centroids)
				c_time += (time.clock() - temp) 
				new_clusters[centroid_index].append(item)

			# Recalculate all centroids
			for centroid_index in range(self.__k):
				temp = time.clock()
				new_centroids[centroid_index] = self.__recalculate(new_clusters[centroid_index])
				r_time += (time.clock() - temp) 

			calc_time = (time.clock() - start)
			calc_times.append(calc_time)
			self.__log ( 'Closest centroid Time: {0}'.format( c_time ) )
			self.__log ( 'Recalculating centroids Time: {0}'.format( r_time ) )
			self.__log ( 'New centroids calculation Time: {0}'.format( calc_time ) )
			self.__log ( '~~~~ centroids ~~~~')
			self.__log ('Old: {0}'.format(old_centroids))
			self.__log ('New: {0}'.format(new_centroids))
			self.__log ( '~~~~~~~~~~~~~~~~~~~')
			self.__log ("+++++++++++++++++++++++++++++++++")
		
		# Once we have converged (or reached max_iterations)
		# Re-assign centroids and clusters to the new values
		self.centroids = new_centroids
	 	self.clusters = new_clusters
	 	self.__log ( 'Total calculation Time: {0}'.format( sum(calc_times) ) )
	 	self.__log ("*********************************")

	def __random_centroid(self, k):
		"""
		Generate a list of 'k' random centroids
		"""
		return [[random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)] for i in range(k)]


	def __recalculate(self, cluster):
		"""
		Recalculate centroid as the new mean of the cluster
		"""
		return map(
			lambda x:sum(x)/float(len(x)), zip(*cluster)
			)


	def __closest_centroid(self, item, centroids):
		"""
		Return the index of the centroid the 'item' is closer to
		"""
		return min([(i[0], sqrt(
			((item[0] - centroids[i[0]][0])**2) + 
			((item[1] - centroids[i[0]][1])**2) + 
			((item[2] - centroids[i[0]][2])**2)
		)) for i in enumerate(centroids)], key=lambda t:t[1])[0]

	def __should_stop(self, old_centroids, centroids, iterations):
		"""
		Verify if we should stop recalculating centroids
		"""
		if iterations > self.__max_iterations:
			return True
		return old_centroids == centroids

	def dot_product(self, item):
		return [ sum([item[i] * self.centroids[j][i] for i in range(len(item))]) for j in range(len(self.centroids))]

	def k(self):
		"""
		Return the value of 'k'
		"""
		return self.__k

	def class_name(self):
		"""
		Return the value of class_name
		"""
		return self.__class_name

	# Logging Helper function
	def __log(self, txt):
		if self.__log_enabled:
			print(txt)
