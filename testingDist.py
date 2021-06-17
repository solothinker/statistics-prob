import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)
from distributionLib import Dist
np.random.seed(404)

sample = 100
bins = 4

data = np.random.choice([0, 1], size=(sample,), p=[0.57, 0.43])

suces = np.sum(data) 
fail = len(data)-np.sum(data)

xBar = (0*fail+1*suces)/len(data)
var = (fail*(0-xBar)**2+suces*(1-xBar)**2)/(len(data)-1)
sd = var**0.5

xDist = xBar*10*sd
xAxis = np.arange(-xDist,xDist,0.01)+xBar
yoX = np.arange(-sd*3,sd*4,sd)+xBar
sdOfSamp = sd/np.sqrt(sd)
print(sd,sdOfSamp)
normalDist = Dist.normalDist(xAxis,xBar,sd)
normalDist2 = Dist.normalDist(yoX,xBar,sd)

##plt.vlines(yoX,normalDist2*0,normalDist2,colors='teal')
##plt.plot(xAxis,normalDist)
##plt.scatter(yoX,normalDist2)
##
##[plt.axvline(ii,ls='--') for ii in yoX]
##plt.show()
