f = open("reverse.in")
b = 1
num_datasets = int(f.readline())
while(b <= num_datasets):
	values = f.readline()
	val1, i, j = values.split(" ")
	i = int(i)
	j = int(j)
	print (val1[0:i] + val1[j:])
f.close() 