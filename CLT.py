# Central Limit Theorem
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)
from distributionLib import Dist
import os
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
np.random.seed(404)

N      = 20
p      = 0.8
N5,N25 = 5,25
temp5  = []
temp25 = []

data = Dist.binomialDist(N,p)
data = np.array(data)

xBar = np.mean(data)
var  = np.var(data)
sd   = np.sqrt(var)

plt.subplot(2,2,(1,3))
plt.plot([0,len(data)-1],[xBar,xBar],color='k',linestyle='--',label='mean={:.4f}'.format(xBar))
plt.bar(np.arange(len(data)),data)
plt.title('Random Distribution')
plt.legend()
plt.grid()

ax5 = plt.subplot(2,2,2)
ax25 = plt.subplot(2,2,4)

filenames = []
for ii in range(500):
    ax5.clear()
    ax25.clear()
    
    ind5  = np.random.randint(0, len(data), size=(N5,1))
    ind25 = np.random.randint(0, len(data), size=(N25,1))
    tempo5, tempo25 = np.mean(data[ind5]),np.mean(data[ind25])

    temp5.append(np.round(tempo5,4))
    temp25.append(np.round(tempo25,4))
    
    plt.subplot(2,2,2)
    sns.distplot(temp5,label='{} Samples mean={:.4f}'.format(N5,np.mean(temp5)))#, fit='norm', kde=False)
    plt.title('{} samples'.format(N5))
    plt.legend()
    plt.grid()
    
    plt.subplot(2,2,4)
    sns.distplot(temp25,label='{} Samples mean={:.4f}'.format(N25,np.mean(temp25)))
    plt.legend()
    plt.grid()
    plt.title('{} samples'.format(N25))

    plt.pause(0.0001)    
    plt.draw()
    if not ii%10:
        filename = f'{ii}.png'
        filenames.append(filename)
        plt.savefig(filename)
plt.close()
Dist.gif(filenames,'CLF.gif')

print("{} samples mean = {:.4f}".format(N5,np.mean(temp5)))
print("{} samples mean = {:.4f}".format(N25,np.mean(temp25)))

