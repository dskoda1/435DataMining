#!/usr/bin/python3

'''
CS 435
David Skoda
Final Project
Environment: Python 3
'''
from scipy.cluster.vq import *
import sys
from helper import *
from scipy.spatial import distance
import random

if __name__ == '__main__':

  #define some variables
  fileName = 'data.txt'  
  data = readFile(fileName)
  args = getUserInput() 
  
  
  #select k random data points
  random.seed()
  centroids = random.sample(data, args['k'])
  
  #map the vectors to their initial clusters
  mappedVecs = [assignToCluster(vec, centroids) for vec in data]

  for x in range(0, args['runs']):
    clusterMeans = [getAverageOfCluster(mappedVecs, i) for i in range(0, args['k'])]
    mappedVecs = [reassignToCluster(vec, clusterMeans) for vec in mappedVecs]  
    
  classes = [0] * 6
  for point in mappedVecs:
    classes[point['cluster']] = classes[point['cluster']] + 1  
  
  for x in range(301, 400):
    print(mappedVecs[x]['cluster'])


