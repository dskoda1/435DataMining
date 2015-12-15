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
import time

if __name__ == '__main__':
  print('')
# number 
  #Get data from file, and cmd line args
  data = readFile('data.txt')
  args = getUserInput() 
  t0, t1 = 0, 0
  #Bundle the following off to a DCTransform function helper
  if args['k'] > -1:
    print('\n\tStarting DCT')
    print('\tK value provided:', args['k'])
    t0 = time.time()
    data = copy.deepcopy(transform(data, args['k']))
    t1 = time.time()
    print('\n\t\tCompleted in:', t1-t0, 'seconds')
    print('\n\tC value selected by DCT:',  (len(data[0]) - args['k']))
    
  print('\tNumber of attributes per data point:', len(data[0]))
  ###
  #Run the kmeans function a bunch of times, save results
  acc = 0
  print('\n\tStarting K Means')
  # gen = percentGen()
  t0 = time.time()
  for x in range(args['runs']):
    sys.stdout.write('\r\tRun %d' % (x+1))
    clusteredVecs = copy.deepcopy(kMeans(data, 6))
    acc = acc + getAccuracy(getOccurences(clusteredVecs))
  t1 = time.time()
  print('\n\t\tCompleted in:', t1-t0, 'seconds')
      
  print('\n\tRuns: ' + str(args['runs']))
  print('\tAccuracy: ' + str(acc/args['runs']))
  print('')

