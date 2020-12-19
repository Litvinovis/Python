print("Введите количество стартовых инвестиций")
start = input()
print("Введите среднюю ежегодную доходность")
profit = input()
print("Введите сумму ежемесячного пополнения")
month = input()
print("Введите количество лет для отслеживания")
years = input()
profit = int(profit)
start = int(start)
month = int(month)
years = int(years)
YearsToMonth = years * 12
MonthProfit = 1 + ((profit / 12) / 100)
while (YearsToMonth > 0):
	start = (start * MonthProfit) + month
	YearsToMonth -= 1
print(f"Сумма через {years} лет = {start:.2f}$, ежемесячно можно получать без ущерба для капитала = {(start * (MonthProfit / 1001)):.2f}$")	
