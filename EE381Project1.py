# -*- coding: utf-8 -*-
#Psuedorandom number generator
#Jordan Lever
#8-31-2017
#This program generators 100 psuedorandom numbers
import math
#the norm N is 10,000
N = 10000
#THe adder A is 4,857
A = 4857
#THe multiplier is 8,601
M = 8601
# End parameter declaration
#-------------------------------
#Inputting initial seed
#S = int(input(" Enter an integer as a seed for the pseduorandom number generator"))
Can = [0,0,0]

S =0
# loop and formula for generator
for i in range(2):
    S = (M*S + A)%N
    r = S/N #float division is used to obtain numbers on (0,1)
   
    
    Can_Number = math.floor(r*5 +1)
    Can[i] = Can_Number
    print(Can)