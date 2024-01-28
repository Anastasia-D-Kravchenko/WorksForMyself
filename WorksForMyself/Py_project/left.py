# import pyglet
# from mutagen.mp3 import MP3
# from threading import Timer
# def stopsound():
#     pyglet., end='', \'''a
# def star():
#     music.play()
#     pyglet.app.run()
# music = pyglet.media.load(r'C:\Users\Admin\PycharmProjects\pythonProject2\maneskin-coraline-mp3uk-net.mp3')
# f = MP3('maneskin-coraline-mp3uk-net.mp3')
# a = f.info.length
# print(a)
# Timer(0.1, star).start()
# Timer(a-299, stopsound).start()


# from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
# file_name = os.path.join(self.dir, item.text())
# content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_name))
# self.mediaPlayer = QtMultimedia.QMediaPlayer()
# self.mediaPlayer.setMedia(content)
# self.mediaPlayer.play()


# import keyboard #pip install keyboard
# print(keyboard.read_hotkey())
# keyboard.add_hotkey("+", lambda:keyboard.send("volume up"))
# keyboard.add_hotkey("-", lambda:keyboard.send("volume down"))
# keyboard.add_hotkey("r", lambda:keyboard.send("volume mute"))
# for i in range(10):
#     keyboard.send("volume up")
# input()


# import keyboard #pip install keyboard
# print(keyboard.read_hotkey())#; input()
# array = {
# "=":"volume up",
# "-":"volume down",
# "r":"volume mute"
# }
# def fun(str): keyboard.send(str)
# for key in array: keyboard.add_hotkey(key, fun, args=[array[key]])
# input()


# import torch
# import sounddevice as sd
# import time
# from omegaconf import OmegaConf
# language = 'ru'
# model_id = 'ru_v3'
# sample_rate = 48000
# speaker = 'baya'
# put_accent = True
# put_yo = True
# device = torch.device('cpu')
# text = "Привет, мир!"
# model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
#                           model='silero_tts',
#                           language=language,
#                           speaker=model_id)
# model.to(device)
# audio = model.apply_tts(text=text,
#                         speaker=speaker,
#                         sample_rate=sample_rate,
#                         put_accent=put_accent,
#                         put_yo=put_yo)
# print(text)
# sd.play(audio, sample_rate)
# time.sleep(len(audio)/sample_rate)
# sd.stop()

# from kivy.app import App
# import pyglet
# from pyglet.media import Player, load
# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.core.window import Window
# import datetime
# import sys
#
# Window.size = (350, 580)
#
# # описание приложения
# KV = """
# Conteiner:
#     orientation: "vertical"
#     size_hint: (0.95, 0.95)
# 	pos_hint: {"center_x": 0.5, "center_y":0.5}
# 	spacing: 10
#
# 	GridLayout:
#         cols: 3
#         BoxLayout:
# 	        padding: [0, 5,0,5]
#
# 	        TextInput:
# 	            id: input_hour
# 		        font_size: "72sp"
# 		        size_hint: 0.8, 0.5
#
# 		    Label:
# 		        size_hint: 0.9, 0.5
# 		        font_size: "72sp"
# 	            text: ":"
#
# 		    TextInput:
# 		        id: input_min
# 		        font_size: "72sp"
# 		        size_hint: 0.8, 0.5
#
# 	TextInput:
# 	    id: music_link
# 		font_size: "30sp"
# 		size_hint: 1, 0.5
#
#     BoxLayout:
# 	    padding: [0,1,0,0]
#
# 	    Button:
# 		    text: "Завести будильник"
# 		    bold: True
# 		    background_color:'#00FFCE'
# 		    size_hint: (1,0.5)
# 		    on_press: root.on_start()
#
# 	Button:
# 		text: "Отменить"
# 		bold: True
# 		background_color:'#00FFCE'
# 		size_hint: (1,0.5)
# 		on_press: root.on_stop()
#
# """
# # I:\Downloads\мелодия.mp3
# # self.ids.music_link.text
#
# player = Player()
# player.loop = True  # то что зацикливает музыку
# source = load('Manu_Chao_Me_gustas_tu_Speed_up_remix.mp3')
# player.queue(source)
#
# class Conteiner(BoxLayout):
#     # процедура обработки нажатия кнопки
#     def on_stop(self):
#         player.pause()
#     def on_start(self):
#         print('Нажалась')
#         if int(self.ids.input_hour.text) > 24 or int(self.ids.input_min.text) > 59:
#             if int(self.ids.input_hour.text) > 24:
#                 self.ids.input_hour.text = ''
#             else:
#                 self.ids.input_hour.text = ''
#         else:
#             while True:
#                 time_now = datetime.datetime.now()
#                 if self.ids.input_hour.text == str(time_now.hour) and self.ids.input_min.text == str(time_now.minute):
#                     print('Ura')
#                     player.play()
#                     print(time_now)
#                     break
#
#     # то чно не хочет работать
#
#
# # запуск всей хуйни написанной выше
# class MyApp(App):
#     def build(self):
#         return Builder.load_string(KV)
#
# MyApp().run()


