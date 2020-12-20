def plus(a, c):
	result = a + c
	return result

def minus(a, c):
	result = a - c
	return result

def inc(a, c):
	result = a * c
	return result

def sub(a, c):
	result = a / c
	return result

def incre(a, c):
	result = a ** c
	return result

def rest(a, c):
	result = a % c
	return result

print(f"Введите целое число")
a = int(input())
print(f"Введите арифметическую операцию (+, -, /, *, %, **)")
b = input()
print(f"Введите второе целое число")
c = int(input())
result = 0
if (b == '+'):
	result = plus(a, c)
elif (b == '-'):
	result = minus(a, c)
elif (b == '*'):
	result = inc(a, c)
elif (b == '/'):
	result = sub(a, c)
elif (b == '**'):
	result = incre(a, c)
elif (b == '%'):
	result = rest(a, c)
else:
	print("Введен некорректный знак операции")
	exit
print(f"Ответ = {result}")