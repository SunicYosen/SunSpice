#!/usr/bin/python3
# -*- encoding="UTF-8" -*-

#Import Package
import numpy as np
from tkinter.messagebox import *

import parameters

from Functions.string2num import string2num

def getOutTitleDC():
    if len(parameters.listDCParam) == 1:
        paramName = parameters.listDCParam[0].paramName
        WriteString = str(paramName) + '\t'

        for index in parameters.NodesDict:
            if index == '0':
                pass
            else:
                WriteString = WriteString + 'v_' + index + '\t'

        #V -> Pluse -> SinV -> E -> F -> H -> L
        #Source Current
        for index in parameters.listDCV:
            WriteString = WriteString + 'i_' + index.name + '\t'
        for index in parameters.listPulseV:
            WriteString = WriteString + 'i_' + index.name + '\t'
        for index in parameters.listSinV:
            WriteString = WriteString + 'i_' + index.name + '\t'
        for index in parameters.listE:
            WriteString = WriteString + 'i_' + index.name + '\t'
        for index in parameters.listF:
            WriteString = WriteString + 'i_' + index.name + '\t'
        for index in parameters.listH:
            WriteString = WriteString + 'i_' + index.name + '\t'
        for index in parameters.listL:
            WriteString = WriteString + 'i_' + index.name + '\t'

        #Elem Current
        for index in parameters.listR:
            WriteString = WriteString + 'i_' + index.name + '\t'
        for index in parameters.listD:
            WriteString = WriteString + 'i_' + index.name + '\t'
        for index in parameters.listG:
            WriteString = WriteString + 'i_' + index.name + '\t'
        for index in parameters.listM:
            WriteString = WriteString + 'i_' + index.name + '\t'

        return WriteString
        
def getOutDataDC(MatResult):
    WriteString = ''

    for node in parameters.NodesDict:
        if node != '0':
            WriteString = WriteString +  str(MatResult[parameters.NodesDict.get(node)-1,0]) + '\t'

    for index in range(len(parameters.listDCV)):
        #V -> Pluse -> SinV -> E -> F -> H -> L
        matAddr = len(parameters.NodesDict) + index - 1
        WriteString = WriteString + str(MatResult[matAddr,0]) + '\t'

    for index in range(len(parameters.listPulseV)):
        #V -> Pluse -> SinV -> E -> F -> H -> L
        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + index - 1
        WriteString = WriteString + str(MatResult[matAddr,0]) + '\t'
    
    for index in range(len(parameters.listSinV)):
        #V -> Pluse -> SinV -> E -> F -> H -> L
        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + index - 1
        WriteString = WriteString + str(MatResult[matAddr,0]) + '\t'
    
    for index in range(len(parameters.listE)):
        #V -> Pluse -> SinV -> E -> F -> H -> L
        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + index - 1
        WriteString = WriteString + str(MatResult[matAddr,0]) + '\t'

    for index in range(len(parameters.listF)):
        #V -> Pluse -> SinV -> E -> F -> H -> L
        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + index - 1
        WriteString = WriteString + str(MatResult[matAddr,0]) + '\t'

    for index in range(len(parameters.listH)):
        #V -> Pluse -> SinV -> E -> F -> H -> L
        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + len(parameters.listF) + 2 * index - 1
        WriteString = WriteString + str(MatResult[matAddr,0]) + '\t'
    
    for index in range(len(parameters.listL)):
        #V -> Pluse -> SinV -> E -> F -> H -> L
        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + len(parameters.listF) + 2 * len(parameters.listH) + index - 1
        WriteString = WriteString + str(MatResult[matAddr,0]) + '\t'
            
    for resistor in parameters.listR:
        port1 = parameters.NodesDict.get(resistor.port1)
        port2 = parameters.NodesDict.get(resistor.port2)
        Rvalue = string2num(resistor.value)
        
        if (port1 != 0) & (port2 != 0):
            R_V = MatResult[port1-1,0] - MatResult[port2-1,0]
        elif (port1 == 0) & (port2 != 0):
            R_V = -1 * MatResult[port2-1,0]
        elif (port1 != 0) & (port2 == 0):
            R_V = MatResult[port1-1,0]
        else:
            R_V = 0

        WriteString = WriteString + str(R_V / Rvalue) + '\t'
    
    for diode in parameters.listD:
        port1 = parameters.NodesDict.get(diode.port1)
        port2 = parameters.NodesDict.get(diode.port2)
        if (port1 != 0) & (port2 != 0):
            D_V = MatResult[port1-1,0] - MatResult[port2-1,0]
        elif (port1 == 0) & (port2 != 0):
            D_V = -1 * MatResult[port2-1,0]
        elif (port1 != 0) & (port2 == 0):
            D_V = MatResult[port1-1,0]
        else:
            D_V = 0
        
        D_I = diode.getI_V(D_V)

        WriteString = WriteString + str(D_I) + '\t'

    for MosFet in parameters.listM:

        pass

    for vccs_g in parameters.listG:
        ctlNodePos = parameters.NodesDict.get(vccs_g.ctlNodePos)
        ctlNodeNeg = parameters.NodesDict.get(vccs_g.ctlNodeNeg)

        if (ctlNodePos != 0) & (ctlNodeNeg != 0):
            C_V = MatResult[ctlNodePos-1,0] - MatResult[ctlNodeNeg-1,0]
        elif (port1 == 0) & (port2 != 0):
            C_V = -1 * MatResult[ctlNodeNeg-1,0]
        elif (port1 != 0) & (port2 == 0):
            C_V = MatResult[ctlNodePos,0]
        else:
            C_V = 0

        vccs_I = vccs_g.getI(C_V)

        WriteString = WriteString + str(vccs_I) + '\t'

    return WriteString


