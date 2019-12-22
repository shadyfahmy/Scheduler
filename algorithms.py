import operator

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
    waiting_time = np.zeros(len(processList))
    turnaround_time = np.zeros(len(processList))
    weighted_turnaround_time = np.zeros(len(processList))
    avg_turnaround_time = 0
    avg_weighted_turnaround_time = 0

    tempsave = np.copy(processList)
    print("HPF")
    Ticks = []
    Ticks.append("idle")
    for i,process in enumerate(processList):
        Ticks.append(str(i+1))
    plt.yticks(np.arange(len(processList)+1),Ticks)
    processList.sort(key=lambda x: x.startTime, reverse=False)
    currentTime = 0
    count = len(processList)
    x = []
    y = []
    readyQueue = []
    x.append(0)
    y.append(0)

    while (len(processList) > 0) or (len(readyQueue) > 0):
        for j in range(len(processList)):
            if processList[0].startTime <= currentTime:
                readyQueue.append(processList[0])
                #count = count - 1
                processList.remove(processList[0])
            else:
                break

        if len(readyQueue) > 0:
            readyQueue.sort(key=lambda x: x.priority, reverse=True)
            for k in range(len(readyQueue) - 1):
                if readyQueue[k].priority == readyQueue[k+1].priority:
                    if readyQueue[k+1].number < readyQueue[k].number:
                        temp = readyQueue[k]
                        readyQueue[k] = readyQueue[k+1]
                        readyQueue[k+1] = temp

            x.append(currentTime)
            y.append(readyQueue[0].number)
            waiting_time[readyQueue[0].number - 1] = currentTime - readyQueue[0].startTime
            currentTime = currentTime + readyQueue[0].burstTime
            turnaround_time[readyQueue[0].number - 1] = currentTime - readyQueue[0].startTime
            weighted_turnaround_time[readyQueue[0].number - 1] = turnaround_time[readyQueue[0].number - 1]/readyQueue[0].burstTime
            x.append(currentTime)
            y.append(readyQueue[0].number)
            readyQueue.remove(readyQueue[0])

        else:
            y.append(0)
            x.append(currentTime)
            currentTime = processList[0].startTime
            y.append(0)
            x.append(currentTime)

    avg_turnaround_time = np.sum(turnaround_time)/len(turnaround_time)
    avg_weighted_turnaround_time = np.sum(weighted_turnaround_time)/len(weighted_turnaround_time)

    file1 = open("Output.txt", "a")
    for i in range(len(tempsave)):
        L = str(tempsave[i].number)+"  \t" + str(waiting_time[tempsave[i].number - 1])+ " \t " + str(turnaround_time[tempsave[i].number - 1]) + "\t  " +str(weighted_turnaround_time[tempsave[i].number - 1])+ "\n"
        file1.write(L)

    file1.write(str(avg_turnaround_time) + "\n")
    file1.write(str(avg_weighted_turnaround_time) + "\n")
    file1.close()

    plt.xticks(np.arange(math.ceil(currentTime+1)))
    plt.grid(b=None, which='major', axis='both')
    plt.plot(x, y, color='green', linestyle='solid', linewidth=1)
    plt.show()


