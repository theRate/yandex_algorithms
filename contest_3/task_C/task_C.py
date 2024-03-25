#  n - количество элементов массива
#  a - сам массив чисел

n = int(input())
a = list(map(int, input().split()))

a_dict = {}
for i in a:
    if i in a_dict:
        a_dict[i] += 1
    else:
        a_dict[i] = 1

if len(a_dict) >= 2:
    max_cnt = 0
    max_keys = 0
    for k in a_dict.keys():
        if a_dict.get(k + 1, False):
            cnt = a_dict[k] + a_dict[k + 1]
            if cnt > max_cnt:
                max_cnt = cnt
                max_keys = k

    if max_cnt:
        del a_dict[max_keys]
        del a_dict[max_keys + 1]

        print(sum(a_dict.values()))
    else:
        print(n - 1)
else:
    print(0)
