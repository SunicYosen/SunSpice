.title rlc
.param VsinA=2
.param VsinW=6.28e7
.param VsinPhi=0
.param VsinOffset=1

Vsin port1 gnd sin VsinA VsinW VsinPhi VsinOffset
R1 port1 port2 1Meg
L2 port1 port2 1m
C1 port2 gnd 1p

.dc VsinOffset 0.0 2.0 0.01
.tran 1n 500n
.ac fre 1 1G

.plot dc v(port1) v(port2)
.plot ac v(port1) v(port2)
.plot tran v(port1) v(port2)

.END
