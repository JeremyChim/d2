def change_midas(path, save_path, xp, gold):
    with open(path, 'r', encoding='utf-8') as f:
        ls = f.readlines()

    ls_new = ls
    for i, line in enumerate(ls, 0):
        if '// Hand of Midas' in line:
            print(i + 1, line, end='')
            break

    for i2, line in enumerate(ls[i:], i):
        if 'xp_multiplier' in line:
            ls_new[i2] = ls_new[i2].replace('"2.1"', f'"{xp}"')
            print(i2 + 1, ls_new[i2], end='')
            break

    for i3, line in enumerate(ls[i2:], i2):
        if 'bonus_gold' in line:
            ls_new[i3] = ls_new[i3].replace('"160"', f'"{gold}"')
            print(i3 + 1, ls_new[i3], end='')
            break

    with open(save_path, 'w', encoding='utf-8') as f:
        f.writelines(ls_new)


if __name__ == '__main__':
    change_midas(r'../npc/items.txt', 'items.txt', 10.0, 2000)
