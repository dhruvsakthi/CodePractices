f = open("ornaments.in")
num_datasets = int(f.readline())
i = 1
while (i <= num_datasets):
	grandtotal = 0
	n = int(f.readline())
	while (n >= 1):
		x = (n * (n + 1)) / (2)
		grandtotal = grandtotal + x
		n -= 1
	print(grandtotal)
	i += 1
f.close()
