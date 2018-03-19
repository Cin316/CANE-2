import time

i = 0

startTime = time.time()
while startTime + 5 > time.time():
	print("test")
	i += 1

print(i)

