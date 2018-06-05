*Elmore
vin1 port1 gnd 1
R1 port1 port2 1k
C1 port2 gnd 2f
R2 port2 port3 1k
C2 port3 gnd 2f
R3 port3 port4 1k
C3 port4 gnd 2f
R4 port3 port5 1k
C4 port5 gnd 2f
R5 port2 port6 1k
C5 port6 gnd 2f
R6 port6 port7 1k
C6 port7 gnd 2f
R7 port7 port8 1k
C7 port8 gnd 2f
R8 port7 port9 1k
C8 port9 gnd 2f
R9 port6 port10 1k
C9 port10 gnd 2f

.tran 0.5p 100p

.plot tran v(port1) v(port2) v(port3) v(port4) v(port10)

.end

