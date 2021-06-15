import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)
np.random.seed(404)

sample = 100
bins = 4

data = np.random.choice([0, 1], size=(sample,), p=[0.57, 0.43])

suces = float(np.sum(data)/len(data))
fail = float((len(data)-np.sum(data))/len(data))

xBar = 0*fail+1*suces
var = fail*(0-xBar)**2+suces*(1-xBar)**2
sd = var**0.5

xDist = xBar*10*sd
xAxis = np.arange(-xDist,xDist,0.01)+xBar

normalDist = 1/(sd*(2*np.pi)**0.5)*np.exp(-((xAxis-xBar)/sd)**2*1/2)
yoX = np.arange(-sd*3,sd*4,sd)+xBar
normalDist2 = 1/(sd*(2*np.pi)**0.5)*np.exp(-((yoX-xBar)/sd)**2*1/2)

##plt.vlines(yoX,normalDist2*0,normalDist2,colors='teal')
plt.plot(xAxis,normalDist)
plt.scatter(yoX,normalDist2)

[plt.axvline(ii,ls='--') for ii in yoX]
plt.show()

##plt.hist(data,bins=bins)
##plt.xticks([0.125,0.875],["Fail","Success"])
##plt.show()
