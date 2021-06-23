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
        '''Factorial Function using recursion'''
        if n==1 or n==0:
            return 1
        return n*Dist.recursion(n-1)

    def nPr(n,r):
        ''' Permutations '''
        return Dist.recursion(n)/Dist.recursion(n-r)
    
    def nCr(n,r):
        '''Combination'''
        return Dist.recursion(n)/(Dist.recursion(r)*Dist.recursion(n-r))
    
    def expt(*args):
        ''' Expectation'''
        
        if len(args) == 1:
            y = args[0]
            x = np.arange(len(y))
        else:
            x = args[0]
            y = args[1]

        xBar=0
                   
        if np.round(np.sum(y),2) == 1:
            for ii,jj in enumerate(y):
                xBar += x[ii]*jj
        else:
            xBar = np.mean(x)
            
        return np.round(xBar,4)
    
    def var(*args,sample=False):
        ''' Variance''' 
        
        xVar = 0
        if len(args) == 1:
            y = args[0]
            x = np.arange(len(y))
        else:
            x = args[0]
            y = args[1]
            
        if np.round(np.sum(y),2) == 1:
            xBar = Dist.expt(x,y)
            for ii,jj in enumerate(y):
                xVar += x[ii]**2 * jj
            xVar -= xBar**2

        else:
            xBar = np.mean(y)
            for ii in y:
                xVar += np.square(ii-xBar)
            if sample:
                xVar /= (len(y)-1)
            else:
                xVar /= len(y)
        
        return np.round(xVar,4)

    def binomialDist(n,p=0.5,*args,plot=False):
        ''' Binomial Distribution Function'''
        def Cal(n,p,k):
            test = Dist.nCr(n,k) * p**k * (1-p)**(n-k)
            return np.round(test,4)
        
        temp = []
        if not len(args):
            for k in range(n+1):
                cal = Cal(n,p,k)
                temp.append(cal)
                
            if plot:
                Dist.tolp(np.arange(n+1),temp,title='Normal Distribution')
        else:
            k=args[0]
            temp = Cal(n,p,k)
        return temp
            
    def poissonDist(lam=1,k=1,plot=True):
        def Cal(lam,k):
            return np.round(lam**k * np.exp(-lam) / Dist.recursion(k),4)
        temp = []
        if plot:
            for ii in range(k+1):
                temp.append(Cal(lam,ii))
            Dist.tolp(np.arange(0,k+1),temp,plot='bar',title='Poisson Distribution')
        else:
            temp = Cal(lam,k)
        return temp
        
    def MOE(rv,moe=0.95,plot=False):
        #Margin of Error
        
        pass

    
    def normalDist(xAxis=np.arange(-1,1.01,0.01),xBar=0,sd=1,plot=False):
        ''' Normal Distribution Function'''
        normalDist = 1/(sd*(2*np.pi)**0.5)*np.exp(-((xAxis-xBar)/sd)**2*1/2)
        if plot:
            Dist.tolp(xAxis,normalDist,'Normal Distribution',plot='bar')
        return normalDist

    def __str__():
        return f"Distribution object"


    
    def zTable(x=0):
        '''Generating z-table'''
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

    def coolPrint(*args):
        '''printing necessary information'''
        if len(args) == 1:
            P = args[0]
            x = np.arange(len(P))
        else:
            x = args[0]
            P = args[1]
            
        xP  = Dist.expt(x,P)
        x2P = Dist.var(x,P)
        sd  = np.sqrt(x2P)
        print("      Distribution = {}".format(P))
        print("              Mean = {}".format(xP))
        print("          Variance = {}".format(x2P))
        print("Standard deviation = {:.4f}".format(sd))

    def tolp(x=0,y=0,plot='plot',title='yo Distribution'):
        ''' Single Plot function '''
        
        if plot == 'plot':
            plt.plot(x,y)
        elif plot == 'bar':
            plt.bar(x,y,width=0.2)
        plt.xlabel('Observed Value')
        plt.ylabel('Probability Density')
        plt.title(title)
        plt.grid()
        plt.draw()
        plt.waitforbuttonpress(0) 
        plt.close()

            
        
