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
    self.setPosNeg()
  def setPosNeg(self):
    for x in self.data:
      if x.label:
        self.pos.append(x)
        self.numPos = self.numPos + 1
      else:
        self.neg.append(x)
        self.numNeg = self.numNeg + 1
