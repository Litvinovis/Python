spis = [1, 5, 1, 5, 1, 5]
a = len(spis) - 1
while (a >= 0):
	if (spis[a] > spis[a - 1]):
		print(spis[a])
	a -= 1