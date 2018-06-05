*Netlist example
.param Vin=2
.param offset=0
.PARAM Alpha=30

Vsin port1 gnd sin Vin 6.28e7 0 offset
R1 port1 port2 1k
D1 port2 gnd Diode Is=7.075E-13 Alpha=Alpha
R2 port2 port3 100
D2 port3 gnd Diode Is=7.075E-13 Alpha=Alpha

.tran 100p 100n

.plot tran v(port1) v(port2) v(port3)
.plot tran i(D1) i(D2)

.END