# import pyglet
# from pyglet.media import Player, load
# song = pyglet.media.load('Manu_Chao_Me_gustas_tu_Speed_up_remix.mp3',streaming=True)
# song.play()
# a = input()
# Player().pause()
# if a == 's':
#     Player().pause()
# for i in range(100):
#     print(i)

# import pygame
# pygame.init()
# song = pygame.mixer.Sound('Manu_Chao_Me_gustas_tu_Speed_up_remix.mp3')
# clock = pygame.time.Clock()
# song.play()
# a = True
# if a == True:
#     clock.tick(60)
#     b = input()
#     if b == 's':
#         a = False
# pygame.quit()


# from audioplayer import AudioPlayer
# a = AudioPlayer("Jengi_Bel_Mercy.mp3")
# a.play(block=True)
# for i in range(10):
#     print(i)
# musu = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть', 'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один', 'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть', 'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два', 'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь', 'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь', 'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два', 'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть', 'шестьдесят семь', 'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один', 'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть', 'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один', 'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять', 'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять', 'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре', 'девяносто пять', 'девяносто шесть', 'девяносто семь', 'девяносто восемь', 'девяносто девять']
# for i in range(100):
#     print(musu[i], end=' ')
# import smtplib
# import os
# from email.mime.text import MIMEText
#
#
# def send_email(message):
#     sender = "bazaprosto82@gmail.com"
#     # your password = "your password"
#     password = "kfsmywqlumglfpnf"
#
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()
#
#     try:
#         server.login(sender, password)
#         msg = MIMEText(message)
#         msg["Subject"] = "CLICK ME PLEASE!"
#         server.sendmail(sender, sender, msg.as_string())
#
#         # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")
#
#         return "The message was sent successfully!"
#     except Exception as _ex:
#         return f"{_ex}\nCheck your login or password please!"
#
#
# def main():
#     message = input("Type your message: ")
#     print(send_email(message=message))
#
#
# if __name__ == "__main__":
#     main()

# a = 'я хочу отправить'
# aa = a
# a = a.split()
# b = []
# for i in range(3):
#     b.append(a[i])
# b = ' '.join(b)
# print(len(aa))

