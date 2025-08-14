def up(old):
    """增加缩进"""
    new: list = []
    cut: list = old.split('\n')
    for row in cut:
        new.append('\t' + row)
    return '\n'.join(new)


def down(old):
    """减少缩进"""
    new: list = []
    cut: list = old.split('\n')
    for row in cut:
        if len(row) != 0 and row[0] == '\t':
            new.append(row[1:])
        else:
            new.append(row)
    return '\n'.join(new)


if __name__ == '__main__':
    inp = '\t"doom"\t\t"100"\n\t"bang"\t\t"200"\n'
    res = up(inp), down(inp)
    print(*res, sep='\n')