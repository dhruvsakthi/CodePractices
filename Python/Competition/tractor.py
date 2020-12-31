
f = open("tractors.dat")
dim = int(f.readline())
# 2-d array define
column = []
for i in range(dim):
  column.append(list(f.readline()))
print(column)
i = 0
j = 0
while(i < dim):
	while(j < dim):
		if (column[i][j + 1] == "."):
			j += 1
		elif (column[i + 1][j] == '.'):
			if(i == (dim - 1) and j == (dim - 1)):
				print("success")
				break
			i += 
1		elif(column[i][j + 1] == 'x' and column[i + 1][j] == 'x'):
			print("no")
			break
		if(column[i][j + 1] == '\n'):
			if(i == (dim - 1) and j == (dim - 1)):
				print("success")
				break
			i += 1
		elif(column[i + 1][j] == '\n'):
			if(i == (dim - 1) and j == (dim - 1)):
				print("success")
				break
			j += 1


