def change_time(path, save_path, time1, time2, time3, time4, time5):
    with open(path, 'r', encoding='utf-8') as f:
        ls = f.readlines()

    ls_new = []
    for i, line in enumerate(ls, 1):
        if '"5:00"' in line:
            line_new = line.replace('"5:00"', f'"{time1}:00"')
            ls_new.append(line_new)
            print(i, line_new, end='')
        elif '"15:00"' in line:
            line_new = line.replace('"15:00"', f'"{time2}:00"')
            ls_new.append(line_new)
            print(i, line_new, end='')
        elif '"25:00"' in line:
            line_new = line.replace('"25:00"', f'"{time3}:00"')
            ls_new.append(line_new)
            print(i, line_new, end='')
        elif '"35:00"' in line:
            line_new = line.replace('"35:00"', f'"{time4}:00"')
            ls_new.append(line_new)
            print(i, line_new, end='')
        elif '"60:00"' in line:
            line_new = line.replace('"60:00"', f'"{time5}:00"')
            ls_new.append(line_new)
            print(i, line_new, end='')
        else:
            ls_new.append(line)
    with open(save_path, 'w', encoding='utf-8') as f:
        f.writelines(ls_new)


if __name__ == '__main__':
    change_time(r'../npc/neutral_items.txt', 'neutral_items.txt', 0, 5, 10, 15, 20)
