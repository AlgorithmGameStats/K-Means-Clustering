#! /bin/bash

KS="1 2 3 4 8 16"
SIZES="10 100 1000 10000 100000 1000000"

for i in ${KS}; do
  for j in ${SIZES}; do
    python kmeans-trials.py -c 0 -t 100 -k ${i} -n ${j}
    echo "Done - K: ${i}, N:${j}"
  done
done