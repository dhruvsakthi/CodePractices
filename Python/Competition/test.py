digits = ["11", "2", "3"]
digits.sort(reverse = True)
print(digits)
if len(digits) < 3:
	for digit in digits:
		digit = ("0" * (3 - len(digit))) + digit	
print(digits)