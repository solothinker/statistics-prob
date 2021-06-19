import numpy as np
from distributionLib import Dist

pois = Dist.poissonDist
xBar = Dist.expt
var = Dist.var
coolPrint = Dist.coolPrint
#test-1
'''
https://en.wikipedia.org/wiki/Poisson_distribution
Example
Ugarte and colleagues report that the average number of goals in a World Cup
soccer match is approximately 2.5 and the Poisson model is appropriate.
Because the average event rate is 2.5 goals per match, λ = 2.5.
'''
print('Test-1')
Lambda=2.5
k = 10 #(number of goals in match)
P = pois(Lambda,k,plot=True)
coolPrint(P)
print('-'*80)

# test-2
'''
https://www.intmath.com/counting-probability/13-poisson-probability-distribution.php
If electricity power failures occur according to a Poisson distribution with an
average of display 3 failures every twenty weeks, calculate the probability that
there will not be more than one failure during a particular week.
'''
Lambda = 3./20
k = 10
P = pois(Lambda,k,plot=True)
coolPrint(P)
#more than one failure
print('Number of Failure = {}'.format(np.sum(P[:2])))
print('-'*80)
