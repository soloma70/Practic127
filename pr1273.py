per = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} # Объявление словаря процентов
mon = float(input("Введите сумму вклада: ")) # Ввод суммы
dep = [int(round(mon * per['ТКБ'] / 100, 0)), int(round(mon * per['СКБ'] / 100, 0)),
       int(round(mon * per['ВТБ'] / 100, 0)), int(round(mon * per['СБЕР'] / 100, 0))] # Вычисление сумм депозитов
keys = list(per.keys()) # Преобразование ключей в список
print("          ", keys[0], " ", keys[1], " ", keys[2], " ", keys[3]) # Вывод заголовков
print("deposit =", dep) # Вывод сумм депозитов
print("Максимальная сумма, которую вы можете заработать —", max(dep)) # Вывод макс.суммы