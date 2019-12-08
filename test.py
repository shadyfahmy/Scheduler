import operator

import matplotlib.pyplot as plt

processList = []

class process(object):
    def __init__(self, number, startTime, burstTime, priority):
        self.number = number
        self.startTime = startTime
        self.burstTime = burstTime
        self.priority = priority

f = open("input.txt", "r")
if f.mode == 'r':
    lines = f.readlines()
N = lines[0]

for i in range(1, int(N)+1):
    processList.append(process(int(lines[i].split()[0]), int(lines[i].split()[1]), int(lines[i].split()[2]), int(lines[i].split()[3])))

processList = sorted(processList, key=operator.attrgetter("priority", "number"), reverse=True)

for i in range(len(processList)):
    print(processList[i].number)