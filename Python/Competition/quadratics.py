f = open("quadratics.in")
num_datasets = int(f.readline())
i = 1
while (i <= num_datasets):
	val = f.readline()
	a, b, c = val.split(" ")
	a = float(a)
	b = float(b)
	c = float(c)
	x = (-b + ((b ** 2) - (4 * a * c)) ** .5) / (2 * a)
	y = (-b - ((b ** 2) - (4 * a * c)) ** .5) / (2 * a)
	x = round(x, 3)
	y = round(y, 3)
	x = str(x)
	y = str(y)
	print(x + "," + " " + y)
	i += 1
f.close()