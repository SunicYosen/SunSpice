.title lowPass

Vin port1 gnd 1
R1 port1 port2 1k
C1 port2 gnd 1u

.ac fre 1 1G

.plot ac v(port1) v(port2)   
*Must more than two,The first is Reference

.END