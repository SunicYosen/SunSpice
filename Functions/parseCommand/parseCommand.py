#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-
import sys
sys.path.append("../..")

import re
import parameters

from parseAcSimulation import parseAcSimulation
from parseDcSimulation import parseDcSimulation
from parseTranSimulation import parseTranSimulation
from parseParam import parseParam
from parsePlot import parsePlot

def parseCommand(comString = ''):
	comString = comString.replace('gnd','0')
	if re.match(parameters.regExpCommandAC,comString):
		print 'Info: --AC Simulation'
		parseAcSimulation(comString)

	elif re.match(parameters.regExpCommandDC,comString):
		print 'Info: --DC Simulation'
		parseDcSimulation(comString)
	
	elif re.match(parameters.regExpCommandTran,comString):
		print 'Info: --Tran Simulation'
		parseTranSimulation(comString)

	elif re.match(parameters.regExpCommandOptions,comString):
		print 'Info: --Options'


	elif re.match(parameters.regExpCommandOp,comString):
		print 'Info: --OP'
		
	
	elif re.match(parameters.regExpCommandEnd, comString):  # Wouldn't here
		print 'Info: --End!--'
	
	elif re.match(parameters.regExpCommandLib,comString):
		print 'Info:  --Include Lib'
		print 'Info:  ----Include:' ,comString.split(' ')[1]
	
	elif re.match(parameters.regExpCommandParam,comString):
		print 'Info:  --Define Param'
		parseParam(comString)

	elif re.match(parameters.regExpCommandPrint,comString):
		print 'Info:  --Print'
		listPrint = comString.split(' ')
		for index in listPrint[1:]:
			print 'Info: ----Print:',index
	
	elif re.match(parameters.regExpCommandPlot,comString):
		print 'Info: --Plot'
		parsePlot(comString)
	
	else:
		print 'Error: --ERROR Command!'
	

	return ''
