import random

#This is the solution to a specific problem.
#The problem is a Binomially dristributed R.V.
#Let n the number of trials be 5 with the probability of 
#success p equal to the 0.7.
#What is the probability of 3 successes

#Below is a frequency simulation program.

n = 5 # The number of trials
p = 0.7 # The probability of success
x = 3 #The number of successes.

N = 100 # The number of frequency repetitions. 


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