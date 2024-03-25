def recurring_number(str1, str2):
    n, k = map(int, str1.split())
    n_list = list(map(int, str2.split()))

    result = 'NO'
    n_dict = {}
    for n, i in enumerate(n_list):
        if i in n_dict:
            n_dict[i][0] += 1
            n_dict[i][1].append(n)
        else:
            n_dict[i] = [1, [n]]

    for v in n_dict.values():
        if v[0] > 1:
            for i in range(len(v[1]) - 1):
                if v[1][i + 1] - v[1][i] <= k:
                    result = 'YES'

    return result
    

print(recurring_number(input(), input()))
