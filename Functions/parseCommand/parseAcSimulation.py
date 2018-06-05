#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-
import sys
sys.path.append("../..")

import parameters
from Functions.string2num import string2num
from Functions.SimulationType.AC import ACSimulation

class SweepF:
	paramName = ''
	paramFStart = 0.0
	paramFStop = 0.0
	default_PointNum = 100

	def __init__(self):
		self.paramName = ''
		self.paramFStart = 0.0
		self.paramFStop = 0.0

def parseAcSimulation(acSimString = ''):
	acSimString = acSimString.replace('.ac ','').strip()
	acSimlist = acSimString.split(' ')

	if len(acSimlist) < 3:
		print "Error: Less parameters than Expected!"
		exit()
	
	elif len(acSimlist) == 3:
		acSimParaTemp = SweepF()
		acSimParaTemp.paramName = acSimlist[0]
		acSimParaTemp.paramFStart = string2num(acSimlist[1])
		acSimParaTemp.paramFStop = string2num(acSimlist[2])
		parameters.listACParam.append(acSimParaTemp)

	elif len(acSimlist) == 7 & acSimlist[4] == 'sweep':        #Wouldnt here
		acSimParaTemp = SweepF()
		acSimParaTemp.paramName = acSimlist[0]
		acSimParaTemp.paramFStart = string2num(acSimlist[1])
		acSimParaTemp.paramFStop = string2num(acSimlist[2])
		parameters.listACParam.append(acSimParaTemp)

		acSimSweepTemp = SweepF()
		acSimSweepTemp.paramName = acSimlist[4]
		acSimSweepTemp.paramFStart = string2num(acSimlist[5])
		acSimSweepTemp.paramFStop = string2num(acSimlist[6])
		parameters.listACParam.append(acSimSweepTemp)

	else:
		print "Error: AC Simulation Expression is ERROR!"
		exit()

	#ACSimulation()  #Start AC Simulation