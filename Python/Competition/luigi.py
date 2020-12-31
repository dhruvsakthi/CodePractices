f = open("Lugi.dat")
num_lines = int(f.readline())
i = 0
while(i < num_lines):
	line = f.readline()
	if (line.find("Mario") != -1):
		print(line.replace("Mario", "Luigi"))
	elif(line.find("Mario") == -1):
		print(line)
	i += 1
f.close()