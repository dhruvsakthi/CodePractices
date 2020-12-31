f = open("box.dat")
vals = int(f.readline())
i = 0
while(i < vals):
	j = 0
	val = int(f.readline())
	while(j < val - 1):
		if(j == val - 2 or j == 0): 
			print("#" * val)
		if(j == val - 2):
			print("\n")
		else: 
			print("#" + ("J" * (val - 2)) + "#")
		j += 1
	i += 1