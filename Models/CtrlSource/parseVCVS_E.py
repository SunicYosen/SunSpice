#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from CtrlSourceClass import vcvs

from Functions.addNode import addNode
from Functions.string2num import string2num

import parameters

def parseVCVS_E(stringVCVS = ''):
	VCVSList = stringVCVS.split()
	if len(VCVSList) > 6:
		print "Error! More parameters than expected!"
	elif len(VCVSList) < 6:
		print "Error! Less parameters than expected!"
	else :
		vcvsTemp = vcvs()
		vcvsTemp.name = VCVSList[0]
		vcvsTemp.portPos = VCVSList[1]
		vcvsTemp.portNeg = VCVSList[2]
		vcvsTemp.ctlNodePos = VCVSList[3]
		vcvsTemp.ctlNodeNeg = VCVSList[4]
		vcvsTemp.voltageGain = VCVSList[5]

		addNode(vcvsTemp.portPos)
		addNode(vcvsTemp.portNeg)
		parameters.listE.append(vcvsTemp)

		#EkValue = string2num(vcvsTemp.voltageGain)

		#print '\t',vcvsTemp.portPos,'\t',vcvsTemp.portNeg,'\t',vcvsTemp.ctlNodePos,'\t',vcvsTemp.ctlNodeNeg,'\t','i'
		#print vcvsTemp.portPos,'\t',0,'\t',0,'\t',0,'\t',0,'\t',1
		#print vcvsTemp.portNeg,'\t',0,'\t',0,'\t',0,'\t',0,'\t',-1
		#print vcvsTemp.ctlNodePos,'\t',0,'\t',0,'\t',0,'\t',0,'\t',0
		#print vcvsTemp.ctlNodeNeg,'\t',0,'\t',0,'\t',0,'\t',0,'\t',0
		#print 'br\t',1,'\t',-1,'\t',-1*EkValue,'\t',EkValue,'\t',0
