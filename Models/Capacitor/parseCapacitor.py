#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

import parameters
from CapacitorClass import Capacitor
from Functions.addNode import addNode
from Functions.string2num import string2num

def parseC(capString = ''):
	capParaList = capString.split(' ')
	if len(capParaList) > 4:
		print 'ERROR: More parameters than expected!'
		exit()
		#return '----False'
	
	elif len(capParaList) < 4:
		print 'ERROR: Less parameters than expected!'
		exit()
		#return '----False'
	
	else :
		capacitorTemp = Capacitor()
		capacitorTemp.name = capParaList[0]
		capacitorTemp.port1 = capParaList[1]
		capacitorTemp.port2 = capParaList[2]
		capacitorTemp.value = capParaList[3]

		addNode(capacitorTemp.port1)
		addNode(capacitorTemp.port2)
		parameters.listC.append(capacitorTemp)

		#value = string2num(capacitorTemp.value)
		#print "--AC stamp"
		#print '\t|',capacitorTemp.port1,'\t\t|',capacitorTemp.port2, '\t\t| RHS'
		#print capacitorTemp.port1,'\t|',value,'s','\t|',-1*value,'s','\t|',0
		#print capacitorTemp.port2,'\t|',-1*value,'s','\t|',value,'s','\t|',0
		#print ''

		#print '\t',capacitorTemp.port1,'\t',capacitorTemp.port2,'\t'
		#print capacitorTemp.port1,'  ',1/value,' \t',-1/value
		#print capacitorTemp.port2,'  ',-1/value,' \t',1/value
		#print ''	

		#return capacitorTemp

	#return ''
