import os
import shutil
import pyperclip
import json


def build_json(path, data):
    if not os.path.exists(path):
        with open(path, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


def build_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def open_dir(path):
    os.startfile(path)


def open_file(path):
    os.startfile(path)


def delete_file(path):
    os.remove(path)


def copy_file(src, dst):
    shutil.copy(src, dst)


def move_file(src, dst):
    shutil.move(src, dst)


def copy_cmd(cmd):
    pyperclip.copy(cmd)


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    open_dir('C:/Users/Jeremy/Desktop/d2/vpk')
    # delete_file('npc_units.txt')
    # move_file('C:/Users/Jeremy/Desktop/d2/vpk/pak01_dir.vpk', 'C:/Users/Jeremy/Desktop/d2/pak01_dir.vpk')
    # copy_cmd('sv_cheats 1; script_reload_code bots/fretbots')
