import matplotlib.pyplot as plt

class process(object):
    def __init__(self, number, startTime, burstTime, priority):
        self.number = number
        self.startTime = startTime
        self.burstTime = burstTime
        self.priority = priority

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
def SRTN(processList):
    print("SRTN")

def RR(processList):
    print("rr")