#! /bin/bash

KS="1 2 3 4"
SIZES="10 100 1000 10000"

for i in ${KS}; do
  for j in ${SIZES}; do
    python kmeans-trials.py --log -c 1 -t 100 -k ${i} -n ${j}
    echo "Done - K: ${i}, N:${j}"
  done
done