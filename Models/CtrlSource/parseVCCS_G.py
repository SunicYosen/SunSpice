#!/usr/bin/python3
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from Models.CtrlSource.CtrlSourceClass import vccs

from Functions.addNode import addNode
from Functions.string2num import string2num

import parameters

def parseVCCS_G(stringVCCS = ''):
	VCCSList = stringVCCS.split()
	if len(VCCSList) > 6:
		print("Error! More parameters than expected!")
	elif len(VCCSList) < 6:
		print("Error! Less parameters than expected!")

	else:
		vccsTemp = vccs()
		vccsTemp.name = VCCSList[0]
		vccsTemp.portPos = VCCSList[1]
		vccsTemp.portNeg = VCCSList[2]
		vccsTemp.ctlNodePos = VCCSList[3]
		vccsTemp.ctlNodeNeg = VCCSList[4]
		vccsTemp.transconValue = VCCSList[5]

		addNode(vccsTemp.portPos)
		addNode(vccsTemp.portNeg)
		parameters.listG.append(vccsTemp)

		#value = string2num(vccsTemp.transconValue)

		#print('\t',vccsTemp.ctlNodePos,'\t',vccsTemp.ctlNodeNeg)
		#print(vccsTemp.portPos,'\t',value,'\t',value*(-1))
		#print(vccsTemp.portNeg,'\t',value*(-1),'\t',value)
		#print('')