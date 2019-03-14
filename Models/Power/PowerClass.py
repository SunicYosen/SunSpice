#!python3
# _*_ encoding=UTF-8 _*_
import sys
sys.path.append("../..")

from math import sin
from Functions.string2num import string2num

class DCPower:                       #V
    name = ''
    portPos = ''
    portNeg = ''
    value = '0'	                     #default value = 0 V

    def __init__(self):
        self.name = ''
        self.portNeg = ''
        self.portPos = ''
        self.value = '0'
    

class SinPower:
    name = ''
    portPos = ''
    portNeg = ''
    A = ''
    w = ''
    phi = '0'
    Vo = '0'

    def __init__(self):
        self.name = ''
        self.portPos = ''
        self.portNeg = ''
        self.A = '5'
        self.w = '10Meg'
        self.phi = '0'
        self.Vo = '0'

    
    def getValue(self,time=0):
        Margin = string2num(self.A)
        Phase = string2num(self.w)
        SinPhi = string2num(self.phi)
        Voffset = string2num(self.Vo)
        valueV = Margin * sin(Phase * time + SinPhi) + Voffset
        return valueV
    
    def loadMatSinV(self,matAddr=0):
        pass
        #TODO or Give up this mathod

class PlusePower:
    name = ''
    portPos = ''
    portNeg = ''
    LowVoltage = ''
    HighVoltage = ''
    Tdelay = ''
    Trise = ''
    Tfall = ''
    Twide = ''
    Tperiod = ''

    def __init__(self,LowVoltage = '0',HighVoltage = '1.8',Tdelay = '0.0',Trise = '0',Tfall = '0',Twide = '1n',Tperiod = '2n'):
        self.name = ''
        self.portPos = ''
        self.portNeg = ''
        self.LowVoltage = LowVoltage
        self.HighVoltage = HighVoltage
        self.Tdelay = Tdelay
        self.Trise = Trise
        self.Tfall = Tfall
        self.Twide = Twide
        self.Tperiod = Tperiod

    def getVoltage(self,Time):
        LowVoltage_value = string2num(self.LowVoltage)
        HighVoltage_value = string2num(self.HighVoltage)
        Tdelay = string2num(self.Tdelay)
        Trise = string2num(self.Trise)
        Tfall = string2num(self.Tfall)
        Twide = string2num(self.Twide)
        Tperiod = string2num(self.Tperiod)

        if Tperiod < (Trise + Tfall + Twide):
            print("****Error! Time Define Error in Pluse Power",self.name)

        if Time < ( Tdelay + Tperiod ):
            Time_temp = Time
        else :
            Count = int((Time-Tdelay)/Tperiod)
            Time_temp = Time - Tperiod*Count

        Voltage_t = 0.0

        if Time_temp <= Tdelay:
            Voltage_t = LowVoltage_value

        elif (Time_temp > Tdelay) & (Time_temp <= (Tdelay + Trise)):
            Voltage_t = (LowVoltage_value + (HighVoltage_value - LowVoltage_value)/Trise*(Time_temp - Tdelay))
        
        elif (Time_temp > (Tdelay + Trise)) & (Time_temp <= (Tdelay + Trise + Twide)):
            Voltage_t = HighVoltage_value
        
        elif (Time_temp > (Tdelay + Trise + Twide)) & (Time_temp <= (Tdelay + Trise + Twide + Tfall)):
            Voltage_t = HighVoltage_value - (HighVoltage_value - LowVoltage_value)/Tfall*(Time_temp - Tdelay - Trise - Twide)
        
        elif (Time_temp > (Tdelay + Trise + Twide + Tfall)) & (Time_temp <= (Tdelay + Tperiod)):
            Voltage_t = LowVoltage_value

        else:
             Voltage_t = 0

        return Voltage_t

class ACPower:
    name = ''
    portPos = ''
    portNeg = ''
    ACMag = '1'
    ACPhase = '0'

    def __init__(self,ACMag='1',ACPhase='0'):
        self.name = ''
        self.portPos = ''
        self.portPos = ''
        self.ACMag = '1'
        self.ACPhase = '0'

    def getVoltage(self,Time):
        pass

