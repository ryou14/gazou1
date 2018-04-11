import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-1,1,0.01)
#f = lambda x: 1 - np.exp(x/400)
#y = 1 - np.exp(x/400)

#y = np.exp(x/2) - 1
y = x*x
y2 = 1 - np.exp(-x*x/0.16)

plt.plot(x,y) 
plt.plot(x,y2)

plt.legend(['y','y2'])

plt.show() 