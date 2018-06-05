#!/usr/bin/python2.7
# -*- encoding="UTF-8" -*-

class Capacitor:					          #C
	name = ''
	port1 = ''
	port2 = ''
	value = '1000f'   #1000fF for default

	def __init__(self):
		self.name = ''
		self.port1 = ''
		self.port2 = ''
		self.value = ''

	def loadMatCapacitor(self):
		pass