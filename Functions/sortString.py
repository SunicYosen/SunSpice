#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-
import sys
sys.path.append("..")

import re
import parameters
from Models.Resistor.parseResistor import parseR
from Models.Capacitor.parseCapacitor import parseC
from Models.Inductor.parseInductor import parseInductor
from Models.Diode.parseDiode import parseDiode
from Models.Mosfet.parseMosfet import parseMosfet

from Models.Power.parsePower import parsePower
from Models.Current.parseCurrent import parseIs
from Models.CtrlSource.parseVCVS_E import parseVCVS_E
from Models.CtrlSource.parseCCCS_F import parseCCCS_F
from Models.CtrlSource.parseVCCS_G import parseVCCS_G
from Models.CtrlSource.parseCCVS_H import parseCCVS_H

from Functions.parseCommand.parseCommand import parseCommand


def sortString(countLine = 0,index = ''):
	index = index.strip().lower().replace(r' gnd ',' 0 ')

	if re.match(parameters.regExpComment,index):	#Comment
		pass
		#print 'Info:' ,countLine, 'line is comment line!'
		
	elif re.match(parameters.regExpCommand,index): #Command
		print 'Info:' , countLine, 'line is command line!'
		parseCommand(index)
		
	elif re.match(parameters.regExpC,index):	#C
		print 'Info:' ,countLine,'line is Cap!'
		parseC(index)
	
	elif re.match(parameters.regExpR,index):	#R
		print 'Info:' ,countLine, 'line is Reg' 
		parseR(index)

	elif re.match(parameters.regExpL,index):	#L
		print 'Info:' ,countLine, 'line is L'
		parseInductor(index)
	
	elif re.match(parameters.regExpV,index): 	#Vs
		print 'Info:' ,countLine, 'line is V'
		parsePower(index)
	
	elif re.match(parameters.regExpI,index):	#Is
		print 'Info:' ,countLine, 'line is I'
		parseIs(index)

	elif re.match(parameters.regExpMos,index):	#MosFet
		print 'Info:' ,countLine, 'line is Mosfet'
		parseMosfet(index)
		
	elif re.match(parameters.regExpExtend,index):   #Woludn't Here
		print 'Info:' ,countLine, 'line is Extend!'

	elif re.match(parameters.regExpVCVS,index):   #E
		print 'Info:' ,countLine, 'VCVS'
		parseVCVS_E(index)

	elif re.match(parameters.regExpCCCS,index):   #F
		print 'Info:' ,countLine, 'CCCS'
		parseCCCS_F(index)

	elif re.match(parameters.regExpVCCS,index):    #G
		print 'Info:' ,countLine, 'VCCS'
		parseVCCS_G(index)

	elif re.match(parameters.regExpCCVS,index):		#H
		print 'Info:' ,countLine, 'CCVS'
		parseCCVS_H(index)

	elif re.match(parameters.regExpD,index):		#Diode
		print 'Info:' ,countLine,'Diode'
		parseDiode(index)

	elif index == '':
		pass

	else :
		 print countLine,'line Error!'