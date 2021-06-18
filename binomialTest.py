import numpy as np
from distributionLib import Dist

binom = Dist.binomialDist
xBar = Dist.expt
var = Dist.var
coolPrint = Dist.coolPrint

# test-1
#A fair coin tossed 6 times. The probability of head coming is as follow
print('test-1')
n   = 6
p   = 0.5
P   = binom(n,p,plot=True)
coolPrint(P)
print('-'*80)

'''
test-2
https://www.statisticshowto.com/probability-and-statistics/binomial-theorem/binomial-distribution-formula/
Example-3
60% of people who purchase sports cars are men.  If 10 sports car owners are randomly
selected, find the probability that exactly 7 are men.
'''
print('test-2')
n = 10
p = 0.6
k = 7
prob = binom(10,0.6,7)
print('Answer = {}'.format(prob))

P = binom(10,0.6,plot=True)
coolPrint(P)

print('-'*80)






