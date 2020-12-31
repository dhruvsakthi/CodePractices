f = open("mathematics.in")
num_datasets = int(f.readline())
i = 1
grandtotal = 0
while(i <= num_datasets):
	value = int(f.readline())
	grandtotal = value + grandtotal
print(grandtotal)
f.close()