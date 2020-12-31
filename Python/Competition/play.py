f = open("play.dat", 'r')
vals = f.readline()
num_list = vals.split(" ")
i = 0
while (i <= len(num_list) - 1):
	ck = 1
	chk = 1
	int_num = int(num_list[i])
	while (ck != int_num * 2):
		star = "*"
		print(star * chk)
		if (ck >= int_num):
			chk -= 2
		else:
			chk += 2
		ck += 1
	print("\n")
	i += 1
f.close()
