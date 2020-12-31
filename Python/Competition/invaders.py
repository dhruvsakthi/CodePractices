f = open("invaders.dat")
numval = int(f.readline())
i = 0
while(i < numval):
	a = f.read()
	print(a)
	i += 1