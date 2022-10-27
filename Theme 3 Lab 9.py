salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

def needed_money(spend, increase):
    spend += spend * increase
    return spend


first_month = spend - salary
for month in range(9):
    need_money += needed_money(spend, increase) - salary
    spend = needed_money(spend,  increase)
need_money += first_month
print(round(need_money, 0))
