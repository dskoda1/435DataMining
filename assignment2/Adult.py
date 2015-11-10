#!/usr/bin/python

'''
Adult is the object used to store data from the file

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
