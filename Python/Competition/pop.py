# Dhruv Sakthivel Populations March 9
#Open File, read the number of datasets that follow, and create a loop with a counter, i.
f = open("pop.dat")
num = int(f.readline().strip())
i = 0
while i < num:

	# Read the line, the begginning pop, and the time allotted
	p, t = f.readline().split(" ")
	p = int(p)
	t = int(t)
	# Devide the time by 7 and 4, to get the number of deaths and births, respectively.
	death = int(t / 7)
	birth = int(t / 4)
	# Subtract the deaths from the birth to find the amount of new peeps, and add to old population
	rem = birth - death
	tot = rem + p
	print(int(tot))
	i += 1z4trfd