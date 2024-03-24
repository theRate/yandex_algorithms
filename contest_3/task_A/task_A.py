# n – количество человек в группе
# k - количество любимых треков члена группы

n = int(input())
playlist = set()
for _ in range(n):
    k = int(input())
    if playlist:
        playlist &= set(input().split())
    else:
        playlist |= set(input().split())

result = list(playlist)
result.sort()

print(len(result))
print(*result)
