#!/usr/bin/python3
# -*- encoding="UTF-8" -*-
#parameters

listR = []					#
listC = []
listL = []
listM = []
listE = []
listF = []
listG = []
listH = []
listD = []
listDCV = []
listSinV = []
listPulseV = []
listACV = []
listDCI = []
listSinI = []
listDCParam = []
listACParam = []
listTranParam = []
listPlotDC = []
listPlotAC = []
listPlotTran = []
opExp = []
opValue = []
opValueString = ''
opExpString = ''

NodesDict = {                  #Dictionary of Nodes
	'0':0
}
ParamDict = {
	'GND':0
}

STEP = '10p'					#STEP
GND = 0							#define GND port is 0

NetlistPath = '/home/sun/Files/AutoDesign/Projects/src/TestCircuits'      #The netlist file path and name

regExpV = r'^v'				#V
regExpI = r'^i'             #I
regExpR = r'^r'				#R
regExpC = r'^c'				#C
regExpL = r'^l'				#L
regExpMos = r'^m'			#Mosfet
regExpD = r'^d'				#Diode
regExpVCVS = r'^e'          #VCVS
regExpCCCS = r'^f'          #CCCS
regExpVCCS = r'^g'          #VCCS
regExpCCVS = r'^h'         	#CCVS

regExpComment = r'^\*'			#Comment line
regExpExtend = r'^\+'			#Extend

regExpCommand = r'^\.'					#Command line
regExpCommandDC = r'^\.dc'				#DC 
regExpCommandAC = r'^\.ac'				#AC
regExpCommandTran = r'^\.tran'			#Tran
regExpCommandPrint = r'^\.print'		#print
regExpCommandPlot = r'^\.plot'			#Plot
regExpCommandEnd = r'^\.end$'			#END

regExpCommandOptions = r'^\.options'	#Option
regExpCommandOp = r'^\.op'				#OP
regExpCommandParam = r'^\.param'		#Param
regExpCommandLib = r'^\.lib'			#lib

FloatWithUnit = r'^[-+]?[0-9]*\.?[0-9]+\s?[fpnumkgt]?e?g?$'    #Float with unit
FloatWithoutUnit = r'^[-+]?[0-9]*\.?[0-9]+'                    #Float without unit
FolatUnit = r'[fpnumkgt]?e?g?$'                                #Float unit  
SciNum = r'^[-+]?[1-9]\.?[0-9]*e?[-+]?[0-9]+$'				   #Sci Num

regExpPlotV = r'^v\((.+)\)$'
regExpPlotI = r'^i\((.+)\)$'

#MosFet