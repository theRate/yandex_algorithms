n = int(input())
lst_lens = list(map(int, input().split()))
max_len = max(lst_lens)
sum_len = sum(lst_lens)
if max_len > sum_len - max_len:
    result = max_len * 2 - sum_len
elif max_len == sum_len - max_len:
    result = max_len * 2
else:
    result = sum_len

print(result)
