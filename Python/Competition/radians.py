f = open("radians.dat", "r")
i = 0
vals = f.readlines()
while(i < len(vals)):
	a = int(vals[i])
	if (a == 180):
		print("%d degrees = PI radians" % (a))
	elif (a/180 < 1):
		print("%d degrees = %.02fPI radians" %(a, a/180))
	else:
		print("%d degrees = %dPI radians" %(a, a/180))
	i += 1