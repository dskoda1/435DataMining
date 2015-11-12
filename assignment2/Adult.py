#!/usr/bin/python

'''
Adult is the object used to store data from the file

'''
class Adult(object):
  def __init__(self):
    self.attr = []
    self.label = False
    self.attrIdents = []

  '''
  Take in a row from the csv reader after it has
  been checked, and set object data to row from file
  '''
  def initData(self, data):
    for x in data[:-1]:
      #for each value attempt a cast to int. if succeeds,
      #then store as int. otherwise catch and store str.
      try:
        a = int(x)
        self.attr.append({'value': a, 'type': 'int'})
      except ValueError:
        self.attr.append({'value': x, 'type': 'str'})
    #store class label.
    if '<=' in data[-1]:
      self.label = False
    else:
      self.label = True
  '''
  Check if row of data is clean to use
  '''
  def checkData(self, data):
    if data == []:
      return -1
    for x in data:
      if '?' in x:
        return -1
      else:
        continue
    return 1
