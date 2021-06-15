# A library for understanding the different Probability distribution

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)
np.random.seed(404)

class Dist:

    def MOE(rv,moe=0.95,plot=False):
        pass
        
    def normalDist(xAxis=np.arange(-1,1.01,0.01),xBar=0,sd=1,plot=False):
        normalDist = 1/(sd*(2*np.pi)**0.5)*np.exp(-((xAxis-xBar)/sd)**2*1/2)
        if plot:
            plt.plot(xAxis,normalDist,label='Normal Distribution')
            plt.legend()
            plt.xlabel('Observed Value')
            plt.ylabel('Probability Density')
            plt.title('Normal Distribution')
            plt.grid()
            plt.show()
        return xAxis,normalDist
        
