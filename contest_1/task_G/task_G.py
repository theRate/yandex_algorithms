def calc(our_soldiers, barrack_hp, enemy_prod, hp):
    round_counter = 0  # считаем раунды
    enemy_soldiers = 0  # считаем солдатов противника

    while barrack_hp >= hp:  # пока мы не достигли предела, до которого атакуем казарму
        if enemy_soldiers >= our_soldiers:
            return 10 ** 9
        barrack_hp -= our_soldiers - enemy_soldiers
        enemy_soldiers = 0
        if barrack_hp > 0:  # если казарма не разрушена, она создает новых вражеских солдат
            enemy_soldiers += enemy_prod
        round_counter += 1

    while barrack_hp > 0:  # ломаем казарму
        if our_soldiers <= 0:
            return 10 ** 9
        if barrack_hp >= our_soldiers:
            barrack_hp -= our_soldiers
        else:
            enemy_soldiers -= our_soldiers - barrack_hp
            barrack_hp = 0
        our_soldiers -= enemy_soldiers
        if barrack_hp > 0:  # если казарма не разрушена, она создает новых вражеских солдат
            enemy_soldiers += enemy_prod
        round_counter += 1

    while enemy_soldiers > 0:  # добиваем вражеских солдат
        if our_soldiers <= 0:
            return 10 ** 9
        enemy_soldiers -= our_soldiers
        if enemy_soldiers > 0:
            our_soldiers -= enemy_soldiers
        round_counter += 1

    return round_counter


x = int(input())  # количество ваших солдат
y = int(input())  # количество очков здоровья казармы
p = int(input())  # количество производимых за раунд казармой солдат

count_enemies = 0  # количество вражеских солдат
result = 10 ** 9  # количество раундов

for i in range(y + 1):
    result = min(result, calc(x, y, p, i))

if result != 10 ** 9:
    print(result)
else:
    print(-1)
