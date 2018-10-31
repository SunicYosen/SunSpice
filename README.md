# Source for SunSpice
    Python Source:
        + Gui.py		#GUI界面入口
		+ SunSpice.py 	#Command Mode
		+ parameters.py	#全局变量
		+ Makefile		#Remove *.pyc(only Linux)
		
		+ Function			#功能模块文件夹
		  + parseCommand 	#解析命令文件夹
		  + PlotAndPrint	#绘图文件夹
		  + SimulationType  #仿真文件夹
		  
		+ Models			#器件模型文件夹
		  + Capacitor		#电容模型
		  + CtrlSource		#受控源
		  + Current			#电流源模型
		  + Diode			#Diode模型
		  + Inductor    	#电感模型
		  + Mosfet 			#MOSFET模型
		  + Power			#电压源模型
		  + Resistor		#电阻模型
		
	Test File:
		+ TestCircuits  	#测试电路文件夹
		  + BandPass		#带通滤波器
		  + BandSup			#带阻滤波器
		  + Diode			#Diode测试
			+ Diode 		#Base Test
			+ DoubleDiode	#双Diode
			
		  + Elmore			#Almore Delay Test
		  + HighPass		#高通滤波器
		  + LowPass			#低通滤波器
		  + MosFet			#CMOS Inverter
		  + MosFetTran		#Cmos Inverter Tran Simulation
		  + RLC				#RLC仿真
		
Platform: python2.7 in Ubuntu 16.04.4 amd64 

Useage:
    if python2.7 in your computer such as /usr/bin/, you can type:
        $ ./Gui.py   \
        $ python2.7 Gui.py
		or you can use Command mode by 
		$ ./SunSpice.py **.sp \
		$ python2.7 SunSpice.py **.sp
    
    else:
        Please install python2.7 at first.
		
IF ANY Problem Please @：
Email:sunicyosen@outlook.com
