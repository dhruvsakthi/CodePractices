f = open("ship.dat")
num_val = int(f.readline())
i = 0
while (i < num_val):
	val_2 = int(f.readline().strip())
	j = 0
	total = 0
	while (j < val_2):
		vals = f.readline().strip()
		a, b, c = vals.split(" ")
		total = total + (float(b) * float(c))
		j += 1
	print("%.02f" %(total))
	i += 1
