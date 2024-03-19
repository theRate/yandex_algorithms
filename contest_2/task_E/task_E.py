n = int(input())  # число ягод (дней)
berries = []
for i in range(n):
    berries.append(list(map(int, input().split())))
    berries[i].append(i + 1)

positive_list = []
negative_list = []

for i in berries:
    if i[0] > i[1]:
        positive_list.append(i)
    else:
        negative_list.append(i)

positive_list.sort(key=lambda x: x[1])
negative_list.sort(key=lambda x: x[0], reverse=True)
berries = positive_list + negative_list

if positive_list:
    result = 0
    for i in positive_list:
        result += i[0] - i[1]
    if negative_list:
        if positive_list[-1][1] > negative_list[0][0]:
            result += positive_list[-1][1]
        else:
            result += negative_list[0][0]
    else:
        result += positive_list[-1][1]
else:
    result = negative_list[0][0]

result_order = []
for i in berries:
    result_order.append(i[2])

print(result)
print(*result_order)
