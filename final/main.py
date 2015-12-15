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
  
  #Get data from file, and cmd line args
  data = readFile('data.txt')
  args = getUserInput() 
  
  #Begin main program execution
  t0, t1, acc = 0, 0, 0
  if args['k'] > -1:
    #Execute DCT on file data
    print('\n\t\033[1m--------Starting DCT--------\033[0m')
    print('\tK value provided:', args['k'])
    t0 = time.time()
    data = copy.deepcopy(transform(data, args['k']))
    t1 = time.time()
    print('\n\t\tCompleted in:', t1-t0, 'seconds')
    print('\n\tC value selected by DCT:',  (len(data[0]) - args['k']))
    
  print('\tNumber of attributes per data point:', len(data[0]))
  print('\n\t\033[1m--------Starting K Means--------\033[0m')
  #Begin execution of K Means algorithm 
  t0 = time.time()
  for x in range(args['runs']):
    clusteredVecs = copy.deepcopy(kMeans(data, 6))
    acc = acc + getAccuracy(getOccurences(clusteredVecs))
    sys.stdout.write('\r\tRun %d' %(x+1))
  t1 = time.time()
  
  #Print out results  
  print('\n\t\tCompleted in:', t1-t0, 'seconds')
  print('\n\tRuns: ' + str(args['runs']))
  print('\tAccuracy: ' + str(acc/args['runs']) + '%')
  print('')

