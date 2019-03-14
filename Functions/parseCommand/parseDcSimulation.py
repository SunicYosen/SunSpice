#!/usr/bin/python3
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")


import parameters
from Functions.string2num import string2num
from Functions.SimulationType.DC import DCSimulation

class SweepPara:
	paramName = ''
	paramValueStart = 0
	paramValueStop = 0
	paramValueStep = 0
	default_PointNum = 100

	def __init__(self):
		self.paramName = ''
		self.paramValueStart = 0
		self.paramValueStop = 0
		self.paramValueStop = 0

def parseDcSimulation(dcSimString = ''):					#parse DC simulation
	dcSimString = dcSimString.replace('.dc ','').strip()
	dcSimlist = dcSimString.split(' ')

	if len(dcSimlist) < 4:
		print( "Error: Less parameters than Expected!")
		exit()
	
	elif len(dcSimlist) == 4:
		dcSimParaTemp = SweepPara()
		dcSimParaTemp.paramName = dcSimlist[0]
		dcSimParaTemp.paramValueStart = string2num(dcSimlist[1])
		dcSimParaTemp.paramValueStop = string2num(dcSimlist[2])
		dcSimParaTemp.paramValueStep = string2num(dcSimlist[3])
		parameters.listDCParam.append(dcSimParaTemp)

	elif len(dcSimlist) == 9 & dcSimlist[4] == 'sweep': 
		dcSimParaTemp = SweepPara()
		dcSimParaTemp.paramName = dcSimlist[0]
		dcSimParaTemp.paramValueStart = string2num(dcSimlist[1])
		dcSimParaTemp.paramValueStop = string2num(dcSimlist[2])
		dcSimParaTemp.paramValueStep = string2num(dcSimlist[3])
		parameters.listDCParam.append(dcSimParaTemp)

		dcSimSweepTemp = SweepPara()
		dcSimSweepTemp.paramName = dcSimlist[5]
		dcSimSweepTemp.paramValueStart = string2num(dcSimlist[6])
		dcSimSweepTemp.paramValueStop = string2num(dcSimlist[7])
		dcSimSweepTemp.paramValueStep = string2num(dcSimlist[8])
		parameters.listDCParam.append(dcSimSweepTemp)

	else:
		print( "Error: DC Simulation Expression is ERROR!")
		exit()
	
	#DCSimulation()   										#Start DC Simulation

	



