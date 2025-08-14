from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from ui.edit import Ui_Form
from script import *


class EditWin(QWidget, Ui_Form):
    def __init__(self, file_path=None):
        super().__init__()
        self.file_path = file_path
        self.setupUi(self)
        self.init_config()
        self.init_win()
        self.init_model()
        self.init_connect()
        self.init_hotkey()

    def init_config(self):
        self.is_top = False
        self.undo_board = None
        self.cut_board = []

    def init_win(self):
        self.setWindowTitle('edit')

    def init_model(self):
        self.model_edit = QStandardItemModel()
        self.lv_edit.setModel(self.model_edit)
        self.lv_edit.setAlternatingRowColors(True)
        # self.lv_edit.setStyleSheet("""
        #     QListView::item {
        #         height: 10px;  /* 设置项的高度 */
        #         padding: 10px;  /* 内边距 */
        #     }
        # """)
        self.update_model()

    def init_connect(self):
        self.btn_on_top.clicked.connect(self.on_top)
        self.btn_reload.clicked.connect(self.reload_file)
        self.btn_load.clicked.connect(self.load_file)
        self.btn_save.clicked.connect(self.save_file)
        self.btn_open.clicked.connect(self.open_file)
        self.btn_undo.clicked.connect(self.undo_select)
        self.btn_cut.clicked.connect(self.cut_select)
        self.btn_paste.clicked.connect(self.paste_select)
        self.btn_auto.clicked.connect(lambda: self.write_select('auto'))
        self.btn_sa.clicked.connect(lambda: self.write_select('sa'))
        self.btn_sp.clicked.connect(lambda: self.write_select('sp'))
        self.btn_has.clicked.connect(lambda: self.write_select('has'))
        self.btn_has_not.clicked.connect(lambda: self.write_select('has_not'))
        self.btn_cd.clicked.connect(lambda: self.write_select('cd'))
        self.btn_ch.clicked.connect(lambda: self.write_select('ch'))
        self.btn_tf.clicked.connect(lambda: self.write_select('tf'))
        self.btn_tab_up.clicked.connect(lambda: self.write_select('up'))
        self.btn_tab_down.clicked.connect(lambda: self.write_select('down'))
        self.btn_1.clicked.connect(lambda: self.write_select('=1'))
        self.btn_2.clicked.connect(lambda: self.write_select('+25%'))
        self.btn_3.clicked.connect(lambda: self.write_select('+33%'))
        self.btn_4.clicked.connect(lambda: self.write_select('+5'))
        self.btn_5.clicked.connect(lambda: self.write_select('+50'))
        self.btn_6.clicked.connect(lambda: self.write_select('+500'))
        self.btn_7.clicked.connect(lambda: self.write_select('+75%'))
        self.btn_8.clicked.connect(lambda: self.write_select('+88%'))
        self.btn_9.clicked.connect(lambda: self.write_select('+99%'))
        self.btn_0.clicked.connect(lambda: self.write_select('=0'))
        self.btn_sub.clicked.connect(lambda: self.write_select('-1'))
        self.btn_add.clicked.connect(lambda: self.write_select('+1'))

    def init_hotkey(self):
        self.btn_reload.setShortcut('r')
        self.btn_save.setShortcut('s')
        self.btn_undo.setShortcut('z')
        self.btn_cut.setShortcut('x')
        self.btn_paste.setShortcut('v')
        self.btn_auto.setShortcut(' ')
        self.btn_cd.setShortcut('c')
        self.btn_ch.setShortcut('h')
        self.btn_tab_up.setShortcut('tab')
        self.btn_tab_down.setShortcut('backspace')
        self.btn_1.setShortcut('1')
        self.btn_2.setShortcut('2')
        self.btn_3.setShortcut('3')
        self.btn_4.setShortcut('4')
        self.btn_5.setShortcut('5')
        self.btn_6.setShortcut('6')
        self.btn_7.setShortcut('7')
        self.btn_8.setShortcut('8')
        self.btn_9.setShortcut('9')
        self.btn_0.setShortcut('0')
        self.btn_sub.setShortcut('-')
        self.btn_add.setShortcut('=')

    def on_top(self):
        self.is_top = not self.is_top
        if self.is_top:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.show()

    def update_model(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = f.readlines()
            self.model_edit.clear()
            for i in data:
                item = QStandardItem(i)
                self.model_edit.appendRow(item)
            self.setWindowTitle(self.file_path)
            self.le_status_bar.setText(f'load file: {self.file_path}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def reload_file(self):
        try:
            self.update_model()
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def load_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, 'load file', self.file_path, '*.txt')[0]
            self.file_path = file_path
            self.update_model()
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def save_file(self):
        try:
            model = self.lv_edit.model()
            row = model.rowCount()
            ls = []
            for r in range(row):
                i = model.index(r, 0)
                c = model.data(i, Qt.DisplayRole)
                ls.append(c)
            with open(self.file_path, 'w', encoding='utf-8', errors='ignore') as f:
                f.writelines(ls)
            self.le_status_bar.setText(f'save file: {self.file_path}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def open_file(self):
        try:
            self.save_file()
            other.open_file(self.file_path)
            self.le_status_bar.setText(f'open file: {self.file_path}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            print(e)

    def read_select(self):
        try:
            model = self.lv_edit.model()
            index = (self.lv_edit.selectionModel().selectedIndexes())[0]
            content = model.data(index, Qt.DisplayRole)
            return model, index, content
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')
            return None, None, None

    def write_select(self, a=None):
        try:
            model, index, old_content = self.read_select()
            match a:
                case 'auto':
                    new_content = ab.auto(old_content)
                case 'sa':
                    new_content = ab.sa(old_content)
                case 'sp':
                    new_content = ab.sp(old_content)
                case 'has_not':
                    new_content = ab.has_not(old_content)
                case 'has':
                    new_content = ab.has(old_content)
                case 'cd':
                    new_content = ab.cd(old_content)
                case 'ch':
                    new_content = ab.ch(old_content)
                case 'tf':
                    new_content = ab.tf(old_content)
                case 'up':
                    new_content = tab.up(old_content)
                case 'down':
                    new_content = tab.down(old_content)
                case _:
                    new_content = ab.user(old_content, a)
            model.setData(index, new_content)
            self.undo_board = old_content
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')

    def undo_select(self):
        try:
            model, index, _ = self.read_select()
            content = self.undo_board
            model.setData(index, content)
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')

    def cut_select(self):
        try:
            model, index, content = self.read_select()
            if content:
                content2 = tab.up(content)
                self.cut_board.append(content2)
                model.setData(index, '')
                self.le_status_bar.setText(f'cut line: {len(self.cut_board)}')
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')

    def paste_select(self):
        try:
            model, index, content = self.read_select()
            content2 = content + '\n'.join(self.cut_board)
            model.setData(index, content2)
            self.le_status_bar.setText(f'paste line: {len(self.cut_board)}')
            self.cut_board = []
        except Exception as e:
            self.le_status_bar.setText(f'error: {e}')


if __name__ == '__main__':
    app = QApplication([])
    window = EditWin('vpk/pak01_dir/scripts/npc/heroes/npc_dota_hero_spectre.txt')
    window.show()
    app.exec_()
