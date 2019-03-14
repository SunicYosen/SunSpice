#!python3
# _*_ encoding=UTF-8 _*_
import sys
sys.path.append("../..")

from math import exp

import parameters
from Functions.string2num import string2num
from Functions.PointMat import PointMat

class Diode:							  #Diode
	name = ''
	port1 = ''
	port2 = ''
	Model = ''
	Isat = '7.075E-9'
	Alpha = '30'
	StampMatDict = {}
	RHSMatDict = {}

	def __init__(self):
		self.name = ''
		self.port1 = ''
		self.port2 = ''
		self.Model = ''
		self.Isat = '7.075E-9'
		self.Alpha = '30'

	def getPort1(self):
		return self.port1

	def getPort2(self):
		return self.port2

	def getModel(self):
		return self.Model
	
	def getName(self):
		return self.name

	def getIsat(self):
		return string2num(self.Isat)
	
	def getAlpha(self):
		return string2num(self.Alpha)

	def loadMatStamps(self,Vd_n = 0.0):
		alpha_self = string2num(self.Alpha)
		isat_self = string2num(self.Isat)
		return alpha_self * isat_self * exp(alpha_self * Vd_n)
	
	def loadRHSStamps(self,Vd_n = 0.0):
		alpha_self = string2num(self.Alpha)
		isat_self = string2num(self.Isat)
		return (isat_self * (exp(alpha_self * Vd_n) - 1) - alpha_self * isat_self * exp(alpha_self * Vd_n)*Vd_n)

	def getI_V(self,Vd_n = 0.0):
		alpha_self = string2num(self.Alpha)
		isat_self = string2num(self.Isat)
		return (isat_self * (exp(alpha_self * Vd_n) - 1))
	
	def loadMatDiode(self,lastVd = 0):
		self.RHSMatDict = {}
		self.StampMatDict = {}
		
		port1 = parameters.NodesDict.get(self.port1)
		port2 = parameters.NodesDict.get(self.port2)

		valueStampMat = self.loadMatStamps(lastVd) #Last Value
		valueRHS = self.loadRHSStamps(lastVd)
		#
		#
		if port1 != 0:
			self.RHSMatDict[PointMat(port1-1,0)] = -1 * valueRHS
			if port2 != 0:
				self.StampMatDict[PointMat(port1-1,port1-1)] = valueStampMat
				self.StampMatDict[PointMat(port1-1,port2-1)] = -1 * valueStampMat
				self.StampMatDict[PointMat(port2-1,port2-1)] = valueStampMat
				self.StampMatDict[PointMat(port2-1,port1-1)] = -1 * valueStampMat
				self.RHSMatDict[PointMat(port2-1,0)] = valueRHS
			else:
				
				self.StampMatDict[PointMat(port1-1,port1-1)] = valueStampMat
		else:
			if port2 != 0:
				self.RHSMatDict[PointMat(port2-1,0)] = valueRHS
				self.StampMatDict[PointMat(port2-1,port2-1)] = valueStampMat
			else:
				pass


