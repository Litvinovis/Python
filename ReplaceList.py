spis = [-10, 20]
a = len(spis) - 1
while (a >= 0):
	if (spis[a] > spis[a - 1]):
		spis[a] = spis[a] + spis[a - 1]
		spis[a - 1] = spis[a] - spis[a - 1]
		spis[a] = spis[a] - spis[a - 1]
	a -= 1
a = len(spis) - 1
while (a >= 0):
	print(spis[a])
	a -= 1
