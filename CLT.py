# Central Limit Theorem
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)
from distributionLib import Dist
import os
import imageio
np.random.seed(404)

N = 100
n = 10

##aa = np.random.randint([1, n], size=(N,1))
data = Dist.binomialDist(10,0.8)
data = np.array(data)
##weights = np.ones_like(aa) / len(aa)
##rDist = np.histogram(aa,weights=weights)
##data = np.round(rDist[0],4)

##Dist.coolPrint(data)
xBar = Dist.expt(data)
var = Dist.var(data)
sd = np.sqrt(var)


xPosition = [xBar-sd,xBar+sd]
plt.subplot(2,2,(1,3))
for ii in xPosition:
    plt.axvline(x=ii,color='k',linestyle='--')
plt.axvline(x=xBar,color='r',linestyle='--')

plt.bar(np.arange(len(data)),data)
plt.title('Random Distribution')
temp5  = []
temp25 = []
N5,N25=5,25
ax5 = plt.subplot(2,2,2)
ax25 = plt.subplot(2,2,4)
for ii in range(100):
    ax5.clear()
    ax25.clear()
    
    ind5  = np.random.randint(0, len(data), size=(N5,1))
    ind25 = np.random.randint(0, len(data), size=(N25,1))
##    tempo5, tempo25 = Dist.expt(ind5,data[ind5]), Dist.expt(ind25,data[ind25])
    tempo5, tempo25 = np.mean(ind5),np.mean(ind25)
    temp5.append(np.round(tempo5,4))
    temp25.append(np.round(tempo25,4))
    
    plt.subplot(2,2,2)
    plt.hist(temp5)
    plt.title('5 sample')
    
    plt.subplot(2,2,4)
    plt.hist(temp25)
    plt.pause(0.0001)

    plt.draw()
##plt.show()

##xBar = 
##print()
##print(Dist.var(rDist[0]))
##from distributionLib import Dist
##x = [1,2,3,4,5,6]
##y = [0.1,	0.1,	0.1,	0.1,	0.1,	0.5]
##print(Dist.expt(y))
