def change_xp_gold_and_tower_hp(path, save_path, xp_gold_mul, tower_hp_mul):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    data_new = []
    for i, line in enumerate(data):
        if 'BountyXP' in line or 'BountyGoldMin' in line or 'BountyGoldMax' in line:
            cut = line.split('"')  # ['\t\t', 'BountyXP', '\t\t\t\t\t', '69', '\t\t// Experience earn.\n']
            val = cut[3]
            val_new = int((int(val) * xp_gold_mul))
            line_new = line.replace(str(val), str(val_new))
            data_new.append(line_new)
            print(i + 1, line_new, end='')
        else:
            data_new.append(line)

    change_index_and_line = {}
    for i, line in enumerate(data_new):
        if 'Good Tower' in line or 'Bad Tower' in line or 'Guys Fort' in line:
            print(i + 1, line, end='')
            for i2, line2 in enumerate(data_new[i:], i):
                if 'StatusHealth' in line2:
                    cut = line2.split('"')
                    val = cut[3]
                    val_new = int((int(val) * tower_hp_mul))
                    line2_new = line2.replace(str(val), str(val_new))
                    print(i2 + 1, line2_new, end='')
                    change_index_and_line[i2] = line2_new
                    break
    for index, line in change_index_and_line.items():
        data_new[index] = line

    with open(save_path, 'w', encoding='utf-8') as f:
        f.writelines(data_new)


if __name__ == '__main__':
    change_xp_gold_and_tower_hp(r'../npc/npc_units.txt', 'npc_units.txt', 2, 1.5)
