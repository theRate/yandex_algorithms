a, b = input(), input()  # первая и вторая строка
a_dict = {}
b_dict = {}

for char in a:
    if char in a_dict:
        a_dict[char] += 1
    else:
        a_dict[char] = 1

for char in b:
    if char in b_dict:
        b_dict[char] += 1
    else:
        b_dict[char] = 1

if a_dict == b_dict:
    print('YES')
else:
    print('NO')
