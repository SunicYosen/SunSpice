#!/usr/bin/python3
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from Models.Inductor.InductorClass import Inductor
from Functions.addNode import addNode
from Functions.string2num import string2num

import parameters

def parseInductor(IndString = ''):
	IndParaList = IndString.split(' ')
	if len(IndParaList) > 4:
		print('----ERROR: More parameters than expected!')
		return '----False'
	
	elif len(IndParaList) < 4:
		print('----ERROR: Less parameters than expected!')
		return '----False'
	
	else :
		InductorTemp = Inductor()
		InductorTemp.name = IndParaList[0]
		InductorTemp.port1 = IndParaList[1]
		InductorTemp.port2 = IndParaList[2]
		InductorTemp.value = IndParaList[3]

		addNode(InductorTemp.port1)
		addNode(InductorTemp.port2)
		parameters.listL.append(InductorTemp)
		
		value = string2num(InductorTemp.value)
		#print("--AC stamp")
		#print('\t|',InductorTemp.port1,'\t|',InductorTemp.port2, '\t| I', '\t\t| RHS')
		#print(InductorTemp.port1,'\t|',0,'\t|',0,'\t|',1,'\t\t|',0)
		#print(InductorTemp.port2,'\t|',0,'\t|',0,'\t|',-1,'\t\t|',0)
		#print('branch','\t|',1,'\t|',-1,'\t|',-1*value,'s','\t|',0)
		#rint ''

		#print('\t',InductorTemp.port1,'\t',InductorTemp.port2,'\t')
		#print(InductorTemp.port1,'  ',1/value,' \t',-1/value)
		#print(InductorTemp.port2,'  ',-1/value,' \t',1/value)
		#print('')

		return InductorTemp

	return ''