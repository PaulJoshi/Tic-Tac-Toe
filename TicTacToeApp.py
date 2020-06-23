import kivy
import ai
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

class Winpop(FloatLayout):
    pass

class Lostpop(FloatLayout):
    pass

class Tiepop(FloatLayout):
    pass

def show_win_popup():
    show = Winpop()

    popupWindow = Popup(title="", content=show, size_hint=(0.6,0.4))

    popupWindow.open()

def show_lost_popup():
    show = Lostpop()

    popupWindow = Popup(title="", content=show, size_hint=(0.6,0.4))

    popupWindow.open()

def show_tie_popup():
    show = Tiepop()

    popupWindow = Popup(title="", content=show, size_hint=(0.6,0.4))

    popupWindow.open()


class MainWindow(Screen):

    def tie_check(self,board):                   #Function to check if game is tied
        tie = False
        count = 0
        for key in board.keys():
            if board[key] == ' ':
                return False
            else:
                count += 1
        if count == 9:
            return True


    def win_check(self,board,avatar):                #Function to check status of the game(win/lose/tie)
        if board['7'] == board['8'] == board['9'] != ' ':
            return 0
        
        elif board['4'] == board['5'] == board['6'] != ' ':
            return 0

        elif board['1'] == board['2'] == board['3'] != ' ':  
            return 0
        
        elif board['1'] == board['4'] == board['7'] != ' ':  
            return 0
        
        elif board['2'] == board['5'] == board['8'] != ' ':
            return 0
        
        elif board['3'] == board['6'] == board['9'] != ' ':
            return 0
        
        elif board['7'] == board['5'] == board['3'] != ' ':  
            return 0
        
        elif board['1'] == board['5'] == board['9'] != ' ': 
            return 0

        return 1

    def press(self,pos):
        app = App.get_running_app()
        if app.flag == 1 :
            app.board[pos] = app.avatar
            print('clicked pos: ' + pos)
            print('Value at clicked pos is: ' + app.board[pos])
            if app.avatar == 'X':
                ai_avatar = 'O'
            else:
                ai_avatar = 'X'
            if pos == '7':
                if self.ids.lbl7.text == ' ':
                    self.ids.lbl7.text = app.board[pos]
                else:
                    return
            elif pos == '8':
                if self.ids.lbl8.text == ' ':
                    self.ids.lbl8.text = app.board[pos]
                else:
                    return
            elif pos == '9':
                if self.ids.lbl9.text == ' ':
                    self.ids.lbl9.text = app.board[pos]
                else:
                    return
            elif pos == '4':
                if self.ids.lbl4.text == ' ':
                    self.ids.lbl4.text = app.board[pos]
                else:
                    return
            elif pos == '5':
                if self.ids.lbl5.text == ' ':
                    self.ids.lbl5.text = app.board[pos]
                else:
                    return
            elif pos == '6':
                if self.ids.lbl6.text == ' ':
                    self.ids.lbl6.text = app.board[pos]
                else:
                    return
            elif pos == '1':
                if self.ids.lbl1.text == ' ':
                    self.ids.lbl1.text = app.board[pos]
                else:
                    return
            elif pos == '2':
                if self.ids.lbl2.text == ' ':
                    self.ids.lbl2.text = app.board[pos]
                else:
                    return
            elif pos == '3':
                if self.ids.lbl3.text == ' ':
                    self.ids.lbl3.text = app.board[pos]
                else:
                    return
            app.count += 1
            if app.count >= 5 and self.win_check(app.board,app.avatar) == 0:
                print('User won')
                show_win_popup()
                app.flag = 0
                return
            elif self.tie_check(app.board):
                print('Tie')
                show_tie_popup()
                app.flag = 0
                return
            move = ai.ai_play(app.board,app.avatar)
            print('ai move is: ')
            print(move)
            app.board[str(move)] = ai_avatar
            if str(move) == '7':
                self.ids.lbl7.text = app.board[str(move)]
            elif str(move) == '8':
                self.ids.lbl8.text = app.board[str(move)]
            elif str(move) == '9':
                self.ids.lbl9.text = app.board[str(move)]
            elif str(move) == '4':
                self.ids.lbl4.text = app.board[str(move)]
            elif str(move) == '5':
                self.ids.lbl5.text = app.board[str(move)]
            elif str(move) == '6':
                self.ids.lbl6.text = app.board[str(move)]
            elif str(move) == '1':
                self.ids.lbl1.text = app.board[str(move)]
            elif str(move) == '2':
                self.ids.lbl2.text = app.board[str(move)]
            elif str(move) == '3':
                self.ids.lbl3.text = app.board[str(move)]
            app.count += 1
            if app.count >= 5 and self.win_check(app.board,app.avatar) == 0:
                show_lost_popup()
                app.flag = 0
                return
            elif self.tie_check(app.board):
                show_tie_popup()
                app.flag = 0
                return
        else:
            return
    
    def newgame(self):
        app = App.get_running_app()
        app.board = {
        '7' : ' ', '8' : ' ', '9' : ' ',
        '4' : ' ', '5' : ' ', '6' : ' ',
        '1' : ' ', '2' : ' ', '3' : ' '}
        app.flag = 1
        app.count = 0
        app.avatar = 'X'
        if app.avatar == 'X':
                ai_avatar = 'O'
        else:
                ai_avatar = 'X'
        app.seed *= -1
        self.ids.lbl7.text = ' '
        self.ids.lbl8.text = ' '
        self.ids.lbl9.text = ' '
        self.ids.lbl4.text = ' '
        self.ids.lbl5.text = ' '
        self.ids.lbl6.text = ' '
        self.ids.lbl1.text = ' '
        self.ids.lbl2.text = ' '
        self.ids.lbl3.text = ' '
        if app.seed == -1:
            move = ai.ai_play(app.board,app.avatar)
            print('ai move is: ')
            print(move)
            app.board[str(move)] = ai_avatar
            if str(move) == '7':
                self.ids.lbl7.text = app.board[str(move)]
            elif str(move) == '8':
                self.ids.lbl8.text = app.board[str(move)]
            elif str(move) == '9':
                self.ids.lbl9.text = app.board[str(move)]
            elif str(move) == '4':
                self.ids.lbl4.text = app.board[str(move)]
            elif str(move) == '5':
                self.ids.lbl5.text = app.board[str(move)]
            elif str(move) == '6':
                self.ids.lbl6.text = app.board[str(move)]
            elif str(move) == '1':
                self.ids.lbl1.text = app.board[str(move)]
            elif str(move) == '2':
                self.ids.lbl2.text = app.board[str(move)]
            elif str(move) == '3':
                self.ids.lbl3.text = app.board[str(move)]
            app.count += 1



class MyApp(App):
    board = {
    '7' : ' ', '8' : ' ', '9' : ' ',
    '4' : ' ', '5' : ' ', '6' : ' ',
    '1' : ' ', '2' : ' ', '3' : ' '}
    flag = 1
    sm = ScreenManager()
    count = 0
    avatar = 'X'
    seed = 1

    def build(self):
        MyApp.sm.add_widget(MainWindow(name='main'))
        return MyApp.sm


if __name__ == "__main__":
    MyApp().run()