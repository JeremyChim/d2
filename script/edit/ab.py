def has_not(old, abv='+50%'):
    """没{}"""
    mod = ('[tab]"[name]"\t\t\t\t\t\t"[val]"\n'
           f'[tab]"special_bonus_shard"\t\t"{abv}"\n'
           f'[tab]"special_bonus_scepter"\t\t"{abv}"\n')
    cut: list = old.split('"')
    new = (mod.replace('[tab]', cut[0])
           .replace('[name]', cut[1])
           .replace('[val]', cut[3]))
    return new


def has(old, abv='+50%'):
    """有{}"""
    mod = ('[tab]"[name]"\n'
           '[tab]{\n'
           '[tab]\t"value"\t\t\t\t\t\t"[val]"\n'
           f'[tab]\t"special_bonus_shard"\t\t"{abv}"\n'
           f'[tab]\t"special_bonus_scepter"\t\t"{abv}"\n'
           '[tab]}\n')
    cut: list = old.split('"')
    new = (mod.replace('[tab]', cut[0])
           .replace('[name]', cut[1])
           .replace('[val]', cut[3]))
    return new


def user(old, abv):
    """自定义"""
    if 'value' in old:
        return has_not(old, abv)
    else:
        return has(old, abv)


def cd(old):
    """改冷却"""
    if 'value' in old:
        return has_not(old, '-25%')
    else:
        return has(old, '-25%')


def ch(old):
    """转充能"""
    mod = ('[tab]"[name]"\t\t\t\t\t\t"0"\n'
           '[tab]"AbilityCharges"\n'
           '[tab]{\n'
           '[tab]\t"value"\t\t\t\t\t\t"1"\n'
           '[tab]\t"special_bonus_shard"\t\t"+1"\n'
           '[tab]\t"special_bonus_scepter"\t\t"+1"\n'
           '[tab]}\n'
           '[tab]"AbilityChargeRestoreTime"\n'
           '[tab]{\n'
           '[tab]\t"value"\t\t\t\t\t\t"[val]"\n'
           '[tab]\t"special_bonus_shard"\t\t"-25%"\n'
           '[tab]\t"special_bonus_scepter"\t\t"-25%"\n'
           '[tab]}\n')
    cut: list = old.split('"')
    new = (mod.replace('[tab]', cut[0])
           .replace('[name]', cut[1])
           .replace('[val]', cut[3]))
    return new


def tf(old, abv='+50%'):
    """改天赋"""
    mod = ('[tab]"value"\t\t\t\t\t\t"[val]"\n'
           f'[tab]"special_bonus_shard"\t\t"{abv}"\n'
           f'[tab]"special_bonus_scepter"\t\t"{abv}"\n')
    cut: list = old.split('"')
    new = (mod.replace('[tab]', cut[0])
           .replace('[val]', cut[3]))
    return new


def auto(old):
    """自判断"""
    if 'CastPoint' in old or 'ManaCost' in old or 'Cooldown' in old or 'RestoreTime' in old:
        return cd(old)
    elif 'value' in old:
        return has_not(old)
    else:
        return has(old)


def sa(old, abv='+50%'):
    mod = ('[tab]"[name]"\t\t\t\t\t\t"[val]"\n'
           f'[tab]"special_bonus_shard"\t\t"{abv}"\n')
    cut: list = old.split('"')
    new = (mod.replace('[tab]', cut[0])
           .replace('[name]', cut[1])
           .replace('[val]', cut[3]))
    return new


def sp(old, abv='+50%'):
    mod = ('[tab]"[name]"\t\t\t\t\t\t"[val]"\n'
           f'[tab]"special_bonus_scepter"\t\t"{abv}"\n')
    cut: list = old.split('"')
    new = (mod.replace('[tab]', cut[0])
           .replace('[name]', cut[1])
           .replace('[val]', cut[3]))
    return new


if __name__ == '__main__':
    inp = '"doom"        "100 200 300 400"'
    res = auto(inp), cd(inp), ch(inp), tf(inp), user(inp, '=0'), sa(inp), sp(inp),
    print(*res, sep='\n')
