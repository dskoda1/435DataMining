#!/usr/bin/python3

"""
David Skoda
CS 435
Assignment 2
Environment: Python3, not compatible with Python2.7
"""
from Population import Population
from Adult import Adult
from Helper import *
from Func import *
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

def mainInput():
  #input the inital adults data file, clean data
  population = readFile("adult.txt")
  
  #get the backbone attribute map to be used later
  attrMap = population.createAttrMap()

  return {'pop': population, 'map': attrMap}
  
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
  args = checkArguments()
  
  #Init variables for bookkeeping 
  runs, x = 0, 0
  results = []
  gen = percentGen()
  t0, t1 = 0, 0
  #Begin timing sequence
  if args['mode'] == 'Regular':
    data = mainInput()
    print("Progress:")
    t0 = time.time()
    #Begin loop
    while x < args['runs']:
      results.append(mainRoutine(data['pop'], data['map'], args['percent']))
      x = x + 1
      if x % (args['runs'] / 10) == 0:
        print( next(gen) , "%") 
    #End timing sequence
    t1 = time.time()
  else:
    print("Functional currently under construction.")
    funcRoutine()
    exit()
  #print out results
  print("\n\n")
  print("\tTraining set size: \t", args['percent'], "%")
  print("\tAverage accuracy of: \t", functools.reduce(lambda x, y: x + y, results) / args['runs'])
  print("\tAverage time of run: \t", (t1 - t0) / args['runs'])
  print("\tNumber of runs: \t", args['runs'])
  print("\tProgram mode: \t\t", args['mode'])
  print("\n\n")

  #funcRoutine(population, attrMap, percent)


main()

