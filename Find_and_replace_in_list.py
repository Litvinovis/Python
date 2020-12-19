cases = [[1, [1, 5, 2, 4, 3],[5, 4]],[2, [1, 2, 3, 4, 5], [2, 3, 4, 5]], [3, [5, 4, 3, 2, 1],[]], [4, [1, 5, 1, 5, 1],[5, 5]]]

# Функция find_more принимает список list_1
# Необходимо вытащить все элементы списка, которые больше предыдущего
# Функция должна возвращать список с этими элементами

def find_more(list_1):
    even_list = []
    #Вставьте свой код ниже
    a = len(list_1) - 1
    b = 1
    c = 0
    
    while (b <= a):
      if (list_1[b] > list_1[b - 1]):
        even_list.insert(c, list_1[b])
        c += 1
      b += 1
    return even_list

for i in cases:
    if find_more(i[1]) == i[2]:
          print("Test #" + str(i[0]) + ': OK!')
    else:
        print("Test #" + str(i[0]) + ': KO!')