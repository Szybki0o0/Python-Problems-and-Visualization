import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
N = 15
count = 0
y = []
def collatz(num):
    return num//2 if num%2==0 else num*3+1

while N > 1:
    y.append(collatz(N))
    N = collatz(N)
    count+=1

x = np.linspace(1,count,count)
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)
plt.show()