#!/usr/bin/python

"""
David Skoda
CS 435
Assignment 2
Environment: Python3, not compatible with Python2.7
"""
from Population import Population
from Adult import Adult
import csv
import sys
import math
import random
import functools
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
Open the file and create the cleaned data set
return the cleaned data set
'''
def readFile(fileName):
	f = open(fileName, 'rU')
	data = []
	try:
		reader = csv.reader(f)
		#go through each row in the file, creating a 
		#new adult. Check if data is legit, then add 
		#adult to list.
		for row in reader:
			a = Adult()
			if a.checkData(row) > 0:
				a.initData(row)
				data.append(a)
	#catch any errors, close file	
	except:
		print("unexpected error" + str(sys.exc_info()[0]))
	finally:
		f.close()
	#Create population object to return 
	return Population(data)
	

'''
Create a training set from the original set
proportionate to the number of positives/negatives
in the file
'''
def createTrainingSet(pop, percent):

	#run some math to get the sample sizes needed
	#for each class
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
	random.seed()
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

	#return what is now the testing set	
	return Population(testSet)

'''
Go through each of the items in the given population.
For each tuples attribute, obtain the probability that
it is positive or negative, and put them in seperate lists.
upon completing the completion of these lists, multiply
them together and pick the higher one, and use that to classify.
Then compare these results with the actual labels.
'''
def attemptClassification(pop, stats, attrMap):

	accuracy = []
	#iterate through the populations adults
	for i, x in enumerate(pop.data):
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

		#print("Positive is greater: ",posProb) if posProb > negProb else print("Negative is greater: ", negProb)



'''
Calculate a probability given value, mean, stddev
'''
def guass(val, mean, dev):
	left = 1 / (dev * math.sqrt(2 * math.pi))
	right = math.pow( ( (val - mean) / dev ), 2 ) * ( - 1 / 2 )
	return left * ( math.pow( math.e , right)) 

def main():
	#Make sure program called correctly	
	runMode = checkArguments()
	#run mode of 1 signifies just a single run, otherwise run
	#sys.argv[2] times and get the average accuracy

	#input the inital adults data file, clean data
	population = readFile("adult.txt")
	
	#get the backbone attribute map to be used later
	attrMap = population.createAttrMap()
	
	#create training data set from the original,
	#along with the percent requested from cmd line
	percent = sys.argv[1]
	

	trainingPop = createTrainingSet(population, percent)
	
	#Get the rest of the data as a testing data set
	testingPop = filterOutTrainingSet(population, trainingPop)

	#sum up/count occurences of values in the training set
	trainingPop.countUpStats(attrMap)

	#create data members that store probabilities for discrete
	#and averages/standard deviation for continuous values
	trainingPop.performStatisticAnalysis(attrMap)

	#Get 20 random tuples from the testing population
	rPop = testingPop.getTestingSamples(20)

	#Use the training population statsMap, and the random
	#population from the testing set and classify them
	accPercent = attemptClassification(rPop, trainingPop.stats, attrMap)
	print(accPercent)

main()

