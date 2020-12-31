f = open("card.dat")
num_lines = int(f.readline())
i = 0
while(i < num_lines):
	a = f.readline().strip()
	line = a.split(", ")
	line.sort()
	print(line)	
	i += 1