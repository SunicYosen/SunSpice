.title BandPass

Vin port1 gnd 1
R1 port1 port2 1k
C1 port2 gnd 0.022u
C2 port1 port3 0.1u
R2 port3 gnd 1k
C3 port3 out 0.1u 
R3 port2 out 1k

.ac fre 1 1G

.plot ac v(port1) v(out)   
*Must more than two,The first is Reference

.END

