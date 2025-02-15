# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr
x=int(input())
y=int(input())
fig, ax = plt.subplots()
matrix = np.array([[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0,]])
print(matrix)
plt.imshow(matrix, cmap='hot')
plt.title("CHESS BOARD")

#coordinates


circle = plt.Circle((x, y), radius=(0.4) , color='green')
for i in range(8):
    circle1 = plt.Circle((x+i, y+i), radius=(0.2), color='red')
    ax.add_patch(circle1)
    circle2 = plt.Circle((x -i, y + i), radius=(0.2), color='red')
    ax.add_patch(circle2)
    circle3 = plt.Circle((x - i, y - i), radius=(0.2), color='red')
    ax.add_patch(circle3)
    circle4 = plt.Circle((x + i, y - i), radius=(0.2), color='red')
    ax.add_patch(circle4)
    circle5 = plt.Circle((x + i, y ), radius=(0.2), color='red')
    ax.add_patch(circle5)
    circle6 = plt.Circle((x - i, y), radius=(0.2), color='red')
    ax.add_patch(circle6)
    circle7 = plt.Circle((x, y - i), radius=(0.2), color='red')
    ax.add_patch(circle7)
    circle8 = plt.Circle((x, y + i), radius=(0.2), color='red')
    ax.add_patch(circle8)

ax.add_patch(circle)
#ax.plot([0, 1], [0, 1], label="Прямая линия")
plt.show()
# facecolor='yellow'