
"""
Python script used to run our KMeans trials.
"""
import json, random, time, argparse
from kmeans.kmeans import KMeans

if __name__ == '__main__':
  
  # Instantiate argument parser
  parser = argparse.ArgumentParser(description='Calculate KMeans from randomly generated data')
  parser.add_argument('-l', '--log', help='Enable KMeans debugging', action='store_true', default=False)
  parser.add_argument('-c', help='Max iterations before convergence', type=int, default=300)
  parser.add_argument('-t', help="Number of trials", type=int, default=1)
  parser.add_argument('-k', help='Value of \'k\' (centroids)', required=True, type=int, default=2)
  parser.add_argument('-n', help='data size', required=True, type=int, default=1000)

  # Get/parse arguments
  args = parser.parse_args()


  # Number of data points
  no_points = args.n

  with open('./trials/time.{0}.{1}.{2}.csv'.format(args.n, args.k, args.t), 'wb') as f:
    f.write('data size,trial,kmeans time (s)\n')
    for trial in xrange(1, args.t + 1):
      # KMeans Object
      k = KMeans(class_name="test", k=args.k, log=args.log, max_iterations=args.c)

      # Generate Data
      data = list()
      for i in range(no_points):
        data.append( [
          random.uniform(0.0, 1.0), # time
          random.uniform(0.0, 1.5), # coins, can be up to 1.5 the ammount of coins
          random.uniform(0.0, 1.0) # kills
        ] )

      # Inster data (this forces KMeans calculation)
      start = time.clock()
      k.put(data)
      f.write('{0},{1},{2},{3}\n'.format(args.n, args.k, trial, (time.clock() - start) ))