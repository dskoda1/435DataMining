#!/usr/bin/python
"""
David Skoda
CS 435
Assignment 1
Environment: Python3, not compatible with Python2.7
To run: python3 hw.py <i*.csv> <bucket_size>
"""

import csv
import sys
import math
"""
Assignment One: 
	Create a program that takes in an image (as a CSV file), and group the values into a number of buckets, determined by the given bucket size.
"""

"""
readFile(fileName)
	Takes in the name of a file, and places CSV data into a list of lists.
	Each row of data is placed in its own list for further processing.
	Returns a list of list of integer RGB values.
"""
def readFile(fileName):
	f = open(fileName, 'rU')
	data = []
	try:
		reader = csv.reader(f)
		for row in reader:
			data.append(row)
	finally:
		f.close()
	return data

"""
checkArguments()
	Ensures the proper usage of program.
	Requires 2 arguments,
		1. File name of csv file to be parsed and analyzed.
		2. Bucket size for data to be grouped in.
	Exits upon any failure with helpful error message.
"""
def checkArguments():
	if(len(sys.argv) != 3):
		print("usage: \n\n\t python3 hw.py <file.csv> <bucket size>\n\n")
		exit()
	size = int(sys.argv[2])
	if size < 1:
		print("\n\nNeed a bucket size of at least 1!\nExiting.")
		exit()
	elif size > 264:
		print("\n\nOnly one bucket if size > 264.\n")


"""
createBuckets(size)
	Takes in bucket size specified as a param.
	Creates the new data structure (list of lists) that 
	will be used to sort values into buckets.
	Returns this data structure.
"""
def createBuckets(size):
	buckets = []
	numBuckets = 1 + (264/size)
			
	for i in range(int(numBuckets)):
		newBucket = []
		buckets.append(newBucket)
	return buckets	

"""
placeInBuckets(buckets, bucketSize, rows)
Parameters:
	buckets- the empty list of buckets to be used for grouping.
	bucketSize- the size of each bucket to determine bucket to be placed in.
	rows- the data to be processed into buckets.
"""
def placeInBuckets(buckets, bucketSize, rows):
	numBuckets = len(buckets)
	for row in rows:
		for val in row:
			buckets[int(int(val)/bucketSize)].append(val)
	return buckets

"""
processBuckets(buckets)
	Use the buckets passed as a parameter to find the average
	of all values in each bucket.
	Pass these calculated averages back in a list of same length.
"""
def processBuckets(buckets):
	avgBuckets = []
	for i, bucket in enumerate(buckets):
		length = len(bucket)
		if length > 0:
			sum = 0
			for data in bucket:
				sum = sum + float(data)
			avgBuckets.append(float(sum) / length)
			#print("Bucket " + str(i) + ": " + str(float(sum) / length))
		else:
			#print("Bucket " + str(i) + ": 0")
			avgBuckets.append(0)
		return avgBuckets	

"""
maxLength(buckets)
	returns the length of the longest bucket
"""
def maxLength(buckets):
	max = 0
	for bucket in buckets:
		if len(bucket) > max:
			max = len(bucket)
	return max
	

"""
printBuckets(buckets, bucketSize)
	Takes in the buckets with values placed correctly inside.
	Outputs a histogram into stdout.
"""
def printBuckets(buckets, size):

	height = maxLength(buckets)
	mid = 0
	min = 1000
	max = 0
	for bucket in buckets:
		print(".", end="")
	print("")
	for x, i in enumerate(range(height, 0, -(int(height/20)))):
		for bucket in buckets:
			if len(bucket) > i:
				print("-", end="")
			else:
				print(" ", end="")
		print(".", end="")
		if x % 5 == 0:
			print(i, end="")
			mid = mid + 1
		if mid == 3:
			print(" Frequency", end="")
			mid = mid + 1
		print("")
	

	totalLength = 0
	for bucket in buckets:
		totalLength = totalLength + len(bucket)
		print(".", end="")
	print("")
	
	#print out the scale at the bottom of histogram
	q = int(len(buckets)/4)
	mid = 0
	for i, bucket in enumerate(buckets):
		if i%q == 0:
			print(i, end="")
		else:
			print(" ", end="")
	print(" - Bucket Number")
	skipFlag = True	
	for i, bucket in enumerate(buckets):
		if i%q == 0 and i != 0:
			print(int(i*size), end="")
			skipFlag = True
		elif int(i*size) > 100 and skipFlag:
			print("", end="")
			skipFlag = False
		else:
			print(" ", end="")
	print(" - Pixel Value ", end="\n")

	for bucket in buckets:
		for value in bucket:
			val = int(value)
			if val > max:
				max = val
			if val < min:
				min = val
			
	
	
	print("Total buckets: %s" % len(buckets))
	print("Total data points: %s" % totalLength)
	print("Max value: %s" % max)
	print("Min value: %s" % min)
def main():
	#error check arguments
	checkArguments()
	
	#Parse the command line arguments	
	#First argument is csv file to read
	rows = readFile(sys.argv[1])
	
	#Second argument is size of bucket 
	bucketSize = int(sys.argv[2])
	
	
	#create the list of lists which represents 
	buckets = createBuckets(bucketSize)
	
	#put values into appropriate buckets now
	buckets = placeInBuckets(buckets, bucketSize, rows)
	
	printBuckets(buckets, bucketSize)


	#average together each of the buckets and place in new container
	#averagedBuckets = processBuckets(buckets)
	
	#print the buckets
	#printBuckets(averagedBuckets)
	
main()	








