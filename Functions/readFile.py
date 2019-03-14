#!/usr/bin/python3
# -*- encoding="UTF-8" -*-

#Import Package
import sys
sys.path.append("..")

import re
from tkinter.messagebox import *

import parameters
#Dont use from parameters import NetlistPath, it Will be import ealier than Changed

from parameters import regExpExtend
from parameters import regExpCommandEnd
from Functions.sortString import sortString


def readFile():

	inputNetlist = open(parameters.NetlistPath,'r')
	countLine = 1

	index = inputNetlist.readline()        #Read the Netlist
	if not index:
		print("Error! Line: ",countLine)
		exit()
	
	print('The Title is: \t' + index)     #Print The Title (First Line)
	print("------------------------------------")
	print("Info: Read File ...")

	line = inputNetlist.readline()
	if not line:
		print('Error: No Circuit!')
		exit()

	countLine = countLine + 1
	
	while 1:
		if re.match(regExpCommandEnd,line.strip().lower()):    # END 
			print('Info: ---Read File END!---')
			break

		if not line:
			print('Waring: Short of END line! Try to IGNORE this and Continue!\t...')
			break

		CompleteLine = line.strip().lower()

		line = inputNetlist.readline()
		countLine = countLine + 1
		countTemp = 0

		while re.match(regExpExtend,line.strip().lower()):
			CompleteLine = CompleteLine + line.strip().lower().replace('+ ',' ').replace('gnd','0')
			line = inputNetlist.readline() 
			countTemp = countTemp + 1

		sortString(countLine-1,CompleteLine)
		countLine = countLine + countTemp
    
	print("Info: Sort String end!")
	print("------------------------------------\n")
	inputNetlist.close()
	showinfo('Parse','Parse End!')
