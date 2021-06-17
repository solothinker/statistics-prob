# A library for understanding the different Probability distribution

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from tabulate import tabulate

plt.rcParams["figure.figsize"] = (20,10)
np.random.seed(404)

class Dist:
    def __init__(self):
        pass

    def MOE(rv,moe=0.95,plot=False):
        #Margin of Error
        
        pass
        
    def normalDist(self,xAxis=np.arange(-1,1.01,0.01),xBar=0,sd=1,plot=False):
        normalDist = 1/(sd*(2*np.pi)**0.5)*np.exp(-((xAxis-xBar)/sd)**2*1/2)
        if plot:
            plt.plot(xAxis,normalDist,label='Normal Distribution')
            plt.legend()
            plt.xlabel('Observed Value')
            plt.ylabel('Probability Density')
            plt.title('Normal Distribution')
            plt.grid()
            plt.show()
        return normalDist

    def __str__(self):
        return f"Distribution object"


    
    def zTable(x=0):

        def nCDF(x=0):
        # normal Cumulative Distribution Function
        # yup, I can use the normalDist object I am making it just for fun
            return 1/(np.sqrt(2*np.pi))*np.exp(-np.square(x)/2)
        if x:
            res, err = quad(nCDF,np.Inf, x)
            return np.round(res,5)
        else:
            columns=np.arange(0.00,0.1,0.01)
            index=np.round(np.arange(0.00,4.1,0.1),3)
            df = pd.DataFrame(columns=columns,index=index)
            for ii in index:
                for jj in columns:
                    df.loc[ii,jj],_ = np.round(np.abs(quad(nCDF,np.Inf, ii+jj)),5)
            print(tabulate(df, headers = 'keys', tablefmt = 'pretty'))

            
        
