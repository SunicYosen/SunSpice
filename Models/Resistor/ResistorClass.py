#!python2.7
# _*_ encoding=UTF-8 _*_
import sys
sys.path.append("../..")

import parameters
from Functions.string2num import string2num
from Functions.PointMat import PointMat

class Resistor:							 #R
	name = ''
	port1 = ''
	port2 = ''
	value = '1k' #1000 ohm for default
	StampMatDict = {}

	def __init__(self,value='1k'):
		self.name = ''
		self.port1 = ''
		self.port2 = ''
		self.value = value
		self.StampMatDict = {}

	def loadMatResistor(self):
		self.StampMatDict = {}

		port1 = parameters.NodesDict.get(self.port1)
		port2 = parameters.NodesDict.get(self.port2)

		valueResistor = string2num(self.value)

		if port1 != 0:
			if port2 != 0:
				self.StampMatDict[PointMat(port1-1,port1-1)] = 1.0/valueResistor
				self.StampMatDict[PointMat(port2-1,port2-1)] = 1.0/valueResistor
				self.StampMatDict[PointMat(port1-1,port2-1)] = -1.0/valueResistor
				self.StampMatDict[PointMat(port2-1,port1-1)] = -1.0/valueResistor
			else:
				self.StampMatDict[PointMat(port1-1,port1-1)] = 1.0/valueResistor
		else:
			if port2 != 0:
				self.StampMatDict[PointMat(port2-1,port2-1)] = 1.0/valueResistor
			else:
				pass