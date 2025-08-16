def change_xp_gold_and_tower_hp(path, save_path, xp_gold_mul, tower_hp_mul):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    data_change_xp_gold = []
    for i, line in enumerate(data, 1):
        if 'BountyXP' in line or 'BountyGoldMin' in line or 'BountyGoldMax' in line:
            cut = line.split('"')  # ['\t\t', 'BountyXP', '\t\t\t\t\t', '69', '\t\t// Experience earn.\n']
            val = cut[3]
            val_new = int((int(val) * xp_gold_mul))
            line_new = line.replace(str(val), str(val_new))
            data_change_xp_gold.append(line_new)
            print(i, line_new, end='')
        else:
            data_change_xp_gold.append(line)

    data_change_tower_hp = []
    for i, line in enumerate(data_change_xp_gold, 1):
        if 'Good Tower' in line or 'Bad Tower' in line or 'Guys Fort' in line:
            print(i, line, end='')
            for i2, line2 in enumerate(data_change_xp_gold[i:], i):
                if 'StatusHealth' in line2:
                    cut = line2.split('"')
                    val = cut[3]
                    val_new = int((int(val) * tower_hp_mul))
                    line2_new = line2.replace(str(val), str(val_new))
                    print(i2 + 1, line2_new, end='')
                    break
        else:
            data_change_tower_hp.append(line)

    with open(save_path, 'w', encoding='utf-8') as f:
        f.writelines(data_change_tower_hp)


if __name__ == '__main__':
    change_xp_gold_and_tower_hp(r'../npc/npc_units.txt', 'npc_units.txt', 2, 2)
