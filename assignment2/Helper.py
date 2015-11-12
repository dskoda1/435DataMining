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


def percentGen():
  y = list(range(1, 11))
  for x in y:
    yield x * 10
