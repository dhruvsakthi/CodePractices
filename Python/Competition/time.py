a = input("Give me a time in this format [hour:minute]:  ")
hour, minute = a.split(":")
hour = int(hour)
minute = int(minute)
print(hour, minute)

if (hour == 12):
	hour = 0

min_degrees = (minute * 6)
hour_deg = (hour * 30)

print(min_degrees, hour_deg)

hour_degrees = hour_deg + ((minute/60) * 30)
print(hour_degrees)

total_degrees = abs(hour_degrees - min_degrees)
print(total_degrees)