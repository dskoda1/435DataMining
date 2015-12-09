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

#Main function
if __name__ == '__main__':

  #define some variables
  fileName = 'data.txt'  
  data = readFile(fileName)
  
  #Get the user input 'k' value
  k = int(sys.argv[1])
  
  #select k random data points
  random.seed()
  centroids = random.sample(data, k)
  for x in centroids:
      print(x)
  
  
  
  
  # print(distance.euclidean(data[1], data[4]))

