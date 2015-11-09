#!/usr/bin/python

"""
David Skoda
CS 435
Assignment 1
Environment: Python3, not compatible with Python2.7
"""

import csv
import sys
import math
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
print(x.labelprint(x.label))Adult is the object used to store data from the file

'''
class Adult(object):
	def __init__(self):
		self.age = 0
		self.workclass = ""	
		self.fnlwgt = 0
		self.education = ""
		self.education_num = 0
		self.marital_status = ""
		self.occupation = ""
		self.relationship = ""
		self.race = ""
		self.sax = ""
		self.capital_gain = 0
		self.capital_loss = 0
		self.hours_per_week = 0
		self.native_country = ""
		self.label = False
	'''
	Take in a row from the csv reader after it has
	been checked, and set object data to row from file
	'''
	def initData(self, data):
		self.age = data[0]
		self.workclass = data[1]	
		self.fnlwgt = data[2]
		self.education = data[3]
		self.education_num = data[4]
		self.marital_status = data[5]
		self.occupation = data[6]
		self.relationship = data[7]
		self.race = data[8]
		self.sax = data[9]
		self.capital_gain = data[10]
		self.capital_loss = data[11]
		self.hours_per_week = data[12]
		self.native_country = data[13]
		if '<=' in data[14]:
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

'''
'''
def checkArguments():
	if(len(sys.argv) != 2):
		print("Usage: \n\n\t python3 hw2.py <sample%>\n\n")
		exit()

'''
Open the file and create the cleaned data set
return the cleaned data set
'''
def readFile(fileName):
	f = open(fileName, 'rU')
	data = []
	removed = 0
	kept = 0
	try:
		reader = csv.reader(f)
		for row in reader:
			a = Adult()
			if a.checkData(row) > 0:
				a.initData(row)
				data.append(a)
				kept = kept + 1
			else:
				removed = removed + 1
	except:
		print("unexpected error" + str(sys.exc_info()[0]))
	finally:
		f.close()
	pop = Population(data)
	return pop
'''
Create a training set from the original set
proportionate to the number of positives/negatives
in the file
'''
def takeSample(pop, percent):

	#run some math to get the sample sizes
	SS = len(pop.data) / (100/int(percent)
	posRatio = pop.numPos / pop.total
	negRatio = pop.numNeg / pop.total
	posSS = SS * posRatio
	negSS = SS * negRatio
	posI = pop.numPos/posSS - 1
	negI = pop.numNeg/negSS - 1
	i = 0
	pos = []
	neg = []

	#Create the pos and neg samples
	#from the original data
	for x in pop.pos:
		if i >= posI:
			pos.append(x)
			i = 0
		else:
			i = i + 1
	for x in pop.neg:
		if i >= negI:
			neg.append(x)
			i = 0
		else:
			i = i + 1

	#actually create the object with
	#the samples created above
	samPop = Population(pos + neg)



def main():
	
	checkArguments()
	population = readFile("adult.txt")
	#print(str(len(population.data)))
	#print(str(len(population.pos)))
	#print(str(len(population.neg)))
	takeSample(population, sys.argv[1])



main()

