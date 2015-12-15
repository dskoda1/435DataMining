#!/usr/bin/python3
import sys
import csv
import functools
import random
import copy
from scipy.spatial import distance
import numpy
import math as m

'''
Kmeans and helper functions below
'''
def kMeans(data, k):
  #select k random data points
  random.seed()
  centroids = random.sample(data, k)
  #centroids = [data[70],data[170],data[270],data[370],data[470],data[570]]
  #Assign the vecs to the initial clusters
  mappedVecs = [copy.deepcopy(assignToCluster(vec, centroids, i)) for i, vec in enumerate(data)]

  #Loop through the algorithm here
  while True:
    #Get new centroids by finding average of each cluster
    centroids = copy.deepcopy([copy.deepcopy(getAverageOfCluster(mappedVecs, i)) for i in range(0, k)])
    #Map the vectors to clusters again based on new centroids found above
    mappedVecs = copy.deepcopy([copy.deepcopy(reassignToCluster(vec, centroids)) for vec in mappedVecs])
    #Check if any of the vectors changed clusters
    numChanged = len(list(filter(lambda vec: vec['change'], mappedVecs)))
    #When none have changed, exit algorithm
    if numChanged == 0:
      break;
  #Return the results of the algorithm
  return mappedVecs
  
#Assigns the raw data points to a map to be used in the algorithm, along with initial cluster
def assignToCluster(vec, centroids, i):
  minK = numpy.argmin([distance.euclidean(vec, centroid) for centroid in centroids])
  return {'cluster': minK, 'vec': vec, 'class': (i // 100), 'change': True}
  
#Filter function to check if a data point lies in a cluster
def isInCluster(vec, cluster):
  return (True if cluster == vec['cluster'] else False)

#Obtain the centroid of a cluster given the k value of the cluster
def getAverageOfCluster(clusterVecs, k):
  #Filter out the vectors that belong to the k'th cluster
  cluster = copy.deepcopy([x for x in clusterVecs if isInCluster(x, cluster=k)])
  #Sum and average all the vectors in the cluster to obtain the centroid
  return copy.deepcopy([(sum([point['vec'][i] for point in cluster]) / len(cluster)) for i in range(0, len(cluster[0]['vec']))])
  
#Find the closest cluster to a vector given the centroids
def reassignToCluster(vec, clusterMeans):
  clus = numpy.argmin([distance.euclidean(vec['vec'], clusterMean) for clusterMean in clusterMeans])
  #update whether or not it changed clusters
  if vec['cluster'] == clus:
    vec['change'] = False
  else:
    vec['change'] = True
  vec['cluster'] = clus
  return vec


'''
DCT and helper functions below
'''
#main function
def transform(data, k):
  #Perform DCT
  uVec = copy.deepcopy(dct(data))
  #Obtain the index to cut off at
  c = findCutOffIndex(uVec)
  #Cut off each data point at the correct dimensionality
  return ([copy.deepcopy(x[:c + k]) for x in data])

#Perform DCT on each data point
def dct(data):
  res = []
  for vec in data:
    dctV = []
    for i, x in enumerate(vec):
      total, a = 0, 0
      length = len(vec)
      total = vec[i] * m.cos(( ((2 * i) + 1) * i * m.pi) / (2 * length))
      for j in range(length):
        val = vec[j] * m.cos(( ((2 * j) + 1) * i * m.pi) / (2 * length))
        total += val
      if i == 0:
        a = m.sqrt(1/length)
      else:
        a = m.sqrt(2/length)
      dctV.append((a * total))
    #Append the u vector to the result
    res.append(copy.deepcopy(dctV))
  return res
  
#Given all the U vectors, get the C value for each
def findCutOffIndex(uVecs):
  res = []
  for vec in uVecs:
    cutOff = max(vec) / 20
    c = 0
    for i, x in enumerate(vec):
      if abs(x) < cutOff:
        c = i
        break
    res.append(c)
  #Return the max
  return max(res)
    
  
'''
Accuracy calculations
'''
#Given the counted up clusters, calc accuracu
def getAccuracy(counter):
  maxApp = 0
  maxApps = []
  for x in counter:
    for k, v in x.items():
      if v != 0 and v > maxApp:
        maxApp = v
    maxApps.append(maxApp)
    maxApp = 0
  return (functools.reduce((lambda x, y: x+y), maxApps) / 6)
  
#Debugging function to print counted up clusters  
def printOccurences(counter):
  for i, x in enumerate(counter):
    print('\nCluster ' + str(i + 1) + ' occurences: ')
    for k, v in x.items():
      if v != 0:
        print("Class " + str(k + 1), ": ", v, "%")
        
#Creates a counter of all the occurences of each ground truth in each cluster
def getOccurences(clusteredVecs):
  occurences = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
  counter = [(copy.deepcopy(occurences)) for i in range(6)]
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
  #Invalid or usage requested
  if len(sys.argv) < 2 or sys.argv[1] == 'usage':
    print('\n\n\t\033[1mUsage:\033[0m python3 main.py <number of runs to average together> <k value for DCT(optional)>')
    print('\n\tThe \033[1moptional\033[0m k value specified could be:')
    print('\t0: This tells the program to simply select the largest C value from all data points, after performing DCT.')
    print('\tn <- [1..59]: This will add n to the largest C value from DCT, allowing for trial and error testing.\n\n')
    exit()
  #Defaults
  ret = {'runs': 1, 'k': -1}
  #DCT mode
  if len(sys.argv) > 2:
    ret['k'] = int(sys.argv[2])
    #Check if k value too big... negative values fine, dct will be skipped
    if ret['k'] > 59:
      print('\n\033[1m--------K value of', ret['k'], 'is invalid, not performing DCT.--------\033[0m\n')
      ret['k'] = -1
  #Regular just KMeans
  if len(sys.argv) > 1:
    ret['runs'] = int(sys.argv[1])
    
  return ret