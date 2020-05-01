#Define the generator function factorial_gen, which is capable of yielding factorial values of natural numbers.
#For e.g : You should able to create a generator fs from factorial_gen and if fs is accessed using next for five times, then it should yield values 1, 1, 2, 6,24, 120,...

#Try it online https://code.sololearn.com/cDUtRHCE6nOL

def fact(n):
    
    def fac(x):
        if x == 0:
            return 1
        return x * fac(x -1)
        
    for i in range(n + 1):
        yield fac(i)


fs = fact(5)

#facto = [i for i in fs]
#print(facto)

for i in range(5):
    print(next(fs))
