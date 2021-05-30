per = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
mon = float(input("Введите сумму вклада: "))
dep = [int(round(mon * per['ТКБ'] / 100, 0)), int(round(mon * per['СКБ'] / 100, 0)),
       int(round(mon * per['ВТБ'] / 100, 0)), int(round(mon * per['СБЕР'] / 100, 0))]
keys = list(per.keys())
print("          ", keys[0], " ", keys[1], " ", keys[2], " ", keys[3])
print("deposit =", dep)
print("Максимальная сумма, которую вы можете заработать —", max(dep))