f = open("periods.dat")
num = int(f.readline())
i = 0
while i < num:
	string = f.readline()
	if (string.find(".") != -1):
		print(string) + "."
	else:
		print(string)