#!/usr/bin/python3
import sys
import csv
import functools
def readFile(fileName):
  #Split lines from file
  lines = open(fileName).read().split("\n")
  reader = csv.reader(lines)
  #Split points now
  
  data = [ point for point in [line for line in reader]]
  #Pop last row out, empty list
  data.pop()
  
  #convert each list of string vals to a list of floats
  fData = list( map(convertListToFloats, data))
  return fData
  
#Input contains some empty strings, seems like we need to clean first
def convertListToFloats(row):
  strings = row[0].split()
  return list( map(convertStringToFloat, strings))
#Helper 
def convertStringToFloat(string):
  return float(string)
