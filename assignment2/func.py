#!/usr/bin/python3
import copy
import random
import sys
import time
'''
Secondary methods to do bayesian classification
primarily following functional programming paradigms
Input: Data set as a Population
       Attribute map for the layout of each Adult
       Percent wanted for the training set

1. Create the training set

2. Get the 20 test samples out of
  remaining population

3. Get the stats for each attribute pos/neg
  Discrete: Count up the occurences
  Continuous: Get the sum, mean, & stdDev

4. Calculate the probabilities
  Discrete: Divide # of occurences by size
  Continuous: 



'''

def funcRoutine(pop, attrMap, percent):
  #get the positive and negative training sets
  #along with the 20 testing samples
  tSet = createTrainTestSet(pop, percent)
 
  #Do some data manipulation on the tSet
  #to organize it into a list of lists, with 
  #each primary list being an attribute
  matrix = manipDataSet(tSet) 

  



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
