#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-
import sys
sys.path.append("../..")

import parameters
from Functions.string2num import string2num
from Functions.PointMat import PointMat

class vcvs:								 #VCVS
	name = ''
	portPos = ''
	portNeg = ''
	ctlNodePos = ''
	ctlNodeNeg = ''
	voltageGain = ''
	matStampsE = {}
	
	def __init__(self):
		self.name =''
		self.portPos = ''
		self.portNeg = ''
		self.ctlNodePos = ''
		self.ctlNodeNeg = ''
		self.voltageGain = ''
		self.matStampsE = {}

	#V -> Pluse -> SinV -> E -> F -> H -> L
	def loadMatE(self,MatAddr=0):
		portPos = parameters.NodesDict.get(self.portPos)
		portNeg = parameters.NodesDict.get(self.portNeg)
		portCtlPos = parameters.NodesDict.get(self.ctlNodePos)
		portCtlNeg = parameters.NodesDict.get(self.ctlNodeNeg)

		valueEk = string2num(self.voltageGain)
		if portPos != 0:
			self.matStampsE[PointMat(MatAddr,portPos-1)] = 1
			self.matStampsE[PointMat(portPos-1,MatAddr)] = 1
		
		if portNeg != 0:
			self.matStampsE[PointMat(MatAddr,portNeg-1)] = -1
			self.matStampsE[PointMat(portNeg-1,MatAddr)] = -1

		if portCtlPos != 0:
			self.matStampsE[PointMat(MatAddr,portCtlPos-1)] = -1 * valueEk

		if portCtlNeg != 0:
			self.matStampsE[PointMat(MatAddr,portCtlNeg-1)] = valueEk


		

class cccs:								#CCCS	
	name = ''
	portPos = ''
	portNeg = ''
	ctlNodePos = ''
	ctlNodeNeg = ''
	currentGain = ''
	matStampsF = {}
	matRhsF = {}

	def __init__(self):
		self.name = ''
		self.portPos = ''
		self.portNeg = ''
		self.ctlNodePos = ''
		self.ctlNodeNeg = ''
		self.currentGain = ''
		self.matRhsF = {}
		self.matStampsF = {}

	def loadMatF(self,MatAddr=0,Vctl=0):
		portPos = parameters.NodesDict.get(self.portPos)
		portNeg = parameters.NodesDict.get(self.portNeg)
		portCtlPos = parameters.NodesDict.get(self.ctlNodePos)
		portCtlNeg = parameters.NodesDict.get(self.ctlNodeNeg)

		valueFk = string2num(self.currentGain)

		self.matRhsF[PointMat(MatAddr,0)] = Vctl

		if portPos != 0:
			self.matStampsF[PointMat(portPos-1,MatAddr)] = valueFk
		if portNeg != 0:
			self.matStampsF[PointMat(portNeg-1,MatAddr)] = -1 * valueFk
		if portCtlPos != 0:
			self.matStampsF[PointMat(portCtlPos-1,MatAddr)] = 1
			self.matStampsF[PointMat(MatAddr,portCtlPos-1)] = 1
		if portCtlNeg != 0:
			self.matStampsF[PointMat(portCtlNeg-1,MatAddr)] = -1
			self.matStampsF[PointMat(MatAddr,portCtlNeg-1)] = -1		

class vccs:								#VCCS
	name = ''
	portPos = ''
	portNeg = ''
	ctlNodePos = ''
	ctlNodeNeg = ''
	transconValue = ''
	matStampsG= {}

	def __init__(self):
		self.name =''
		self.portPos = ''
		self.portNeg = ''
		self.ctlNodePos = ''
		self.ctlNodeNeg = ''
		self.transconValue = ''
		self.matStampsG = {}
	
	def getI(self,Vd=0):
		ValueGk = string2num(self.transconValue)
		return Vd * ValueGk

	def loadMatG(self):
		portPos = parameters.NodesDict.get(self.portPos)
		portNeg = parameters.NodesDict.get(self.portNeg)
		portCtlPos = parameters.NodesDict.get(self.ctlNodePos)
		portCtlNeg = parameters.NodesDict.get(self.ctlNodeNeg)

		ValueGk = string2num(self.transconValue)
		
		if portPos != 0:
			if portCtlPos != 0:
				self.matStampsG[PointMat(portPos-1,portCtlPos-1)] = ValueGk
			if portCtlNeg != 0:
				self.matStampsG[PointMat(portPos-1,portCtlNeg-1)] = -1 * ValueGk
		if portNeg != 0:
			if portCtlPos != 0:
				self.matStampsG[PointMat(portNeg-1,portCtlPos-1)] = -1 * ValueGk
			if portCtlNeg != 0:
				self.matStampsG[PointMat(portNeg-1,portCtlNeg-1)] = ValueGk

	


class ccvs:								#CCVS
	name = ''
	portPos = ''
	portNeg = ''
	ctlNodePos = ''
	ctlNodeNeg = ''
	transResValue = ''
	matStampsH = {}

	def __init__(self):
		self.name = ''
		self.portPos = ''
		self.portNeg = ''
		self.ctlNodePos = ''
		self.ctlNodeNeg = ''
		self.transResValue = ''
		self.matStampsH = {}

	def loadMatH(self,MatAddr=0,Vctl=0):
		portPos = parameters.NodesDict.get(self.portPos)
		portNeg = parameters.NodesDict.get(self.portNeg)
		portCtlPos = parameters.NodesDict.get(self.ctlNodePos)
		portCtlNeg = parameters.NodesDict.get(self.ctlNodeNeg)

		ValueHk = string2num(self.transResValue)

		self.matStampsH[PointMat(MatAddr,MatAddr+1)] = -1 * ValueHk

		if portPos != 0:
			self.matStampsH[PointMat(MatAddr,portPos-1)] = 1
			self.matStampsH[PointMat(portPos-1,MatAddr)] = 1
		
		if portNeg != 0:
			self.matStampsH[PointMat(MatAddr,portNeg-1)] = -1
			self.matStampsH[PointMat(portNeg-1,MatAddr)] = -1
		
		if portCtlPos != 0:
			self.matStampsH[PointMat(MatAddr+1,portCtlPos-1)] = 1
			self.matStampsH[PointMat(portCtlPos-1,MatAddr+1)] = 1
		
		if portCtlNeg != 0:
			self.matStampsH[PointMat(MatAddr+1,portCtlNeg-1)] = -1
			self.matStampsH[PointMat(portCtlNeg-1,MatAddr+1)] = -1
