cases = [[1, [1, 2, 3, 4, 5],[1, 3, 5]],[2, [9, 4, 5, 2, 3], [9, 5, 3]], [3, [7, 8],[7]], [4, [90, 45, 3, 43],[90, 3]]]

def find_even(list_1):
    even_list = []
    a = len(list_1) - 1
    c = 0
    d = 0
    
    while (d <= a):
        if ((d % 2) == 0):
          b = list_1[d]
          even_list.insert(c, b)
          c += 1
        d += 1
    return even_list
	
for i in cases:
    if find_even(i[1]) == i[2]:
        print("Test #" + str(i[0]) + ': OK!')
    else:
        print("Test #" + str(i[0]) + ': KO!')