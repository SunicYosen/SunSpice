#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-
import sys

def helpGuide(argsString = []):
    if len(argsString) == 1:
        printHelp(argsString[0])
        exit()

    for index in range(len(argsString)):
        if (index == 0):
            pass
        elif (argsString[index] == '--help') | (argsString[index] == '-h'):
            printHelp(argsString[0])
            exit()

        elif (argsString[index] == '--version') | (argsString[index] == '-v'):
            print 'SunSpice -V1.0 (2018-4-15) \nAll Rights Reserved By SunYongshuai'
            exit()

        elif (argsString[index] == '--print') | (argsString[index] == '-pr'):
            pass
        
        elif (argsString[index] == '--plot') | (argsString[index] == '-pl'):
            pass
            
        else:
            printHelp(argsString[0])

def printHelp(ProgramName=''):
    print ProgramName, '[Options]'
    print 'Options:'
    print '\t--help|-h   \t Show Options Help'
    print '\t--version|-v\t Show The Verion of the script' 
    print '\t<Filename>  \t Simulation the Netlist Given'
    print '\t--print|-pr \t Print The Value'
    print '\t--plot |-pl  \t Plot the Value'
    return 


    