import time

def SieveOfEratosthenes(n): 
       
    # Create a boolean array "prime[0..n]" and  
    # initialize all entries it as true. A value  
    # in prime[i] will finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n+1)] 
      
    p = 2
    while(p * p <= n): 
           
        # If prime[p] is not changed, then it is  
       # a prime 
        if (prime[p] == True): 
               
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    c = 0
  
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            # print(p)
            c += 1
    return c 
  
# Driver function 
# c = SieveOfEratosthenes(100000) 
# print("Total prime numbers in range:", c) 

def primeit(n):
    primes = []
    for i in range(2, n):
        isPrime = False
        for x in primes:
            if i % x == 0:
                isPrime = True
        if isPrime == False:
            primes.append(i)
    return primes

n = 10000
t0 = time.time() 
primeit(n)
print(time.time()-t0)

t0 = time.time()
SieveOfEratosthenes(n)
print(time.time() - t0)