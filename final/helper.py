#!/usr/bin/python3
import sys
import csv
import functools
import random
import copy
from scipy.spatial import distance
import numpy


#Main function that glues together algorithms parts
def kMeans(data, k, runs):
  #select k random data points
  random.seed()
  centroids = random.sample(data, k)
  oldCentroids = copy.deepcopy(centroids)
  
  #Assign each vector to an initial cluster, save as array of dict like
  #{'vec': [x1, x2, x3..], 'cluster': kx, 'class': ky}
  mappedVecs = [assignToCluster(vec, centroids, i) for i, vec in enumerate(data)]
  #reassign each vector the specified amount of times, 
  #recomputing the average of each cluster every run
  track = []
  for x in mappedVecs:
    track.append(x['cluster'])
    
  print(track[:5])
  for x in range(15):
    didChange = False
    print([distance.euclidean(centroids[i], oldCentroids[i]) for i in range(0, k)])

    centroids = list(copy.deepcopy([getAverageOfCluster(mappedVecs, i) for i in range(0, k)]))
    oldCentroids = list(copy.deepcopy(centroids))
    mappedVecs = list(copy.deepcopy([reassignToCluster(vec, centroids) for vec in mappedVecs]))
    
    # for i, x in enumerate(mappedVecs):
    #   if track[i] != x['cluster']:
    #     didChange = True
    #     track[i] = x['cluster']
    # if  not didChange:
    #   break
    #numChanged = len(list(filter(lambda vec: (vec['change'] == True), mappedVecs)))
    #print(numChanged)
    # for vec in numChanged:
    #   print('id:' + str(vec['class']))
    #   print('cluster:' + str(vec['cluster']))
    # print('\n\n')
    #if numChanged == 0:
    #  break

  
  #Return the vectors and their classes in a dict
  return mappedVecs

#Assign each vector to a cluster, return 
#in the form of a dictionary
def assignToCluster(vec, centroids, i):
  minK = numpy.argmin([distance.euclidean(vec, centroid) for centroid in centroids])
  return {'cluster': minK, 'vec': vec, 'class': i, 'change': True}
  
#filter function to return vecs from a cluster
def isInCluster(vec, cluster):
  return (True if cluster == vec['cluster'] else False)
  
#Get the average of all vectors in some cluster
def getAverageOfCluster(clusterVecs, k):
  #print(clusterVecs[0])
  cluster = [vec for vec in clusterVecs if isInCluster(vec, cluster=k)]
  #Get length of vectors
  length = len(clusterVecs[0]['vec'])
  
 
  return  [(sum([point['vec'][i] for point in cluster]) / len(cluster)) for i in range(0, length)]  
  #a = numpy.array([vec['vec'] for vec in cluster])
  #print(numpy.mean(a, axis=0))

#Reassign a vector to the closest cluster given the means
def reassignToCluster(vec, clusterMeans):
  closest = numpy.argmin([distance.euclidean(vec['vec'], clusterMean) for clusterMean in clusterMeans])
  if closest == vec['cluster']:
    vec['change'] = False
  else:
    vec['change'] = True
  return vec

def checkForChange(vec):
  return vec['change']

'''
File input and cmd line arg helper functions
'''
def readFile(fileName):
  #Split lines from file
  lines = open(fileName).read().split("\n")
  reader = csv.reader(lines)
  
  #Split points now
  data = [ point for point in [line for line in reader]]
  #Pop last row out, contains empty list
  data.pop()
  
  #convert each list of string vals to a list of floats
  fData = list(map(convertListToFloats, data))
  return fData
  
def convertListToFloats(row):
  strings = row[0].split()
  return list(map(convertStringToFloat, strings))
  
def convertStringToFloat(string):
  return float(string)
  

def getUserInput():
  k = int(sys.argv[1])
  runs = int(sys.argv[2])
  return {'k': k, 'runs': runs}