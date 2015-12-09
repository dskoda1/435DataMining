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

  #Get data from file, and cmd line args
  data = readFile('data.txt')
  args = getUserInput() 
  
  #Run the kmeans function a bunch of times, save results
  classes = [0] * 6
  for x in range(args['runs']):
    clusteredVecs = kMeans(data, args['k'], 50)
    for point in clusteredVecs:
      classes[point['cluster']] = classes[point['cluster']] + 1  
  
  #average and print out results
  for i, x in enumerate(classes):
    classes[i] = x / args['runs']
    print(classes[i])  
  
    
    
  


