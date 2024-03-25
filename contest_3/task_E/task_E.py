def two_out_of_three(n1, l1, n2, l2, n3, l3):
    n1_list = list(map(int, l1.split()))
    n2_list = list(map(int, l2.split()))
    n3_list = list(map(int, l3.split()))

    result = set()

    for i in n1_list:
        if i in n2_list or i in n3_list:
            result.add(i)
    for i in n2_list:
        if i in n3_list:
            result.add(i)

    result = list(result)
    result.sort()

    return result


args = []
for _ in range(6):
    args.append(input())

print(*two_out_of_three(*args))
