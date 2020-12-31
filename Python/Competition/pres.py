f = open("pres.dat")
num = int(f.readline().strip())
i = 0
pres = {
	"Washington" : 1,
	"Lincoln" : 5,
	"Hamilton" : 10,
	"Jackson" : 20,
	"Grant" : 50,
	"Franklin" : 100
}
while i < num:
	prs_lst = f.readline().split()
	total = 0
	for prs in prs_lst:
		total = total + pres.get(prs)
	print("$" + str(total))
	i += 1
	
'''
#	j = 0
#	a = 0
	total = 0
#	while j < len(prs_lst):
	for prs in prs_lst:
#		if prs_lst[j] in pres:
#			a = pres[prs_lst[j]]
		total = total + pres.get(prs)
#		j += 1
	print("$" + str(total))
	i += 1
'''