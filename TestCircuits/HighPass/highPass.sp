.title rlc

Vin port1 gnd 1
C1 port1 port2 1u
R1 port2 gnd 1k

.ac fre 1 1G

.plot ac v(port1) v(port2)
.END

