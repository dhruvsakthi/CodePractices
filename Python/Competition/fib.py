def fib(n):
	if (n == 1):
		return 1
	else:
		return(fib(n-1) + fib(n-2))

n = int(input("Give me a number: "))
print(n)
