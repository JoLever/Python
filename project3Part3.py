import random
#This is a simulation of a binomial distribution.

#The problem is a Binomially dristributed R.V.
#Let n the number of trials 
#success p between 0 and 1
#What is the probability of number of successes between low and high.

#Below is a frequency simulation program.

n = int(input("Enter the number of trials")) # The number of trials
p = float(input("Enter the probability of success")) # The probability of success
x_low = int(input("Enter the number of successes from the lowest")) #The number of successes.
x_high = int(input("Enter the number of successes from the highest"))

N = 50000 # The number of frequency repetitions. 


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

    if (s >= x_low) & (s <= x_high): 
        j = j + 1
        
prob = j/N
   

print(prob)