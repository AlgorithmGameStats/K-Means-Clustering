
import json, random, time
from kmeans.kmeans import KMeans

# Number of data points
no_points = 1000

# KMeans Object
k = KMeans(class_name="test", k=2, log=True)

# Generate Data
data = list()
for i in range(no_points):
  data.append([random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)])

# Inster data (this forces KMeans calculation)
start = time.clock()
k.put(data)
print ('KMeans calculation Time: {0}'.format( (time.clock() - start) ))

# Print the final centroids
print ('Final Centroids: {0}'.format(k.centroids))