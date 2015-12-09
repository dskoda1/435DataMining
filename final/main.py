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
  acc = 0
  for x in range(args['runs']):
    clusteredVecs = kMeans(data, args['k'], 50)
    acc = acc + (len([vec for vec in clusteredVecs if vec['class'] == vec['cluster']]) / len(clusteredVecs))
  print(str(acc / args['runs']))
  #  for point in clusteredVecs:
  #    classes[point['cluster']] = classes[point['cluster']] + 1  
  
  #average and print out results
  #for i, x in enumerate(classes):
  #  classes[i] = x / args['runs']
  #  print(classes[i])  
  
    
    
  


