# -*- coding: utf-8 -*-
"""
Created on Sat May 16 13:50:09 2020

@author: cohae
"""
import pymysql
import random
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, BooleanProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.clock import Clock
from functools import partial
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.image import Image
import os
import certifi
from android.storage import primary_external_storage_path

os.environ["SSL_CERT_FILE"]=certifi.where()
primary_ext_storage = primary_external_storage_path()

connection = pymysql.connect("sql.haegelix.de", "db_flunky", "fsdhjkvgu245jhsdg", "flunkyball")
# connection=s.connect("Nutzerdatenbank.db")
cursor1 = connection.cursor()
connection.commit()

# c='''PRAGMA foreign_keys= ON'''
# cursor1.execute(c)

command = """CREATE TABLE IF NOT EXISTS Nutzer(id int PRIMARY KEY, Nutzername TEXT, Passwort TEXT)"""
cursor1.execute(command)
connection.commit()


def donothing():
    u = 1
    return u

class WindowManager(ScreenManager):
    pass


# -------------------------CHOOSE-----------------------------------------


class LogInOrRegister(Screen):
    pass


class NumberOfGamersLayout(Screen):
    pass

class OddNumber(Screen):
    pass

class UserProfile(Screen):
    pass

#------------------Team Layouts---------------------
class TeamLayoutFourGamers(Screen):
    number= ObjectProperty()
    def showrules(self):
        popup = Popup(title='Da Rules',
                      content=Label(text='Your will be divided in two equally-sized teams. \n'
                                         'The upper team will have the first move!\nWhether the bottle will fall or not, will be\ndetermined by a random generator\n'
                                         'Every team will have the same odds of winning.\n ' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()


class TeamLayoutSixGamers(Screen):
    number= ObjectProperty()
    def showrules(self):
        popup = Popup(title='Da Rules',
                      content=Label(text='Your will be divided in two equally-sized teams. \n'
                                         'The upper team will have the first move!\nWhether the bottle will fall or not, will be\ndetermined by a random generator\n'
                                         'Every team will have the same odds of winning.\n ' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()

class TeamLayoutEightGamers(Screen):
    number= ObjectProperty()
    def showrules(self):
        popup = Popup(title='Da Rules',
                      content=Label(text='Your will be divided in two equally-sized teams. \n'
                                         'The upper team will have the first move!\nWhether the bottle will fall or not, will be\ndetermined by a random generator\n'
                                         'Every team will have the same odds of winning.\n ' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()


class TeamLayoutTenGamers(Screen):
    number= ObjectProperty()
    def showrules(self):
        popup = Popup(title='Da Rules',
                      content=Label(text='Your will be divided in two equally-sized teams. \n'
                                         'The upper team will have the first move!\nWhether the bottle will fall or not, will be\ndetermined by a random generator\n'
                                         'Every team will have the same odds of winning.\n ' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()

#------------------------Game Layouts-----------------

class Game_Four_Players(Screen):
    counter =0
    dictid = {"Team1": ["layoutfour_teamone_playerone", "layoutfour_teamone_playertwo"], "Team2": ["layoutfour_teamtwo_playerone", "layoutfour_teamtwo_playertwo"]}

    def showrules(self):
        popup = Popup(title='Da Rules',
                      content=Label(text='Your will be divided in two equally-sized teams. \n'
                                         'The upper team will have the first move!\nWhether the bottle will fall or not, will be\ndetermined by a random generator\n'
                                         'Every team will have the same odds of winning.\n ' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()

    def about(self):
        popup = Popup(title='About this game',
                      content=Label(text='This mobile app has been developed by\nme (Coco/f/23.y.o./studying Medical Engineering)\n'
                                         'as a private project to defeat boredom during my quarantine.\nThis app was the first time ever for me to use the kivy-language,\nso please be forgiving and patient if there are any bugs\nduring the  game.\n\nI am thankful for every tip regarding things that can\n'
                                         'be improved so please do not hesitate to\ncontact me under COHAE97@YAHOO.DE' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()
    def increment(self):
        self.counter += 1
        if self.counter == 1:
            Game_Ten_Players.player11(self)
        elif self.counter == 2:
            Game_Ten_Players.player21(self)
        elif self.counter == 3:
            Game_Ten_Players.player12(self)
        elif self.counter == 4:
            Game_Ten_Players.player22(self)
        else:
            self.ids["startbutton_four"].text = "VORBEI"
    def labeltored(self, Team, el, *largs):
        self.ids[self.dictid[Team][el]].background_color = [1,0,0, 0.5]
    def labeltoblue(self, Team, el, *largs):
        self.ids[self.dictid[Team][el]].background_color = [0, 0.5, 0.5, 0.8]
    def changebutton(self, *args):
        self.ids["startbutton_four"].text = "Next Player!"



class Game_Six_Players(Screen):
    counter =0
    dictid = {"Team1": ["layoutsix_teamone_playerone", "layoutsix_teamone_playertwo", "layoutsix_teamone_playerthree"], "Team2": ["layoutsix_teamtwo_playerone", "layoutsix_teamtwo_playertwo", "layoutsix_teamtwo_playerthree"]}

    def showrules(self):
        popup = Popup(title='Da Rules',
                      content=Label(text='Your will be divided in two equally-sized teams. \n'
                                         'The upper team will have the first move!\nWhether the bottle will fall or not, will be\ndetermined by a random generator\n'
                                         'Every team will have the same odds of winning.\n ' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()

    def about(self):
        popup = Popup(title='About this game',
                      content=Label(text='This mobile app has been developed by\nme (Coco/f/23.y.o./studying Medical Engineering)\n'
                                         'as a private project to defeat boredom during my quarantine.\nThis app was the first time ever for me to use the kivy-language,\nso please be forgiving and patient if there are any bugs\nduring the  game.\n\nI am thankful for every tip regarding things that can\n'
                                         'be improved so please do not hesitate to\ncontact me under COHAE97@YAHOO.DE' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()
    def increment(self):
        self.counter += 1
        if self.counter == 1:
            Game_Ten_Players.player11(self)
        elif self.counter == 2:
            Game_Ten_Players.player21(self)
        elif self.counter == 3:
            Game_Ten_Players.player12(self)
        elif self.counter == 4:
            Game_Ten_Players.player22(self)
        elif self.counter == 5:
            Game_Ten_Players.player13(self)
        elif self.counter == 6:
            Game_Ten_Players.player23(self)
        else:
            self.ids["startbutton_six"].text = "VORBEI"
    def labeltored(self, Team, el, *largs):
        self.ids[self.dictid[Team][el]].background_color = [1,0,0, 0.5]
    def labeltoblue(self, Team, el, *largs):
        self.ids[self.dictid[Team][el]].background_color = [0, 0.5, 0.5, 0.8]
    def changebutton(self, *args):
        self.ids["startbutton_six"].text = "Next Player!"


class Game_Eight_Players(Screen):
    counter =0
    dictid = {"Team1": ["layouteight_teamone_playerone", "layouteight_teamone_playertwo", "layouteight_teamone_playerthree", "layouteight_teamone_playerfour"], "Team2": ["layouteight_teamtwo_playerone", "layouteight_teamtwo_playertwo", "layouteight_teamtwo_playerthree", "layouteight_teamtwo_playerfour"]}

    def showrules(self):
        popup = Popup(title='Da Rules',
                      content=Label(text='Your will be divided in two equally-sized teams. \n'
                                         'The upper team will have the first move!\nWhether the bottle will fall or not, will be\ndetermined by a random generator\n'
                                         'Every team will have the same odds of winning.\n ',
                                    pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()
    def about(self):
        popup = Popup(title='About this game',
                      content=Label(text='This mobile app has been developed by\nme (Coco/f/23.y.o./studying Medical Engineering)\n'
                                         'as a private project to defeat boredom during my quarantine.\nThis app was the first time ever for me to use the kivy-language,\nso please be forgiving and patient if there are any bugs\nduring the  game.\n\nI am thankful for every tip regarding things that can\n'
                                         'be improved so please do not hesitate to\ncontact me under COHAE97@YAHOO.DE' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()

    def increment(self):
        self.counter += 1
        if self.counter == 1:
            Game_Ten_Players.player11(self)
        elif self.counter == 2:
            Game_Ten_Players.player21(self)
        elif self.counter == 3:
            Game_Ten_Players.player12(self)
        elif self.counter == 4:
            Game_Ten_Players.player22(self)
        elif self.counter == 5:
            Game_Ten_Players.player13(self)
        elif self.counter == 6:
            Game_Ten_Players.player23(self)
        elif self.counter == 7:
            Game_Ten_Players.player14(self)
        elif self.counter == 8:
            Game_Ten_Players.player24(self)
        else:
            self.ids["startbutton_eight"].text = "VORBEI"
    def labeltored(self, Team, el, *largs):
        self.ids[self.dictid[Team][el]].background_color = [1,0,0, 0.5]
    def labeltoblue(self, Team, el, *largs):
        self.ids[self.dictid[Team][el]].background_color = [0, 0.5, 0.5, 0.8]
    def changebutton(self, *args):
        self.ids["startbutton_eight"].text = "Next Player!"


class Game_Ten_Players(Screen):
    #TeamOnePlayerOne = StringProperty(None)
    counter =0
    dictid = {"Team1": ["layoutten_teamone_playerone", "layoutten_teamone_playertwo", "layoutten_teamone_playerthree", "layoutten_teamone_playerfour", "layoutten_teamone_playerfive"], "Team2": ["layoutten_teamtwo_playerone", "layoutten_teamtwo_playertwo", "layoutten_teamtwo_playerthree", "layoutten_teamtwo_playerfour", "layoutten_teamtwo_playerfive"]}
    def showrules(self):
        popup = Popup(title='Da Rules',
                      content=Label(text='Your will be divided in two equally-sized teams. \n'
                                         'The upper team will have the first move!\nWhether the bottle will fall or not, will be\ndetermined by a random generator\n'
                                         'Every team will have the same odds of winning.\n ' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()

    def about(self):
        popup = Popup(title='About this game',
                      content=Label(text='This mobile app has been developed by\nme (Coco/f/23.y.o./studying Medical Engineering)\n'
                                         'as a private project to defeat boredom during my quarantine.\nThis app was the first time ever for me to use the kivy-language,\nso please be forgiving and patient if there are any bugs\nduring the  game.\n\nI am thankful for every tip regarding things that can\n'
                                         'be improved so please do not hesitate to\ncontact me under COHAE97@YAHOO.DE' , pos_hint={"x": 0.2, "top": 0.6}),
                      pos_hint={"x": 0.2, "top": 0.8})
        popup.open()

    def increment(self):
        self.counter += 1
        if self.counter == 1:
            self.player11()
        elif self.counter==2:
            self.player21()
        elif self.counter==3:
            self.player12()
        elif self.counter==4:
            self.player22()
        elif self.counter==5:
            self.player13()
        elif self.counter==6:
            self.player23()
        elif self.counter==7:
            self.player14()
        elif self.counter==8:
            self.player24()
        elif self.counter==9:
            self.player15()
        elif self.counter==10:
            self.player25()
        else:
            self.ids["startbutton"].text="VORBEI"


    def player11(self):
        Clock.schedule_once(partial(self.labeltored, "Team1", 0), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team1", 0), 9)
        Clock.schedule_once(self.changebutton, 10)
    def player12(self):
        Clock.schedule_once(partial(self.labeltored, "Team1", 1), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team1", 1), 9)
        Clock.schedule_once(self.changebutton, 10)
    def player13(self):
        Clock.schedule_once(partial(self.labeltored, "Team1", 2), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team1", 2), 9)
        Clock.schedule_once(self.changebutton, 10)
    def player14(self):
        Clock.schedule_once(partial(self.labeltored, "Team1", 3), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team1", 3), 9)
        Clock.schedule_once(self.changebutton, 10)
    def player15(self):
        Clock.schedule_once(partial(self.labeltored, "Team1", 4), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team1", 4), 9)
        Clock.schedule_once(self.changebutton, 10)

    def player21(self):
        Clock.schedule_once(partial(self.labeltored, "Team2", 0), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team2", 0), 9)
        Clock.schedule_once(self.changebutton, 10)
    def player22(self):
        Clock.schedule_once(partial(self.labeltored, "Team2", 1), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team2", 1), 9)
        Clock.schedule_once(self.changebutton, 10)
    def player23(self):
        Clock.schedule_once(partial(self.labeltored, "Team2", 2), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team2", 2), 9)
        Clock.schedule_once(self.changebutton, 10)
    def player24(self):
        Clock.schedule_once(partial(self.labeltored, "Team2", 3), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team2", 3), 9)
        Clock.schedule_once(self.changebutton, 10)
    def player25(self):
        Clock.schedule_once(partial(self.labeltored, "Team2", 4), 0.5)
        Clock.schedule_once(partial(self.labeltoblue, "Team2", 4), 9)
        Clock.schedule_once(self.changebutton, 10)



    def labeltored(self, Team, el, *largs):
        self.ids[self.dictid[Team][el]].background_color = [1,0,0, 0.5]
    def labeltoblue(self, Team, el, *largs):
        self.ids[self.dictid[Team][el]].background_color = [0, 0.5, 0.5, 0.8]
    def changebutton(self, *args):
        self.ids["startbutton"].text = "Next Player!"

# -----------------------------LOGIN--------------------------------------

class LogInLayout(Screen):
    benutzername = ObjectProperty(None)
    passwort = ObjectProperty(None)
    check = ObjectProperty(None)

    def logIn(self):
        checkname = self.benutzername.text
        command = """SELECT Nutzername, Passwort FROM Nutzer WHERE Nutzername = '""" + checkname + """'"""
        cursor1.execute(command)
        value = cursor1.fetchall()

        try:
            checkedusername = str(value[0][0])
            checkedpassword = str(value[0][1])
            if self.benutzername.text == checkedusername and self.passwort.text == checkedpassword:
                popup = Popup(title='Login successful!',
                              content=Label(text='WELCOME!', pos_hint={"x": 0.2, "top": 0.6}),
                              pos_hint={"x": 0.2, "top": 0.8})
                popup.open()
                self.check.text = "True"
                return self.check.text



            elif self.benutzername.text == checkedusername and self.passwort.text != checkedpassword:
                popup = Popup(title='Error!',
                              content=Label(text='Whoops, drunk already? \n\nPlease re-enter username and password!',
                                            pos_hint={"x": 0.2, "top": 0.6}), pos_hint={"x": 0.2, "top": 0.8})
                popup.open()
                self.benutzername.text = ""
                self.passwort.text = ""

                self.check.text = "Sign In!"
                return self.check.text


        except:
            popup = Popup(title='Error!',
                          content=Label(text='Whoops, drunk already? \n\nPlease re-enter username and password!',
                                        pos_hint={"x": 0.2, "top": 0.6}), pos_hint={"x": 0.2, "top": 0.8})
            popup.open()
            self.benutzername.text = ""
            self.passwort.text = ""

            self.check.text = "Sign In!"
            return self.check.text

        return self.check.text


# ------------------------------NewAccount--------------------------

class NewAccountLayout(Screen):
    neuerbenutzername = ObjectProperty(None)
    neuerbenutzerkey = ObjectProperty(None)
    checkednew = ObjectProperty(None)

    def createnewaccount(self):
        newusername = self.neuerbenutzername.text
        newuserpassword = self.neuerbenutzerkey.text

        if newusername=="":
            popup = Popup(title='Try again!',
                          content=Label(
                              text='Hey there! Could you please enter a username AND password?\n\n(The input fields should not be blank :D)!',
                              pos_hint={"x": 0.2, "top": 0.6}), pos_hint={"x": 0.2, "top": 0.8})
            popup.open()
            self.checkednew.text = "Create new account!"
            return self.checkednew.text

        else:
            command = """INSERT INTO `Nutzer` (`id`, `Nutzername`, `Passwort`) VALUES (NULL, '""" + newusername + """','""" + newuserpassword + """')"""
            cursor1.execute(command)
            connection.commit()
            popup = Popup(title='The creation of your new account was successful!',
                          content=Label(text='Welcome to the bingedrinking community!\n\n                         CHEERS!',
                                        pos_hint={"x": 0.2, "top": 0.6}), pos_hint={"x": 0.2, "top": 0.8})
            popup.open()
            self.checkednew.text ="True"
            return self.checkednew.text

        return self.checkednew.text

kv = Builder.load_file("flunkyball.kv")


class MeineApp(App):
    Window.clearcolor = (0,0,0,1)
    def build(self):
        return kv


if __name__ == "__main__":
    MeineApp().run()

connection.close()
