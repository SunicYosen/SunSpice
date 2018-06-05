#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-
import sys
sys.path.append("../..")

import parameters
from Functions.string2num import string2num

class TranParam:
	StartTime = 0.0
	StopTime = 0.0
	StepTime = 0.0
	UIC = False

	def __init__(self):
		self.StartTime = 0.0
		self.StepTime = 0.0
		self.StopTime = 0.0
		self.UIC = False


def parseTranSimulation(TranSimulationString = ''):
	TranSimulationString = TranSimulationString.replace('.tran ','').strip()

	listTranTemp = TranSimulationString.split(' ')
	TranParamTemp = TranParam()

	if len(listTranTemp) == 2:
		TranParamTemp.StepTime = string2num(listTranTemp[0])
		TranParamTemp.StopTime = string2num(listTranTemp[1])
		parameters.listTranParam.append(TranParamTemp)

	elif len(listTranTemp) == 3:
		TranParamTemp.StepTime = string2num(listTranTemp[0])
		TranParamTemp.StopTime = string2num(listTranTemp[1])
		if (listTranTemp[2] == 'uic'):
			TranParamTemp.UIC = True
		elif ('tstart' in listTranTemp[2]):
			TranParamTemp.StartTime = string2num(listTranTemp[2].split('=')[1])
		else:
			print "Error: Tran parameter Unknown!",listTranTemp[2]
			exit()

		parameters.listTranParam.append(TranParamTemp)
	
	elif len(listTranTemp) == 4:
		TranParamTemp.StepTime = string2num(listTranTemp[0])
		TranParamTemp.StopTime = string2num(listTranTemp[1])
		if ('tstart' in listTranTemp[2]):
			TranParamTemp.StartTime = string2num(listTranTemp[2].split('=')[1])
		else:
			print "Error: Tran parameter Unknown!",listTranTemp[2]
			exit()

		if (listTranTemp[3] == 'uic'):
			TranParamTemp.UIC = True
		else:
			print "Error: Tran parameter Unknown!",listTranTemp[3]
			exit()
		parameters.listTranParam.append(TranParamTemp)
	
	else:
		print "Error: Tran Params More Than Expected!"
		exit()

	#TranSimulation()  #Start Tran Simulation
