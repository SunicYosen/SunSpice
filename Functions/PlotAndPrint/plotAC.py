#!/usr/bin/python3
# -*- encoding="UTF-8" -*-
import os
import sys
sys.path.append("../..")

import matplotlib.pyplot as plt

import parameters
from math import sqrt
from math import atan


def plotAC():
    ResultPath =  parameters.NetlistPath+'.ac'
    if not os.access(ResultPath,os.F_OK):
        print( "Warning: No AC Simulation Data!")
        return
    else:
        print( 'Info: Plot AC ...')
        XValue = []
        XLabel = ''

        fileResult = open(ResultPath,'r')
        listFigure = []
        listFigureEXP = []      #The Expressions of Figure Y expressions
        figureYLabel = []       #All Figures
        AllFigureYlabel = []

        print( "Info: --Reading Data ...")
        print( 'Info: File Title:',fileResult.readline())

        StringTitle = fileResult.readline()
        StringTitle = StringTitle.strip()
        listTitle = StringTitle.split('\t')

        XLabel = 'Frequency (Hz)'

        DictTitle = {'v_0':0}
        for index in range(len(listTitle)):
            value = listTitle[index]
            DictTitle[value] = index+1

        for index in range(len(parameters.listPlotAC)):
            listFigure.append([])           #Addr One Figure
            listYValueAddr = []         #list Y Expresses of one Figure
            Ylabel = []                 #list Y label of one Figure

            if parameters.listPlotAC[index].typeDC == 'v':
                figureYLabel.append('U (v)')
                
                for VoltageExp in parameters.listPlotAC[index].VoltageExps:    #One Figure
                    listFigure[index].append([[],[]])        #Add one Value in Figure index

                    portPos = VoltageExp.portPos 
                    portNeg = VoltageExp.portNeg
                    

                    listOneY = []          #List of One Y

                    Ylabel.append('V(' + portPos + ',' + portNeg + ')')

                    if 'v_'+portPos in DictTitle:
                        portPosAddr = DictTitle.get('v_'+portPos)
                    else:
                        print( "Error: No port Named: ",portPos)
                        return 
                    
                    if 'v_'+portNeg in DictTitle:
                        portNegAddr = DictTitle.get('v_'+portNeg)
                    else:
                        print( "Error: No port Named: ",portNeg)
                        return

                    listOneY.append(portPosAddr)
                    listOneY.append(portNegAddr)
                    listYValueAddr.append(listOneY)
            
            elif parameters.listPlotAC[index].typeDC == 'i':
                figureYLabel.append('I (A)')
                listYValueAddr = []          #list Y Expresses of one Figure
                
                for CurrentExp in parameters.listPlotAC[index].CurrentDeviceName:
                    listFigure[index].append([[],[]])        #Add one Value in Figure index
                    DeviceName = CurrentExp
                    listOneY = []
                    Ylabel.append('I(' + DeviceName + ')')

                    listOneY.append(DictTitle.get('i_'+DeviceName))
                    listYValueAddr.append(listOneY)
            
            else:
                print( "Error: Unknow Type",parameters.listPlotAC[index].typeDC)

            listFigureEXP.append(listYValueAddr)
            AllFigureYlabel.append(Ylabel)
            

        for index in fileResult:
            listValue = index.strip().split('\t')

            if len(listValue) != 0:
                XValue.append(float(listValue[0]))

                for ValueYOneFigure in range(len(listFigureEXP)):
                    OneFigureExp = listFigureEXP[ValueYOneFigure]
                    for ValueY in range(len(OneFigureExp)):
                        OneValueYExp = OneFigureExp[ValueY]

                        addValue = 0.0
                        if len(OneValueYExp) == 0:
                            addValue = 0.0

                        elif len(OneValueYExp) == 1:
                            if OneValueYExp[0] == 0:
                                addValue = 0.0
                            else:
                                addValue = complex(listValue[OneValueYExp[0] - 1])
                        
                        elif len(OneValueYExp) == 2:
                            if (OneValueYExp[0] == 0) & (OneValueYExp[1] == 0):
                                addValue = 0.0
                            elif (OneValueYExp[0] == 0) & (OneValueYExp[1] != 0):
                                addValue = 0 - complex(listValue[OneValueYExp[1] - 1])
                            elif (OneValueYExp[0] != 0) & (OneValueYExp[1] == 0):
                                addValue = complex(listValue[OneValueYExp[0] - 1])

                            else:
                                addValue = complex(listValue[OneValueYExp[0] - 1]) - complex(listValue[OneValueYExp[1] - 1])
                        else:
                            print( "Error: Unknown ValueY.More Than 2 NUM")

                        Real = addValue.real
                        Imag = addValue.imag

                        Phase = atan(Imag/Real) * 360 / 3.14
                        Margin = sqrt(Real*Real + Imag * Imag)
                        
                        listFigure[ValueYOneFigure][ValueY][0].append(Margin)
                        listFigure[ValueYOneFigure][ValueY][1].append(Phase)

        for index in range(len(listFigure)):
            OneFigureValue = listFigure[index]
            plt.figure('AC Plot'+ str(index))
            pindexM = plt.subplot(211)
            pindexM.set_title("AC Simulation Plot")
            #pindexM.set_xlabel(XLabel,fontsize=14)
            pindexM.set_ylabel(figureYLabel[index] + ' Margin',fontsize=14)
            pindexM.grid(True)

            pindexP = plt.subplot(212)
            #pindexP.set_title("AC Simulation Plot")
            pindexP.set_xlabel(XLabel,fontsize=14)
            pindexP.set_ylabel(figureYLabel[index] + 'Phase',fontsize=14)
            pindexP.grid(True)

            for oneY in range(len(OneFigureValue)):
                OneValueY = OneFigureValue[oneY]
                YlabelOneY = AllFigureYlabel[index][oneY]  
                pindexM.semilogx(XValue,OneValueY[0],label=YlabelOneY)
                pindexP.semilogx(XValue,OneValueY[1],label=YlabelOneY)
                pindexM.legend()
                pindexP.legend()
        
        fileResult.close()
        
