board = [list('X' * 10)]
for _ in range(8):
    board.append(['X'] + list('*' * 8) + ['X'])
board.append(list('X' * 10))

n = int(input())  # количество выпиленных клеток
coords = []
for _ in range(n):
    i, j = map(int, input().split())
    board[i][j] = 'F'

di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)

p = 0
for i in range(1, 10):
    for j in range(1, 10):
        if board[i][j] == 'F':
            res = 4
            for step in range(4):
                if board[i + di[step]][j + dj[step]] == 'F':
                    res -= 1
            p += res

print(p)
