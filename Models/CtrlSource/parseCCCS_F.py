#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from CtrlSourceClass import cccs

from Functions.addNode import addNode
from Functions.string2num import string2num

import parameters

def parseCCCS_F(stringCCCS = ''):
	CCCSList = stringCCCS.split()
	if len(CCCSList) > 6:
		print "Error! More parameters than expected!"
	elif len(CCCSList) < 6:
		print "Error! Less parameters than expected!"
	else :
		cccsTemp = cccs()
		cccsTemp.name = CCCSList[0]
		cccsTemp.portPos = CCCSList[1]
		cccsTemp.portNeg = CCCSList[2]
		cccsTemp.ctlNodePos = CCCSList[3]
		cccsTemp.ctlNodeNeg = CCCSList[4]
		cccsTemp.currentGain = CCCSList[5]

		addNode(cccsTemp.portPos)
		addNode(cccsTemp.portNeg)
		parameters.listF.append(cccsTemp)

		#FkValue = string2num(cccsTemp.currentGain)

		#print '\t',cccsTemp.portPos,'\t',cccsTemp.portNeg,'\t',cccsTemp.ctlNodePos,'\t',cccsTemp.ctlNodeNeg,'\t','i'
		#print cccsTemp.portPos,'\t',0,'\t',0,'\t',0,'\t',0,'\t',FkValue
		#print cccsTemp.portNeg,'\t',0,'\t',0,'\t',0,'\t',0,'\t',-1*FkValue
		#print cccsTemp.ctlNodePos,'\t',0,'\t',0,'\t',0,'\t',0,'\t',1
		#print cccsTemp.ctlNodeNeg,'\t',0,'\t',0,'\t',0,'\t',0,'\t',-1
		#print 'br\t',0,'\t',0,'\t',1,'\t',-1,'\t',0