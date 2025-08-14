def change_team_and_push_lv(path, save_path, friend1, friend2, friend3, friend4, enemy1, enemy2, enemy3, enemy4, enemy5, push_lv):
    with open(path, 'r', encoding='utf-8') as f:
        ls = f.readlines()
    ls_new = []
    for i, line in enumerate(ls, 1):
        if i == 47:
            line = "\t'" + friend1 + "',\n"
            print(i, line, end='')
        elif i == 48:
            line = "\t'" + friend2 + "',\n"
            print(i, line, end='')
        elif i == 49:
            line = "\t'" + friend3 + "',\n"
            print(i, line, end='')
        elif i == 50:
            line = "\t'" + friend4 + "',\n"
            print(i, line, end='')
        elif i == 55:
            line = "\t'" + enemy1 + "',\n"
            print(i, line, end='')
        elif i == 56:
            line = "\t'" + enemy2 + "',\n"
            print(i, line, end='')
        elif i == 57:
            line = "\t'" + enemy3 + "',\n"
            print(i, line, end='')
        elif i == 58:
            line = "\t'" + enemy4 + "',\n"
            print(i, line, end='')
        elif i == 59:
            line = "\t'" + enemy5 + "',\n"
            print(i, line, end='')
        elif i == 94:
            line = f'Customize.Force_Group_Push_Level = {push_lv}\n'
            print(i, line, end='')
        ls_new.append(line)
    with open(save_path, 'w', encoding='utf-8') as f:
        f.writelines(ls_new)


def get_team_and_push_lv(path):
    with open(path, 'r', encoding='utf-8') as f:
        ls = f.readlines()
    for i, line in enumerate(ls, 1):
        if i == 47:
            friend1 = line.split("'")[1]
        elif i == 48:
            friend2 = line.split("'")[1]
        elif i == 49:
            friend3 = line.split("'")[1]
        elif i == 50:
            friend4 = line.split("'")[1]
        elif i == 55:
            enemy1 = line.split("'")[1]
        elif i == 56:
            enemy2 = line.split("'")[1]
        elif i == 57:
            enemy3 = line.split("'")[1]
        elif i == 58:
            enemy4 = line.split("'")[1]
        elif i == 59:
            enemy5 = line.split("'")[1]
        elif i == 94:
            push_lv = int(line.split(' = ')[1])
    return friend1, friend2, friend3, friend4, enemy1, enemy2, enemy3, enemy4, enemy5, push_lv


def get_team(path):
    with open(path, 'r', encoding='utf-8') as f:
        ls = f.readlines()
    for i, line in enumerate(ls, 1):
        if i == 47:
            friend1 = line.split("'")[1]
        elif i == 48:
            friend2 = line.split("'")[1]
        elif i == 49:
            friend3 = line.split("'")[1]
        elif i == 50:
            friend4 = line.split("'")[1]
        elif i == 55:
            enemy1 = line.split("'")[1]
        elif i == 56:
            enemy2 = line.split("'")[1]
        elif i == 57:
            enemy3 = line.split("'")[1]
        elif i == 58:
            enemy4 = line.split("'")[1]
        elif i == 59:
            enemy5 = line.split("'")[1]
    return friend1, friend2, friend3, friend4, enemy1, enemy2, enemy3, enemy4, enemy5


def get_push_lv(path):
    with open(path, 'r', encoding='utf-8') as f:
        ls = f.readlines()
    for i, line in enumerate(ls, 1):
        if i == 94:
            push_lv = int(line.split(' = ')[1])
    return push_lv


if __name__ == '__main__':
    change_team_and_push_lv('../lua/reset/general.lua', '../lua/general.lua',
                            'friend1', 'friend2', 'friend3', 'friend4',
                            'enemy1', 'enemy2', 'enemy3', 'enemy4', 'enemy5',
                            3)
    # results = get_heroes_and_push('../lua/general.lua')
    # hero_files, push_lv = results[:-1], results[-1]
    # print(hero_files, push_lv)
