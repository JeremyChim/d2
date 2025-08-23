def change_items(path, save_path, xp, gold, attack_speed, attack_damage, magic_damage, move_speed, move_speed2):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    data_new = data.copy()
    change_index_and_line = {}
    for i, line in enumerate(data):
        if '// Hand of Midas' in line:
            print(i + 1, line, end='')
            for i2, line2 in enumerate(data[i:], i):
                if 'xp_multiplier' in line2:
                    line2_new = line2.replace('2.1', f'{xp}')
                    change_index_and_line[i2] = line2_new
                    print(i2 + 1, line2_new, end='')
                if 'bonus_gold' in line2:
                    line2_new = line2.replace('160', f'{gold}')
                    change_index_and_line[i2] = line2_new
                    print(i2 + 1, line2_new, end='')
                    break

        if '// Moon Shard' in line:
            print(i + 1, line, end='')
            for i2, line2 in enumerate(data[i:], i):
                if 'consumed_bonus' in line2:
                    line2_new = line2.replace('60', f'{attack_speed}')
                    change_index_and_line[i2] = line2_new
                    print(i2 + 1, line2_new, end='')
                    break

        if '// Rapier' in line:
            print(i + 1, line, end='')
            for i2, line2 in enumerate(data[i:], i):
                if 'bonus_spell_amp' in line2:
                    line2_new = line2.replace('25', f'{magic_damage}')
                    change_index_and_line[i2] = line2_new
                    print(i2 + 1, line2_new, end='')
                if 'bonus_damage' in line2:
                    line2_new = line2.replace('250', f'{attack_damage}')
                    change_index_and_line[i2] = line2_new
                    print(i2 + 1, line2_new, end='')
                    break

        if '\t// Travel Boots\n' == line:
            print(i + 1, line, end='')
            for i2, line2 in enumerate(data[i:], i):
                if 'bonus_movement_speed' in line2:
                    line2_new = line2.replace('90', f'{move_speed}')
                    change_index_and_line[i2] = line2_new
                    print(i2 + 1, line2_new, end='')
                    break

        if '// Travel Boots 2' in line:
            print(i + 1, line, end='')
            for i2, line2 in enumerate(data[i:], i):
                if 'bonus_movement_speed' in line2:
                    line2_new = line2.replace('110', f'{move_speed2}')
                    change_index_and_line[i2] = line2_new
                    print(i2 + 1, line2_new, end='')
                    break

    for index, line in change_index_and_line.items():
        data_new[index] = line

    with open(save_path, 'w', encoding='utf-8') as f:
        f.writelines(data_new)


if __name__ == '__main__':
    change_items(r'../npc/items.txt', 'items.txt', 10.0, 2000, 300, 400, 100, 100, 120)
