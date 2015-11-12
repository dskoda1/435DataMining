#!/usr/bin/python

"""
David Skoda
CS 435
Assignment 2
Environment: Python3, not compatible with Python2.7
"""
from Population import Population
from Adult import Adult
from Helper import *
import csv
import sys
import math
import random
import functools
import time

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


def mainRoutine(population, attrMap, percent):
	#Create the training population
	trainingPop = population.createTrainingSet( percent)
		
	#Get the rest of the data as a testing data set
	testingPop = population.filterOutTrainingSet(trainingPop)
	
	#sum up/count occurences of values in the training set
	trainingPop.countUpStats(attrMap)
	
	#create data members that store probabilities for discrete
	#and averages/standard deviation for continuous values
	trainingPop.performStatisticAnalysis(attrMap)
	
	#Get 20 random tuples from the testing population
	rPop = testingPop.getTestingSamples(20)
	
	#Use the training population statsMap, and the random
	#population from the testing set and classify them
	return rPop.attemptClassification(trainingPop.stats, attrMap)
		
		

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

	#Init variables for bookkeeping	
	runs, x = 0, 0
	results = []
	gen = percentGen()
	#Check whether to loop many times or not
	if runMode == 1: 
		runs = 1 
	else: 
		runs = int(sys.argv[2])
		if runs < 10:
			#Less than 10 runs in multirun is not allowed
			print("Minimum amount of runs is 10.")
			runs = 10
	#Begin timing sequence
	t0 = time.time()
	#Begin loop
	while x < runs:	
		#Call the main, non functional routine
		results.append(mainRoutine(population, attrMap, percent))
		x = x + 1
		if x % (runs / 10) ==0:
			print( next(gen) , "%") 
	#End timing sequence
	t1 = time.time()

	#print out results
	print("\n\n")
	print("\tAverage accuracy of: ", functools.reduce(lambda x, y: x + y, results) / runs)
	print("\tAverage time of run: ", (t1 - t0) / runs)
	print("\tNumber of runs: ", runs)
	print("\n\n")

main()

