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

    def recursion(n):
        if n==1 or n==0:
            return 1
        return n*Dist.recursion(n-1)

    def nPr(n,r):
        return Dist.recursion(n)/Dist.recursion(n-r)
    
    def nCr(n,r):
        return Dist.recursion(n)/(Dist.recursion(r)*Dist.recursion(n-r))
    
    def binomialDist(n,p=0.5,*args,plot=False):
        def Cal(n,p,k):
            test = Dist.nCr(n,k) * p**k * (1-p)**(n-k)
            return np.round(test,4)
        
        temp = []
        if not len(args):
            for k in range(n+1):
                cal = Cal(n,p,k)
                temp.append(cal)
                
            if plot:

                plt.bar(np.arange(n+1),temp)
                plt.xlabel('Observed Value')
                plt.ylabel('Probability Density')
                plt.title('Binomial Distribution')
                plt.grid()
                plt.draw()
                plt.waitforbuttonpress(0) 
                plt.close()
        else:
            k=args[0]
            temp = Cal(n,p,k)
        return temp
            
    def expt(x):
        xBar=0
        for ii,jj in enumerate(x):
            xBar += ii*jj
        return np.round(xBar,4)
    
    def var(x):
        xVar = 0
        xBar = Dist.expt(x)
        for ii,jj in enumerate(x):
            xVar += jj*np.square(xBar-ii)
        return np.round(xVar,4)
        
    def MOE(rv,moe=0.95,plot=False):
        #Margin of Error
        
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
        return normalDist

    def __str__():
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

    def coolPrint(P):
        xP  = Dist.expt(P)
        x2P = Dist.var(P)
        sd  = np.sqrt(x2P)
        print("Binomial Distribution = {}".format(P))
        print("                 Mean = {}".format(xP))
        print("             Variance = {}".format(x2P))
        print("   Standard deviation = {:.4f}".format(sd))

            
        
