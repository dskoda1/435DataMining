#!/usr/bin/python3
import sys
import csv
import functools
import random
import copy
from scipy.spatial import distance
import numpy

def kMeans(data, k):
  #select k random data points
  random.seed()
  centroids = random.sample(data, k)
  mappedVecs = [copy.deepcopy(assignToCluster(vec, centroids, i)) for i, vec in enumerate(data)]

  while True:
    #Get new centroids
    centroids = copy.deepcopy([copy.deepcopy(getAverageOfCluster(mappedVecs, i)) for i in range(0, k)])
    mappedVecs = copy.deepcopy([copy.deepcopy(reassignToCluster(vec, centroids)) for vec in mappedVecs])
    numChanged = len(list(filter(lambda vec: vec['change'], mappedVecs)))
    if numChanged == 0:
      break;
    
  return mappedVecs

def assignToCluster(vec, centroids, i):
  minK = numpy.argmin([distance.euclidean(vec, centroid) for centroid in centroids])
  return {'cluster': minK, 'vec': vec, 'class': (i // 100), 'change': True}
  
def isInCluster(vec, cluster):
  return (True if cluster == vec['cluster'] else False)
  
def getAverageOfCluster(clusterVecs, k)  :
  cluster = copy.deepcopy([x for x in clusterVecs if isInCluster(x, cluster=k)])
  return copy.deepcopy([(sum([point['vec'][i] for point in cluster]) / len(cluster)) for i in range(0, len(cluster[0]['vec']))])
  
def reassignToCluster(vec, clusterMeans):
  clus = numpy.argmin([distance.euclidean(vec['vec'], clusterMean) for clusterMean in clusterMeans])
  if vec['cluster'] == clus:
    vec['change'] = False
  else:
    vec['change'] = True
  vec['cluster'] = clus
  return vec
def add(x, y): return (x + y)  

def getAccuracy(counter):
  maxApp = 0
  maxApps = []
  for x in counter:
    for k, v in x.items():
      if v != 0 and v > maxApp:
        maxApp = v
    maxApps.append(maxApp)
    maxApp = 0
  return (functools.reduce(add, maxApps) / 6)
  
def printOccurences(counter):
  
  for i, x in enumerate(counter):
    print('\nCluster ' + str(i + 1) + ' occurences: ')
    for k, v in x.items():
      if v != 0:
        print("Class " + str(k + 1), ": ", v, "%")

def getOccurences(clusteredVecs):
  occurences = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
  counter = [(copy.deepcopy(occurences)), (copy.deepcopy(occurences)),
            (copy.deepcopy(occurences)), (copy.deepcopy(occurences)),
            (copy.deepcopy(occurences)), (copy.deepcopy(occurences))]
  res = [[] for i in range(6)]
        
  for vec in (clusteredVecs):
    res[vec['cluster']].append(vec['class'])
  for i, r in enumerate(res):
    for c in r:
      counter[i][c] = counter[i][c] + 1
  return counter

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
  #k = int(sys.argv[1])
  runs = int(sys.argv[1])
  return {'runs': runs}