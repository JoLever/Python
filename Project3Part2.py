import random
#This is a simulation of a binomial distribution.

#The problem is a Binomially dristributed R.V.
#Let n the number of trials 
#success p between 0 and 1
#What is the probability of of x successes

#Below is a frequency simulation program.
# n =18 , succes = 5, rate is .25
n = int(input("Enter the number of trials")) # The number of trials
p = float(input("Enter the probability of success")) # The probability of success
x = int(input("Enter the number of successes")) #The number of successes.

N = 5000000 # The number of frequency repetitions. 


trial = [0] # List to record trial.
trial = trial*n
j = 0 #counter

for k in range(N):


    for i in range(n):
    
        r = random.uniform(0,1)
    
        if r < p:
            trial[i] = 1
        
        else:
            trial[i] = 0
        
        s = sum(trial)

    if s == x:  
        j = j + 1
        
prob = j/N
   

print(prob)