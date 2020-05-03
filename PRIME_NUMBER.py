def isPrime(num):
    
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    
    return True

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
