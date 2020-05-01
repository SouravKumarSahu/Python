#Define the generator function fib_gen, which is capable of yielding values of infinite fibonacci series.
#For e.g : You should able to create a generator fs from fib_gen and if fs is accessed using next for four times, then it should yield values 0, 1, 1, 2.
#To use yield generator must have loop inside itself

#Try it online https://code.sololearn.com/cBcy1fmlCoiB

def fsg(n):
    x, y = 0, 1
    while x >= 0 and x <= n:
        yield x
        x, y = y, x+y
        
fs = fsg(50)

#next(fs)

#febo = [i for i in fs]
#print(febo)

for i in range(5):
    print(next(fs))
