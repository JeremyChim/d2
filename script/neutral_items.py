def change_time(path, save_path, time1, time2, time3, time4, time5, time6):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    data_new = []
    for i, line in enumerate(data):
        if '"5:00"' in line:
            line_new = line.replace('"5:00"', f'"{time1}:00"')
        elif '"15:00"' in line:
            line_new = line.replace('"15:00"', f'"{time2}:00"')
        elif '"25:00"' in line:
            line_new = line.replace('"25:00"', f'"{time3}:00"')
        elif '"35:00"' in line:
            line_new = line.replace('"35:00"', f'"{time4}:00"')
        elif '"60:00"' in line:
            line_new = line.replace('"60:00"', f'"{time5}:00"')
        elif '"70:00"' in line:
            line_new = line.replace('"70:00"', f'"{time6}:00"')
        else:
            line_new = line
        if line_new != line:
            print(i + 1, line_new, end='')
        data_new.append(line_new)

    with open(save_path, 'w', encoding='utf-8') as f:
        f.writelines(data_new)


if __name__ == '__main__':
    change_time(r'../npc/neutral_items.txt', 'neutral_items.txt', 0, 5, 10, 15, 20, 25)
