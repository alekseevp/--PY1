money_capital = 10000
salary = 5000
spend = 6000
increase = 1.05

survival = 0
month = 0  # количество месяцев, которое можно прожить


while survival >= 0:
    if month == 0:
        survival = money_capital - spend
        month = month + 1
    else:
        spend *= (1 + increase)
        survival = money_capital - spend + salary
        month = month + 1


print(month)
