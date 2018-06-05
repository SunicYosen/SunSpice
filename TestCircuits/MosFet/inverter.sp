*Inverter
.param VinV=0.9

VDD1 portVDD gnd 1.8
Vin VinN gnd VinV
M1 portD VinN gnd 0 nmos w=1000n l=500n
*R2 portVDD portD 400k

M2 portD VinN portVDD gnd pmos w=1000n l=250n
*R1 portD gnd 100k

.dc VinV 0.1 1.8 0.01

.plot dc V(portD) V(VinN)

.end
















