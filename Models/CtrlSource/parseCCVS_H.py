#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from CtrlSourceClass import ccvs

from Functions.addNode import addNode
from Functions.string2num import string2num

import parameters

def parseCCVS_H(stringCCVS = ''):
	CCVSList = stringCCVS.split()
	if len(CCVSList) > 6:
		print "Error! More parameters than expected!"
	elif len(CCVSList) < 6:
		print "Error! Less parameters than expected!"
	else :
		ccvsTemp = ccvs()
		ccvsTemp.name = CCVSList[0]
		ccvsTemp.portPos = CCVSList[1]
		ccvsTemp.portNeg = CCVSList[2]
		ccvsTemp.ctlNodePos = CCVSList[3]
		ccvsTemp.ctlNodeNeg = CCVSList[4]
		ccvsTemp.transResValue = CCVSList[5]

		addNode(ccvsTemp.portPos)
		addNode(ccvsTemp.portNeg)
		parameters.listH.append(ccvsTemp)

		#HkValue = string2num(ccvsTemp.transResValue)
		#print '\t',ccvsTemp.portPos,'\t',ccvsTemp.portNeg,'\t',ccvsTemp.ctlNodePos,'\t',ccvsTemp.ctlNodeNeg,'\t','Ik','\t','Ic'
		#print ccvsTemp.portPos,'\t',0,'\t',0,'\t',0,'\t',0,'\t',1,'\t',0
		#print ccvsTemp.portNeg,'\t',0,'\t',0,'\t',0,'\t',0,'\t',-1,'\t',0
		#print ccvsTemp.ctlNodePos,'\t',0,'\t',0,'\t',0,'\t',0,'\t',0,'\t',1
		#print ccvsTemp.ctlNodeNeg,'\t',0,'\t',0,'\t',0,'\t',0,'\t',0,'\t',-1
		#print 'br-vs\t',1,'\t',-1,'\t',0,'\t',0,'\t',0,'\t',-1*HkValue
		#print 'br-cc\t',0,'\t',0,'\t',1,'\t',-1,'\t',0,'\t',0