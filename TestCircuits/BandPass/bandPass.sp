.title BandPass

Vin port1 gnd 1
R1 port1 port2 1k
C1 port2 out 0.01u
R2 out gnd 100k
C2 out gnd 0.001u

.ac fre 1 1G
.plot ac v(port1) v(out)   
*Must more than two,The first is Reference

.END
