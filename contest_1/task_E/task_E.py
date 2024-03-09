n, k, d = map(int, input().split())
result = 0
for i in range(10):
    result = int(str(n) + str(i))
    if result % k == 0:
        break
    if i == 9 and result % k != 0:
        result = -1

if result != -1:
    result = str(result) + '0' * (d - 1)

print(result)
