
def next_num(nx_num):
	exitl = False
	while (exitl == False):
		nx_num = int(nx_num) + 1
		sx_num = str(nx_num)
		if (sx_num.find("0") == -1):
			exitl = True
	return sx_num



f = open("zero.in")
num_datasets = int(f.readline())
i = 1
while (i <= num_datasets):
	value = f.readline()
	num = next_num(value)
	print(num)
	i += 1
f.close()