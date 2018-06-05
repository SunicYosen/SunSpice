*Netlist example 
.PARAM Vin=2
.PARAM GND=0
.PARAM Alpha=30
.PARAM Offset=0

Vsin port1 gnd sin Vin 6.28e7 0 Offset
R1 port1 port2 1k
D1 port2 gnd Diode Is=7.075E-13 Alpha=Alpha

.dc Offset 0.0 2 0.001
.tran 1n 500n

.plot dc v(port1) v(port2)
.plot dc i(d1)
.plot tran v(port1) v(port2)
.plot tran i(d1)

.END


