# Central Limit Theorem
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)
from distributionLib import Dist
import os
import imageio
import warnings
warnings.filterwarnings("ignore")
np.random.seed(404)

N = 20
p = 0.8
N5,N25=5,25

data = Dist.binomialDist(N,p)
data = np.array(data)

xBar = np.mean(data)
var = np.var(data)
sd = np.sqrt(var)


plt.subplot(2,2,(1,3))
plt.plot([0,len(data)-1],[xBar,xBar],color='k',linestyle='--',label='mean={:.4f}'.format(xBar))
plt.bar(np.arange(len(data)),data)
plt.title('Random Distribution')
plt.legend()
plt.grid()
temp5  = []
temp25 = []

ax5 = plt.subplot(2,2,2)
ax25 = plt.subplot(2,2,4)

for ii in range(200):
    ax5.clear()
    ax25.clear()
    
    ind5  = np.random.randint(0, len(data), size=(N5,1))
    ind25 = np.random.randint(0, len(data), size=(N25,1))
    tempo5, tempo25 = np.mean(data[ind5]),np.mean(data[ind25])

    temp5.append(np.round(tempo5,4))
    temp25.append(np.round(tempo25,4))
    
    plt.subplot(2,2,2)
    hist5 = np.histogram(temp5,bins=10)
    plt.scatter(hist5[1][1:],hist5[0],color='k')
    plt.plot(hist5[1][1:],hist5[0],color='r')
    max5 = hist5[1][hist5[0].argmax()+1]    
    plt.axvline(max5,color='k',linestyle='--',label='{} Samples mean={:.4f}'.format(N5,max5))
    plt.title('{} samples'.format(N5))
    plt.legend()
    plt.grid()
    
    plt.subplot(2,2,4)
    hist25 = np.histogram(temp25,bins=10)
    plt.scatter(hist25[1][1:],hist25[0],color='k')
    plt.plot(hist25[1][1:],hist25[0],color='r')
    max25 = hist25[1][hist25[0].argmax()+1]
    plt.axvline(max25,color='k',linestyle='--',label='{} Samples mean={:.4f}'.format(N25,max25))
    plt.legend()
    plt.grid()
    plt.title('{} samples'.format(N25))

    plt.pause(0.0001)    
    plt.draw()



