n = int(input())
numbers = list(map(int, input().split()))

result = ''
if sum(numbers) % 2 != 0:
    result = '+' * (n - 1)
else:
    for i in range(len(numbers) - 1):
        if numbers[i] % 2 != 0 and numbers[i + 1] % 2 != 0:
            result += 'x' + '+' * (n - 2 - i)
            break
        elif i == len(numbers) - 2:
            result += 'x'
        else:
            result += '+'

print(result)
