print("Введите количество стартовых инвестиций")
start = int(input())
print("Введите среднюю ежегодную доходность в процентах")
profit = int(input())
print("Введите сумму ежемесячного пополнения")
month = int(input())
print("Введите срок инвестирования в годах")
years = int(input())
YearsToMonth = years * 12
MonthProfit = 1 + ((profit / 12) / 100)
selfmade = start + (month * YearsToMonth)
while (YearsToMonth > 0):
	start = (start * MonthProfit) + month
	YearsToMonth -= 1
print(f"Сумма через {years} лет = {start:,.2f}$")
print(f"Из них: ваших вложений = {selfmade:,.2f}$, накопленных процентов = {(start - selfmade):,.2f}$")
print(f"Ежемесячно можно получать без ущерба для капитала = {(start * (MonthProfit / 1001)):,.2f}$")
