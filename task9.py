salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
month = 0

earnings = salary * months

for x in range(months):
    if month == 0:
        month = month + 1
        spend_new = spend
    else:
        spend *= 1 + increase
        spend_new = spend_new + spend

balance = earnings - spend_new
need_money = - balance

print(round(need_money))
