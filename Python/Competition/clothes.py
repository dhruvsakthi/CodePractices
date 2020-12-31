f = open("clothes.dat")
nums = int(f.readline())
i = 0
while i < nums:
	num_data = int(f.readline())
	j = 0
	shirts = []
	socks = []
	pants = []
	while j < num_data:
		val = f.readline()
		a, b = val.split("(")
		a = a[0:-1]
		b = b[0:-2]
		if b == "shirt":
			shirts.append(a)
		elif b == "pants":
			pants.append(a)
		elif b == "socks":
			socks.append(a)
		j += 1
	shirts.reverse()
	socks.reverse()
	pants.reverse()
	count = 0
	low_count = 0
	if len(shirts) < len(pants) and len(shirts) < len(socks):
		low_count = len(shirts)
	elif len(pants) < len(shirts) and len(pants) < len(socks):
		low_count = len(pants)
	else:
		low_count = len(socks)
	while count < low_count:
		shirt = shirts[count]
		pant = pants[count]
		sock = socks[count]
		print("%s, %s, %s" %(shirt, pant, sock))
		count += 1
	if i != nums - 1:
		print("\n")
	i += 1