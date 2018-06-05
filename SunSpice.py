#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

#
#Function: hspice-like
#Python Version: Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
#Date:  Mar 2018
#Autor: Sun Yongshuai
#

#Import Package
import sys
import os
import multiprocessing
import matplotlib.pyplot as plt

import parameters
from Functions.readFile import readFile

from Functions.SimulationType.DC import DCSimulation
from Functions.SimulationType.AC import ACSimulation
from Functions.SimulationType.Tran import TranSimulation
from Functions.SimulationType.OP import OpSimulation

from Functions.helpGuide import helpGuide
from Functions.PlotAndPrint.plotDC import plotDC
from Functions.PlotAndPrint.plotTran import plotTran
from Functions.PlotAndPrint.plotAC import plotAC

def main(args):
	if (len(args) == 1):
		helpGuide(args)
		
	elif (not os.access(args[1],os.F_OK)):
		helpGuide(args)

	else:
		parameters.NetlistPath = args[1]
		print parameters.NetlistPath
		readFile()

		OpSimulation()
		#DCSimulation()
		#ACSimulation()
		#TranSimulation()

		#plotDC()
		#plotAC()
		#plotTran()

		#plt.show()

if __name__ == '__main__':
	main(sys.argv)
	
