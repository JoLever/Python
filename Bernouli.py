## EE 381 Project2
## Bernoulli Trials, Boyes' Rule, and General Probability
## Jordan Lever
## 09-19-17
## These project demonstrates the bernouli trials

import math
print("Bernoulli trial simulaton.")

p = float(input("Enter the probability of success"))

k = int(input(" Enter the number of trials"))

#code reuase of generator

# the norm N is 100,000.
N = 100000
# the adder A is 4,857.
A = 4857
# the multiplier is 8,601
M = 8601
# End parameter declaration
#---------------------------

#Inputing initial seed
S=1
for i in range(k):
    S = (M*S + A)%N
    r = S/N
    if r < p: 
        print("Success")
        else:
        print("failure")
