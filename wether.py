# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import numpy as np
import matplotlib as plt
a = np.random.randint(-10,36,365)
# Поиск уникальных значений
print('Исходный:', a) # [2 3 3 4 1 1 1 3 4 2]
print('Уникальные значения', np.unique(a)) # [1 2 3 4]
c  = np.unique(a, return_counts=True)
print(c)
#average temperature
s = 0
for i in range(len(a)):
    s = s +a[i]
print(s/365)

x= 0
for t in range(len(a)):
    if a[t] > 25:
        x = x +1
print(x)



#function for serching the longest sequence
def zzz(okk):
    max_count = 0
    current_count = 1

    for i in range(1, len(okk)):
        if okk[i] < 0:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1

    return max(max_count, current_count)

print(zzz(a))
