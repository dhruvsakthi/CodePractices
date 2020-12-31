f = open("friends.dat")
num_data = int(f.readline().strip())
i = 0
while i < num_data:
  data = int(f.readline().strip())
  j = 0
  a = []
  while j < data:
    c, b = f.readline().strip().split(" ")
    #converting number to 3 character string and moving it to beginning
    vals = (("000" + b)[-3:]) + " " + c
    a.append(vals)
    j += 1
  a.sort(reverse=True)
  k = 0
  end_val = ""
  #To be able to print out only the names
  while k < len(a):
    if k == 0:
      end_val = a[k][4:]
    else:
      end_val = end_val + ", " + a[k][4:]
    k += 1
  print(end_val)
  i += 1
f.close()