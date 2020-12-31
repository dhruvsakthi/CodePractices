f = open("mathematics.dat")
i = int(f.readline())
j = 0
total = 0
while j< i:
	val = int(f.readline())
	total += val
	j+=1
print(total)