# text = 'я хочу отправить привет друг'
# text = text.split()
# bext = []
# if text[0] == 'я' and text[1] == 'хочу' and text[2] == 'отправить':
#     for i in range(3):
#         bext.append(text[i])
#     cext = []
#     for i in range(3,len(text)):
#         cext.append(text[i])
# print(' '.join(bext))
# print(' '.join(cext))
#
# import subprocess
# import time
# import psutil
#
# subprocess.call('C:/Users/Admin/AppData/Roaming/Telegram Desktop/Telegram.exe')
# time.sleep(5)
# for process in (process for process in psutil.process_iter() if process.name()=="Telegram.exe"):
#     process.kill()
#
# # or x['text'] == f'назови рандомное число'
# # programs = ['телеграмм','хром','роблокс','кс','стим','доту','танки','геншин','торент','ассасин','пайчарм','код','вайбер','дс']
# filer = ['C:/Users/Admin/AppData/Roaming/Telegram Desktop/Telegram.exe','C:\Program Files\Google\Chrome\Application\chrome.exe','C:\Program Files (x86)\Roblox\Versions\version-f51be0bac4f14d35\RobloxPlayerLauncher.exe','C:\Users\Admin\Desktop\Game\Counter-Strike Global Offensive','C:\Program Files (x86)\Steam\steam.exe','C:\Users\Admin\Desktop\Game\Dota 2','C:\Users\Admin\Desktop\Game\WoT Blitz','C:\Program Files\Genshin Impact\launcher.exe','C:\Users\Admin\AppData\Roaming\utorrent\uTorrent.exe','C:\Games\Assassins Creed Rogue\ACC.exe','C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.2\bin\pycharm64.exe','C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe','C:\Users\Admin\AppData\Local\Viber\Viber.exe','C:\Users\Admin\AppData\Local\Discord\Update.exe']
# nazv = ['Telegram.exe','chrome.exe','RobloxPlayerLauncher.exe','Counter-Strike Global Offensive','steam.exe','Dota 2','WoT Blitz','launcher.exe','uTorrent.exe','ACC.exe','pycharm64.exe','Code.exe','Viber.exe','Update.exe']
# import lxml.html as lhtml
# import urllib
# data = urllib2.urlopen(query)
# document = lhtml.document_fromstring(data.read())
# import webbrowser as wb
# q = input()
# wb.open('http://www.google.com/search?q=' + q)
# import requests
# def send_msg(text):
#     token = "TOKEN-TELEGRAM-BOT"
#     chat_id = "CHAT-ID"
#     url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
#     results = requests.get(url_req)
#     print(results.json())
# send_msg("Hello python!")

# !/usr/bin/env python3

# import requests
#
# def send_msg(text):
#     token = "TOKEN-TELEGRAM-BOT"
#     chat_id = "CHAT-ID"
#     url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
#     results = requests.get(url_req)
#     print(results.json())
#
# send_msg("Hello python!")

# from threading import Timer
# import datetime
# import pyglet
# from pyglet.media import Player, load
# song = pyglet.media.load('Manu_Chao_Me_gustas_tu_Speed_up_remix.mp3',streaming=True)
# time_now = datetime.datetime.now()
# h = int(input())
# m = int(input())
# tot_h = h - time_now.hour
# tot_m = m - time_now.minute
# h_in_sec = tot_h * 3600
# m_in_sec = tot_m * 60
# res = h_in_sec + m_in_sec
# print(res)
# def songgg():
#     song.play()
# Timer(res, songgg).start()
# a = input()
# if a == 's':
#     Player().pause()

