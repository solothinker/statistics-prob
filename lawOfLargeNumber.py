# Law of large numbers
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)
from distributionLib import Dist
import os
import imageio
np.random.seed(404)

N = 1000

data = np.random.choice([0, 1], size=(N,1), p=[0.49, 0.51])
E_x = np.sum(data)/N

sampleLook = 801
temp = 0
yData = []
xData = []
sample = 100

plt.plot([0,sampleLook],[E_x,E_x],'r--',label='E(x)')
plt.ylim(E_x - E_x/20, E_x +E_x/20)
plt.xlim(0,sampleLook)
plt.title('Law of Large Numbers')
plt.xlabel('Number of samples')
plt.ylabel('Mean of sample Data')
filenames = []
for ii in range(sampleLook):
    tSample = np.random.randint(0, N,size=(sample,1))
    temp += np.mean(data[tSample])
    if not ii%10:
        if not ii:
            plt.scatter(ii,temp/(ii+1),color='k',label='Sample Data mean')
            plt.legend()
        else:
            plt.scatter(ii,temp/(ii+1),color='k')
        filename = f'{ii}.png'
        filenames.append(filename)
        plt.pause(0.00001)
        plt.draw()
        plt.savefig(filename)

with imageio.get_writer('mygif.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
        
# Remove files
for filename in set(filenames):
    os.remove(filename)
    
