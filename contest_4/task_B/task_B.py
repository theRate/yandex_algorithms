def check(flagship, field):
    ship_counter = 0
    ship_length = 0
    ship_multiplier = 1
    while flagship != 0:
        ship_counter += ship_multiplier
        ship_length += flagship * ship_multiplier
        ship_multiplier += 1
        flagship -= 1

    return ship_length + ship_counter - 1 <= field


def naval_battle(n):
    l, r = 0, round(n ** 0.4)
    while l < r:
        m = (l + r + 1) // 2
        if check(m, n):
            l = m
        else:
            r = m - 1

    return l
    
print(naval_battle(int(input())))
