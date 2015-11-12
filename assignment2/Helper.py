#!/usr/bin/python

import sys
import math
'''
'''
def checkArguments():

  if(len(sys.argv) == 2):
    return 1
  elif(len(sys.argv) == 3):
    return 2
  else:
    print("\n\n\t Usage: python3 hw2.py <sampleSize %>")
    print("\t Optional: python3 hw2.py <sampleSize %> <number of tests to run>\n\n")
    exit()

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

