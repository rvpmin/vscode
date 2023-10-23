#!/usr/bin/env python3


import math
import matplotlib.pyplot as plt

def f(x):
    y = math.cos(x)
    return y
def g(x):
    y = math.sin(x)
    return y

n = 500 #number of jumpsx)
a = 0 #beginning of range
b = 10 * 2 * 3.1416 #end of range

dx = (b - a)/n
values = range(n + 1)
X = []
Y = []

Y1 = []
x = a
for jump in values:
    x = a + jump * dx
    y = f(x)
    y1 = g(x)
    X.append(x)
    Y.append(y)
    Y1.append(y1)
    print(x)

plt.plot(X, Y, color = 'green')
plt.plot(X, Y1, color = 'purple')
#plt.scatter(X, Y, color = 'green')
plt.show()


