import random
N = 10000
results = {}

for i in range(2,13):
    
    results[i] = 0
    
for i in range(N):
    
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = x + y
    results[z]+=1

for i in results:
  
   print('The Probability of the number %d is: %.2f%%' %(i, (results[i])/(N)*100))
   
      
