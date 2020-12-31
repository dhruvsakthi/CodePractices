f = open("exam.dat")
dat = int(f.readline())
i = 0
while i < dat:
	f_cor = int(f.readline().strip())
	me = f.readline().strip()
	f_as = f.readline().strip()
	j = 0
	me = list(me)
	f_as = list(f_as)
	s_cor = 0
	n = len(me)
	while j < n:
		if me[j] == f_as[j]:
			s_cor += 1
		j += 1
	print(n - (abs(f_cor - s_cor)))
	i += 1
