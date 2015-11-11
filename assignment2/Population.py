#!/usr/bin/python3
import copy
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
    self.stats = []
    self.ncStats = []   
    self.setPosNeg()
    #self.initStatsDS()	
    
	
  def setPosNeg(self):
    for x in self.data:
      if x.label:
        self.pos.append(x)
        self.numPos = self.numPos + 1
      else:
        self.neg.append(x)
        self.numNeg = self.numNeg + 1


  '''
  Need to go through entire data set analyzing each 
  attributes potential values. if value is an integer,
  store that in appropriate index in self.contVals. Else
  create a map value for the string value in self.stats
  '''
  def initStatsDS(self):
	  for x in self.data[0].attr:
		  if x['type'] == 'str':
			  self.stats.append([])
		  else:
			  self.stats.append(0)

	  for x in self.data:
		  for i, y in enumerate(x.attr):
			  if y['type'] == 'int':
				  self.stats[i] = self.stats[i] + y['value']
			  else:
				  if y['value'] not in self.stats[i]:
					  self.stats[i].append(y['value'])
	  print(self.stats)
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

































