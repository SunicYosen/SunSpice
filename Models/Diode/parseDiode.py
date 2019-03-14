#!/usr/bin/python3
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from Models.Diode.DiodeClass import Diode

from Functions.addNode import addNode
from Functions.string2num import string2num

import parameters

def parseDiode(stringDiode = ''):
	DiodeList = stringDiode.split()
	if len(DiodeList) > 6:
		print("****Error! More parameters than EXPECTED!")
	elif len(DiodeList) < 6:
		print("****Error! Less parameters than EXPECTED!")
	else:
		DiodeTemp = Diode()
		DiodeTemp.name = DiodeList[0]
		DiodeTemp.port1 = DiodeList[1]
		DiodeTemp.port2 = DiodeList[2]
		DiodeTemp.Model = DiodeList[3]
		ITemp = 4
		while ITemp < len(DiodeList):
			if '=' in DiodeList[ITemp]:
				DiodeValTemp = DiodeList[ITemp].split('=')
				if DiodeValTemp[0] == 'is':
					DiodeTemp.Isat = DiodeValTemp[1]
				elif DiodeValTemp[0] == 'alpha':
					DiodeTemp.Alpha = DiodeValTemp[1]
				else :
					print("****Error! Unknow parameter NAME",DiodeValTemp[0])
				ITemp = ITemp + 1
			else:
				print("****Error! Unknow parameter NAME",DiodeList[ITemp])
				exit()
				
		parameters.listD.append(DiodeTemp)
		addNode(DiodeTemp.port1)
		addNode(DiodeTemp.port2)
		return DiodeTemp
