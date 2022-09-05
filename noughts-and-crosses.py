import sys
import sqlite3
import game_ui
import create_ui
import choice_ui
import menu_ui
import authorization_ui
import rename_ui
import new_password_ui
from random import choice
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog, QMessageBox
nickname = ''


class GameWindow(QWidget, game_ui.Ui_Form):
    def __init__(self, *game_mode):
        super().__init__()
        self.setupUi(self)
        self.nickname = ''
        self.gm_mode = ''
        self.initUI(game_mode)
        self.con = sqlite3.connect('players.db')

        self.examination_hod = ''
        self.now_hod = ''
        self.start_hod = ''
        self.ex1 = ''
        self.buttonGroup.buttonClicked.connect(self.start)
        self.buttons = [self.pushButton, self.pushButton_2, self.pushButton_3,
                        self.pushButton_4, self.pushButton_5, self.pushButton_6,
                        self.pushButton_7, self.pushButton_8, self.pushButton_9]
        global nickname
        self.nickname = nickname
        self.restart.clicked.connect(self.restart_game)
        self.menu.clicked.connect(self.menu_open)
        self.regime_change.clicked.connect(self.change_mode)
        for btn in self.buttons:
            btn.clicked.connect(self.run_game)
        if self.gm_mode == 'Игра против бота':
            self.regime_change.setText('Играть вдвоём')
            self.setWindowTitle('Игра с ботом')
        else:
            self.regime_change.setText('Играть с ботом')
            self.setWindowTitle('Игра вдвоём')

    def initUI(self, game_mode):
        self.gm_mode = game_mode[1]

    def start(self, checked):
        self.start_hod = checked.text()
        if self.examination_hod == '':
            self.examination_hod = self.start_hod
        if self.start_hod != self.examination_hod:
            self.restart_game()
            self.examination_hod = self.start_hod
        self.now_hod = self.start_hod

    def run_game(self):
        if self.start_hod == '':
            self.info.setText('Выберите первого игрока!')
        else:
            self.info.setText('')
            btn = self.sender()
            btn.setText(self.now_hod)
            btn.setEnabled(False)
            who_win = self.win()
            if who_win != 'no':
                for b in self.buttons:
                    b.setEnabled(False)
                self.info.setText(f'Победил {who_win}')
                if self.gm_mode == 'Игра против бота':
                    cur = self.con.cursor()
                    cur.execute(f"""UPDATE info SET num_wins=num_wins+1 WHERE nickname='{self.nickname}'""")
                    cur.execute(f"""UPDATE info SET num_games=num_games+1 WHERE nickname='{self.nickname}'""")
                    self.con.commit()
            if self.now_hod == '0':
                self.now_hod = 'X'
            else:
                self.now_hod = '0'
            if self.gm_mode == 'Игра против бота' and who_win == 'no' and who_win != 'draw':
                self.bot_move()
                who_win = self.win()
                if who_win != 'no':
                    for b in self.buttons:
                        b.setEnabled(False)
                    self.info.setText(f'Победил {who_win}')
                    if who_win == 'draw':
                        for b in self.buttons:
                            b.setEnabled(False)
                        self.info.setText('Ничья')
            if who_win == 'draw':
                for b in self.buttons:
                    b.setEnabled(False)
                self.info.setText('Ничья')

    def bot_move(self):
        allied_pair_ind = self.pair_search(self.now_hod)
        enemy_pair_ind = self.pair_search(self.start_hod)
        singles_ind = self.singles_search()
        no_signs_ind = self.no_allied_signs()
        if isinstance(allied_pair_ind, int):
            self.buttons[allied_pair_ind].setText(self.now_hod)
            self.buttons[allied_pair_ind].setEnabled(False)
            if self.now_hod == '0':
                self.now_hod = 'X'
            else:
                self.now_hod = '0'
        elif isinstance(enemy_pair_ind, int):
            self.buttons[enemy_pair_ind].setText(self.now_hod)
            self.buttons[enemy_pair_ind].setEnabled(False)
            if self.now_hod == '0':
                self.now_hod = 'X'
            else:
                self.now_hod = '0'
        elif isinstance(singles_ind, int):
            self.buttons[singles_ind].setText(self.now_hod)
            self.buttons[singles_ind].setEnabled(False)
            if self.now_hod == '0':
                self.now_hod = 'X'
            else:
                self.now_hod = '0'
        elif isinstance(no_signs_ind, int):
            self.buttons[no_signs_ind].setText(self.now_hod)
            self.buttons[no_signs_ind].setEnabled(False)
            if self.now_hod == '0':
                self.now_hod = 'X'
            else:
                self.now_hod = '0'
        else:
            ind = [self.pushButton.text(), self.pushButton_2.text(), self.pushButton_3.text(),
                   self.pushButton_4.text(), self.pushButton_5.text(), self.pushButton_6.text(),
                   self.pushButton_7.text(), self.pushButton_8.text(), self.pushButton_9.text()].index('')
            self.buttons[ind].setText(self.now_hod)
            self.buttons[ind].setEnabled(False)
            if self.now_hod == '0':
                self.now_hod = 'X'
            else:
                self.now_hod = '0'
            return

    def pair_search(self, mark):
        # функция для поика линий с двумя одинаковыми символами(Х или 0) и пустой клетки
        test = ['', mark, mark]
        # горизонталь
        if test == sorted([self.buttons[0].text(), self.buttons[1].text(), self.buttons[2].text()]):
            return [0, 1, 2][[self.buttons[0].text(), self.buttons[1].text(), self.buttons[2].text()].index('')]
        if test == sorted([self.buttons[3].text(), self.buttons[4].text(), self.buttons[5].text()]):
            return [3, 4, 5][[self.buttons[3].text(), self.buttons[4].text(), self.buttons[5].text()].index('')]
        if test == sorted([self.buttons[6].text(), self.buttons[7].text(), self.buttons[8].text()]):
            return [6, 7, 8][[self.buttons[6].text(), self.buttons[7].text(), self.buttons[8].text()].index('')]
        # вертикаль
        if test == sorted([self.buttons[0].text(), self.buttons[3].text(), self.buttons[6].text()]):
            return [0, 3, 6][[self.buttons[0].text(), self.buttons[3].text(), self.buttons[6].text()].index('')]
        if test == sorted([self.buttons[1].text(), self.buttons[4].text(), self.buttons[7].text()]):
            return [1, 4, 7][[self.buttons[1].text(), self.buttons[4].text(), self.buttons[7].text()].index('')]
        if test == sorted([self.buttons[2].text(), self.buttons[5].text(), self.buttons[8].text()]):
            return [2, 5, 8][[self.buttons[2].text(), self.buttons[5].text(), self.buttons[8].text()].index('')]
        # диагональ
        if test == sorted([self.buttons[0].text(), self.buttons[4].text(), self.buttons[8].text()]):
            return [0, 4, 8][[self.buttons[0].text(), self.buttons[4].text(), self.buttons[8].text()].index('')]
        if test == sorted([self.buttons[2].text(), self.buttons[4].text(), self.buttons[6].text()]):
            return [2, 4, 6][[self.buttons[2].text(), self.buttons[4].text(), self.buttons[6].text()].index('')]
        return ''

    def singles_search(self):
        # функция ищет строки с одним знаком и двумя пустыми клетками и ставит знак в наилучшей клетке

        # диагональ
        test = ['', '', self.now_hod]
        if test == sorted([self.buttons[0].text(), self.buttons[4].text(), self.buttons[8].text()]):
            if self.buttons[4].text() == self.now_hod:
                exam1 = [self.buttons[5].text(), self.buttons[7].text(), self.buttons[8].text()]
                exam2 = [self.buttons[0].text(), self.buttons[1].text(), self.buttons[3].text()]
                if exam1.count(self.now_hod) + exam1.count('') >= exam2.count(self.now_hod) + exam2.count(''):
                    return 8
                else:
                    return 0
            else:
                return 4
        if test == sorted([self.buttons[2].text(), self.buttons[4].text(), self.buttons[6].text()]):
            if self.buttons[4].text() == self.now_hod:
                exam1 = [self.buttons[1].text(), self.buttons[2].text(), self.buttons[5].text()]
                exam2 = [self.buttons[3].text(), self.buttons[6].text(), self.buttons[7].text()]
                if exam1.count(self.now_hod) + exam1.count('') >= exam2.count(self.now_hod) + exam2.count(''):
                    return 2
                else:
                    return 6
            else:
                return 4

        # горизонталь
        if test == sorted([self.buttons[0].text(), self.buttons[1].text(), self.buttons[2].text()]):
            if self.buttons[0].text() == self.now_hod:
                return 2
            else:
                return 0
        if test == sorted([self.buttons[3].text(), self.buttons[4].text(), self.buttons[5].text()]):
            if self.buttons[4].text() == self.now_hod:
                exam1 = [self.buttons[0].text(), self.buttons[6].text()]
                exam2 = [self.buttons[2].text(), self.buttons[8].text()]
                if exam1.count(self.now_hod) + exam1.count('') >= exam2.count(self.now_hod) + exam2.count(''):
                    return 3
                else:
                    return 5
            else:
                return 4
        if test == sorted([self.buttons[5].text(), self.buttons[7].text(), self.buttons[8].text()]):
            if self.buttons[5].text() == self.now_hod:
                return 8
            else:
                return 5

        # вертикаль
        if test == sorted([self.buttons[0].text(), self.buttons[3].text(), self.buttons[6].text()]):
            if self.buttons[0].text() == self.now_hod:
                return 6
            else:
                return 0
        if test == sorted([self.buttons[1].text(), self.buttons[4].text(), self.buttons[7].text()]):
            if self.buttons[4].text() == self.now_hod:
                exam1 = [self.buttons[0].text(), self.buttons[2].text()]
                exam2 = [self.buttons[6].text(), self.buttons[8].text()]
                if exam1.count(self.now_hod) + exam1.count('') >= exam2.count(self.now_hod) + exam2.count(''):
                    return 1
                else:
                    return 7
            else:
                return 4
        if test == sorted([self.buttons[2].text(), self.buttons[5].text(), self.buttons[8].text()]):
            if self.buttons[2].text() == self.now_hod:
                return 8
            else:
                return 2
        else:
            return ''

    def no_allied_signs(self):
        if [self.pushButton.text(), self.pushButton_2.text(), self.pushButton_3.text(),
            self.pushButton_4.text(), self.pushButton_5.text(), self.pushButton_6.text(),
                self.pushButton_7.text(), self.pushButton_8.text(), self.pushButton_9.text()].count(self.now_hod) == 0:
            if self.buttons[4].text() == self.start_hod:
                return choice([0, 2, 8, 6])
            else:
                return 4
        else:
            return ''

    def win(self):
        # горизонталь
        if self.buttons[0].text() == self.buttons[1].text() == self.buttons[2].text() == 'X' or\
                self.buttons[0].text() == self.buttons[1].text() == self.buttons[2].text() == '0':
            return f'{self.buttons[0].text()}'
        if self.buttons[3].text() == self.buttons[4].text() == self.buttons[5].text() == 'X' or\
                self.buttons[3].text() == self.buttons[4].text() == self.buttons[5].text() == '0':
            return f'{self.buttons[3].text()}'
        if self.buttons[6].text() == self.buttons[7].text() == self.buttons[8].text() == 'X' or\
                self.buttons[6].text() == self.buttons[7].text() == self.buttons[8].text() == '0':
            return f'{self.buttons[6].text()}'
        # вертикаль
        if self.buttons[0].text() == self.buttons[3].text() == self.buttons[6].text() == 'X' or\
                self.buttons[0].text() == self.buttons[3].text() == self.buttons[6].text() == '0':
            return f'{self.buttons[0].text()}'
        if self.buttons[1].text() == self.buttons[4].text() == self.buttons[7].text() == 'X' or\
                self.buttons[1].text() == self.buttons[4].text() == self.buttons[7].text() == '0':
            return f'{self.buttons[1].text()}'
        if self.buttons[2].text() == self.buttons[5].text() == self.buttons[8].text() == 'X' or\
                self.buttons[2].text() == self.buttons[5].text() == self.buttons[8].text() == '0':
            return f'{self.buttons[2].text()}'
        # диагональ
        if self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text() == 'X' or\
                self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text() == '0':
            return f'{self.buttons[0].text()}'
        if self.buttons[2].text() == self.buttons[4].text() == self.buttons[6].text() == 'X' or\
                self.buttons[2].text() == self.buttons[4].text() == self.buttons[6].text() == '0':
            return f'{self.buttons[2].text()}'
        try:
            [self.pushButton.text(), self.pushButton_2.text(), self.pushButton_3.text(),
                self.pushButton_4.text(), self.pushButton_5.text(), self.pushButton_6.text(),
                self.pushButton_7.text(), self.pushButton_8.text(), self.pushButton_9.text()].index('')
        except Exception:
            return 'draw'

        else:
            return 'no'

    def menu_open(self):
        self.hide()
        self.ex1 = MenuWindow()
        self.ex1.show()

    def change_mode(self):
        if self.regime_change.text() == 'Играть вдвоём':
            self.regime_change.setText('Играть с ботом')
            self.gm_mode = 'Игра вдвоём'
            self.setWindowTitle('Игра вдвоём')
            self.restart_game()
        else:
            self.gm_mode = 'Игра против бота'
            self.regime_change.setText('Играть вдвоём')
            self.setWindowTitle('Игра с ботом')
            self.restart_game()

    def restart_game(self):
        # функция перезапуска игры
        for b in self.buttons:
            b.setText('')
            b.setEnabled(True)
            self.info.setText('')
            self.now_hod = self.start_hod


