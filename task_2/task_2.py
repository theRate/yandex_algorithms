first_match = input().split(':')
second_match = input().split(':')
flag = int(input())

result = None
score_1st = int(first_match[0]) + int(second_match[0])
score_2nd = int(first_match[1]) + int(second_match[1])

if score_1st > score_2nd:
    result = 0
elif score_1st == score_2nd and flag == 1:
    if int(second_match[0]) > int(first_match[1]):
        result = 0
    else:
        result = 1
elif score_1st == score_2nd and flag == 2:
    if int(first_match[0]) > int(second_match[1]):
        result = 0
    else:
        result = 1
else:
    diff = score_2nd - score_1st
    if flag == 1 and int(second_match[0]) + diff > int(first_match[1]):
        result = diff
    elif flag == 2 and int(first_match[0]) > int(second_match[1]):
        result = diff
    else:
        result = diff + 1

print(result)
