#!/usr/bin/python3
import copy
import math
import random
from Helper import *
import functools
'''
Population is the object used to store all of the 
data. It also tracks how many pos/negative vals there
are after parsing the file.
'''
class Population(object):
  def __init__(self, data):
    self.data = data
    self.numPos = 0
    self.numNeg = 0
    self.total = len(data)
    self.pos = []
    self.neg = []
    self.setPosNeg()
    
	
  def setPosNeg(self):
    for x in self.data:
      if x.label:
        self.pos.append(x)
        self.numPos = self.numPos + 1
      else:
        self.neg.append(x)
        self.numNeg = self.numNeg + 1


  '''
  create the attribute map dynamically from the entire
  population. this is meant to be called on the entire 
  data set, not either of the sample sets. Use this to 
  reference 
  '''
  def createAttrMap(self):
	  #create the empty stats container
	  stats = []
	  for x in self.data[0].attr:
		  if x['type'] == 'str':
			  stats.append([])
		  else:
			  stats.append(0)
	  
	  #Go through the entire population getting the 
	  #potential values for all discrete attributes
	  for x in self.data:
		  for i, y in enumerate(x.attr):
			  if y['type'] == 'str':
				  if y['value'] not in stats[i]:
					  stats[i].append(y['value'])

	  return stats


  '''
  Create a training set from the original set
  proportionate to the number of positives/negatives
  in the file
  '''
  def createTrainingSet(self, percent):

    #run some math to get the sample sizes needed
    #for each class
    SS = len(self.data) / (100/int(percent))
    posRatio = self.numPos / self.total
    negRatio = self.numNeg / self.total
    posSS = SS * posRatio
    negSS = SS * negRatio

    #create a random sample from pop pos/neg
    sSets = self.createTrainingSetHelper( posSS, negSS)
    posSet = sSets['pSet']
    negSet = sSets['nSet']

    #actually create the object with
    #the samples created above
    return  Population(posSet + negSet)

  '''
  Based on the sample sizes for pos/neg requested,
  create two sets of random integers which will be used 
  to create the stratified Samples
  '''
  def createTrainingSetHelper(self, posSS, negSS):
    #Initialize the sets use to store random indices
    posSet = set()
    negSet = set()
    #initialize the lists to store objects
    posObjLst = []
    negObjLst = []
    #cast parameters to int
    posSS = int(posSS)
    negSS = int(negSS)

    #actually create the random samples now
    x = 0
    random.seed()
    while x < posSS:
      r = random.randrange(0, posSS)
      if r not in posSet:
        posSet.add(r)
        posObjLst.append(self.pos[x])
        x = x + 1

    x = 0
    while x < negSS:
      r = random.randrange(0, negSS)
      if r not in negSet:
        negSet.add(r)
        negObjLst.append(self.neg[x])
        x = x + 1
    #return the sample sets obtained in a dict
    return {'pSet': posObjLst, 'nSet': negObjLst}

  def filterOutTrainingSet(self, tPop):
    trainingSet = set()
    testSet = []
    #place training data into a set(was a list)
    for x in tPop.data:
      trainingSet.add(x)
    for x in self.data:
      if x not in trainingSet:
        testSet.append(x)

    #return what is now the testing set 
    return Population(testSet)


  '''
  For the given population, count up the occurences of 
  each discrete value, store in the counts member at the 
  appropriate index. For continuous values get a running
  sum of the values.
  '''
  def countUpStats(self, attrMap):
	  
	  #The data member multiple others will be based off
	  self.emptyCounterMap = []
	  
	  #initialize the data member
	  for i, x in enumerate(attrMap):
		  if isinstance(x, int):
			  self.emptyCounterMap.append(0)
		  else:
			  self.emptyCounterMap.append(list())
			  for y in x:
				  self.emptyCounterMap[i].append(0)

	  #copy above into one for positive and negative values
	  #need to use deep copy, because shallow copies are no good
	  self.negCounts = copy.deepcopy(self.emptyCounterMap)
	  self.posCounts = copy.deepcopy(self.emptyCounterMap)
	  
	  #actually go through the data now, counting up 
	  #occurences in first positive
	  for x in self.pos:
		  for i, y in enumerate(x.attr):
			  if y['type'] == 'int':
				  self.posCounts[i] = self.posCounts[i] + y['value']
			  else:
				  j = attrMap[i].index(y['value'])
				  self.posCounts[i][j] = self.posCounts[i][j] + 1
	  #now negatives
	  for x in self.neg:
		  for i, y in enumerate(x.attr):
			  if y['type'] == 'int':
				  self.negCounts[i] = self.negCounts[i] + y['value']
			  else:
				  j = attrMap[i].index(y['value'])
				  self.negCounts[i][j] = self.negCounts[i][j] + 1
	
	  #verify accuracy, the sum of each discrete attributes
	  #values count should be the same as the entire data set
	  #for x in self.posCounts:
		#  if not isinstance(x, int):
	 	#	  print(sum(x))

	  #for i, x in enumerate(self.posCounts):
		#  print(id(self.posCounts[i]))
		#  print(id(self.negCounts[i]))
	  #print(self.posCounts)
	  #print(self.negCounts)

  '''
  for continuous values: calculate the average&std dev
  for discrete: divide each amount of occurences by length
  of sample to obtain probablity
  '''
  def performStatisticAnalysis(self, attrMap):
	  #Create the data structure that will be used
	  #a dictionary
	  self.stats = {'posStats': [], 'negStats': []}

	  #for the continuous values, add a map to that index
	  #designating each required stat to be calculated
	  #for the discrete values, just copy from the 
	  for i, x in enumerate(attrMap):
		  if isinstance(x, int):
			  #pass the sum, along with the positive objects and attr index
			  #get a stats map back, which has sum, mean, variance,
			  #standard deviation. append this to stats['posStats']
			  #statsMap = generateContinuousStats(i, self.posCounts[i], self.pos)
			  self.stats['negStats'].append(generateContinuousStats(i, self.negCounts[i], self.neg))
			  self.stats['posStats'].append(generateContinuousStats(i, self.posCounts[i], self.pos))
		  else:
			  #pass the occurences list at this index, along with the count
			  #to a function which returns a probability list for each discrete val
			  self.stats['negStats'].append(generateDiscreteProbs(self.negCounts[i], self.numNeg))
			  self.stats['posStats'].append(generateDiscreteProbs(self.posCounts[i], self.numPos))
			
	  #print(self.stats)	
			 
  '''
  Return a population of 20 random tuples
  '''
  def getTestingSamples(self, ss):
	  random.seed()
	  tSet = set()
	  x = 0
	  #Get the 20 random indices
	  while x < ss:
		  r = random.randrange(0, self.total)
		  if r not in tSet:
			  tSet.add(r)
			  x = x + 1
	  #Get the 20 actual objects now
	  tPop = []
	  for x in tSet:
		  tPop.append(self.data[x])
 
	  return Population(tPop)

  '''
	Go through each of the items in the given population.
	For each tuples attribute, obtain the probability that
	it is positive or negative, and put them in seperate lists.
	upon completing the completion of these lists, multiply
	them together and pick the higher one, and use that to classify.
	Then compare these results with the actual labels.
	'''
  def attemptClassification(self, stats, attrMap):
	  accuracy = []
    #iterate through the populations adults
	  for i, x in enumerate(self.data):
		  probMap = {'posProbs': [], 'negProbs': []}
		  #iterate through a specific adults attributes 
		  for j, y in enumerate(x.attr):
			  #for continuous variable, pass value to guass function
			  #along with the current mean and std dev for both
			  #pos/neg
			  if y['type'] == 'int':
				  posProb = guass(y['value'], stats['posStats'][j]['mean'], stats['posStats'][j]['dev'])
				  negProb = guass(y['value'], stats['negStats'][j]['mean'], stats['negStats'][j]['dev'])
				  probMap['posProbs'].append(posProb)
				  probMap['negProbs'].append(negProb)
			  #for discrete value, get the index value has in attribute map, 
			  #and use that to look up the probablity for that value inside stats
			  else:
				  idx = attrMap[j].index(y['value'])
				  probMap['posProbs'].append(stats['posStats'][j][idx])
				  probMap['negProbs'].append(stats['negStats'][j][idx])
		  #multiply each index of the separate lists together
		  posProb = functools.reduce(lambda x, y: x * y, probMap['posProbs'])
		  negProb = functools.reduce(lambda x, y: x * y, probMap['negProbs'])
		  #Now figure the larger one, and use that as classification label
		  label = 0
		  if posProb > negProb:
			  label = True
		  else:
			  label = False
		  #Check our label against actual label, store in accuracy list
		  accuracy.append(1) if label == x.label else accuracy.append(0)

	  return (functools.reduce(lambda x, y: x + y, accuracy)/20) * 100












