#!/usr/bin/python3
import sys
import csv
import functools
def readFile(fileName):
#  f = open(fileName, 'rU')
#  data = []
#  try:
#    reader = csv.reader(f)
#    print('opened file')
#    for row in reader:
#      vec = []
#      for x in row:
#        vec.append(x)
#      data.append(vec)
#  except:
#    print('unexpected error reading file: ' + str(sys.exc_info()[0]))
#  finally:
#    f.close()
 
  lines = open(fileName).read().split("\n")
  reader = csv.reader(lines, delimiter=' ')
  data = [ point for point in [line for line in reader]]
  data.pop()
  
  fData =list( map(convertListToFloats, data))

  print(fData)
  
#Input contains some empty strings, seems like we need to clean first
def convertListToFloats(row):
  print(row)
  return list(map(convertStringToFloat, row))

def convertStringToFloat(string):
  print(string)
  return float(string)
