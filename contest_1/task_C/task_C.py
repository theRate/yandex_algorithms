n = int(input())
count = 0
result = 0
while count < n:
    count += 1
    a = int(input())
    result += a // 4
    rem = a % 4
    if rem == 0:
        continue
    elif rem == 1:
        result += 1
    else:
        result += 2

print(result)
