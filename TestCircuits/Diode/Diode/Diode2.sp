*Netlist example 
.PARAM Vin=2
.PARAM GND=0
.PARAM Alpha=30
.PARAM Offset=0

V1 port1 gnd Vin
R1 port1 port2 1k
R2 port2 gnd 1k
D1 port2 gnd Diode Is=7.075E-13 Alpha=Alpha

.dc Offset 0.0 2 0.001

.plot dc v(port2)

.END



