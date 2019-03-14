#!/usr/bin/python3
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("..")

import re
import parameters

def string2num(stringNum = ''):                                      #string to float with unit & sci num
	stringNum = stringNum.lower()

	if re.match(parameters.FloatWithUnit,stringNum):
		numWithoutUnit = float(re.findall(parameters.FloatWithoutUnit,stringNum)[0])
		numUnit = re.findall(parameters.FolatUnit,stringNum)[0]

		uintNum = {
			''   : numWithoutUnit,
			'meg': numWithoutUnit * (10**6),
			'f'  : numWithoutUnit * (10**(-15)),
			'p'  : numWithoutUnit * (10**(-12)),
			'n'  : numWithoutUnit * (10**(-9)),
			'u'  : numWithoutUnit * (10**(-6)),
			'm'  : numWithoutUnit * (10**(-3)),
			'k'  : numWithoutUnit * (10**(3)),
			'g'  : numWithoutUnit * (10**(9)),
			't'  : numWithoutUnit * (10**(12))
			#'db' : 20 * math.log(numWithoutUnit) / math.log(10)
		}

		numFloat = uintNum.get(numUnit,numWithoutUnit)

		return numFloat

	elif re.match(parameters.SciNum,stringNum):
		#SciNumList = stringNum.split('e')
		#return float(SciNumList[0]) * (10 ** int(SciNumList[1]))
		return float(stringNum)
	
	elif stringNum in parameters.ParamDict:
		NumValue = float(parameters.ParamDict.get(stringNum))
		return NumValue
		
	else:
		print( "Error NUM:", stringNum)
		exit()