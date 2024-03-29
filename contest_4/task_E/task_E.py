def sum_arithmetic_sequence(a1, d, n):
    return n * (2 * a1 + (n - 1) * d) // 2


def create_list(n):
    my_list = list(range(1, n + 1))
    my_list += list(range(n - 1, 0, -1))
    return my_list


def divide_and_merge_list(input_list):
    middle_idx = len(input_list) // 2
    sublist1 = input_list[:middle_idx + 1]
    sublist2 = input_list[middle_idx + 1:]
    result_list = sublist2 + sublist1
    return result_list


n = int(input())
left, right = 1, n
while left < right:
    middle = (left + right) // 2
    if sum_arithmetic_sequence(3, 4, middle) >= n:
        right = middle
    else:
        left = middle + 1

index = n - sum_arithmetic_sequence(3, 4, left - 1) - 1
cnt_el = sum_arithmetic_sequence(3, 4, left) - sum_arithmetic_sequence(3, 4, left - 1)
flag = cnt_el // 2
numerator = 1
denominator = flag
if index <= flag:
    numerator += index
else:
    numerator = cnt_el - index

if index < flag:
    denominator -= index
else:
    denominator = index - flag + 1

print(numerator, denominator, sep='/')