def DCSimulation():
    if len(parameters.listDCParam) == 0:
        print("Warning: No DC Simulation Parameter!")
        print('')
        return

    elif len(parameters.listDCParam) == 1:
        print('Info: DC Simulation ...')

        ParamName = parameters.listDCParam[0].paramName
        print("Info: --Param:", ParamName)

        StartVal = parameters.listDCParam[0].paramValueStart
        StopVal = parameters.listDCParam[0].paramValueStop
        StepVal = parameters.listDCParam[0].paramValueStep
        #PiontNum = parameters.listDCParam[0].default_PointNum

        if ParamName in parameters.ParamDict:
            flagParam = True
            Value_Param = parameters.ParamDict.get(ParamName)   #Store Origin Param Value

        else:
            parameters.ParamDict[ParamName] = StartVal
            flagParam = False

        Val_Temp = StartVal                          #Sweep Temp
        
        NodeNum = len(parameters.NodesDict) - 1        # Nodes but GND
        branchnum = len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + len(parameters.listF) + 2 * len(parameters.listH) + len(parameters.listL)   
        #V -> Pluse -> SinV -> E -> F -> H -> L

        MatNum = NodeNum + branchnum

        MatStamps = np.mat(np.zeros((MatNum,MatNum)))
        MatRhs = np.mat(np.zeros((MatNum,1)))
        MatResult = np.mat(np.zeros((MatNum,1)))

        fileResult = open(parameters.NetlistPath+'.dc','w')
        fileResult.write('*\tDC Result\n')

        WriteString = getOutTitleDC()
        fileResult.write(WriteString + '\n')

        #for index in range(NodeNum):            #No Load I of Voltage Source
        #    MatResult[index,0] = parameters.opValue[index]

        InitFlag = True

        while Val_Temp <= StopVal:
            print(Val_Temp)
            parameters.ParamDict[ParamName] = Val_Temp
            if (len(parameters.listD) != 0) | (len(parameters.listM) != 0):    #Unlinear Diode Devices
                if (len(parameters.listD)!=0):
                    MarkPort = parameters.NodesDict.get(parameters.listD[0].port1)
                elif len(parameters.listM) != 0:
                    MarkPort = parameters.NodesDict.get(parameters.listM[0].portD)
                else:
                    print("Error: Logic Error!")     #Wouldn't Here
                    exit()
                
                lastVMarkPort = 1.8     #No Mater
                VMarkPort = 0.9

                while abs(VMarkPort - lastVMarkPort) > 0.01:
                
                    MatStamps = np.mat(np.zeros((MatNum,MatNum)))
                    MatRhs = np.mat(np.zeros((MatNum,1)))

                    for elem in parameters.listR:							#Load R
                        elem.loadMatResistor()
                        for keyPoint in elem.StampMatDict:
                            MatStamps[keyPoint.pointX,keyPoint.pointY] += elem.StampMatDict.get(keyPoint)
                    
                    for elem in parameters.listD:                          #load D
                        port1 = parameters.NodesDict.get(elem.port1)
                        port2 = parameters.NodesDict.get(elem.port2)

                        if (port1 != 0) & (port2 != 0):
                            ResultVd_temp = MatResult[port1-1,0] - MatResult[port2-1,0]
                        elif port1 == 0:
                            ResultVd_temp = -1 * MatResult[port2-1,0]
                        elif port2 == 0:
                            ResultVd_temp = MatResult[port1-1,0]
                        else:
                            ResultVd_temp = 0
                            
                        elem.loadMatDiode(ResultVd_temp)

                        for keyPoint in elem.StampMatDict:
                            MatStamps[keyPoint.pointX,keyPoint.pointY] += elem.StampMatDict.get(keyPoint)

                        for keyPoint in elem.RHSMatDict:
                            MatRhs[keyPoint.pointX,keyPoint.pointY] += elem.RHSMatDict.get(keyPoint)
 
                    for elem in range(len(parameters.listE)):				#Load E
                        #V -> Pluse -> SinV -> E -> F -> H -> L
                        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + elem - 1
                        parameters.listE[elem].loadMatE(matAddr)
                        for keyPoint in parameters.listE[elem].matStampsE:
                            MatStamps[keyPoint.pointX,keyPoint.pointY] = parameters.listE[elem].matStampsE.get(keyPoint)

                    for elem in range(len(parameters.listF)):              #loadF
                        #V -> Pluse -> SinV -> E -> F -> H -> L
                        portCtlPos = parameters.NodesDict.get(parameters.listF[elem].ctlNodePos)
                        portCtlNeg = parameters.NodesDict.get(parameters.listF[elem].ctlNodePos)

                        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + elem - 1
                        Vctl = MatResult[portCtlPos-1] - MatResult[portCtlNeg-1]

                        parameters.listF[elem].loadMatF(matAddr,Vctl)

                        for keyPoint in parameters.listF[elem].matStampsF:
                            MatStamps[keyPoint.pointX,keyPoint.pointY] = parameters.listF[elem].matStampsF.get(keyPoint)
                        
                        for keyPoint in parameters.listF[elem].matStampsF:
                            MatRhs[keyPoint.pointX,keyPoint.pointY] = parameters.listF[elem].matRhsF.get(keyPoint)
                    
                    for elem in parameters.listG:                          #loadG
                        elem.loadMatG()
                        for keyPoint in elem.matStampsG:
                            MatStamps[keyPoint.pointX,keyPoint.pointY] += elem.matStampsG.get(keyPoint)

                    for elem in range(len(parameters.listH)):              #load H
                        #V -> Pluse -> SinV -> E -> F -> H -> L
                        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + len(parameters.listF) + 2 * elem - 1
                        portCtlPos = parameters.NodesDict.get(parameters.listH[elem].ctlNodePos)
                        portCtlNeg = parameters.NodesDict.get(parameters.listH[elem].ctlNodePos)

                        Vctl = MatResult[portCtlPos-1] - MatResult[portCtlNeg-1]
                        parameters.listH[elem].loadMatH(matAddr,Vctl)

                        MatRhs[matAddr+1] = string2num(parameters.listH[elem].transResValue)

                        for keyPoint in parameters.listH[elem].matStampsH:
                            MatStamps[keyPoint.pointX,keyPoint.pointY] = parameters.listH[elem].matStampsH.get(keyPoint)
                      
                    for elem in parameters.listDCI:                        #load DC Is
                        elem.loadMatDCIs()
                        for keyPoint in elem.RHSMatDict:
                            MatRhs[keyPoint.pointX,keyPoint.pointY] += elem.RHSMatDict.get(keyPoint)
                    
                    for elem in range(len(parameters.listDCV)):                   #load DC Vs
                        #V -> Pluse -> SinV -> E -> F -> H -> L
                        VsDC = parameters.listDCV[elem]
                        matAddr = len(parameters.NodesDict) + elem - 1
                        portPos = parameters.NodesDict.get(VsDC.portPos)
                        portNeg = parameters.NodesDict.get(VsDC.portNeg)
                        DCV_Value = string2num(VsDC.value)
                        MatRhs[matAddr,0] = DCV_Value

                        if portPos != 0:
                            MatStamps[matAddr,portPos-1] = 1
                            MatStamps[portPos-1,matAddr] = 1
                        if portNeg != 0:
                            MatStamps[matAddr,portNeg-1] = -1
                            MatStamps[portNeg-1,matAddr] = -1
                    
                    for elem in range(len(parameters.listPulseV)):                #load DC Pluse
                        #V -> Pluse -> SinV -> E -> F -> H -> L
                        VsPluseDC = parameters.listPulseV[elem]
                        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + elem - 1
                        portPos = parameters.NodesDict.get(VsPluseDC.portPos)
                        portNeg = parameters.NodesDict.get(VsPluseDC.portNeg)
                        Pluse_DCValue = VsPluseDC.getVoltage(0)

                        MatRhs[matAddr,0] = Pluse_DCValue

                        if portPos != 0:
                            MatStamps[matAddr,portPos-1] = 1
                            MatStamps[portPos-1,matAddr] = 1
                        if portNeg != 0:
                            MatStamps[matAddr,portNeg-1] = -1
                            MatStamps[portNeg-1,matAddr] = -1

                    for elem in range(len(parameters.listSinV)):                  #load DC sin Vs
                        #V -> Pluse -> SinV -> E -> F -> H -> L
                        VsSinDC = parameters.listSinV[elem]
                        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + elem - 1
                        portPos = parameters.NodesDict.get(VsSinDC.portPos)
                        portNeg = parameters.NodesDict.get(VsSinDC.portNeg)
                        Sin_DcValue = VsSinDC.getValue(0)

                        MatRhs[matAddr,0] = Sin_DcValue

                        if portPos != 0:
                            MatStamps[matAddr,portPos-1] = 1
                            MatStamps[portPos-1,matAddr] = 1
                        if portNeg != 0:
                            MatStamps[matAddr,portNeg-1] = -1
                            MatStamps[portNeg-1,matAddr] = -1

                    for elem in range(len(parameters.listL)):                     #Load L in DC simulation
                        LTemp = parameters.listL[elem]
                        #V -> Pluse -> SinV -> E -> F -> H -> L
                        matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + len(parameters.listF) + 2 * len(parameters.listH) + elem - 1
                        portPos = parameters.NodesDict.get(LTemp.port1)
                        portNeg = parameters.NodesDict.get(LTemp,port2)

                        if portPos != 0:
                            MatStamps[matAddr,portPos-1] = 1
                            MatStamps[portPos-1,matAddr] = 1
                        if portNeg != 0:
                            MatStamps[matAddr,portNeg-1] = -1
                            MatStamps[portNeg-1,matAddr] = -1
                        
                    for elem in parameters.listM:
                        portD = parameters.NodesDict.get(elem.portD)
                        portG = parameters.NodesDict.get(elem.portG)
                        portS = parameters.NodesDict.get(elem.portS)
                        portB = parameters.NodesDict.get(elem.portB)

                        if portD == 0:
                            Vd = 0

                        else:
                            Vd = MatResult[portD-1,0]

                        if portG == 0:
                            Vg = 0

                        else:
                            Vg = MatResult[portG-1,0]
                        
                        if portS == 0:
                            Vs = 0
                        else:
                            Vs = MatResult[portS-1,0]
                        
                        if portB == 0:
                            pass
                            #Vb = 0
                            
                        else:
                            pass
                            #Vb = MatResult[portB-1,0]
                        
                        Vds = Vd - Vs

                        if(elem.MosType == 'pmos'):
                            if Vd > Vs:
                                Vgs = Vg-Vd
                            else:
                                Vgs = Vg-Vs
                        
                        elif(elem.MosType == 'nmos'):
                            if Vd < Vs:
                                Vgs = Vg-Vd
                            else:
                                Vgs = Vg-Vs

                        if(InitFlag):
                             if(elem.MosType == 'pmos'):
                                 #Vds = -1.3
                                 Vgs = -1.3
                            
                             elif (elem.MosType == 'nmos'):
                                 #Vds = 0.6
                                 Vgs = 0.5 
                             else:
                                 pass                     
                        
                        Ids = elem.getIds(vgs=Vgs,vds=Vds)
                        Gm = elem.getGm(vds=Vds,vgs=Vgs)
                        Gds = elem.getGds(vds=Vds,vgs=Vgs)

                        if portD != 0:
                            MatRhs[portD-1,0] -= Ids
                            MatStamps[portD-1,portD-1] += Gds

                        if portS != 0:
                            MatRhs[portS-1,0] += Ids
                            MatStamps[portS-1,portS-1] += (Gds + Gm)
                        
                        if (portD!=0) & (portS!=0):
                            MatStamps[portD-1,portS-1] -= (Gds + Gm)
                            MatStamps[portS-1,portD-1] -= Gds
                        
                        if (portD!=0) & (portG!=0):
                            MatStamps[portD-1,portG-1] += Gm
                        
                        if (portS!=0) & (portG!=0):
                            MatStamps[portS-1,portG-1] -= Gm

                    InitFlag = False
                    MatResult = np.linalg.solve(MatStamps,MatRhs)   #Result
                    lastVMarkPort = VMarkPort
                    VMarkPort = MatResult[MarkPort-1,0]

            else:
                MatStamps = np.mat(np.zeros((MatNum,MatNum)))
                MatRhs = np.mat(np.zeros((MatNum,1)))

                for elem in parameters.listR:							#Load R
                    elem.loadMatResistor()
                    for keyPoint in elem.StampMatDict:
                        MatStamps[keyPoint.pointX,keyPoint.pointY] += elem.StampMatDict.get(keyPoint)
        
                for elem in range(len(parameters.listE)):				#Load E
                    #V -> Pluse -> SinV -> E -> F -> H -> L
                    matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + elem - 1
                    parameters.listE[elem].loadMatE(matAddr)
                    for keyPoint in parameters.listE[elem].matStampsE:
                        MatStamps[keyPoint.pointX,keyPoint.pointY] = parameters.listE[elem].matStampsE.get(keyPoint)

                for elem in range(len(parameters.listF)):              #loadF
                    #V -> Pluse -> SinV -> E -> F -> H -> L
                    portCtlPos = parameters.NodesDict.get(parameters.listF[elem].ctlNodePos)
                    portCtlNeg = parameters.NodesDict.get(parameters.listF[elem].ctlNodePos)

                    matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + elem - 1
                    Vctl = MatResult[portCtlPos-1] - MatResult[portCtlNeg-1]

                    parameters.listF[elem].loadMatF(matAddr,Vctl)

                    for keyPoint in parameters.listF[elem].matStampsF:
                        MatStamps[keyPoint.pointX,keyPoint.pointY] = parameters.listF[elem].matStampsF.get(keyPoint)
                                
                    for keyPoint in parameters.listF[elem].matStampsF:
                        MatRhs[keyPoint.pointX,keyPoint.pointY] = parameters.listF[elem].matRhsF.get(keyPoint)
                            
                for elem in parameters.listG:                          #loadG
                    elem.loadMatG()
                    for keyPoint in elem.matStampsG:
                        MatStamps[keyPoint.pointX,keyPoint.pointY] += elem.matStampsG.get(keyPoint)

                for elem in range(len(parameters.listH)):              #load H
                    #V -> Pluse -> SinV -> E -> F -> H -> L
                    matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + len(parameters.listF) + 2 * elem - 1
                    portCtlPos = parameters.NodesDict.get(parameters.listH[elem].ctlNodePos)
                    portCtlNeg = parameters.NodesDict.get(parameters.listH[elem].ctlNodePos)

                    Vctl = MatResult[portCtlPos-1] - MatResult[portCtlNeg-1]
                    parameters.listH[elem].loadMatH(matAddr,Vctl)

                    MatRhs[matAddr+1] = string2num(parameters.listH[elem].transResValue)

                    for keyPoint in parameters.listH[elem].matStampsH:
                        MatStamps[keyPoint.pointX,keyPoint.pointY] = parameters.listH[elem].matStampsH.get(keyPoint)
                            
                for elem in parameters.listDCI:                        #load DC Is
                    elem.loadMatDCIs()
                    for keyPoint in elem.RHSMatDict:
                        MatRhs[keyPoint.pointX,keyPoint.pointY] += elem.RHSMatDict.get(keyPoint)
                            
                for elem in range(len(parameters.listDCV)):                   #load DC Vs
                    #V -> Pluse -> SinV -> E -> F -> H -> L
                    VsDC = parameters.listDCV[elem]
                    matAddr = len(parameters.NodesDict) + elem - 1
                    portPos = parameters.NodesDict.get(VsDC.portPos)
                    portNeg = parameters.NodesDict.get(VsDC.portNeg)
                    DCV_Value = string2num(VsDC.value)
                    MatRhs[matAddr,0] = DCV_Value

                    if portPos != 0:
                        MatStamps[matAddr,portPos-1] = 1
                        MatStamps[portPos-1,matAddr] = 1
                    if portNeg != 0:
                        MatStamps[matAddr,portNeg-1] = -1
                        MatStamps[portNeg-1,matAddr] = -1
                            
                for elem in range(len(parameters.listPulseV)):                #load DC Pluse
                    #V -> Pluse -> SinV -> E -> F -> H -> L
                    VsPluseDC = parameters.listPulseV[elem]
                    matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + elem - 1
                    portPos = parameters.NodesDict.get(VsPluseDC.portPos)
                    portNeg = parameters.NodesDict.get(VsPluseDC.portNeg)
                    Pluse_DCValue = VsPluseDC.getVoltage(0)

                    MatRhs[matAddr,0] = Pluse_DCValue

                    if portPos != 0:
                        MatStamps[matAddr,portPos-1] = 1
                        MatStamps[portPos-1,matAddr] = 1
                    if portNeg != 0:
                        MatStamps[matAddr,portNeg-1] = -1
                        MatStamps[portNeg-1,matAddr] = -1

                for elem in range(len(parameters.listSinV)):                  #load DC sin Vs
                    #V -> Pluse -> SinV -> E -> F -> H -> L
                    VsSinDC = parameters.listSinV[elem]
                    matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + elem - 1
                    portPos = parameters.NodesDict.get(VsSinDC.portPos)
                    portNeg = parameters.NodesDict.get(VsSinDC.portNeg)
                    Sin_DcValue = VsSinDC.getValue(0)

                    MatRhs[matAddr,0] = Sin_DcValue

                    if portPos != 0:
                        MatStamps[matAddr,portPos-1] = 1
                        MatStamps[portPos-1,matAddr] = 1
                    if portNeg != 0:
                        MatStamps[matAddr,portNeg-1] = -1
                        MatStamps[portNeg-1,matAddr] = -1

                for elem in range(len(parameters.listL)):                     #Load L in DC simulation
                    LTemp = parameters.listL[elem]
                    #V -> Pluse -> SinV -> E -> F -> H -> L
                    matAddr = len(parameters.NodesDict) + len(parameters.listDCV) + len(parameters.listPulseV) + len(parameters.listSinV) + len(parameters.listE) + len(parameters.listF) + 2 * len(parameters.listH) + elem - 1
                    portPos = parameters.NodesDict.get(LTemp.port1)
                    portNeg = parameters.NodesDict.get(LTemp.port2)

                    if portPos != 0:
                        MatStamps[matAddr,portPos-1] = 1
                        MatStamps[portPos-1,matAddr] = 1
                    if portNeg != 0:
                        MatStamps[matAddr,portNeg-1] = -1
                        MatStamps[portNeg-1,matAddr] = -1
                    

                MatResult = np.linalg.solve(MatStamps,MatRhs)   #Result            

            WriteString = str(Val_Temp) + '\t'

            WriteString = WriteString + getOutDataDC(MatResult)
            
            fileResult.write(WriteString + '\n')

            Val_Temp = Val_Temp + StepVal

        if flagParam:
            parameters.ParamDict[ParamName] = Value_Param
            
        fileResult.close()
        print('Info: End DC Simulation ...')
        
    elif len(parameters.listDCParam) == 2:
        print("Info: SWEEP:",parameters.listDCParam[0].paramName,parameters.listDCParam[1].paramName)
    
    else:
        print("Error: Error Expression of DC Simulation" )

    showinfo('DC','DC Simulation End!')
    