# musu = ['одного', 'двух', 'трёх', 'четырёх', 'пяти', 'шести', 'семи', 'восьми', 'девяти', 'десяти', 'одиннадцати', 'двенадцати', 'тринадцати', 'четырнадцати', 'пятнадцати', 'шестнадцати', 'семнадцати', 'восемнадцати', 'девятнадцати', 'двадцати', 'двадцати одного', 'двадцати двух', 'двадцати трёх', 'двадцати четырёх', 'двадцати пяти', 'двадцати шести', 'двадцати семи', 'двадцати восьми', 'двадцати девяти', 'тридцати', 'тридцати одного', 'тридцати двух', 'тридцати трёх', 'тридцати четырёх', 'тридцати пяти', 'тридцати шести', 'тридцати семи', 'тридцати восьми', 'тридцати девяти', 'сорока', 'сорока одного', 'сорока двух', 'сорока трёх', 'сорока четырёх', 'сорока пяти', 'сорока шести', 'сорока семи', 'сорока восьми', 'сорока девяти', 'пятидесяти', 'пятидесяти одного', 'пятидесяти двух', 'пятидесяти трёх', 'пятидесяти четырёх', 'пятидесяти пяти', 'пятидесяти шести', 'пятидесяти семи', 'пятидесяти восьми', 'пятидесяти девяти', 'шестидесяти', 'шестидесяти одного', 'шестидесяти двух', 'шестидесяти трёх', 'шестидесяти четырёх', 'шестидесяти пяти', 'шестидесяти шести', 'шестидесяти семи', 'шестидесяти восьми', 'шестидесяти девяти', 'семидесяти', 'семидесяти одного', 'семидесяти двух', 'семидесяти трёх', 'семидесяти четырёх', 'семидесяти пяти', 'семидесяти шести', 'семидесяти семи', 'семидесяти восьми', 'семидесяти девяти', 'восьмидесяти', 'восьмидесяти одного', 'восьмидесяти двух', 'восьмидесяти трёх', 'восьмидесяти четырёх', 'восьмидесяти пяти', 'восьмидесяти шести', 'восьмидесяти семи', 'восьмидесяти восьми', 'восьмидесяти девяти', 'девяноста', 'девяноста одного', 'девяноста двух', 'девяноста трёх', 'девяноста четырёх', 'девяноста пяти', 'девяноста шести', 'девяноста семи', 'девяноста восьми', 'девяноста девяти','ста']
# text = 'от двадцати до тридцати одного'
# text = text.split()
# if len(text) == 4:
#     aext = []
#     for a in range(len(text)):
#         for b in range(len(musu)):
#             if musu[b] == text[a]:
#                 aext.append(b+1)
#     aext.sort()
#     print(aext)
# elif len(text) == 6:
#     aext = []
#     for a in range(len(text)):
#         for b in range(len(musu)):
#             if musu[b] == text[a]:
#                 aext.append(b + 1)
#     aext1 = aext[0] + aext[1]
#     aext2 = aext[2] + aext[3]
#     aext.clear()
#     aext.append(aext1)
#     aext.append(aext2)
#     aext.sort()
#     print(aext)
# elif len(text) == 5:
#     aext = []
#     aext1 = []
#     for a in range(len(text)):
#         for b in range(len(musu)):
#             if musu[b] == text[a]:
#                 aext.append(musu[b])
#                 aext1.append(b+1)
#     zext = []
#     zext1 = []
#     for b in range(len(musu)):
#         if musu[b] == aext[0] + ' ' + aext[1]:
#             zext.append(b+1)
#             zext1.append(aext[1] + ' ' + aext[2])
#         if musu[b] == aext[1] + ' ' + aext[2]:
#             zext.append(b+1)
#             zext1.append(aext[0] + ' ' + aext[1])
#     if zext1[0] == aext[0] + ' ' + aext[1]:
#         zext.append(aext1[0])
#     if zext1[0] == aext[1] + ' ' + aext[2]:
#         zext.append(aext1[2])
#     zext.sort()
#     print(zext)


# import os
# import keyboard
#
# def pressedKey(key):
#     with open("log.txt", "a") as openFile:
#         openFile.write(key.name)
#
#
# def main():
#
#     key_list = keyboard.record()
#     for key in key_list:
#         print(key, ' ' )
#         pressedKey(key)
#
# main()

# gooogles = ['гугл','гугл класс','почту','ответы','ютюб','оценки','нарешалку','график','переводчик','проверку текста','счетчик слов','школу']
# links = ['http://www.google.com/search?q=','https://classroom.google.com/u/2/?pli=1','https://mail.google.com/mail/u/1/#inbox','https://pomahach.com/search/','https://www.youtube.com/','https://nz.ua/dashboard/news','https://nareshalka.ml/index','https://www.desmos.com/calculator/s60mqvyp85?lang=ru','https://www.deepl.com/ru/translator#ru/en/','https://ukr-mova.in.ua/perevirka-tekstu','https://hyperhost.ua/tools/ru/character-counter?gclid=Cj0KCQiAnNacBhDvARIsABnDa6_RlmXCVkMMAzmza7dzreZ080XBDjUswKI_xomNdxVTWMvM6R92kL0aAtdUEALw_wcB','https://www.w3schools.com/java/java_methods.asp']


# a = 'двести двадцать плюс ноль'
# a = a.split()
# print(a.index('плюс'))

import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__left__':
    unittest.main(verbosity=2)