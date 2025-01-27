# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr
matrix = np.array([[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,]])
print(matrix)
plt.imshow(data, cmap='viridis')
plt.colorbar(label="Интенсивность")
plt.title("Тепловая карта")
plt.show()
def sdelai_docsku(board):
    board = np.zeros(shape:(size,size), dtype = int)