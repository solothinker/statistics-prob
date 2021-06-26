import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)
from distributionLib import Dist
np.random.seed(404)
N = 1000000

data = np.random.choice([0, 1], size=(N,1), p=[0.57, 0.43])

for sample in range(100,10000,500):
    ind = np.random.randint(0,N,[sample,1])
    Dist.MOE(data[ind])
    
Dist.MOE(data)
