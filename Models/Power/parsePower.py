#!/usr/bin/python3
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("../..")

from Models.Power.PowerClass import DCPower,ACPower,SinPower,PlusePower

from Functions.addNode import addNode
from Functions.string2num import string2num
import parameters

def parsePower(powString = ''):
	powParaList = powString.split(' ')

	if len(powParaList) < 4:
		print('----ERROR: Less parameters than expected!')
		return '----False'
	
	elif 'sin' in powParaList:
		SinPowerTemp = SinPower()
		SinPowerTemp.name = powParaList[0]
		SinPowerTemp.portPos = powParaList[1]
		SinPowerTemp.portNeg = powParaList[2]

		addrTemp = 4
		while addrTemp < len(powParaList):
			if '=' in powParaList[addrTemp]:
				paraTempList = powParaList[addrTemp].split('=')
				if paraTempList[0] == 'a':
					SinPowerTemp.A = paraTempList[1]
				elif paraTempList[0] == 'w':
					SinPowerTemp.w = paraTempList[1]
				elif paraTempList[0] == 'phi':
					SinPowerTemp.phi = paraTempList[1]
				elif paraTempList[0] == 'vo':
					SinPowerTemp.Vo = paraTempList[1]
				else:
					print("****Error! Unknow parameter : ",paraTempList[0])

			else:
				if addrTemp == 4 :
					SinPowerTemp.A = powParaList[addrTemp]
				elif addrTemp == 5:
					SinPowerTemp.w = powParaList[addrTemp]
				elif addrTemp == 6:
					SinPowerTemp.phi = powParaList[addrTemp]
				elif addrTemp == 7:
					SinPowerTemp.Vo = powParaList[addrTemp]
				else:
					print(powParaList[addrTemp],"is Unexpected! It will be Ignored!")
					pass
			
			addrTemp = addrTemp + 1
		
		addNode(SinPowerTemp.portPos)
		addNode(SinPowerTemp.portNeg)
		parameters.listSinV.append(SinPowerTemp)

	elif 'pluse' in powParaList:
		plusePowerTemp = PlusePower()
		plusePowerTemp.name = powParaList[0]
		plusePowerTemp.portPos = powParaList[1]
		plusePowerTemp.portNeg = powParaList[2]

		addrTemp = 4

		while addrTemp < len(powParaList):
			if '=' in powParaList[addrTemp]:
				paraTempList = powParaList[addrTemp].split('=')
				if paraTempList[0] == 'tdelay' | paraTempList[0] == 'td':
					plusePowerTemp.Tdelay = paraTempList[1]
				elif paraTempList[0] == 'lowv' | paraTempList[0] == 'lv':
					plusePowerTemp.LowVoltage = paraTempList[1]
				elif paraTempList[0] == 'highv' | paraTempList[0] == 'hv':
					plusePowerTemp.HighVoltage = paraTempList[1]
				elif paraTempList[0] == 'trise' | paraTempList[0] == 'tr':
					plusePowerTemp.Trise = paraTempList[1]
				elif paraTempList[0] == 'tfall' | paraTempList[0] == 'tf':
					plusePowerTemp.Tfall = paraTempList[1]
				elif paraTempList[0] == 'twide' | paraTempList[0] == 'tw':
					plusePowerTemp.Twide = paraTempList[1]
				elif paraTempList[0] == 'tperiod' | paraTempList[0] == 'tp':
					plusePowerTemp.Tperiod = paraTempList[1]
				else:
					print("****Error! Unknow parameter : ",paraTempList[0])

			else:
				if addrTemp == 4 :
					plusePowerTemp.LowVoltage = powParaList[addrTemp]
				elif addrTemp == 5:
					plusePowerTemp.HighVoltage = powParaList[addrTemp]
				elif addrTemp == 6:
					plusePowerTemp.Tdelay = powParaList[addrTemp]
				elif addrTemp == 7:
					plusePowerTemp.Trise = powParaList[addrTemp]
				elif addrTemp == 8:
					plusePowerTemp.Tfall = powParaList[addrTemp]
				elif addrTemp == 9:
					plusePowerTemp.Twide = powParaList[addrTemp]
				elif addrTemp == 10:
					plusePowerTemp.Tperiod = powParaList[addrTemp]
				else:
					print(powParaList[addrTemp],"is Unexpected! It will be Ignored!")
					pass
			
			addrTemp = addrTemp + 1
		
		addNode(plusePowerTemp.portPos)
		addNode(plusePowerTemp.portNeg)
		parameters.listPulseV.append(plusePowerTemp)
	
	elif len(powParaList) == 4:
		dcpowerTemp = DCPower()
		dcpowerTemp.name = powParaList[0]
		dcpowerTemp.portPos = powParaList[1]
		dcpowerTemp.portNeg = powParaList[2]

		if '=' in powParaList[3]:
			paraTempList = powParaList[3].split('=')
			if(paraTempList[0] == 'dc'):
				dcpowerTemp.value = paraTempList[1]
		else:
			dcpowerTemp.value = powParaList[3]

		addNode(dcpowerTemp.portPos)
		addNode(dcpowerTemp.portNeg)
		parameters.listDCV.append(dcpowerTemp)

		#value = string2num(powerTemp.value)
		#print('\t',powerTemp.portPos,'\t',powerTemp.portNeg,'\t','i','\t','RHS')
		#print(powerTemp.portPos,'\t',0,'\t',0,'\t',1,'\t',0)
		#print(powerTemp.portNeg,'\t',0,'\t',0,'\t',-1,'\t',0)
		#print('branch\t',1,'\t',-1,'\t',0,'\t',value	)
	

	else:
		print('****ERROR! Wrong expression of Power: ')
		print('      ', powString)
		return '----False'

	return ''
