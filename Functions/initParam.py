import parameters
from tkMessageBox import *

def initParams():
    parameters.listR = []					#
    parameters.listC = []
    parameters.listL = []
    parameters.listM = []
    parameters.listE = []
    parameters.listF = []
    parameters.listG = []
    parameters.listH = []
    parameters.listD = []

    parameters.listDCV = []
    parameters.listSinV = []
    parameters.listPulseV = []

    parameters.listACV = []

    parameters.listDCI = []
    parameters.listSinI = []

    parameters.listDCParam = []
    parameters.listACParam = []
    parameters.listTranParam = []

    parameters.listPlotDC = []
    parameters.listPlotAC = []
    parameters.listPlotTran = []

    parameters.opExp = []
    parameters.opValue = []

    parameters.opValueString = ''
    parameters.opExpString = ''

    parameters.NodesDict = {                  #Dictionary of Nodes
        '0':0
    }

    parameters.ParamDict = {
        'GND':0
    }

    parameters.STEP = '10p'					#STEP
    parameters.GND = 0							#define GND port is 

    showinfo('Init','Initital Parameters Fuccessfully!')