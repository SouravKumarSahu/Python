# Different prime number generators in python

from math import sqrt

# is it a prime number check function

def isPrime(num):
    
    if num <= 1: return False
    if num == 2: return True
    if num%2 == 0: return False
    
    for i in range(3, int(sqrt(num) + 1),2):
        if num % i == 0:
            return False
        
    return True

# generator with isPrime check > it is the best
def prime_num_gen_with_isPrime():
    i = 2
    while True:
        if isPrime(i): yield i
        i += 1
        
p_1 = prime_num_gen_with_isPrime()

# generator with recursive yield & yield from > shortest but ends with recursion error
def num_gen(n):
    yield n
    yield from num_gen(n+1)

n_gen = num_gen(2)

def prime_num_gen_with_recursion(gen):
    n = next(gen)
    yield n
    yield from prime_num_gen_with_recursion(i for i in gen if i%n != 0)
    
p_2 = prime_num_gen_with_recursion(n_gen)
