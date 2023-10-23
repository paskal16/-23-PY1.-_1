salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(1, 11):
    if i == 1:
        money_capital = spend-salary
    else:
        spend *= (1+increase)
        ost = salary-spend
        money_capital -= ost

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
