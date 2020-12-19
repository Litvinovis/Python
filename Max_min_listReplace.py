cases = [[1, [3, 4, 5, 2, 1],[3, 4, 1, 2, 5]],[2, [-3000, 3000], [3000, -3000]], [3, [1, 2, 3, 4, 5, 6, 7],[7, 2, 3, 4, 5, 6, 1]], [4, [-5, 5, 10],[10, 5, -5]]]

# Функция change_elems принимает список list_1
# Необходимо поменять местами максимальный и минимальный элементы
# Функция должна возвращать измененный список

def change_elems(list_1):
    new_list = []
    a = len(list_1) - 1
    b = 1
    max = 0
    min = 0
    while (b <= a):
      if (list_1[b] < list_1[min]):
        min = b
      if (list_1[b] > list_1[max]):
        max = b
      b += 1
    new_list = list_1.copy()
    new_list[max] = list_1[min]
    new_list[min] = list_1[max]
    return new_list

for i in cases:
    if change_elems(i[1]) == i[2]:
    	print("Test #" + str(i[0]) + ': OK!')
    else:
        print("Test #" + str(i[0]) + ': KO!')
