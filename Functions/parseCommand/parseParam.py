#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-
import sys
sys.path.append("../..")

import re

import parameters

def parseParam(paramString = ''):
    paramString = paramString.replace('.param ','').strip()
    if paramString == '':
        print "Warning: ", paramString, "Define Error!"

    elif '=' in paramString:
        paramlist = paramString.split('=')
        if len(paramlist) != 2:
            print "Warning: ", paramString, "Define Error!"
        else:
            parameters.ParamDict[paramlist[0].strip()] = paramlist[1].strip()

    else:
        paramlist = paramString.split(' ')
        if len(paramlist) != 2:
            print "Warning: ", paramString, "Define Error!"

        else:
            parameters.ParamDict[paramlist[0].strip()] = paramlist[1].strip()
            print 'Add param: ',paramlist[0].strip()