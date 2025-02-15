# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import numpy as np
a = np.random.randint(1,7,1000)
# Поиск уникальных значений
print('Исходный:', a) # [2 3 3 4 1 1 1 3 4 2]
print('Уникальные значения', np.unique(a)) # [1 2 3 4]
c  = np.unique(a, return_counts=True)
print(c)
g = c[1]
d1 = g[0]
d2 = g[1]
d3 = g[2]
d4 = g[3]
d5 = g[4]
d6 = g[5]
r1 = d1/1000
r2 = d2/1000
r3 = d3/1000
r4 = d4/1000
r5 = d5/1000
r6 = d6/1000
#for searching probability
for t in range(len(g)):
    w = g[t]/1000
    print(w)



# Функция для нахождения максимального количества подряд одинаковых значений
def zzz(okk):
    max_count = 0
    current_count = 1

    for i in range(1, len(okk)):
        if okk[i] == okk[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1

    return max(max_count, current_count)

print(zzz(a))


import matplotlib.pyplot as plt

categories = ["1", "2", "3", "4","5","6"]
values = [r1, r2, r3, r4,r5,r6]

plt.bar(categories, values, color='purple')
plt.title("Столбчатая диаграмма")
plt.show()

