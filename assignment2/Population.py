#!/usr/bin/python3

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
    self.initStatsDS()	

	
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



