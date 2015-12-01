#!/usr/bin/python3
import copy
import random
import sys
import time
import csv
import functools
'''
Secondary methods to do bayesian classification
primarily following functional programming paradigms
Input: Data set as a Population
       Attribute map for the layout of each Adult
       Percent wanted for the training set
1. Read the file into an array, cleaning tuples
that have ? as an attr value

2. Create the empty attr map that has a list
of all possible values for discrete attributes
at that index

3. Create the training set using stratified sampling

4. Get the 20 test samples out of
  remaining population

5. Get the stats for each attribute pos/neg
  Discrete: Count up the occurences
  Continuous: Get the sum, mean, & stdDev

6. Calculate the probabilities
  Discrete: Divide # of occurences by size
  Continuous: 



'''

def funcRoutine(percent): 
  
  data = readFile()
  attrMap = createAttrMap(data)
  tSet = createTTset(data, percent)


def createTTset(pop, percent):
  SS = len(pop[0]) / (100/int(percent))
  pos = list(filter(isPos, pop[len(pop) - 1]))
  print(pos)
  

def isPos(val):
  if '>' in val:
    return True
  else:
    return False

def createTrainTestSet(pop, percent):
  SS = len(pop.data) / (100/int(percent))
  posRatio = len(pop.pos) / pop.total
  negRatio = len(pop.neg) / pop.total
  posSS = int(SS * posRatio)
  negSS = int(SS * negRatio)
  random.seed()
  #Get the random values of objects to be plucked out
  pos = set(random.sample(pop.pos, posSS))
  neg = set(random.sample(pop.neg, negSS))

  #get 20 values from the rest of the list
  rem = set(pop.data) - (pos | neg)
  test = set(random.sample(rem, 20))
  return {'pos': pos, 'neg': neg, 'test': test}
  

def createAttrMap(pop):
  
  attrMap = []
  #Go through just the first object available  
  for i, x in enumerate(pop):
    for y in x:
      #push a 0, and break to next
      if isinstance(y, int):
        attrMap.append(0)
        break
      else:
        attrMap.append([])
        break

  for i, x in enumerate(attrMap):
    if isinstance(x, int):
      continue
    else:
      distinct = set(pop[i])
      attrMap[i] = copy.deepcopy(list(distinct))

  return attrMap



def readFile():
  f = open('adult.txt', 'rU')
  data = []
  #initialize the array with a single tuple from 
  #the file
  try:
    reader = csv.reader(f)
    for row in reader:
      for x in row:
        data.append([])
      break
  finally:
    f.close
  f = open('adult.txt', 'rU')

  valid = True
  try:
    reader = csv.reader(f)
    for row in reader:
      temp = []
      valid = True
      for x in row:
        #get rid of row if attr has ?
        if '?' in x:
          valid = False
          break
        try:
          a = int(x)
          temp.append(a)
        except ValueError:
          temp.append(x)
      if valid:
        for i, y in enumerate(temp):
          data[i].append(y)
  finally:
    f.close()

  return data
  #get the positive and negative training sets
  #along with the 20 testing samples
  #tSet = createTrainTestSet(pop, percent)
 
  #Do some data manipulation on the tSet
  #to organize it into a list of lists, with 
  #each primary list being an attribute
  #matrix = manipDataSet(tSet) 

def manipDataSet(tSet):
  #create the skeleton
  i = 0
  data = []
  for x in tSet['pos']:
    for y in x.attr:
      data.append([])
    break
  
  #place the positive and negative data
  #into arrays
  






'''
Code that proved to be slower than set operations
when obtaining remaining population
  foo = makeFilter(pos, neg)
  t0 = time.time()
  rem = set(filter(foo, pop.data))
  t1 = time.time()
  print(t1- t0)

def makeFilter(pos, neg):
  def notInEither(x):
    if x not in pos and x not in neg:
      return True
    else:
      return False
  return notInEither
'''
