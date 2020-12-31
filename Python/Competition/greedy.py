f = open("greedy.dat")
num_data = int(f.readline().strip())
i = 0
while i < num_data:
	n, c = f.readline().split(" ")
	c = int(c)
	n = int(n)
	cashiers = []
	j = 0
	cust = f.readline().split(" ")
	sec = ""
	while j < n:
		cashiers.append(int(cust[j]))
		sec = sec + str(j + 1) + " "
		j += 1
	while j < c:
		low_idx = cashiers.index(min(cashiers))
		sec = sec + str(low_idx + 1) + " "
		cashiers[low_idx] = int(cust[j]) + cashiers[low_idx]
		j += 1

	print(sec)
	i += 1