# Source for SunSpice

## Python Source

1. Gui.py #GUI界面入口
2. SunSpice.py #Command Mode
3. parameters.py #全局变量
4. Makefile #Remove *.pyc(only Linux)
5. Function #功能模块文件夹
      + parseCommand #解析命令文件夹
      + PlotAndPrint #绘图文件夹
      + SimulationType  #仿真文件夹

6. Models #器件模型文件夹
      + Capacitor #电容模型
      + CtrlSource #受控源
      + Current #电流源模型
      + Diode #Diode模型
      + Inductor #电感模型
      + Mosfet #MOSFET模型
      + Power #电压源模型
      + Resistor #电阻模型

7. Test File
      + TestCircuits #测试电路文件夹
      + BandPass #带通滤波器
      + BandSup #带阻滤波器
      + Diode #Diode测试
      + Diode #Base Test
      + DoubleDiode #双Diode
      + Elmore #Almore Delay Test
      + HighPass #高通滤波器
      + LowPass #低通滤波器
      + MosFet #CMOS Inverter
      + MosFetTran #Cmos Inverte
      + Tran Simulation
        + RLC #RLC仿真

## Test Platform

python3.6 in Ubuntu 16.04.4&18.04.1 amd64 

## Useage

  If python3 in your computer such as /usr/bin/, you can type:

      $ ./Gui.py
      $ python3 Gui.py

  Or you can use Command mode by

      $ ./SunSpice.py **.sp
      $ python3 SunSpice.py **.sp

IF ANY Problem, Please add issue at: [Github New Issue](https://github.com/SunicYosen/SunSpice/issues/new)

All right reserved at [SunicYosen](https://github.com/SunicYosen)
