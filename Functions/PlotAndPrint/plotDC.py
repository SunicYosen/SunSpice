#!/usr/bin/python3
# -*- encoding="UTF-8" -*-
import os
import sys
sys.path.append("../..")

import multiprocessing
import matplotlib.pyplot as plt

import parameters

def plotDC():
    ResultPath =  parameters.NetlistPath+'.dc'
    if not os.access(ResultPath,os.F_OK):
        print("Warning: No DC Simulation Data!")
        print('')
        return
    else:
        print('Info: Plot DC ...')
        XValue = []
        XLabel = ''

        fileResult = open(ResultPath,'r')
        listFigure = []
        listFigureEXP = []      #The Expressions of Figure Y expressions
        figureYLabel = []       #All Figures
        AllFigureYlabel = []

        print("Info: --Reading Data ...")
        print('Info: File Title:',fileResult.readline())


        StringTitle = fileResult.readline()
        StringTitle = StringTitle.strip()
        listTitle = StringTitle.split('\t')

        XLabel = listTitle[0]

        DictTitle = {'v_0':0}
        for index in range(len(listTitle)):
            value = listTitle[index]
            DictTitle[value] = index+1

        for index in range(len(parameters.listPlotDC)):
            listFigure.append([])           #Addr One Figure
            listYValueAddr = []         #list Y Expresses of one Figure
            Ylabel = []                 #list Y label of one Figure

            if parameters.listPlotDC[index].typeDC == 'v':
                figureYLabel.append('U (v)')
                
                for VoltageExp in parameters.listPlotDC[index].VoltageExps:    #One Figure
                    listFigure[index].append([])        #Add one Value in Figure index

                    portPos = VoltageExp.portPos 
                    portNeg = VoltageExp.portNeg

                    listOneY = []          #List of One Y

                    Ylabel.append('V(' + portPos + ',' + portNeg + ')')

                    if 'v_'+portPos in DictTitle:
                        portPosAddr = DictTitle.get('v_'+portPos)
                    else:
                        print("Error: No port Named: ",portPos)
                        return 
                    
                    if 'v_'+portNeg in DictTitle:
                        portNegAddr = DictTitle.get('v_'+portNeg)
                    else:
                        print( "Error: No port Named: ",portNeg)
                        return

                    listOneY.append(portPosAddr)
                    listOneY.append(portNegAddr)
                    listYValueAddr.append(listOneY)
            
            elif parameters.listPlotDC[index].typeDC == 'i':
                figureYLabel.append('I (A)')
                listYValueAddr = []          #list Y Expresses of one Figure
                
                for CurrentExp in parameters.listPlotDC[index].CurrentDeviceName:
                    listFigure[index].append([])        #Add one Value in Figure index
                    DeviceName = CurrentExp
                    listOneY = []
                    Ylabel.append('I(' + DeviceName + ')')

                    listOneY.append(DictTitle.get('i_'+DeviceName))
                    listYValueAddr.append(listOneY)
            
            else:
                print("Error: Unknow Type",parameters.listPlotDC[index].typeDC)

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
                                addValue = float(listValue[OneValueYExp[0] - 1])
                        
                        elif len(OneValueYExp) == 2:
                            if (OneValueYExp[0] == 0) & (OneValueYExp[1] == 0):
                                addValue = 0.0
                            elif (OneValueYExp[0] == 0) & (OneValueYExp[1] != 0):
                                addValue = 0 - float(listValue[OneValueYExp[1] - 1])
                            elif (OneValueYExp[0] != 0) & (OneValueYExp[1] == 0):
                                addValue = float(listValue[OneValueYExp[0] - 1])

                            else:
                                addValue = float(listValue[OneValueYExp[0] - 1]) - float(listValue[OneValueYExp[1] - 1])
                        else:
                            print("Error: Unknown ValueY.More Than 2 NUM")
                        
                        listFigure[ValueYOneFigure][ValueY].append(addValue)

        #plotDCProcess = multiprocessing.Process(target=plotDCing,args=(listFigure,figureYLabel,AllFigureYlabel,XValue,XLabel))
        #plotDCProcess.start
        #print(plotDCProcess.name)
        fileResult.close()
        plotDCing(listFigure,figureYLabel,AllFigureYlabel,XValue,XLabel)
        

def plotDCing(listFigure=[], figureYLabel=[],AllFigureYlabel=[],XValue=[], XLabel=''):
    for index in range(len(listFigure)):
        OneFigureValue = listFigure[index]

        plt.figure('DC Plot' + str(index))

        pindex = plt.subplot(111)
        pindex.set_title("DC Simulation Plot")
        pindex.set_xlabel(XLabel,fontsize=14)
        pindex.set_ylabel(figureYLabel[index],fontsize=14)
        pindex.grid(True)

        for oneY in range(len(OneFigureValue)):
            OneValueY = OneFigureValue[oneY]
            YlabelOneY = AllFigureYlabel[index][oneY]
            pindex.plot(XValue,OneValueY,label=YlabelOneY)
            pindex.legend()
    #plt.show()


