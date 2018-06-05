#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

import sys
sys.path.append("..")

import parameters

def addNode(stringNode = ''):
	if stringNode == '':
		pass
		#print "--NONE ADDED!"

	elif stringNode == '0':
		pass
		#print "--0 is GND!"

	else:
		if parameters.NodesDict.has_key(stringNode):        #Already exit
			pass
			#print stringNode,'is already exit!'
		else:
			lenNodes = len(parameters.NodesDict)
			parameters.NodesDict[stringNode] = lenNodes
			#print "Add Node: ",stringNode, 'as', lenNodes
