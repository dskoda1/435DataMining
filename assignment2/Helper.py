#!/usr/bin/python

import sys
import math
'''
'''
def checkArguments():
  #Check for usage first  
  if sys.argv[1] == 'usage':
    print("\n\n\t Usage: python3 hw2.py <sampleSize %>")
    print("\t Optional: python3 hw2.py <sampleSize %> <number of tests to run> <0: regular mode, 1: functional mode>\n\n")
    exit()
  #Otherwise parse arguments
  #Default values below
  ret = {'mode': 'Regular', 'runs': 1, 'percent': 10}
  numArgs = len(sys.argv)
  #Program execution mode
  if numArgs > 3:
    if int(sys.argv[3]) == 1:
      ret['mode'] = 'Functional'
    else:
      ret['mode'] = 'Regular'  
  #Number of test runs to execute
  if numArgs > 2:
    runs = int(sys.argv[2])
    if(runs < 10):
      print("Minimum # of runs is 10 in multirun mode. Changing to 10.")
      runs = 10
    ret['runs'] = runs
  #Training set percentage
  if numArgs > 1:
    percent = int(sys.argv[1])
    if percent > 99:
      print("Sample size greater than 99% not legal. Changing to 99.")
      percent = 99
    elif percent < 1:
      print("Sample size less than 1% not legal. Changing to 1%.")
      percent = 1
    ret['percent'] = percent
  
  if numArgs == 1:
    print("\n\n\t Usage: python3 hw2.py <sampleSize %>")
    print("\t Optional: python3 hw2.py <sampleSize %> <number of tests to run> <0: regular mode, 1: functional mode>\n\n")
    exit()
  return ret
'''
Calculate a probability given value, mean, stddev
'''
def guass(val, mean, dev):
  left = 1 / (dev * math.sqrt(2 * math.pi))
  right = math.pow( ( (val - mean) / dev ), 2 ) * ( - 1 / 2 )
  return left * ( math.pow( math.e , right))

#Generator for main function
def percentGen():
  y = list(range(1, 11))
  for x in y:
    yield x * 10

'''
calculate mean, variance, standard deviation for a given class, attribute
'''
def generateContinuousStats(attrI, attrSum, classObjects):
  statsMap = {'sum': attrSum, 'variance': 0, 'mean': 0, 'dev': 0, 'count': len(classObjects)}
  #calculate mean
  statsMap['mean'] = statsMap['sum'] / statsMap['count']
  #calculate variance
  varSum = 0
  for x in classObjects:
    varSum = varSum + pow((x.attr[attrI]['value'] - statsMap['mean']), 2)
  statsMap['variance'] = varSum / statsMap['count']
  statsMap['dev'] = math.sqrt(statsMap['variance']) 
  return statsMap

def generateDiscreteProbs(occurL, count):
  retList = []
  for x in occurL:
    retList.append(x / count)

  return retList



