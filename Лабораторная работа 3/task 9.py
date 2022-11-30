salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
summa = spend
money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(2, months + 1):
    spend = spend * 1.03
    summa += spend

print(round((summa - salary * months) // 1))