class ChoiceWindow(QMainWindow, choice_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ex = ''
        self.setWindowTitle('Авторизвция/Новый игрок')
        self.authorization_btn.clicked.connect(self.authorization_window)
        self.create_player_btn.clicked.connect(self.create_player_window)

    def authorization_window(self):
        self.hide()
        self.ex = AuthorizationWindow()
        self.ex.show()

    def create_player_window(self):
        self.hide()
        self.ex = CreateWindow()
        self.ex.show()


class CreateWindow(QWidget, create_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ex = ''
        self.game_mode = ''
        self.setWindowTitle('Создание нового игрока')
        self.create_btn.clicked.connect(self.create_player)
        self.con = sqlite3.connect('players.db')
        self.previous_window.clicked.connect(self.back)
        self.requirements.clicked.connect(self.requirements_open)

    def create_player(self):
        if self.examination():
            cur = self.con.cursor()
            cur.execute(f"""INSERT INTO info(nickname, password, num_wins) 
            VALUES('{self.nickname.text()}', '{self.password.text()}', {0})""")
            self.con.commit()

            self.game_mode, ok_pressed = QInputDialog.getItem(
                self, 'Выберите режим игры', 'Режим игры?', ('Игра против бота', 'Игра вдвоём'), 1, False)
            if ok_pressed:
                global nickname
                nickname = self.nickname.text()
                self.con.close()
                self.hide()
                self.ex = GameWindow(self, self.game_mode)
                self.ex.show()

    def examination(self):
        cur = self.con.cursor()
        if not(self.nickname.text()) or not(self.password.text()) or\
                not(self.confirm_password.text()):
            self.error.setText('Пожалуйста, заполните все поля')
            return False
        if len(self.nickname.text()) < 3:
            self.error.setText('Ваше имя должно быть длинее 2 символов')
            return False
        if len(self.nickname.text()) > 8:
            self.error.setText('Ваше имя не должно быть длинее 8 символов')
            return False
        if not(self.nickname.text().isalnum()):
            self.error.setText('Ваше имя должно состоять только из цифр и букв')
            return False
        if self.nickname.text() in [i[0] for i in cur.execute("SELECT nickname FROM info").fetchall()]:
            self.error.setText('Игрок с таким именем уже существует')
            return False
        if len(self.password.text()) < 5:
            self.error.setText('Ваш пароль должен быть длинее 4 символов')
            return False
        if self.password.text() != self.confirm_password.text():
            self.error.setText('Пароли должны совпадать')
            return False
        if self.password.text() == self.password.text().lower()\
                or self.password.text() == self.password.text().upper():
            self.error.setText('В вашем пароле обязательно должны быть заглавные и строчные буквы')
            return False
        else:
            return True

    def requirements_open(self):
        QMessageBox.information(self, 'Требования', 'Требовния к паролю:\n1. Должен быть длинее 4 символов\n'
                                                    '2. В нем обязательно должны быть заглавные и строчные буквы\n'
                                                    'Требования к имени:\n1. Ваше имя должно быть длинее 2 сиволов,'
                                                    'но не больше 8\n2. Ваше имя должно состоять только из цифр и букв')

    def back(self):
        self.con.close()
        self.hide()
        self.ex = ChoiceWindow()
        self.ex.show()


class AuthorizationWindow(QWidget, authorization_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ex = ''
        self.game_mode = ''
        self.setWindowTitle('Авторизация')
        self.enter_btn.clicked.connect(self.authorization)
        self.con = sqlite3.connect('players.db')
        self.previous_window.clicked.connect(self.back)

    def authorization(self):
        if self.examination():
            self.game_mode, ok_pressed = QInputDialog.getItem(
                self, 'Выберите режим игры', 'Режим игры?', ('Игра против бота', 'Игра вдвоём'), 1, False)
            if ok_pressed:
                global nickname
                nickname = self.nickname.text()
                self.con.close()
                self.hide()
                self.ex = GameWindow(self, self.game_mode)
                self.ex.show()

    def examination(self):
        cur = self.con.cursor()
        if not(self.nickname.text()) or not(self.password.text()):
            self.error.setText('Пожалуйста, заполните все поля')
            return False
        if self.nickname.text() not in [i[0] for i in cur.execute("SELECT nickname FROM info").fetchall()]:
            self.error.setText('Пользователя с таким именем не существует')
            return False
        if self.password.text() not in [i[0] for i in cur.execute(
                f"SELECT password FROM info WHERE nickname = '{self.nickname.text()}'").fetchall()]:
            self.error.setText('Неверный пароль')
            return False
        return True

    def back(self):
        self.hide()
        self.con.close()
        self.hide()
        self.ex = ChoiceWindow()
        self.ex.show()


class MenuWindow(QWidget, menu_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Меню')
        self.con = sqlite3.connect('players.db')
        cur = self.con.cursor()
        self.ex = ''
        self.nickname = ''
        data = cur.execute('SELECT nickname, num_wins, num_games FROM info').fetchall()
        result = [*data]
        for i in result:
            distance = ' ' * (12 - len(i[0]))
            if i[1] == 0:
                self.players_list.addItem(f'{i[0] + distance}{i[2]}              {0}%')
            else:
                self.players_list.addItem(f'{i[0] + distance}{i[2]}              {round((i[1] / i[2]) * 100)}%')
        self.rename_btn.clicked.connect(self.rename_window_open)
        self.change_password_btn.clicked.connect(self.change_password_window)
        self.delete_btn.clicked.connect(self.delete_window_open)

    def rename_window_open(self):
        if self.alterable_nickname.text() == '':
            self.message.setText('Ввод изменяемого имени обязателен!')
            return
        cur = self.con.cursor()
        data = cur.execute('SELECT nickname FROM info').fetchall()
        result = [nick for i in data for nick in i]
        if self.alterable_nickname.text() not in result:
            self.message.setText('Игрока с таким именем не существует')
            return
        alter_nickname = self.alterable_nickname.text()
        self.ex = RenameWindow(self, alter_nickname)

        self.ex.show()

    def change_password_window(self):
        if self.alterable_nickname.text() == '':
            self.message.setText('Ввод изменяемого имени обязателен!')
            return
        cur = self.con.cursor()
        data = cur.execute('SELECT nickname FROM info').fetchall()
        result = [nick for i in data for nick in i]
        if self.alterable_nickname.text() not in result:
            self.message.setText('Игрока с таким именем не существует')
            return
        alter_nickname = self.alterable_nickname.text()
        self.ex = NewPasswordWindow(self, alter_nickname)
        self.ex.show()

    def delete_window_open(self):
        if self.alterable_nickname.text() == '':
            self.message.setText('Ввод изменяемого имени обязателен!')
            return
        cur = self.con.cursor()
        data = cur.execute('SELECT nickname FROM info').fetchall()
        result = [nick for i in data for nick in i]
        if self.alterable_nickname.text() not in result:
            self.message.setText('Игрока с таким именем не существует')
            return
        cur.execute(f"DELETE FROM info WHERE nickname='{self.alterable_nickname.text()}'")
        self.con.commit()
        global nickname
        self.nickname = nickname
        if self.nickname == self.alterable_nickname.text():
            QMessageBox.information(self, 'Удаление игрока', 'Аккаунт был успешно удалён!\n'
                                                             'По прчине того, что вы удалили акккаунт в котором \n'
                                                             'находились, нужно будет заново войти в аккаунт')
            self.hide()
            self.ex = ChoiceWindow()
            self.ex.show()
        else:
            QMessageBox.information(self, 'Удаление аккаунта', 'Аккаунт был успешно удалён!\n'
                                                               'Обновите меню для просмотра результата')

    def closeEvent(self, event):
        alt = self.alterable_nickname.text()
        self.ex = GameWindow(self, alt)
        self.ex.show()


class RenameWindow(QWidget, rename_ui.Ui_Form):
    def __init__(self, *alter_nickname):
        super().__init__()
        self.setupUi(self)
        self.alter_nickname = ''
        self.initUI(alter_nickname)

        self.con = sqlite3.connect('players.db')
        self.setWindowTitle('Изменение имени')
        self.accept_btn.clicked.connect(self.accept)

    def initUI(self, alter_nick):
        self.alter_nickname = alter_nick[1]

    def accept(self):
        if self.examination():
            cur = self.con.cursor()
            cur.execute(f"""UPDATE info SET nickname='{self.new_nickname.text()}'
            WHERE nickname='{self.alter_nickname}'""")
            global nickname
            nickname = self.new_nickname.text()
            self.con.commit()
            self.hide()
            QMessageBox.information(self, 'Переименование', 'Переименование прошло успешно!,\n'
                                                            'Обновите меню для просмотра результата')

    def examination(self):
        cur = self.con.cursor()
        if self.new_nickname.text() == '' or self.confirm_new_name.text() == '':
            self.error.setText('Заполните все поля')
            return False
        if self.new_nickname.text() != self.confirm_new_name.text():
            self.error.setText('Ваши имена не совпадают')
            return False
        if len(self.new_nickname.text()) < 3:
            self.error.setText('Ваше прозвище должно быть длинее 2 символов')
            return False
        if len(self.new_nickname.text()) > 8:
            self.error.setText('Ваше прозвище не должно быть длинее 8 символов')
            return False
        if self.alter_nickname == self.new_nickname.text():
            self.error.setText('Предыдущее имя не должно совпадать новым')
            return False
        if self.new_nickname.text() in [i[0] for i in cur.execute("SELECT nickname FROM info").fetchall()]:
            self.error.setText('Игрок с таким именем уже существует')
            return False
        return True


class NewPasswordWindow(QWidget, new_password_ui.Ui_Form):
    def __init__(self, *alter_nickname):
        super().__init__()
        self.setupUi(self)
        self.alter_nickname = ''
        self.initUI(alter_nickname)

        self.con = sqlite3.connect('players.db')
        self.setWindowTitle('Изменение пароля')
        self.accept_btn.clicked.connect(self.accept)

    def initUI(self, alter_nick):
        self.alter_nickname = alter_nick[1]

    def accept(self):
        if self.examination():
            cur = self.con.cursor()
            cur.execute(f"""UPDATE info SET password='{self.new_password.text()}'
            WHERE nickname='{self.alter_nickname}'""")
            self.con.commit()
            self.hide()
            QMessageBox.information(self, 'Смена пароля', 'Смена пароля произошла успешно!\n')

    def examination(self):
        cur = self.con.cursor()
        previous_password = cur.execute(
            f"SELECT password FROM info WHERE nickname = '{self.alter_nickname}'").fetchall()
        if not (self.password.text()) or not (self.new_password.text()) or not(self.confirm_new_password.text()):
            self.error.setText('Пожалуйста, заполните все поля')
            return False
        if self.password.text() not in [i[0] for i in previous_password]:
            self.error.setText('Текущий пароль неверный')
            return False
        if len(self.new_password.text()) < 5:
            self.error.setText('Ваш новый пароль должен быть длинее 4 символов')
            return False
        if self.new_password.text() == self.new_password.text().lower()\
                or self.new_password.text() == self.new_password.text().upper():
            self.error.setText('В вашем пароле обязательно должны\n быть заглавные и строчные буквы')
            return False
        if self.new_password.text() != self.confirm_new_password.text():
            self.error.setText('Пароли не совпадают')
            return False
        if self.new_password.text() in previous_password[0]:
            self.error.setText('Предыдущий пароль не должен совпадать с новым')
            return False
        else:
            return True


def main():
    app = QApplication(sys.argv)
    ex = ChoiceWindow()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
