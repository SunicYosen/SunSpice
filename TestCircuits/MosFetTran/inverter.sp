*Inverter

VDD1 portVDD gnd 1.8
Vpluse1 VinN gnd pluse 0 1.8 0 100p 100p 5n 10n 

M1 portD VinN gnd 0 nmos w=1000n l=500n
R2 portVDD portD 600k

M2 portD VinN portVDD gnd pmos w=1000n l=500n
*R1 portD gnd 100k

.tran 0.01n 10n

.plot tran V(portD) V(VinN)

.end










