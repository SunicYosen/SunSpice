#!/usr/bin/python3
# -*- encoding="UTF-8" -*-
import sys
sys.path.append("../..")

from Functions.string2num import string2num

class Mosfet:				 			  #NMOS
	name = ''
	portG = ''
	portD = ''
	portS = ''
	portB = '0'
	MosType = ''	#NMOS or PMOS
	valueW = '500n'	#500nm for Default
	valueL = '250n'	#250nm for Default
	kn = '115e-6'
	kp = '-30e-6'
	Vt0n = '0.43'
	Vt0p = '-0.4'
	lambdaN = '0.06'
	lambdaP = '-0.1'


	def __init__(self):
		self.name = ''
		self.portD = ''
		self.portG = ''
		self.portS = ''
		self.portB = '0'
		self.MosType = ''
		self.valueW = '500n'
		self.valueL = '250n'
		self.kn = '115e-6'    #un*Cox
		self.kp = '-30e-6'    #up*Cox
		self.Vt0n = '0.43'
		self.Vt0p = '-0.4'
		self.lambdaN = '0.06'
		self.lambdaP == '-0.1'
			
	def getIds(self,vgs=0.0,vds=0.0):

		if self.MosType == 'nmos':
			width = string2num(self.valueW)
			length = string2num(self.valueL)
			kn = string2num(self.kn)
			Vt0 = string2num(self.Vt0n)
			lambdaN = string2num(self.lambdaN)

			Vgt = float(vgs-Vt0)
			Beta = kn/2.0 * (width/length)

			gm = self.getGm(vds=vds,vgs=vgs)
			gds = self.getGds(vds=vds,vgs=vgs)

			if (vgs <= Vt0):
				Ids = 0

			elif (vds >= 0) & (vds <= Vgt):
				Ids = Beta * (2.0 * Vgt * vds - vds*vds) * (1.0 + lambdaN * vds) - gds*vds - gm*vgs
			elif (vds >= 0) & (vds > Vgt):
				Ids = Beta * (Vgt*Vgt)  * (1 + lambdaN * vds) - gds*vds - gm*vgs
				
			elif (vds < 0) & ((-1 * vds) <= Vgt):
				Ids =  -1 * Beta * (-2 * Vgt * vds - vds*vds) * (1 - lambdaN * vds) - gds*vds - gm*vgs

			elif (vds < 0) & ((-1 * vds) > Vgt):
				Ids = -1 * Beta * (Vgt*Vgt)  * (1 - lambdaN * vds) - gds*vds - gm*vgs

			else:
				print("Error: Error logic NMosFet Vds!")
				exit()

		elif self.MosType == 'pmos':
			width = string2num(self.valueW)
			length = string2num(self.valueL)
			kp = string2num(self.kp)
			Vt0 = string2num(self.Vt0p)
			lambdaP = string2num(self.lambdaP)

			Vgt = vgs-Vt0
			Beta = kp/2.0 * (width/length)

			gm = self.getGm(vds=vds,vgs=vgs)
			gds = self.getGds(vds=vds,vgs=vgs)

			# if (vds <= 0) & (vds >= Vgt):
			# 	Ids = Beta * (2.0 * Vgt * vds - vds*vds) * (1.0 + lambdaP * vds) - gds * vds - gm*vgs
			# elif vds < Vgt:
			# 	Ids = Beta * (Vgt*Vgt)  * (1 + lambdaP * vds) - gds * vds - gm*vgs
			# else:
			# 	Ids = Beta * (2.0 * Vgt * vds - vds*vds)  - gds * vds - gm*vgs

			if vgs >= Vt0:
				Ids = 0.0

			elif (vds <= 0) & (vds >= Vgt):
				Ids = Beta * (2.0 * Vgt * vds - vds*vds) * (1.0 + lambdaP * vds) - gds * vds - gm*vgs

			elif (vds <= 0) & (vds < Vgt):
				Ids = Beta * (Vgt*Vgt)  * (1 + lambdaP * vds) - gds * vds - gm*vgs

			elif (vds > 0) & ((-1 * vds) >= Vgt):
				Ids = -1 * Beta * (-2 * Vgt * vds - vds*vds) * (1 - lambdaP * vds) - gds * vds - gm*vgs
				
			elif (vds > 0) & ((-1 * vds) < Vgt):
				Ids = -1 * Beta * (Vgt**2)  * (1 - lambdaP * vds) - gds * vds - gm*vgs
				
			else:		#wouldn't Here
				print("Error: Error logic PMosFet Vds!")
				exit()

		else:
			print("Error: Error Mos Type!",self.MosType)
			exit()
		
		return Ids
		
	def getGm(self,vds=0,vgs=0):
		gm=0.00001
		if self.MosType == 'nmos':
			width = string2num(self.valueW)
			length = string2num(self.valueL)
			kn = string2num(self.kn)
			Vt0 = string2num(self.Vt0n)
			lambdaN = string2num(self.lambdaN)
			Vgt = vgs-Vt0
			Beta = kn/2.0 * (width/length)

			if vgs <= Vt0:
				gm=0

			elif (vds >= 0) & (vds <= Vgt):
				gm = 2 * Beta * vds * (1 + lambdaN * vds) 

			elif (vds >= 0) & (vds > Vgt):
				gm = 2 * Beta * Vgt * (1 + lambdaN * vds)

			elif (vds < 0) & ((-1 * vds) <= Vgt):
				gm = 2 * Beta * vds * (1 - lambdaN * vds)

			elif (vds < 0) & ((-1 * vds) > Vgt):
				gm = -2 * Beta * Vgt * (1 - lambdaN * vds)

			else:		#wouldn't Here
				print("Error: GetGm-- Error logic NMosFet Vds!")

		elif self.MosType == 'pmos':
			width = string2num(self.valueW)
			length = string2num(self.valueL)
			kp = string2num(self.kp)
			Vt0 = string2num(self.Vt0p)
			lambdaP = string2num(self.lambdaP)
			Vgt = vgs-Vt0
			Beta =kp/2.0 * (width/length)
			
			# if (vds <= 0) & (vds >= Vgt):
			# 	gm = 2.0 * Beta * vds * (1.0 + lambdaP * vds)
			# elif vds < Vgt:
			# 	gm = 2 * Beta * Vgt * (1 + lambdaP * vds)
			# else:
			# 	gm = 2.0 * Beta * vds
 

			if vgs >= Vt0:
				gm = 0

			elif (vds <= 0) & (vds >= Vgt):
				gm = 2.0 * Beta * vds * (1.0 + lambdaP * vds)

			elif (vds <= 0) & (vds < Vgt):
				gm = 2 * Beta * Vgt * (1 + lambdaP * vds)

			elif (vds > 0) & ((-1 * vds) >= Vgt):
				gm = 2 * Beta * vds * (1 - lambdaP * vds)

			elif (vds > 0) & ((-1 * vds) < Vgt):
				gm = -2 * Beta * Vgt * (1 - lambdaP * vds)

			else:		#wouldn't Here
				print("Error: GetGm-- Error logic MosFet Vds!")
				exit()

		else:
			print("Error: Error Mos Type!",self.MosType)
			exit()

		return gm
	
	def getGds(self,vds=0.0,vgs=0.0):
		if self.MosType == 'nmos':
			width = string2num(self.valueW)
			length = string2num(self.valueL)
			kn = string2num(self.kn)
			Vt0 = string2num(self.Vt0n)
			lambdaN = string2num(self.lambdaN)
			Vgt = vgs-Vt0
			Beta = kn/2.0 * (width/length)

			if vgs <= Vt0:
				gds = 0

			elif (vds >= 0) & (vds <= Vgt):
				gds = Beta * (2 * Vgt - vds*2) * (1 + lambdaN * vds) + Beta * (2 * Vgt * vds - vds*vds) * lambdaN

			elif (vds >= 0) & (vds > Vgt):
				gds = Beta * (Vgt*Vgt)  * lambdaN 

			elif (vds < 0) & ((-1 * vds) <= Vgt):
				gds = -1 * Beta * (-2 * Vgt - vds*2) * (1 - lambdaN * vds) + 1 * Beta * (-2 * Vgt * vds - vds**2) * (lambdaN)

			elif (vds < 0) & ((-1 * vds) > Vgt):
				gds = Beta * (Vgt*Vgt)  * lambdaN

			else:		#wouldn't Here
				print("Error: GetGds-- Error logic NMosFet Vds!")

		elif self.MosType == 'pmos':
			width = string2num(self.valueW)
			length = string2num(self.valueL)
			kp = string2num(self.kp)
			Vt0 = string2num(self.Vt0p)
			lambdaP = string2num(self.lambdaP)
			Vgt = vgs-Vt0
			Beta = kp/2.0 * (width/length)

			# if (vds <= 0) & (vds >= Vgt):
			# 	gds = Beta * (2 * Vgt - vds * 2) * (1 + lambdaP * vds) + Beta * (2 * Vgt * vds - vds**2) * lambdaP
			# elif vds < Vgt:
			# 	gds = Beta * (Vgt**2)  * lambdaP
			# else:
			# 	gds = 2.0 * Beta * (Vgt - vds)

			if vgs >= Vt0:
				gds = 0

			elif (vds <= 0) & (vds >= Vgt):
				gds = Beta * (2 * Vgt - vds * 2) * (1 + lambdaP * vds) + Beta * (2 * Vgt * vds - vds**2) * lambdaP

			elif (vds <= 0) & (vds < Vgt):
				gds = Beta * (Vgt**2)  * lambdaP

			elif (vds > 0) & ((-1 * vds) >= Vgt):
				gds = -1 * Beta * (-2 * Vgt - vds * 2) * (1 - lambdaP * vds) + 1 * Beta * (-2 * Vgt * vds - vds**2) *(lambdaP)

			elif (vds > 0) & ((-1 * vds) < Vgt):
				gds = Beta * (Vgt**2)  * lambdaP
				
			else:		#wouldn't Here
				print("Error: GetGds-- Error logic MosFet Vds!")

		else:
			print("Error: Error Mos Type!",self.MosType)
			exit()

		return gds
