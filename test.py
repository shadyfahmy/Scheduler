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

print(N)
print(processList[0].number)
print(processList[0].startTime)
print(processList[0].burstTime)
print(processList[0].priority)
print(len(processList))

x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2,4,1,5,2,6]

plt.plot(x, y, color='green', linestyle='solid', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)
plt.show()