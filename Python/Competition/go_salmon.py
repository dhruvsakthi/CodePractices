f = open("gosalmon.dat")
i = 1
num_set = int(f.readline())
while (i <= num_set):
	nums = f.readline()
	nums = nums.strip()
	val_1, val_2 = nums.split(" ")
	print(val_1, val_2)
	if (val_1 == val_2):
		print("PAIR")
	else:
		print("GO SALMON")
	i += 1