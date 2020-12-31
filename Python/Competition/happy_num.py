f = open("happy.dat")
num_val = int(f.readline())
i = 0
while (i < num_val):
	visited = set()
	val = f.readline()
	cur_num = val.strip()
	while(int(cur_num) != 1):
		j = 0
		sqr_sum = 0
		while(j < len(cur_num)):
			sqr_sum = sqr_sum + int(cur_num[j]) * int(cur_num[j])
			j += 1
		cur_num = str(sqr_sum)
		if(sqr_sum == 1):
			print("%s :-)" %(val))
			break
		elif cur_num in visited:
			print("%s :-(" %(val))
			break
		visited.add(cur_num)
	i += 1
f.close()
