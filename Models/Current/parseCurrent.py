#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from CurrentClass import DCCurrent

from Functions.addNode import addNode
from Functions.string2num import string2num

import parameters

def parseIs(IsString = ''):
	IsParaList = IsString.split(' ')
	if len(IsParaList) > 4:
		print '----ERROR: More parameters than expected!'
		return '----False'
	
	elif len(IsParaList) < 4:
		print '----ERROR: Less parameters than expected!'
		return '----False'
	
	else :
		IsTemp = DCCurrent()
		IsTemp.name = IsParaList[0]
		IsTemp.portPos = IsParaList[1]
		IsTemp.portNeg = IsParaList[2]
		IsTemp.value = IsParaList[3]

		value = string2num(IsTemp.value)

		addNode(IsTemp.portPos)
		addNode(IsTemp.portNeg)
		parameters.listDCI.append(IsTemp)
		
		print '\t RHS'
		print IsTemp.portPos,'\t',-1*value
		print IsTemp.portNeg,'\t',value
		print ''

		return IsTemp

	return ''
