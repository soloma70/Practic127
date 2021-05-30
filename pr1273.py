per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}  # Объявление словаря процентов
money = float(input("money = "))  # Ввод суммы
deposit = [int(round(money * per_cent['ТКБ'] / 100, 0)), int(round(money * per_cent['СКБ'] / 100, 0)),
       int(round(money * per_cent['ВТБ'] / 100, 0)), int(round(money * per_cent['СБЕР'] / 100, 0))]  # Вычисление сумм депозитов
keys = list(per_cent.keys())  # Преобразование ключей в список
print("          ", keys[0], " ", keys[1], " ", keys[2], " ", keys[3])  # Вывод заголовков
print("deposit =", deposit)  # Вывод сумм депозитов
print("Максимальная сумма, которую вы можете заработать —", max(deposit))  # Вывод макс.суммы
