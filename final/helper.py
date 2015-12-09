#!/usr/bin/python3
import sys
import csv
import functools
import random
from scipy.spatial import distance
import numpy



def kMeans(data, k, runs):
  #select k random data points
  random.seed()
  centroids = random.sample(data, k)
  mappedVecs = [assignToCluster(vec, centroids) for vec in data]

  for x in range(runs):
    clusterMeans = [getAverageOfCluster(mappedVecs, i) for i in range(0, k)]
    mappedVecs = [reassignToCluster(vec, clusterMeans) for vec in mappedVecs]  
    
  return mappedVecs

def assignToCluster(vec, centroids):
  minK = numpy.argmin([distance.euclidean(vec, centroid) for centroid in centroids])
  return {'cluster': minK, 'vec': vec}
  
def isInCluster(vec, cluster):
  return (True if cluster == vec['cluster'] else False)
  
def getAverageOfCluster(clusterVecs, k)  :
  cluster = [x for x in clusterVecs if isInCluster(x, cluster=k)]
  #This is only part that might need to not be hard coded for part 2
  return [(sum([point['vec'][i] for point in cluster]) / len(cluster)) for i in range(0, 60)]  
  
def reassignToCluster(vec, clusterMeans):
  vec['cluster'] = numpy.argmin([distance.euclidean(vec['vec'], clusterMean) for clusterMean in clusterMeans])
  return vec



'''
File input and cmd line arg helper functions
'''
def readFile(fileName):
  #Split lines from file
  lines = open(fileName).read().split("\n")
  reader = csv.reader(lines)
  #Split points now
  
  data = [ point for point in [line for line in reader]]
  #Pop last row out, empty list
  data.pop()
  
  #convert each list of string vals to a list of floats
  fData = list( map(convertListToFloats, data))
  return fData
  
def convertListToFloats(row):
  strings = row[0].split()
  return list( map(convertStringToFloat, strings))
  
def convertStringToFloat(string):
  return float(string)
  
def getUserInput():
  k = int(sys.argv[1])
  runs = int(sys.argv[2])
  return {'k': k, 'runs': runs}