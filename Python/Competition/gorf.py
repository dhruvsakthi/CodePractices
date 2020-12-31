f = open("gorf.dat")
i = 1
num_datasets = int(f.readline())
while (i <= num_datasets):
	values = f.readline()
	a, b, c = values.split(" ")
	a = float(a)
	b = float(b)
	c = float(c)
	Start_loc = (-b - ((b ** 2) - (4 * a * c))**.5) / (2 * a)
	End_loc = (-b + ((b ** 2) - (4 * a * c)) **.5) / (2 * a)
	Dist = End_loc - Start_loc
	print(str(abs(round(Dist, 1))))
	i += 1
f.close()