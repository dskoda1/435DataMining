#!/usr/bin/python

"""
David Skoda
CS 435
Assignment 1
Environment: Python3, not compatible with Python2.7
"""
from Population import Population
from Adult import Adult
import csv
import sys
import math
import random

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
def createTrainingSet(pop, percent):

	#run some math to get the sample sizes
	SS = len(pop.data) / (100/int(percent))
	posRatio = pop.numPos / pop.total
	negRatio = pop.numNeg / pop.total
	posSS = SS * posRatio
	negSS = SS * negRatio

	#create a random sample from pop pos/neg
	sSets = createTrainingSetHelper(pop, posSS, negSS)
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
def createTrainingSetHelper(pop, posSS, negSS):
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
	while x < posSS:
		r = random.randrange(0, posSS)
		if r not in posSet:
			posSet.add(r)
			posObjLst.append(pop.pos[x])
			x = x + 1

	x = 0
	while x < negSS:
		r = random.randrange(0, negSS)
		if r not in negSet:
			negSet.add(r)
			negObjLst.append(pop.neg[x])
			x = x + 1
	#return the sample sets obtained in a dict
	return {'pSet': posObjLst, 'nSet': negObjLst}

def filterOutTrainingSet(pop, tPop):
	trainingSet = set()
	testSet = []
	#place training data into a set(was a list)
	for x in tPop.data:
		trainingSet.add(x)
	for x in pop.data:
		if x not in trainingSet:
			testSet.append(x)
		
	return Population(testSet)


def main():
	#Make sure program called correctly	
	checkArguments()
	#input the inital adults data file, clean data
	population = readFile("adult.txt")
	#create training data set from the original,
	#along with the percent requested from cmd line
	trainingPop = createTrainingSet(population, sys.argv[1])
	#Get the rest of the data as a testing data set
	testingPop = filterOutTrainingSet(population, trainingPop)
	print(str(len(trainingPop.data)))
	print(str(len(testingPop.data)))

main()

