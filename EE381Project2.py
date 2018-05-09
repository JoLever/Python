## EE 381 Project2
## Bernoulli Trials, Boyes' Rule, and General Probability
## Jordan Lever
## 09-19-17
## These project demonstrates the balls and cans
# ------------------------------------
import math
#print('Bernoulli trial simulation.')

#p = float(input('Enter the probability of success.  '))
#k = int(input('Enter the number of trials.   '))

#code reuase of generator

# the norm N is 100,000.
N = 100000
# the adder A is 4,857.
A = 4857
# the multiplier is 8,601
M = 8601
# End parameter declaration
#--------------------------

# Declare a list for the containers.
Balls = [0,0,0]

# Initialize counters
Sum_One = 0

Sum_Two = 0
# inputting initial seed
S = 0

# Loop and formula for generator

K = int(input('Enter the number of experiments. '))

for k in range(K):
    # Below generator
    for i in range(3):
        S = (M*S + A)%N
        r = S/N #Float division is used to obtain the numbers on [0,1)
        # Generate numbers 1 through 5
        Can_Number = math.floor(r*5 + 1)
        #Fill list
        Balls[i] = Can_Number
        # Test 
        if (i == 2) & ((Balls[0]!= Balls[1]) & (Balls[1] != Balls[2]) & (Balls[0] != Balls[2])):
            Sum_One = Sum_One + 1    
            #print('distinct', Balls)
        elif (i == 2):
            Sum_Two = Sum_Two + 1
            #print('not', Balls)
print(Sum_One/(Sum_One + Sum_Two))