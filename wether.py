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
print("average temperature", s/365)

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

print("the longest sequence", zzz(a))

import matplotlib.pyplot as plt
import numpy as np

# Данные
x = np.linspace(1, 365, 365)  # 100 точек от -10 до 10
y = a

days = range(1, 366)
unique_temp, days = np.unique(a, return_counts=True)
plt.bar(unique_temp, days, color='red')
plt.title("Распределение температуры по дням")
plt.show()

# Построение графиков
plt.plot(x, y,  color="yellow")
for i in range(len(a)):
    temp = a[i]
    if temp < 0:
        plt.scatter([i], [temp], color='blue')
    if temp > 15:
        plt.scatter([i], [temp], color='red')

# Настройка
plt.title("как график на англ")
plt.xlabel("дэйз")
plt.ylabel("темпречер")
plt.show()







