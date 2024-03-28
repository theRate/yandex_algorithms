n, m = map(int, input().split())
n_list = tuple(map(int, input().split()))
m_list = []
for _ in range(m):
    m_list.append(tuple(map(int, input().split())))

pref_list = [0]
pref_sum = 0
for i in n_list:
    pref_sum += i
    pref_list.append(pref_sum)

for con in m_list:
    l, r = 0, n - con[0]
    while l < r:
        m = (l + r) // 2
        if pref_list[m + con[0]] - pref_list[m] >= con[1]:
            r = m
        else:
            l = m + 1
    if pref_list[l + con[0]] - pref_list[l] == con[1]:
        print(l + 1)
    else:
        print(-1)
