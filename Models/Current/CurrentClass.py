#!python2.7
# _*_ encoding=UTF-8 _*_
import sys
sys.path.append("../..")

from math import sin

import parameters
from Functions.string2num import string2num
from Functions.PointMat import PointMat

class DCCurrent:					 #DC Is
	name = ''
	portPos = ''
	portNeg = ''
	value = ''
	MatRhs = {}

	def __init__(self):
		self.name = ''
		self.portNeg = ''
		self.portPos = ''
		self.value = ''
		self.RHSMatDict = {}
	
	def getDCCurrent(self):
		DCCurrent = string2num(self.value)
		return DCCurrent
	
	def loadMatDCIs(self):
		self.RHSMatDict = {}

		portPos = parameters.NodesDict.get(self.portPos)
		portNeg = parameters.NodesDict.get(self.portNeg)

		ValueIs = self.getDCCurrent()

		if portPos != 0:
			self.RHSMatDict[PointMat(portPos-1,0)] = -1 * ValueIs
		else:
			pass

		if portNeg != 0:
			self.RHSMatDict[PointMat(portNeg-1,0)] = ValueIs

	
class ACCurrent:				#AC Is
	name = ''
	portPos = ''
	portNeg = ''
	ACMag = ''
	ACPhase = ''

	def __init__(self,ACMag='1',ACPhase='0'):
		self.name = ''
		self.portPos = ''
		self.portNeg = ''
		self.ACMag = ACMag
		self.ACPhase = ACPhase

	

	
