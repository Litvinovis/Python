spis = [i for i in range(0,100)]
a = len(spis) - 1
while (a >= 0):
	if ((spis[a] % 2) == 0):
		print(spis[a])
	a -= 1