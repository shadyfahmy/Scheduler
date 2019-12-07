import matplotlib.pyplot as plt
import numpy as np
import math

class process(object):
    def __init__(self, number, startTime, burstTime, priority):
        self.number = number
        self.startTime = float(startTime)
        self.burstTime = float(burstTime)
        self.priority = float(priority)
        self.remainingTime = float(burstTime)

def HPF(processList):
    print("HPF")
    '''processList = processList.sort(key=lambda x: x.priority, reverse=True)
    x = []
    y = []

    for i in range(len(processList)):
        x.append(0)
'''

def FCFS():
    print("FCFS")
    '''processList = processList.sort(key=lambda x: x.startTime, reverse=False)
    temp = 0
    x = []
    y = []

    for i in range(len(processList)):
        y.append(processList[i].number)
        if processList[i].startTime <= temp:
            temp2 = temp
        else:
            temp2 = temp + (processList[i].startTime - temp)
        temp2 = processList[i].startTime - temp
        x.append(temp2)
        x.append(temp2)
        temp3 = temp2 + processList[i].burstTime
        x.append(temp3)
        y.append(0)
        y.append(processList[i].number)
        y.append(processList[i].number)
        temp = temp3

    plt.plot(x, y, color='green', linestyle='solid', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    plt.show()
'''
incVal = 1
def SRTN(processList,switchingTime):
    workingQueue = []
    processList.sort(key=lambda x: x.startTime)
    y = []
    x = []
    y.append(0)
    x.append(0)
    print(processList)
    count = len(processList)
    Ticks = []
    Ticks.append("idle")
    for i,process in enumerate(processList):
        Ticks.append(str(i+1))
    plt.yticks(np.arange(count+1),Ticks)
    currentProcess = -1
    currentTime = 0
    while len(processList)>0 or len(workingQueue)>0 or currentProcess!= -1:
        while(len(processList)>0):
            if (currentTime >= processList[0].startTime):
                if(currentProcess == -1):
                    currentProcess = processList[0]
                else:
                    workingQueue.append(processList[0])
                    workingQueue.sort(key=lambda x: x.remainingTime)
                    if(currentProcess.remainingTime >workingQueue[0].remainingTime):
                        workingQueue.append(currentProcess)
                        currentProcess = workingQueue.pop(0)
                        workingQueue.sort(key=lambda x: x.remainingTime)
                        if switchingTime > 0:
                            y.append(0)
                            x.append(currentTime)
                            currentTime+=switchingTime
                            y.append(0)
                            x.append(currentTime)
                        
                processList.remove(processList[0])
            else:
                break
        if(currentProcess != -1):
            y.append(currentProcess.number)
            x.append(currentTime)
            if(incVal < currentProcess.remainingTime):
                currentProcess.remainingTime-= incVal
                currentTime+= incVal
                y.append(currentProcess.number)
                x.append(currentTime)
            else:
                remTime = currentProcess.remainingTime
                currentTime+= remTime
                currentProcess.remainingTime-= remTime
                y.append(currentProcess.number)
                x.append(currentTime)
                currentProcess = -1
                if switchingTime > 0:
                    y.append(0)
                    x.append(currentTime)
                    currentTime+=switchingTime
                    y.append(0)
                    x.append(currentTime)

        elif(len(workingQueue)>0):
            currentProcess = workingQueue.pop(0)
        else:
            currentTime+=incVal
            y.append(0)
            x.append(currentTime)
    plt.xticks(np.arange(math.ceil(currentTime+1)))
    plt.grid(b=None, which='major', axis='both')
    plt.plot(x, y, color='green', linestyle='solid', linewidth=1)
    plt.show()

def RR(processList,quantumTime,switchingTime):
    workingQueue = []
    processList.sort(key=lambda x: x.startTime)
    y = []
    x = []
    y.append(0)
    x.append(0)
    print(processList)
    count = len(processList)
    Ticks = []
    Ticks.append("idle")
    for i,process in enumerate(processList):
        Ticks.append(str(i+1))
    plt.yticks(np.arange(count+1),Ticks)
    currentProcess = -1
    lastProcess = -1
    currentTime = 0
    while len(processList)>0 or len(workingQueue)>0 or currentProcess !=-1 or lastProcess !=-1:
        while(len(processList)>0):
            if (currentTime >= processList[0].startTime):
                if(currentProcess == -1):
                    if(lastProcess != -1):
                        y.append(0)
                        x.append(currentTime)
                        currentTime+=switchingTime
                        y.append(0)
                        x.append(currentTime)
                    currentProcess = processList[0]
                else:
                    workingQueue.append(processList[0])
                processList.remove(processList[0])
            else:
                break
        if(lastProcess != -1):
            if(currentProcess == -1):
                currentProcess = lastProcess
            else:
                workingQueue.append(lastProcess)
            lastProcess = -1
        if(currentProcess != -1):
            y.append(currentProcess.number)
            x.append(currentTime)
            if(quantumTime < currentProcess.remainingTime):
                currentProcess.remainingTime-= quantumTime
                currentTime+= quantumTime
                y.append(currentProcess.number)
                x.append(currentTime)
                lastProcess = currentProcess
                currentProcess = -1
                if(len(workingQueue) != 0):
                    currentProcess = workingQueue.pop(0)
                    if switchingTime > 0:
                        y.append(0)
                        x.append(currentTime)
                        currentTime+=switchingTime
                        y.append(0)
                        x.append(currentTime)
            else:
                remTime = currentProcess.remainingTime
                currentTime+= remTime
                currentProcess.remainingTime-= remTime
                y.append(currentProcess.number)
                x.append(currentTime)
                currentProcess = -1
                if(len(workingQueue) != 0):
                    currentProcess = workingQueue.pop(0)
                if switchingTime > 0:
                    y.append(0)
                    x.append(currentTime)
                    currentTime+=switchingTime
                    y.append(0)
                    x.append(currentTime)
        else:
            currentTime+=0.01
            y.append(0)
            x.append(currentTime)
    plt.xticks(np.arange(math.ceil(currentTime+1)))
    plt.grid(b=None, which='major', axis='both')
    plt.plot(x, y, color='green', linestyle='solid', linewidth=1)
    plt.show()
        