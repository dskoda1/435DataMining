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
import copy

if __name__ == '__main__':
# number 
  #Get data from file, and cmd line args
  data = readFile('data.txt')
  #args = getUserInput() 
  
  #Run the kmeans function a bunch of times, save results
  acc = 0
  #for x in range(args['runs']):
  clusteredVecs = kMeans(data, 6, 5)
  occurences = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
  counter = [(copy.deepcopy(occurences)), (copy.deepcopy(occurences)),
            (copy.deepcopy(occurences)), (copy.deepcopy(occurences)),
            (copy.deepcopy(occurences)), (copy.deepcopy(occurences))]
#   for i, vec in enumerate(clusteredVecs):
#       counter[i//100][vec['cluster']] = 1 + counter[i//100][vec['cluster']]
#   print("Ground truth results")
#   for i, cluster in enumerate(counter):
#       print("Class ", i)
#       for k, v in cluster.items():
#           if v != 0:
#               print(k, ": ", v, "%")
              
  #for x in range(0, 100):
   #   print(clusteredVecs[x]['cluster'])
   # acc = acc + (len([vec for vec in clusteredVecs if vec['class'] == vec['cluster']]) / len(clusteredVecs))
  #print(str((acc / args['runs']) * 100))

  
    
    
  


