def mark_attacked_fields(di, dj, field):
    for trend in range(4):
        ni, nj = i + di[trend], j + dj[trend]
        while field[ni][nj] == '*' or field[ni][nj] == 'a':
            field[ni][nj] = 'a'
            ni += di[trend]
            nj += dj[trend]


board = [list('X' * 10)]
for _ in range(8):
    board.append(['X'] + list(input().strip()) + ['X'])
board.append(list('X' * 10))

for i in range(1, 10):
    for j in range(1, 10):
        if board[i][j] == 'R':
            si = [-1, 0, 1, 0]
            sj = [0, 1, 0, -1]
            mark_attacked_fields(si, sj, board)
        if board[i][j] == 'B':
            si = [-1, 1, 1, -1]
            sj = [1, 1, -1, -1]
            mark_attacked_fields(si, sj, board)

result = 0
for row in board:
    for cell in row:
        if cell == '*':
            result += 1

print(result)
