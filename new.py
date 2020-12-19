cases = [[1, [1, 2, 3, 4, 5],[1, 3, 5]],[2, [9, 4, 5, 2, 3], [9, 5, 3]], [3, [7, 8],[7]], [4, [90, 45, 3, 43],[90, 3]]]

def find_even(list_1):
    even_list = []
    #Вставьте свой код ниже
    a = len(list_1) - 1
    c = 0
    while (a >= 0):
        if ((a % 2) == 0):
          b = list_1[a]
          even_list.insert(c, b)
          c += 1
        a -= 1
    return even_list
	

if __name__ == '__main__':
    
    for i in cases:
        if find_even(i[1]) == i[2]:
            print("Test #" + str(i[0]) + ': OK!')
        else:
            print("Test #" + str(i[0]) + ': KO!')