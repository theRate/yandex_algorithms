# пишем ввод
k = int(input())  # количество принимаемых пар координат
coords = []  # список для хранения координат
for n in range(k):
    coords.append(list(map(int, input().split())))  # добавляем координаты в список K-раз

zip_coords = list(zip(*coords))
min_x = min(zip_coords[0])
min_y = min(zip_coords[1])
max_x = max(zip_coords[0])
max_y = max(zip_coords[1])

print(min_x, min_y, max_x, max_y)
