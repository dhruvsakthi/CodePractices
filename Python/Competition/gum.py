f = open("gum.dat")
num_lines = sum(1 for line in f)
print(num_lines)