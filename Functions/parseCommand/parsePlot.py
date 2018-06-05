#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-
import sys
sys.path.append("../..")
import re

import parameters
from parameters import regExpPlotV
from parameters import regExpPlotI
from Functions.string2num import string2num

class VoltageExp:
    portPos = ''
    portNeg = ''
    
    def __init__(self):
        self.portPos = '0'
        self.portNeg = '0'



class plotDCParam:
    typeDC = ''
    VoltageExps = []
    CurrentDeviceName = []          

    def __init__(self):
        self.typeDC = ''            #Voltage or Current
        self.VoltageExps = []       #Voltage List
        self.CurrentDeviceName = [] #Current Plot

def parsePlot(PlotString = ''):
    PlotString = PlotString.lower().replace('.plot ','').strip()
    listPlotParam = PlotString.split(' ')

    if listPlotParam[0] == 'ac':
        print 'Info: AC Plot'
        plotNum = len(listPlotParam)-1

        if plotNum <= 1 :
            print 'Warning: No AC Plot'
        
        else:
            plotACParam_v = plotDCParam()
            plotACParam_i = plotDCParam()

            plotACParam_v.typeDC = 'v'
            plotACParam_i.typeDC = 'i'

            flag_v = False
            flag_i = False

            for index in range(plotNum):
                if re.match(regExpPlotV,listPlotParam[index+1]):        #Plot V
                    flag_v = True
                    VoltageExpTemp = VoltageExp()                   #Define VoltageExp
                    VoltageExpStr = listPlotParam[index+1].replace('v(','').replace(')','').strip() #remove
                    if ',' in VoltageExpStr:
                        VoltageExpList = VoltageExpStr.split(',')
                        if len(VoltageExpList) != 2:
                            print 'Error: Error Plot Voltage Expression: ',listPlotParam[index+1]
                        else:
                            VoltageExpTemp.portPos = VoltageExpList[0]
                            VoltageExpTemp.portNeg = VoltageExpList[1]
                    else:
                        VoltageExpTemp.portPos = VoltageExpStr

                    plotACParam_v.VoltageExps.append(VoltageExpTemp)

                elif re.match(regExpPlotI,listPlotParam[index+1]):
                    flag_i = True
                    CurrentDeviceNameTemp = listPlotParam[index+1].replace('i(','').replace(')','').strip() #remove
                    plotACParam_i.CurrentDeviceName.append(CurrentDeviceNameTemp)
                
                else:
                    print "Error: Unkown AC Plot Type(Voltage or Current)"
                    exit()

            if flag_v:
                parameters.listPlotAC.append(plotACParam_v)

            if flag_i:
                parameters.listPlotAC.append(plotACParam_i)


    elif listPlotParam[0] == 'dc':
        print 'Info: DC Plot'
        plotNum = len(listPlotParam) - 1

        if plotNum <= 0:
            print 'Warning: No DC plot!'
        
        else:
            plotDCParam_v = plotDCParam()
            plotDCParam_i = plotDCParam()

            plotDCParam_v.typeDC = 'v'
            plotDCParam_i.typeDC = 'i'

            flag_v = False
            flag_i = False
            
            for index in range(plotNum):
                if re.match(regExpPlotV,listPlotParam[index+1]):        #Plot V
                    flag_v = True
                    VoltageExpTemp = VoltageExp()                   #Define VoltageExp
                    VoltageExpStr = listPlotParam[index+1].replace('v(','').replace(')','').strip() #remove
                    if ',' in VoltageExpStr:
                        VoltageExpList = VoltageExpStr.split(',')
                        if len(VoltageExpList) != 2:
                            print 'Error: Error Plot Voltage Expression: ',listPlotParam[index+1]
                        else:
                            VoltageExpTemp.portPos = VoltageExpList[0]
                            VoltageExpTemp.portNeg = VoltageExpList[1]
                    else:
                        VoltageExpTemp.portPos = VoltageExpStr

                    plotDCParam_v.VoltageExps.append(VoltageExpTemp)

                elif re.match(regExpPlotI,listPlotParam[index+1]):
                    flag_i = True
                    CurrentDeviceNameTemp = listPlotParam[index+1].replace('i(','').replace(')','').strip() #remove
                    plotDCParam_i.CurrentDeviceName.append(CurrentDeviceNameTemp)
                
                else:
                    print "Error: Unkown DC Plot Type(Voltage or Current)"
                    exit()

            if flag_v:
                parameters.listPlotDC.append(plotDCParam_v)

            if flag_i:
                parameters.listPlotDC.append(plotDCParam_i)
                    
    elif listPlotParam[0] == 'tran':
        print 'Info: Tran Plot'
        plotNum = len(listPlotParam) - 1

        if plotNum <= 0:
            print 'Warning: No Tran plot!'
        
        else:
            plotTranParam_v = plotDCParam()
            plotTranParam_i = plotDCParam()

            plotTranParam_v.typeDC = 'v'
            plotTranParam_i.typeDC = 'i'

            flag_v = False
            flag_i = False
            
            for index in range(plotNum):
                if re.match(regExpPlotV,listPlotParam[index+1]):        #Plot V
                    flag_v = True
                    VoltageExpTemp = VoltageExp()                   #Define VoltageExp
                    VoltageExpStr = listPlotParam[index+1].replace('v(','').replace(')','').strip() #remove
                    if ',' in VoltageExpStr:
                        VoltageExpList = VoltageExpStr.split(',')
                        if len(VoltageExpList) != 2:
                            print 'Error: Error Plot Voltage Expression: ',listPlotParam[index+1]
                        else:
                            VoltageExpTemp.portPos = VoltageExpList[0]
                            VoltageExpTemp.portNeg = VoltageExpList[1]
                    else:
                        VoltageExpTemp.portPos = VoltageExpStr

                    plotTranParam_v.VoltageExps.append(VoltageExpTemp)

                elif re.match(regExpPlotI,listPlotParam[index+1]):
                    flag_i = True
                    CurrentDeviceNameTemp = listPlotParam[index+1].replace('i(','').replace(')','').strip() #remove
                    plotTranParam_i.CurrentDeviceName.append(CurrentDeviceNameTemp)
                
                else:
                    print "Error: Unkown DC Plot Type(Voltage or Current)"
                    exit()

            if flag_v:
                parameters.listPlotTran.append(plotTranParam_v)

            if flag_i:
                parameters.listPlotTran.append(plotTranParam_i)

    else:
        print 'Error: Unkown Simlation Type!',listPlotParam[0]
    