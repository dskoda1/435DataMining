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
  args = getUserInput() 
  
  #Run the kmeans function a bunch of times, save results
  acc = 0
  for x in range(args['runs']):
    clusteredVecs = copy.deepcopy(kMeans(data, 6))
    acc = acc + getAccuracy(getOccurences(clusteredVecs))
      
  print('\n\tRuns: ' + str(args['runs']))
  print('\tAccuracy: ' + str(acc/args['runs']))
  print('')

