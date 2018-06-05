#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from MosfetClass import Mosfet

from Functions.addNode import addNode
from Functions.string2num import string2num

import parameters

def parseMosfet(mosString = ''):
	mosParaList = mosString.split(' ')
	if len(mosParaList) > 8:
		print 'ERROR: More parameters than expected!'
		exit()
	
	elif len(mosParaList) < 8:
		print 'ERROR: Less parameters than expected!'
		exit()
	
	else:
		MosfetTemp = Mosfet()
		MosfetTemp.name = mosParaList[0]
		MosfetTemp.portD = mosParaList[1]
		MosfetTemp.portG = mosParaList[2]
		MosfetTemp.portS = mosParaList[3]
		MosfetTemp.portB = mosParaList[4]
		MosfetTemp.valueL = mosParaList[6].split('=')[1]
		MosfetTemp.valueW = mosParaList[7].split('=')[1]

		addNode(MosfetTemp.portB)
		addNode(MosfetTemp.portD)
		addNode(MosfetTemp.portG)
		addNode(MosfetTemp.portS)

		if mosParaList[5] == 'nmos':
			MosfetTemp.MosType = 'nmos'
			print 'Info: --Type: nmos'

		elif mosParaList[5] == 'pmos':
			MosfetTemp.MosType = 'pmos'
			print 'Info: --Type: pmos'
		
		else :
			print 'Error: Error mosfet TYPE!',mosParaList[5]
			exit()

		parameters.listM.append(MosfetTemp)