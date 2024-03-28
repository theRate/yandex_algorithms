n = int(input())
n_list = list(map(int, input().split()))
k = int(input())
k_list = []
for _ in range(k):
    k_list.append(list(map(int, input().split())))

n_list.sort()
result = []

for b in k_list:
    l = 0
    r = n - 1
    while l < r:
        m = (l + r) // 2
        if n_list[m] >= b[0]:
            r = m
        else:
            l = m + 1

    left_index = l
    r = n - 1
    while l < r:
        m = (l + r + 1) // 2
        if n_list[m] <= b[1]:
            l = m
        else:
            r = m - 1

    right_index = l

    if left_index == right_index and not b[0] <= n_list[left_index] <= b[1]:
        result.append(0)
    else:
        result.append(right_index - left_index + 1)

print(*result)
