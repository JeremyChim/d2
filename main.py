from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from ui.main import Ui_Form
from edit import EditWin
from script import *
import os


class MainWin(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_config()
        self.init_win()
        self.init_path()
        self.init_model()
        self.init_connect()
        self.init_lua_btn()

    def init_config(self):
        self.is_top = False
        self.ch_name_dict = {
            "abaddon": "亚巴顿",
            "abyssal_underlord": "孽主",
            "alchemist": "炼金术士",
            "ancient_apparition": "远古冰魄",
            "antimage": "敌法师",
            "arc_warden": "天穹守望者",
            "axe": "斧王",
            "bane": "祸乱之源",
            "batrider": "蝙蝠骑士",
            "beastmaster": "兽王",
            "bloodseeker": "血魔",
            "bounty_hunter": "赏金猎人",
            "brewmaster": "酒仙",
            "bristleback": "钢背兽",
            "broodmother": "育母蜘蛛",
            "centaur": "半人马战行者",
            "chaos_knight": "混沌骑士",
            "chen": "陈",
            "clinkz": "克林克兹",
            "crystal_maiden": "水晶室女",
            "dark_seer": "黑暗贤者",
            "dark_willow": "邪影芳灵",
            "dawnbreaker": "破晓辰星",
            "dazzle": "戴泽",
            "death_prophet": "死亡先知",
            "disruptor": "干扰者",
            "doom_bringer": "末日使者",
            "dragon_knight": "龙骑士",
            "drow_ranger": "卓尔游侠",
            "earth_spirit": "大地之灵",
            "earthshaker": "撼地者",
            "elder_titan": "上古巨神",
            "ember_spirit": "灰烬之灵",
            "enchantress": "魅惑魔女",
            "enigma": "谜团",
            "faceless_void": "虚空假面",
            "furion": "先知",
            "grimstroke": "天涯墨客",
            "gyrocopter": "矮人直升机",
            "hoodwink": "森海飞霞",
            "huskar": "哈斯卡",
            "invoker": "祈求者",
            "jakiro": "杰奇洛",
            "juggernaut": "主宰",
            "keeper_of_the_light": "光之守卫",
            "kez": "凯",
            "kunkka": "昆卡",
            "legion_commander": "军团指挥官",
            "leshrac": "拉席克",
            "lich": "巫妖",
            "life_stealer": "噬魂鬼",
            "lina": "莉娜",
            "lion": "莱恩",
            "lone_druid": "德鲁伊",
            "luna": "露娜",
            "lycan": "狼人",
            "magnataur": "马格纳斯",
            "marci": "马西",
            "mars": "马尔斯",
            "medusa": "美杜莎",
            "meepo": "米波",
            "mirana": "米拉娜",
            "monkey_king": "齐天大圣",
            "morphling": "变体精灵",
            "muerta": "琼英碧灵",
            "naga_siren": "娜迦海妖",
            "necrolyte": "瘟疫法师",
            "nevermore": "影魔",
            "night_stalker": "暗夜魔王",
            "nyx_assassin": "司夜刺客",
            "obsidian_destroyer": "殁境神蚀者",
            "ogre_magi": "食人魔魔法师",
            "omniknight": "全能骑士",
            "oracle": "神谕者",
            "pangolier": "石鳞剑士",
            "phantom_assassin": "幻影刺客",
            "phantom_lancer": "幻影长矛手",
            "phoenix": "凤凰",
            "primal_beast": "兽",
            "puck": "帕克",
            "pudge": "帕吉",
            "pugna": "帕格纳",
            "queenofpain": "痛苦女王",
            "rattletrap": "发条技师",
            "razor": "剃刀",
            "riki": "力丸",
            "ringmaster": "百戏大王",
            "rubick": "拉比克",
            "sand_king": "沙王",
            "shadow_demon": "暗影恶魔",
            "shadow_shaman": "暗影萨满",
            "shredder": "伐木机",
            "silencer": "沉默术士",
            "skeleton_king": "冥魂大帝",
            "skywrath_mage": "天怒法师",
            "slardar": "斯拉达",
            "slark": "斯拉克",
            "snapfire": "电炎绝手",
            "sniper": "狙击手",
            "spectre": "幽鬼",
            "spirit_breaker": "裂魂人",
            "storm_spirit": "风暴之灵",
            "sven": "斯温",
            "target_dummy": "目标假人",
            "techies": "工程师",
            "templar_assassin": "圣堂刺客",
            "terrorblade": "恐怖利刃",
            "tidehunter": "潮汐猎人",
            "tinker": "修补匠",
            "tiny": "小小",
            "treant": "树精卫士",
            "troll_warlord": "巨魔战将",
            "tusk": "巨牙海民",
            "undying": "不朽尸王",
            "ursa": "熊战士",
            "vengefulspirit": "复仇之魂",
            "venomancer": "剧毒术士",
            "viper": "冥界亚龙",
            "visage": "维萨吉",
            "void_spirit": "虚无之灵",
            "warlock": "术士",
            "weaver": "编织者",
            "windrunner": "风行者",
            "winter_wyvern": "寒冬飞龙",
            "wisp": "艾欧",
            "witch_doctor": "巫医",
            "zuus": "宙斯"
        }

    def init_win(self):
        self.setWindowTitle('d2')
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.width(), self.height())

    def init_path(self):
        data = {'root_path': 'C:/Users/Jeremy/Desktop/d2', 'game_path': 'E:/GAME/steamapps/common/dota 2 beta'}
        other.build_json('config.json', data)
        config = other.read_json('config.json')
        root_path = config['root_path']
        game_path = config['game_path']
        self.le_root.setText(root_path)
        self.le_game.setText(game_path)

    def init_model(self):
        self.model_hero = QStandardItemModel()
        self.model_hero_vpk = QStandardItemModel()
        self.model_hero_ban = QStandardItemModel()
        self.lv_hero.setModel(self.model_hero)
        self.lv_hero_vpk.setModel(self.model_hero_vpk)
        self.lv_hero_ban.setModel(self.model_hero_ban)
        self.lv_hero.setAlternatingRowColors(True)
        self.lv_hero_vpk.setAlternatingRowColors(True)
        self.lv_hero_ban.setAlternatingRowColors(True)
        self.update_model_hero()
        self.update_model_hero_vpk()
        self.update_model_hero_ban()

    def init_connect(self):
        self.btn_on_top.clicked.connect(self.on_top)
        self.btn_refresh_lv_hero_vpk_ban.clicked.connect(self.refresh_lv_hero_vpk_ban)
        self.btn_npc_units_apply.clicked.connect(self.npc_units_apply)
        self.btn_npc_units_reset.clicked.connect(self.npc_units_reset)
        self.btn_neutral_items_apply.clicked.connect(self.neutral_items_apply)
        self.btn_neutral_items_reset.clicked.connect(self.neutral_items_reset)
        self.btn_items_apply.clicked.connect(self.items_apply)
        self.btn_items_reset.clicked.connect(self.items_reset)
        self.btn_gi_apply.clicked.connect(self.gi_apply)
        self.btn_gi_reset.clicked.connect(self.gi_reset)
        self.btn_vpk_build.clicked.connect(self.vpk_build)
        self.btn_vpk_build_run.clicked.connect(self.vpk_build_run)
        self.btn_open_pak01.clicked.connect(self.open_pak01)
        self.btn_open_vpk_dir.clicked.connect(self.open_vpk_dir)
        self.btn_open_hero_dir.clicked.connect(self.open_hero_dir)
        self.btn_open_game_dir.clicked.connect(self.oepn_game_dir)
        self.btn_open_skin_dir.clicked.connect(self.oepn_skin_dir)
        self.btn_open_skin2_dir.clicked.connect(self.oepn_skin2_dir)
        self.btn_open_mod_dir.clicked.connect(self.oepn_mod_dir)
        self.btn_open_bot_script_dir.clicked.connect(self.open_bot_script_dir)
        self.btn_open_lua.clicked.connect(self.open_lua_file)
        self.btn_lua_apply.clicked.connect(self.lua_apply)
        self.btn_lua_reset.clicked.connect(self.lua_reset)
        self.btn_bot_cmd.clicked.connect(self.bot_cmd)
        self.btn_steam_cmd.clicked.connect(self.steam_cmd)
        self.btn_mipo_cmd.clicked.connect(self.mipo_cmd)
        self.btn_add_hero_to_vpk.clicked.connect(self.add_hero_to_vpk)
        self.btn_edit_hero_in_vpk_and_ban.clicked.connect(self.edit_hero_in_vpk_and_ban)
        self.btn_del_hero_in_vpk_and_ban.clicked.connect(self.del_hero_in_vpk_and_ban)
        self.lv_hero.doubleClicked.connect(self.double_clicked_in_lv_hero)
        self.lv_hero_vpk.doubleClicked.connect(self.double_clicked_in_lv_hero_vpk)
        self.lv_hero_ban.doubleClicked.connect(self.double_clicked_in_lv_hero_ban)
        self.le_search.textChanged.connect(self.on_search_text_changed)
        self.btn_lua_firend1.clicked.connect(lambda: self.add_hero_to_lua(self.btn_lua_firend1))
        self.btn_lua_firend2.clicked.connect(lambda: self.add_hero_to_lua(self.btn_lua_firend2))
        self.btn_lua_firend3.clicked.connect(lambda: self.add_hero_to_lua(self.btn_lua_firend3))
        self.btn_lua_firend4.clicked.connect(lambda: self.add_hero_to_lua(self.btn_lua_firend4))
        self.btn_lua_enemy1.clicked.connect(lambda: self.add_hero_to_lua(self.btn_lua_enemy1))
        self.btn_lua_enemy2.clicked.connect(lambda: self.add_hero_to_lua(self.btn_lua_enemy2))
        self.btn_lua_enemy3.clicked.connect(lambda: self.add_hero_to_lua(self.btn_lua_enemy3))
        self.btn_lua_enemy4.clicked.connect(lambda: self.add_hero_to_lua(self.btn_lua_enemy4))
        self.btn_lua_enemy5.clicked.connect(lambda: self.add_hero_to_lua(self.btn_lua_enemy5))

    def init_lua_btn(self):
        try:
            ch_name_list = []
            lua_btn_list = [self.btn_lua_firend1,
                            self.btn_lua_firend2,
                            self.btn_lua_firend3,
                            self.btn_lua_firend4,
                            self.btn_lua_enemy1,
                            self.btn_lua_enemy2,
                            self.btn_lua_enemy3,
                            self.btn_lua_enemy4,
                            self.btn_lua_enemy5]
            lua_path = self.le_root.text() + '/lua/general.lua'
            if os.path.exists(lua_path):
                hero_file_tuple = lua.get_team(lua_path)
                push_lv = lua.get_push_lv(lua_path)
                for hero_file in hero_file_tuple:
                    if hero_file != 'Random':
                        hero_name = hero_file.removeprefix('npc_dota_hero_')
                        ch_name = self.ch_name_dict[hero_name]
                        ch_name_list.append(ch_name)
                    else:
                        ch_name = '?'
                        ch_name_list.append(ch_name)
                for i, btn in enumerate(lua_btn_list):
                    ch_name = ch_name_list[i]
                    btn.setText(ch_name)
                self.box_lua_push_lv.setValue(push_lv)
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def get_en_hero_name(self, ch_hero_name):
        for en_name, ch_name in self.ch_name_dict.items():
            if ch_hero_name == ch_name:
                return en_name
        return None

    def on_top(self):
        self.is_top = not self.is_top
        if self.is_top:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.show()

    def update_model_hero(self):
        try:
            self.model_hero.clear()
            hero_dir = self.le_root.text() + '/npc/heroes'
            hero_list = os.listdir(hero_dir)
            for hero_file in hero_list:
                hero_name = hero_file.removeprefix("npc_dota_hero_").removesuffix(".txt")
                ch_name = self.ch_name_dict[hero_name]
                show_text = f'{hero_name:22}' + ch_name
                item = QStandardItem(show_text)
                item.setEditable(False)
                self.model_hero.appendRow(item)
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def update_model_hero_vpk(self):
        try:
            self.model_hero_vpk.clear()
            hero_dir = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes'
            hero_list = os.listdir(hero_dir)
            for hero_file in hero_list:
                hero_name = hero_file.removeprefix("npc_dota_hero_").removesuffix(".txt")
                ch_name = self.ch_name_dict[hero_name]
                show_text = ch_name
                item = QStandardItem(show_text)
                item.setEditable(False)
                self.model_hero_vpk.appendRow(item)
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def update_model_hero_ban(self):
        try:
            self.model_hero_ban.clear()
            hero_dir = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes_ban'
            hero_list = os.listdir(hero_dir)
            for hero_file in hero_list:
                hero_name = hero_file.removeprefix("npc_dota_hero_").removesuffix(".txt")
                ch_name = self.ch_name_dict[hero_name]
                show_text = ch_name
                item = QStandardItem(show_text)
                item.setEditable(False)
                self.model_hero_ban.appendRow(item)
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def refresh_lv_hero_vpk_ban(self):
        try:
            self.update_model_hero()
            self.update_model_hero_vpk()
            self.update_model_hero_ban()
            self.le_status_bar.setText(f'refresh hero done.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def double_clicked_in_lv_hero(self, index):
        try:
            item = self.model_hero.itemFromIndex(index)
            show_text = item.text()
            hero_name = show_text.split(' ')[0]
            hero_file = 'npc_dota_hero_' + hero_name + '.txt'
            hero_path = self.le_root.text() + '/npc/heroes/' + hero_file
            vpk_hero_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes/'
            other.copy_file(hero_path, vpk_hero_path)
            self.update_model_hero_vpk()
            self.le_status_bar.setText(f'add hero to vpk : {hero_name}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def double_clicked_in_lv_hero_vpk(self, index):
        try:
            item = self.model_hero_vpk.itemFromIndex(index)
            show_text = item.text()
            for hero_name, ch_name in self.ch_name_dict.items():
                if show_text == ch_name:
                    break
            hero_file = 'npc_dota_hero_' + hero_name + '.txt'
            vpk_hero_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes/' + hero_file
            ban_hero_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes_ban/' + hero_file
            other.move_file(vpk_hero_path, ban_hero_path)
            self.update_model_hero_vpk()
            self.update_model_hero_ban()
            self.le_status_bar.setText(f'ban hero in vpk : {hero_name}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def double_clicked_in_lv_hero_ban(self, index):
        try:
            item = self.model_hero_ban.itemFromIndex(index)
            show_text = item.text()
            for hero_name, ch_name in self.ch_name_dict.items():
                if show_text == ch_name:
                    break
            hero_file = 'npc_dota_hero_' + hero_name + '.txt'
            ban_hero_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes_ban/' + hero_file
            vpk_hero_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes/' + hero_file
            other.move_file(ban_hero_path, vpk_hero_path)
            self.update_model_hero_ban()
            self.update_model_hero_vpk()
            self.le_status_bar.setText(f'unban hero in vpk : {hero_name}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def add_hero_to_vpk(self):
        try:
            index = self.lv_hero.selectedIndexes()
            item = self.model_hero.itemFromIndex(index[0])
            show_text = item.text()
            hero_name = show_text.split(' ')[0]
            hero_file = 'npc_dota_hero_' + hero_name + '.txt'
            hero_path = self.le_root.text() + '/npc/heroes/' + hero_file
            copy_to_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes/'
            other.copy_file(hero_path, copy_to_path)
            self.update_model_hero_vpk()
            self.le_status_bar.setText(f'add hero to vpk : {hero_name}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def edit_hero_in_vpk_and_ban(self):
        try:
            index = self.lv_hero_vpk.selectedIndexes()
            if index:
                item = self.model_hero_vpk.itemFromIndex(index[0])
                show_text = item.text()
                for hero_name, ch_name in self.ch_name_dict.items():
                    if show_text == ch_name:
                        break
                hero_file = 'npc_dota_hero_' + hero_name + '.txt'
                hero_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes/' + hero_file
                edit_win = EditWin(hero_path)
                edit_win.show()
                self.le_status_bar.setText(f'edit hero in vpk : {hero_name}')
            index = self.lv_hero_ban.selectedIndexes()
            if index:
                item = self.model_hero_ban.itemFromIndex(index[0])
                show_text = item.text()
                for hero_name, ch_name in self.ch_name_dict.items():
                    if show_text == ch_name:
                        break
                hero_file = 'npc_dota_hero_' + hero_name + '.txt'
                ban_hero_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes_ban/' + hero_file
                edit_win = EditWin(ban_hero_path)
                edit_win.show()
                self.le_status_bar.setText(f'edit hero in ban : {ban_hero_path}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def del_hero_in_vpk_and_ban(self):
        try:
            index = self.lv_hero_vpk.selectedIndexes()
            if index:
                item = self.model_hero_vpk.itemFromIndex(index[0])
                show_text = item.text()
                for hero_name, ch_name in self.ch_name_dict.items():
                    if show_text == ch_name:
                        break
                hero_file = 'npc_dota_hero_' + hero_name + '.txt'
                ban_hero_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes/' + hero_file
                other.delete_file(ban_hero_path)
                self.update_model_hero_vpk()
                self.le_status_bar.setText(f'del hero in vpk : {hero_name}')
            index = self.lv_hero_ban.selectedIndexes()
            if index:
                item = self.model_hero_ban.itemFromIndex(index[0])
                show_text = item.text()
                for hero_name, ch_name in self.ch_name_dict.items():
                    if show_text == ch_name:
                        break
                hero_file = 'npc_dota_hero_' + hero_name + '.txt'
                ban_hero_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes_ban/' + hero_file
                other.delete_file(ban_hero_path)
                self.update_model_hero_ban()
                self.le_status_bar.setText(f'del hero in ban : {hero_name}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def on_search_text_changed(self, text):
        try:
            for i in range(self.model_hero.rowCount()):
                item = self.model_hero.item(i)
                if text.lower() in item.text().lower():
                    self.lv_hero.setRowHidden(i, False)
                else:
                    self.lv_hero.setRowHidden(i, True)
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def add_hero_to_lua(self, btn):
        try:
            index = self.lv_hero.selectedIndexes()
            item = self.model_hero.itemFromIndex(index[0])
            show_text = item.text()
            hero_name = show_text.split(' ')[0]
            ch_name = self.ch_name_dict[hero_name]
            btn.setText(ch_name)
            self.le_status_bar.setText(f'add hero to lua : {hero_name}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def lua_apply(self):
        try:
            arg_dict = {}
            hero_file_list = []
            lua_btn_list = [self.btn_lua_firend1,
                            self.btn_lua_firend2,
                            self.btn_lua_firend3,
                            self.btn_lua_firend4,
                            self.btn_lua_enemy1,
                            self.btn_lua_enemy2,
                            self.btn_lua_enemy3,
                            self.btn_lua_enemy4,
                            self.btn_lua_enemy5]
            lua_path = self.le_root.text() + '/lua/general.lua'
            script_path = self.le_game.text() + '/game/dota/scripts/vscripts/game/Customize/general.lua'
            push_lv = self.box_lua_push_lv.value()
            for btn in lua_btn_list:
                ch_name = btn.text()
                if ch_name != '?':
                    hero_name = self.get_en_hero_name(ch_name)
                    hero_file = 'npc_dota_hero_' + hero_name
                    hero_file_list.append(hero_file)
                else:
                    hero_file = 'Random'
                    hero_file_list.append(hero_file)
            arg_dict['path'] = lua_path
            arg_dict['save_path'] = lua_path
            arg_dict['push_lv'] = push_lv
            arg_dict['friend1'] = hero_file_list[0]
            arg_dict['friend2'] = hero_file_list[1]
            arg_dict['friend3'] = hero_file_list[2]
            arg_dict['friend4'] = hero_file_list[3]
            arg_dict['enemy1'] = hero_file_list[4]
            arg_dict['enemy2'] = hero_file_list[5]
            arg_dict['enemy3'] = hero_file_list[6]
            arg_dict['enemy4'] = hero_file_list[7]
            arg_dict['enemy5'] = hero_file_list[8]
            lua.change_team_and_push_lv(**arg_dict)
            other.copy_file(lua_path, script_path)
            self.le_status_bar.setText('general.lua apply.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def lua_reset(self):
        try:
            reset_path = self.le_root.text() + '/lua/reset/general.lua'
            lua_path = self.le_root.text() + '/lua/general.lua'
            script_path = self.le_game.text() + '/game/dota/scripts/vscripts/game/Customize/general.lua'
            other.copy_file(reset_path, lua_path)
            other.copy_file(reset_path, script_path)
            self.init_lua_btn()
            self.le_status_bar.setText('general.lua reset.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def npc_units_apply(self):
        try:
            path = self.le_root.text() + '/npc/npc_units.txt'
            save_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/npc_units.txt'
            xp_gold_mul = self.box_npc_units_xp_gold.value()
            tower_hp_mul = self.box_npc_units_tower_hp.value()
            npc_units.change_xp_gold_and_tower_hp(path, save_path, xp_gold_mul, tower_hp_mul)
            self.le_status_bar.setText('npc_units.txt apply.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def npc_units_reset(self):
        try:
            save_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/npc_units.txt'
            other.delete_file(save_path)
            self.le_status_bar.setText('npc_units.txt reset.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def neutral_items_apply(self):
        try:
            path = self.le_root.text() + '/npc/neutral_items.txt'
            save_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/neutral_items.txt'
            time1 = self.box_neutral_items_lv1.value()
            time2 = self.box_neutral_items_lv2.value()
            time3 = self.box_neutral_items_lv3.value()
            time4 = self.box_neutral_items_lv4.value()
            time5 = self.box_neutral_items_lv5.value()
            neutral_items.change_time(path, save_path, time1, time2, time3, time4, time5)
            self.le_status_bar.setText('neutral_items.txt apply.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def neutral_items_reset(self):
        try:
            save_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/neutral_items.txt'
            other.delete_file(save_path)
            self.le_status_bar.setText('neutral_items.txt reset.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def items_apply(self):
        try:
            path = self.le_root.text() + '/npc/items.txt'
            save_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/items.txt'
            xp = self.box_item_hand_of_midas_xp.value()
            gold = self.box_item_hand_of_midas_gold.value()
            items.change_midas(path, save_path, xp, gold)
            self.le_status_bar.setText('items.txt apply.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def items_reset(self):
        try:
            save_path = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/items.txt'
            other.delete_file(save_path)
            self.le_status_bar.setText('items.txt reset.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def gi_apply(self):
        try:
            gi_path = self.le_root.text() + '/gi/gameinfo_branchspecific.gi'
            dota_path = self.le_game.text() + '/game/dota/gameinfo_branchspecific.gi'
            other.copy_file(gi_path, dota_path)
            self.le_status_bar.setText('gameinfo_branchspecific.gi apply.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def gi_reset(self):
        try:
            gi_path = self.le_root.text() + '/gi/reset/gameinfo_branchspecific.gi'
            dota_path = self.le_game.text() + '/game/dota/gameinfo_branchspecific.gi'
            other.copy_file(gi_path, dota_path)
            self.le_status_bar.setText('gameinfo_branchspecific.gi reset.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def vpk_build(self):
        try:
            vpk_bat = self.le_root.text() + '/vpk/vpk.bat'
            vpk_path = self.le_root.text() + '/vpk/pak01_dir.vpk'
            mod_path = self.le_game.text() + '/game/mod/pak01_dir.vpk'
            cmd = 'sv_cheats 1; script_reload_code bots/fretbots'
            vpk.vpk_create(vpk_bat)
            other.move_file(vpk_path, mod_path)
            other.copy_cmd(cmd)
            self.le_status_bar.setText('vpk build.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def vpk_build_run(self):
        try:
            vpk_bat = self.le_root.text() + '/vpk/vpk.bat'
            src = self.le_root.text() + '/vpk/pak01_dir.vpk'
            dst = self.le_game.text() + '/game/mod/pak01_dir.vpk'
            vpk.vpk_create(vpk_bat)
            other.move_file(src, dst)
            other.copy_cmd('sv_cheats 1; script_reload_code bots/fretbots')
            self.le_status_bar.setText('vpk build.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def open_pak01(self):
        try:
            pak01_file = self.le_game.text() + '/game/dota/pak01_dir.vpk'
            other.open_file(pak01_file)
            self.le_status_bar.setText('pak01_dir open.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def open_vpk_dir(self):
        try:
            vpk_dir = self.le_root.text() + '/vpk'
            other.open_dir(vpk_dir)
            self.le_status_bar.setText('vpk dir open.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def open_hero_dir(self):
        try:
            hero_dir = self.le_root.text() + '/vpk/pak01_dir/scripts/npc/heroes'
            other.open_dir(hero_dir)
            self.le_status_bar.setText('hero dir open.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def oepn_game_dir(self):
        try:
            game_dir = self.le_game.text() + '/game'
            other.open_dir(game_dir)
            self.le_status_bar.setText('game dir open.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def oepn_mod_dir(self):
        try:
            mod_dir = self.le_game.text() + '/game/mod'
            other.build_dir(mod_dir)
            other.open_dir(mod_dir)
            self.le_status_bar.setText('mod dir open.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def oepn_skin_dir(self):
        try:
            skin_dir = self.le_game.text() + '/game/Dota2SkinChanger'
            other.build_dir(skin_dir)
            other.open_dir(skin_dir)
            self.le_status_bar.setText('skin dir open.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def oepn_skin2_dir(self):
        try:
            skin2_dir = self.le_game.text() + '/game/Dota2SkinChanger2'
            other.build_dir(skin2_dir)
            other.open_dir(skin2_dir)
            self.le_status_bar.setText('skin2 dir open.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def open_bot_script_dir(self):
        try:
            bot_script_dir = self.le_game.text().replace('/steamapps/common/dota 2 beta', '/steamapps/workshop/content/570/3246316298')
            other.open_dir(bot_script_dir)
            self.le_status_bar.setText('bot script dir open.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def open_lua_file(self):
        try:
            script_path = self.le_game.text() + '/game/dota/scripts/vscripts/game/Customize/general.lua'
            other.open_file(script_path)
            self.le_status_bar.setText('lua open.')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def bot_cmd(self):
        try:
            cmd = 'sv_cheats 1; script_reload_code bots/fretbots'
            other.copy_cmd(cmd)
            self.le_status_bar.setText(cmd)
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def steam_cmd(self):
        try:
            cmd = '-novid -prewarm -high -map dota -nod3d9ex -nohltv -novr -nojoy +map_enable_background_maps 1'
            other.copy_cmd(cmd)
            self.le_status_bar.setText(cmd)
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def mipo_cmd(self):
        try:
            cmd = 'dota_player_smart_multiunit_cast 1'
            other.copy_cmd(cmd)
            self.le_status_bar.setText(cmd)
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWin()
    window.show()
    app.exec_()
