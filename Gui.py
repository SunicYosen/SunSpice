#!/usr/bin/python3
# -*- encoding: utf8 -*-

import os
from tkinter import messagebox,filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *

import matplotlib.pyplot as plt

from Functions.helpGuide import printHelp
from Functions.initParam import initParams

import parameters
from Functions.readFile import readFile

from Functions.SimulationType.DC import DCSimulation
from Functions.SimulationType.AC import ACSimulation
from Functions.SimulationType.Tran import TranSimulation
from Functions.SimulationType.OP import OpSimulation

from Functions.helpGuide import helpGuide
from Functions.PlotAndPrint.plotDC import plotDC
from Functions.PlotAndPrint.plotTran import plotTran
from Functions.PlotAndPrint.plotAC import plotAC

 
def author():
    showinfo('Author:','SunYongshuai')
 
def about():
    showinfo('Copyright','SunSpice')

def showHelp():
    showinfo('Help:','./SunSpice [Options]\n\
    Options: \n\
    --help|-h    \t Show Help \n \
    --version|-v \t Show Verion\n\
    <Filename>   \t Simulation\n\
    --print|-pr  \t Print \n \
    --plot |-pl  \t Plot the Value')

def plot():
    plotAC()
    plotDC()
    plotTran()
    plt.show()
 
def openfile():
    parameters.NetlistPath = askopenfilename(defaultextension = '.sp')

    if parameters.NetlistPath == '':
        parameters.NetlistPath = None

    else:
        root.title('FileName:'+os.path.basename(parameters.NetlistPath))
        textPad.delete(1.0,END)
        f = open(parameters.NetlistPath,'r')
        textPad.insert(1.0,f.read())
        f.close()
 
def new():
    root.title('UnamedFile')
    parameters.NetlistPath = None
    textPad.delete(1.0,END)
 
def save():
    try:
        f = open(parameters.NetlistPath,'w')
        msg = textPad.get(1.0,END)
        f.write(msg)
        f.close()
    except:
        saveas()
 
 
def saveas():
    f = asksaveasfilename(initialfile= 'Unnamed.sp', defaultextension='.sp')
    parameters.NetlistPath = f
    fh = open(f,'w')
    msg = textPad.get(1.0,END)
    fh.write(msg)
    fh.close()
    root.title('FileName:'+os.path.basename(f))
 
def cut():
    textPad.event_generate('<<Cut>>')
 
def copy():
    textPad.event_generate('<<Copy>>')
 
def paste():
    textPad.event_generate('<<Paste>>')
 
def redo():
    textPad.event_generate('<<Redo>>')
 
def undo():
    textPad.event_generate('<<Undo>>')
 
def selectAll():
    textPad.tag_add('sel','1.0',END)
 
def search():
    def dosearch():
        myentry = entry1.get()             #获取查找的内容--string型
        whatever = str(textPad.get(1.0,END))
        # print( textPad.index('zxc'))
        # print(myentry)
        # print("%d个"%(whatever.count(myentry)))    #计算substr在S中出现的次数
        showinfo("Search Result：","you searched %s, there are %d in the text"%(myentry,whatever.count(myentry)))
        # print(whatever.find(myentry))
 
        # teIndex = textPad.index(myentry)
        # textPad.linestart(teIndex)
        # textPad.mark_set('insert', teIndex)
        # textPad.mark_set(myentry,CURRENT + '+5c')
        # textPad.mark_set(myentry,CURRENT + ' wordstart')
    topsearch = Toplevel(root)
    topsearch.geometry('300x30+200+250')
    label1 = Label(topsearch,text='Find')
    label1.grid(row=0, column=0,padx=5)
    entry1 = Entry(topsearch,width=20)
    entry1.grid(row=0, column=1,padx=5)
    button1 = Button(topsearch,text='Search',command=dosearch)
    button1.grid(row=0, column=2)
     
 
root = Tk()
root.title('SunSpice')
root.geometry("800x500+100+100")
 
#Create Menu
menubar = Menu(root)
root.config(menu = menubar)
 
filemenu = Menu(menubar)
filemenu.add_command(label='New', accelerator='Ctrl + N', command= new)
filemenu.add_command(label='Open', accelerator='Ctrl + O',command = openfile)
filemenu.add_command(label='Save', accelerator='Ctrl + S', command=save)
filemenu.add_command(label='Save As', accelerator='Ctrl + Shift + S',command=saveas)
filemenu.add_command(label='Exit', accelerator='Ctrl + Q',command=exit)
menubar.add_cascade(label='File',menu=filemenu)
 
editmenu = Menu(menubar)
editmenu.add_command(label='Undo', accelerator='Ctrl + Z', command=undo)
editmenu.add_command(label='Redo', accelerator='Ctrl + y', command=redo)
editmenu.add_separator()
editmenu.add_command(label = "Cut",accelerator = "Ctrl + X",command=cut)
editmenu.add_command(label = "Copy",accelerator = "Ctrl + C", command=copy)
editmenu.add_command(label = "Paste",accelerator = "Ctrl + V", command= paste)
editmenu.add_separator()
editmenu.add_command(label = "Search",accelerator = "Ctrl + F", command=search)
editmenu.add_command(label = "Select All",accelerator = "Ctrl + A", command= selectAll)
menubar.add_cascade(label = "Edit",menu = editmenu)

helpmenu=Menu(menubar)              #Help Guide
helpmenu.add_command(label = 'HelpGuide',command=showHelp)
menubar.add_cascade(label='Help',menu=helpmenu)

aboutmenu = Menu(menubar)
aboutmenu.add_command(label = "Author", command=author)
aboutmenu.add_command(label = "About", command=about)
menubar.add_cascade(label = "About",menu=aboutmenu)
 
#toolbar
toolbar = Frame(root, height=30,bg='grey')

shortButton = Button(toolbar, text='Open',command = openfile)
shortButton.pack(side=LEFT, padx=5, pady=5)
 
shortButton = Button(toolbar, text='Save', command = save)
shortButton.pack(side=LEFT)

shortButton = Button(toolbar,text='Parse',command = readFile)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar,text='OP',command = OpSimulation)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar,text='DC',command = DCSimulation)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar,text='AC',command = ACSimulation)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar,text='Tran',command = TranSimulation)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar,text='Plot',command = plot)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar,text='Init',command = initParams)
shortButton.pack(side=LEFT, padx=5, pady=5)

#shortButton = Button(toolbar,text='Clear',command = 'exec clear')
#shortButton.pack(side=LEFT, padx=5, pady=5)

toolbar.pack(expand=NO,fill=X)

 
#Status Bar
status = Label(root, text='Ln20',bd=1, relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)
 
#linenumber&text
lnlabel =Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, fill=Y)
 
textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)
 
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand= scroll.set)
scroll.config(command = textPad.yview)
scroll.pack(side=RIGHT,fill=Y)

TextInfo = Text(root,height=120)
TextInfo.pack(expand=NO,fill=BOTH)
TextInfo.insert(END,"Welcome To SunSpice GUI!")
scollInfo = Scrollbar(TextInfo)
TextInfo.config(yscrollcommand= scroll.set)
scollInfo.config(command=TextInfo.yview)
scollInfo.pack(side=RIGHT,fill=Y)

root.mainloop()