from tkinter import *
from tkinter import messagebox
from algorithms import*
import matplotlib.pyplot as plt

master = Tk(className='Scheduler')
master.geometry('500x500')
label5 = Label(master, text='Scheduler', width=20,font=("bold", 20))
label5.place(x=90, y=53)


#===================================== Data ==============================================
fileName = ""
scheduling = ""
contextSwitch = 0
quantum = 0
N = 0
processList = []
#==========================================================================================
class process(object):
    def __init__(self, number, startTime, burstTime, priority):
        self.number = number
        self.startTime = startTime
        self.burstTime = burstTime
        self.priority = priority
#==================================== Get Data From GUI ===================================
def data1():
    global fileName,scheduling,contextSwitch,quantum
    fileName = e0.get()
    scheduling = c.get()
    contextSwitch = e2.get()
    quantum = e3.get()
   # messagebox.showinfo('Message', fileName)
    readData()
#==========================================================================================

#============================== Read Data From the input file =============================

def readData():
    global N, processList
    messagebox.showinfo('Message', fileName)
    f = open(fileName, "r")
    if f.mode == 'r':
        lines = f.readlines()
    N = lines[0]

    for i in range(1, int(N)+1):
        processList.append(process(int(lines[i].split()[0]), int(lines[i].split()[1]), int(lines[i].split()[2]), int(lines[i].split()[3])))


    if scheduling == "HPF":
        HPF(processList)
    elif scheduling == "FCFS":
        FCFS()
    elif scheduling == "STRN":
        SRTN(processList)
    elif scheduling == "RR":
        RR(processList)



#====================================== GUI ===============================================

label0 = Label(master, text='File Name')
label0.place(x=80, y=130)
label1 = Label(master, text='Scheduling Algorithm')
label1.place(x=68, y=180)
label2 = Label(master, text='Context Switch time')
label2.place(x=70, y=230)
label3 = Label(master, text='Time Quantum')
label3.place(x=70, y=280)
e0 = Entry(master)
#e2 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e0.place(x=240,y=130)
#e1.place(x=240,y=180)
e2.place(x=240,y=230)
e3.place(x=240, y=280)
list1 = {'HPF', 'FCFS', 'RR', 'SRTN'}
c = StringVar()
droplist = OptionMenu(master, c, *list1)
droplist.config(width=15)
c.set('Select Algorithm')
droplist.place(x=240, y=180)

b = Button(master, text='OK', width=20, bg='brown', fg='white', command=data1)
b.place(x=180, y=380)
mainloop()