def FCFS(processList):
    tempsave = np.copy(processList)
    waiting_time = np.zeros(len(processList))
    turnaround_time = np.zeros(len(processList))
    weighted_turnaround_time = np.zeros(len(processList))
    avg_turnaround_time = 0
    avg_weighted_turnaround_time = 0

    print("FCFS")
    Ticks = []
    Ticks.append("idle")
    for i,process in enumerate(processList):
        Ticks.append(str(i+1))
    plt.yticks(np.arange(len(processList)+1),Ticks)
    processList.sort(key=lambda x: x.startTime, reverse=False)
    currentTime = 0
    x = []
    y = []
    x.append(0)
    y.append(0)

    for i in range(len(processList)):
        if processList[i].startTime <= currentTime:
            x.append(currentTime)
            y.append(processList[i].number)
            waiting_time[processList[i].number - 1] = currentTime - processList[i].startTime
            currentTime = currentTime+processList[i].burstTime
            x.append(currentTime)
            y.append(processList[i].number)

            turnaround_time[processList[i].number - 1] = currentTime - processList[i].startTime
            weighted_turnaround_time[processList[i].number - 1] = turnaround_time[processList[i].number - 1]/processList[i].burstTime

        else:
            y.append(0)
            x.append(currentTime)
            currentTime = processList[i].startTime
            y.append(0)
            x.append(currentTime)
            x.append(currentTime)
            y.append(processList[i].number)
            waiting_time[processList[i].number - 1] = currentTime - processList[i].startTime
            currentTime = currentTime + processList[i].burstTime
            x.append(currentTime)
            y.append(processList[i].number)

            turnaround_time[processList[i].number - 1] = currentTime - processList[i].startTime
            weighted_turnaround_time[processList[i].number - 1] = turnaround_time[processList[i].number - 1]/processList[i].burstTime

    avg_turnaround_time = np.sum(turnaround_time)/len(processList)
    avg_weighted_turnaround_time = np.sum(weighted_turnaround_time)/len(processList)

    file1 = open("Output.txt", "a")
    for i in range(len(tempsave)):
        L = str(tempsave[i].number)+"  \t" + str(waiting_time[tempsave[i].number - 1])+ " \t " + str(turnaround_time[tempsave[i].number - 1]) + "\t  " +str(weighted_turnaround_time[tempsave[i].number - 1])+ "\n"
        file1.write(L)

    file1.write(str(avg_turnaround_time) + "\n")
    file1.write(str(avg_weighted_turnaround_time) + "\n")
    file1.close()

    plt.xticks(np.arange(math.ceil(currentTime+1)))
    plt.grid(b=None, which='major', axis='both')
    plt.plot(x, y, color='green', linestyle='solid', linewidth=1)
    plt.show()

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
    Ticks.append("switching")
    for i,process in enumerate(processList):
        Ticks.append(str(i+1))
    plt.yticks(np.arange(count+2),Ticks)
    currentProcess = -1
    currentTime = 0
    switch = False
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
                            switch = True
                        
                processList.remove(processList[0])
            else:
                break
        if(switch):
            if switchingTime > 0:
                y.append(1)
                x.append(currentTime)
                currentTime+=switchingTime
                y.append(1)
                x.append(currentTime)
            switch = False
        if(currentProcess != -1):
            y.append(currentProcess.number+1)
            x.append(currentTime)
            if(incVal < currentProcess.remainingTime):
                currentProcess.remainingTime-= incVal
                currentTime+= incVal
                y.append(currentProcess.number+1)
                x.append(currentTime)
            else:
                remTime = currentProcess.remainingTime
                currentTime+= remTime
                currentProcess.remainingTime-= remTime
                y.append(currentProcess.number+1)
                x.append(currentTime)
                currentProcess = -1
                # if switchingTime > 0:
                #     switch = True

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
    Ticks.append("switching")
    for i,process in enumerate(processList):
        Ticks.append(str(i+1))
    plt.yticks(np.arange(count+2),Ticks)
    currentProcess = -1
    lastProcess = -1
    currentTime = 0
    switch = False
    while len(processList)>0 or len(workingQueue)>0 or currentProcess !=-1 or lastProcess !=-1:
        while(len(processList)>0):
            if (currentTime >= processList[0].startTime):
                if(currentProcess == -1):
                    if(lastProcess != -1):
                       switch = True
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
        if(switch):
            if switchingTime > 0:
                y.append(1)
                x.append(currentTime)
                currentTime+=switchingTime
                y.append(1)
                x.append(currentTime)
            switch = False
        if(currentProcess != -1):
            y.append(currentProcess.number+1)
            x.append(currentTime)
            if(quantumTime < currentProcess.remainingTime):
                currentProcess.remainingTime-= quantumTime
                currentTime+= quantumTime
                y.append(currentProcess.number+1)
                x.append(currentTime)
                lastProcess = currentProcess
                currentProcess = -1
                if(len(workingQueue) != 0):
                    currentProcess = workingQueue.pop(0)
                    switch = True
            else:
                remTime = currentProcess.remainingTime
                currentTime+= remTime
                currentProcess.remainingTime-= remTime
                y.append(currentProcess.number+1)
                x.append(currentTime)
                currentProcess = -1
                if(len(workingQueue) != 0):
                    currentProcess = workingQueue.pop(0)
                # if switchingTime > 0:
                #     switch = True
        else:
            currentTime+=0.01
            y.append(0)
            x.append(currentTime)
    plt.xticks(np.arange(math.ceil(currentTime+1)))
    plt.grid(b=None, which='major', axis='both')
    plt.plot(x, y, color='green', linestyle='solid', linewidth=1)
    plt.show()
        