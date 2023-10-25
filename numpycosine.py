#!/usr/bin/env python3


import numpy as np
import math
import matplotlib.pyplot as plt

'''def f(x):
    return np.cos(x)
def g(x):
    return np.sin(x)'''

n = 5000 #number of jumpsx)
a = -(np.pi / 2.0) + 1e-1#beginning of range
b = (np.pi / 2.0) #end of range

dx = (b - a)/n
domain = np.arange(a, b, dx)

'''plt.plot(x, f(x), color = 'green')
plt.plot(x, g(x), color = 'purple')
#plt.scatter(X, Y, color = 'green')
plt.show()'''

'''y = [math.cos(x) for x in domain]
plt.plot(x, y)'''

y = [math.tan(x) for x in domain]
plt.plot(domain, y)
plt.show()

