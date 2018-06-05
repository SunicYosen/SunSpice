#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from ResistorClass import Resistor

from Functions.addNode import addNode
from Functions.string2num import string2num
import parameters

def parseR(resString =''):							#parse Resistor
	resParaList = resString.split(' ')

	if len(resParaList) > 4:
		print '----ERROR: More parameters than expected!'
		return '----False'

	elif len(resParaList) < 4:
		print '----ERROR: Lese parameters than expected!'
		return '----False'
	
	else:
		resistorTemp = Resistor()
		resistorTemp.name = resParaList[0]
		resistorTemp.port1 = resParaList[1]
		resistorTemp.port2 = resParaList[2]
		resistorTemp.value = resParaList[3]

		#value = string2num(resistorTemp.value)

		addNode(resistorTemp.port1)
		addNode(resistorTemp.port2)
		
		parameters.listR.append(resistorTemp)

		#print '\t',resistorTemp.port1,'\t',resistorTemp.port2,'\t'
		#print resistorTemp.port1,'  ',1/value,' \t',-1/value
		#print resistorTemp.port2,'  ',-1/value,' \t',1/value
		#print ''

		return resistorTemp
	
	return ''