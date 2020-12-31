f = open("redgreen.dat")
num_data = int(f.readline())
i = 1
while (i <= num_data):
	inpt = f.readline()
	inpt = inpt.strip()
	time, speed = inpt.split(" ")
	time = float(time)
	speed = float(speed)
	print(str(round(time * speed), 2))
	i += 1
f.close()
