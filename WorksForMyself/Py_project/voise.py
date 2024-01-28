from vosk import Model, KaldiRecognizer
import pyaudio
import json, os, sys, smtplib
from email.mime.text import MIMEText
import keyboard
import torch
import sounddevice as sd
import time
from random import randint
import pyglet
from pyglet.media import Player
import webbrowser as wb
import datetime
if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)
model = Model("model")
def send_email(message):
    sender = "bazaprosto82@gmail.com"
    password = "kfsmywqlumglfpnf"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "CLICK ME PLEASE!"
        server.sendmail(sender, sender, msg.as_string())

        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"
rec = KaldiRecognizer(model, 16000)
language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya'
put_accent = True
put_yo = True
device = torch.device('cpu')
model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)
programs = ['телеграмм','хром','роблокс','лампочку','зефир','торрент','ассасина','пушку','код','вайбер','дэс']
filer = ['C:/Users/Admin/AppData/Roaming/Telegram Desktop/Telegram.exe','C:/Program Files/Google/Chrome/Application/chrome.exe','C:/Program Files (x86)/Roblox/Versions/version-f51be0bac4f14d35/RobloxPlayerLauncher.exe','C:/Program Files (x86)/Steam/steam.exe','C:/Program Files/Genshin Impact/launcher.exe','C:/Users/Admin/AppData/Roaming/utorrent/uTorrent.exe','C:/Games/Assassins Creed Rogue/ACC.exe','C:/Program Files/JetBrains/PyCharm Community Edition 2022.2.2/bin/pycharm64.exe','C:/Users/Admin/AppData/Local/Programs/Microsoft VS Code/Code.exe','C:/Users/Admin/AppData/Local/Viber/Viber.exe','C:/Users/Admin/AppData/Local/Discord/Update.exe']
nazv = ['Telegram.exe','chrome.exe','RobloxPlayerLauncher.exe','steam.exe','launcher.exe','uTorrent.exe','ACC.exe','pycharm64.exe','Code.exe','Viber.exe','Update.exe']
gooogles = ['гугл','гугл класс','почту','ответы','ютюб','оценки','нарешалку','график','переводчик','проверку текста','счетчик слов','школу']
links = ['http://www.google.com/search?q=','https://classroom.google.com/u/2/?pli=1','https://mail.google.com/mail/u/1/#inbox','https://pomahach.com/search/','https://www.youtube.com/','https://nz.ua/dashboard/news','https://nareshalka.ml/index','https://www.desmos.com/calculator/s60mqvyp85?lang=ru','https://www.deepl.com/ru/translator#ru/en/','https://ukr-mova.in.ua/perevirka-tekstu','https://hyperhost.ua/tools/ru/character-counter?gclid=Cj0KCQiAnNacBhDvARIsABnDa6_RlmXCVkMMAzmza7dzreZ080XBDjUswKI_xomNdxVTWMvM6R92kL0aAtdUEALw_wcB','https://www.w3schools.com/java/java_methods.asp']
mus = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть', 'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один', 'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть', 'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два', 'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь', 'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь', 'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два', 'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть', 'шестьдесят семь', 'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один', 'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть', 'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один', 'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять', 'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять', 'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре', 'девяносто пять', 'девяносто шесть', 'девяносто семь', 'девяносто восемь', 'девяносто девять','сто']
ones = ['','один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь','девять']
decs = ['', 'десять', 'двадцать', 'тридцать', 'сорок','пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
hundreds = ['', 'сто', 'двести', 'триста', 'четыреста','пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
thousands = ['', 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи']
ones1 = ['','один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять','десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать','шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
dess= ['десять','одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать','шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
def schetchek(fgh):
    for a in range(len(thousands)):
        for b in range(len(hundreds)):
            for c in range(len(decs)):
                for d in range(len(ones)):
                    if a != 0:
                        nur.append(thousands[a])
                    if b != 0:
                        nur.append(hundreds[b])
                    if c != 0:
                        nur.append(decs[c])
                    if d != 0:
                        nur.append(ones[d])
                    if ' '.join(fgh) == ' '.join(nur):
                        print(a*1000+b*100+c*10+d)
                        glob.append(str(a*1000+b*100+c*10+d))
                    nur.clear()
musu = ['одного', 'двух', 'трёх', 'четырёх', 'пяти', 'шести', 'семи', 'восьми', 'девяти', 'десяти', 'одиннадцати', 'двенадцати', 'тринадцати', 'четырнадцати', 'пятнадцати', 'шестнадцати', 'семнадцати', 'восемнадцати', 'девятнадцати', 'двадцати', 'двадцати одного', 'двадцати двух', 'двадцати трёх', 'двадцати четырёх', 'двадцати пяти', 'двадцати шести', 'двадцати семи', 'двадцати восьми', 'двадцати девяти', 'тридцати', 'тридцати одного', 'тридцати двух', 'тридцати трёх', 'тридцати четырёх', 'тридцати пяти', 'тридцати шести', 'тридцати семи', 'тридцати восьми', 'тридцати девяти', 'сорока', 'сорока одного', 'сорока двух', 'сорока трёх', 'сорока четырёх', 'сорока пяти', 'сорока шести', 'сорока семи', 'сорока восьми', 'сорока девяти', 'пятидесяти', 'пятидесяти одного', 'пятидесяти двух', 'пятидесяти трёх', 'пятидесяти четырёх', 'пятидесяти пяти', 'пятидесяти шести', 'пятидесяти семи', 'пятидесяти восьми', 'пятидесяти девяти', 'шестидесяти', 'шестидесяти одного', 'шестидесяти двух', 'шестидесяти трёх', 'шестидесяти четырёх', 'шестидесяти пяти', 'шестидесяти шести', 'шестидесяти семи', 'шестидесяти восьми', 'шестидесяти девяти', 'семидесяти', 'семидесяти одного', 'семидесяти двух', 'семидесяти трёх', 'семидесяти четырёх', 'семидесяти пяти', 'семидесяти шести', 'семидесяти семи', 'семидесяти восьми', 'семидесяти девяти', 'восьмидесяти', 'восьмидесяти одного', 'восьмидесяти двух', 'восьмидесяти трёх', 'восьмидесяти четырёх', 'восьмидесяти пяти', 'восьмидесяти шести', 'восьмидесяти семи', 'восьмидесяти восьми', 'восьмидесяти девяти', 'девяноста', 'девяноста одного', 'девяноста двух', 'девяноста трёх', 'девяноста четырёх', 'девяноста пяти', 'девяноста шести', 'девяноста семи', 'девяноста восьми', 'девяноста девяти','ста']
morning = ['доброе утро','как спалось','давно не виделись','привет','привет','здравствуй']
good = ['рада стараться','спасибо за похвалу','хвалите меня чаще','обращайтесь']
how = ['Спасибо, что спросили. Не жалуюсь, а у вас?','все прекрастно','чудесно, сегодня такая прекрастная погода','отлично, готова к работе']
num = ['два','четыре','шесть','восемь','десять','двенадцать','четырнадцать','шестнадцать','восемнадцать','двадцать','двадцать два','двадцать четыре','двадцать шесть','двадцать восемь','тридцать','тридцать два','тридцать четыре','тридцать шесть','тридцать восемь','сорок','сорок два','сорок четыре','сорок шесть','сорок восемь','пятьдесят','пятьдесят два','пятьдесят четыре','пятьдесят шесть','пятьдесят восемь','шестьдесят','шестьдесят два','шестьдесят четыре','шестьдесят шесть','шестьдесят восемь','семьдесят','семьдесят два','семьдесят четыре','семьдесят шесть','семьдесят восемь','восемьдесят','восемьдесят два','восемьдесят четыре','восемьдесят шесть','восемьдесят восемь','девяносто','девяносто два','девяносто четыре','девяносто шесть','девяносто восемь','сто']
times = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть', 'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один', 'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть', 'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два', 'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь', 'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь', 'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два', 'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть', 'шестьдесят семь', 'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один', 'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть', 'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один', 'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять', 'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять', 'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре', 'девяносто пять', 'девяносто шесть', 'девяносто семь', 'девяносто восемь', 'девяносто девять']
nur = []
# keyboard = Controller()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,input=True, frames_per_buffer=8000)
stream.start_stream()
song = pyglet.media.load('Manu_Chao_Me_gustas_tu_Speed_up_remix.mp3')
# music = pyglet.media.load(r'C:\Users\Admin\PycharmProjects\pythonProject2\Manu_Chao_Me_gustas_tu_Speed_up_remix.mp3')
# f = MP3('Manu_Chao_Me_gustas_tu_Speed_up_remix.mp3')
# a = f.info.length
# def stopsound():
#     pyglet.app.exit()
# def star():
#     music.play()
#     pyglet.app.run()
def speker(text):
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    print(text)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate)
while True:
    data = stream.read(8000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        x = json.loads(rec.Result())
        print(x['text'])
        for i in range(len(gooogles)):
            if x['text'] == f'открой {gooogles[i]}':
                wb.open(f'{links[i]}')
                speker(f'{gooogles[i]} открыт')
        for i in range(len(programs)):
            if x['text'] == f'открой {programs[i]}':
                os.startfile(f'{filer[i]}')
                speker(f'{programs[i]} открыт')
            if x['text'] == f'закрой {programs[i]}':
                os.system(f"taskkill /IM {nazv[i]} /F")
                speker(f'{programs[i]} закрыт')
        for i in range(len(morning)):
            if x['text'] == morning[i]:
                a = randint(0,len(morning)-1)
                speker(morning[a])
        text = x['text']
        text = text.split()
        if x['text'] == 'сколько время' or x['text'] == "время" or x['text'] == 'сколько времени':
            now = datetime.datetime.now()
            print(f"{now.hour}:{now.minute}")
            for i in range(len(times)):
                if i + 1 == now.hour:
                    tim = times[i]
                    for a in range(len(times)):
                        if a + 1 == now.minute:
                            tim2 = times[a]
                            speker(f'сейчас {tim} часов и {tim2} минуты')
        if any(text) == True:
            if text[0] == 'посчитай' or text[0] == 'сколько':
                asd = text
                sdff = asd
                sdff.pop(0)
                fibi = ''
                for i in range(len(sdff)):
                    if sdff[i] == 'плюс':
                        nu = sdff.index('плюс')
                        fibi = '+'
                    elif sdff[i] == 'минус':
                        nu = sdff.index('минус')
                        fibi = '-'
                    elif sdff[i] == 'на':
                        nu = sdff.index('на')
                        fibi = '/'
                    elif sdff[i] == 'умножить':
                        nu = sdff.index('умножить')
                        fibi = '*'
                if any(fibi) == True:
                    glob = []
                    asd1 = []
                    for i in range(nu):
                        asd1.append(sdff[i])
                    asd2 = []
                    if nu + 1 != len(sdff):
                        for i in range(nu + 1, len(sdff)):
                            asd2.append(sdff[i])
                    nur = []
                    schetchek(asd1)
                    glob.append(fibi)
                    schetchek(asd2)
                    op = eval(' '.join(glob))
                    print(int(op))
                    zuz = []
                    def zaskil(fgh):
                        for a in range(len(thousands)):
                            for b in range(len(hundreds)):
                                for c in range(len(decs)):
                                    for d in range(len(ones)):
                                        if a != 0:
                                            nur.append(thousands[a])
                                        if b != 0:
                                            nur.append(hundreds[b])
                                        if c != 0:
                                            nur.append(decs[c])
                                        if d != 0:
                                            nur.append(ones[d])
                                        if str(a * 1000 + b * 100 + c * 10 + d) == str(fgh):
                                            aga = ' '.join(nur)
                                            lert = 'десять '
                                            for i in range(len(ones)):
                                                if aga == lert + ones[i]:
                                                    aga = dess[i]
                                            zuz.append(aga)
                                        nur.clear()
                    zaskil(op)
                    if len(zuz) > 1:
                        speker(f'ответ {zuz[1]}')
                    else:
                        speker(f'ответ {" ".join(zuz)}')
        if x['text'] == 'отправить сообщение' or x['text'] == 'отправь сообщение':
            speker('что вы хотите отправить?')
        text = x['text']
        text = text.split()
        if x['text'] == 'ты нас слушаешь':
            speker('нет я вас не слушаю')
        if any(text) == True:
            if len(text) > 2:
                if text[0] == 'гугл' and text[len(text)-1] != 'отмена' or text[0] + " " + text[1] == 'что такое':
                    def main():
                        bext = []
                        if text[0] == 'гугл':
                            for i in range(1,len(text)):
                                bext.append(text[i])
                        else:
                            for i in range(2,len(text)):
                                bext.append(text[i])
                        bext = ' '.join(bext)
                        message = bext
                        wb.open('http://www.google.com/search?q=' + message)
                    main()
                    speker(f'Вот что мне удалось найти:')
            elif text[0] == 'гугл' and text[len(text)-1] == 'отмена':
                speker(f'Запрос отменен')
            elif text[0] == 'ютюб' and text[len(text)-1] != 'отмена':
                def main():
                    bext = []
                    for i in range(1,len(text)):
                        bext.append(text[i])
                    bext = ' '.join(bext)
                    message = bext
                    wb.open('https://www.youtube.com/results?search_query=' + message)
                main()
                speker(f'Вот что мне удалось найти:')
            elif text[0] == 'ютюб' and text[len(text)-1] == 'отмена':
                speker(f'Запрос отменен')
            elif text[0] == 'ответы' and text[len(text)-1] != 'отмена':
                def main():
                    bext = []
                    for i in range(1,len(text)):
                        bext.append(text[i])
                    bext = ' '.join(bext)
                    message = bext
                    wb.open('https://pomahach.com/search/#gsc.tab=0&gsc.q=' + message)
                main()
                speker(f'Вот что мне удалось найти:')
            elif text[0] == 'ответы' and text[len(text)-1] == 'отмена':
                speker(f'Запрос отменен')
            elif text[0] == 'перевод' and text[len(text)-1] != 'отмена':
                def main():
                    bext = []
                    for i in range(1,len(text)):
                        bext.append(text[i])
                    bext = ' '.join(bext)
                    message = bext
                    wb.open('https://www.deepl.com/ru/translator#ru/en/' + message)
                main()
                speker(f'Вот что мне удалось найти:')
            elif text[0] == 'перевод' and text[len(text)-1] == 'отмена':
                speker(f'Запрос отменен')
            elif text[0] == 'аниме' and text[len(text)-1] != 'отмена':
                def main():
                    bext = []
                    for i in range(1,len(text)):
                        bext.append(text[i])
                    bext = ' '.join(bext)
                    message = bext
                    wb.open('https://jut.su/search/?searchid=1893616&text=' + message)
                main()
                speker(f'Вот что мне удалось найти:')
            elif text[0] == 'аниме' and text[len(text)-1] == 'отмена':
                speker(f'Запрос отменен')
        if any(text) == True:
            if text[0] == 'я' and text[1] == 'хочу' and text[2] == 'отправить':
                def main():
                    bext = []
                    for i in range(3,len(text)):
                        bext.append(text[i])
                    bext = ' '.join(bext)
                    message = bext
                    print(send_email(message=message))
                main()
                speker(f'сообщение было отправлено')
        if x['text'] == 'спасибо' or x['text'] == 'молодец' or x['text'] == 'умничка' or x['text'] == 'так держать' or x['text'] == 'что бы я без тебя делала':
            a = randint(0, len(good)-1)
            if x['text'] == 'спасибо':
                speker('всегда пожалуйста')
            else:
                speker(good[a])
        if x['text'] == 'как дела':
            a = randint(0, len(good) - 1)
            speker(how[a])
        if x['text'] == 'слава украине':
            speker('героям слава')
        if x['text'] == 'как тебя зовут':
            speker('Меня зовут Стэлла')
        if x['text'] == 'стелла':
            speker('Да, с чем помочь?')
        if x['text'] == f'назови число' or x['text'] == f'назови рандомное число' or x['text'] == f'скажи рандомное число':
            speker('от какого числа? могу назвать от одного до ста')
        for i in range(len(musu)):
            if x['text'] == f'от {musu[i]}':
                musu1 = i + 1
                speker('до какого?')
        for i in range(len(musu)):
            if x['text'] == f'до {musu[i]}':
                musu2 = i + 1
                ran = randint(musu1, musu2)
                speker(f'Пусть будет {mus[ran-1]}')
        for a in range(len(musu)):
            for b in range(len(musu)):
                if x['text'] == f'от {musu[a]} до {musu[b]}':
                    rand = randint(a+1,b+1)
                    speker(f'Пусть будет {mus[rand-1]}')
        if x['text'] == 'супер' or x['text'] == 'у меня все отлично' or x['text'] == 'отлично' or x['text'] == 'хорошо':
            speker('Как хорошо, что у вас хорошее настроение) Чем сегодня займемся?')
        if x['text'] == 'не знаю чем хочешь заняться' or x['text'] == 'не знаю чем хочешь':
            speker('Давайте меня улучшим')
        if x['text'] == 'давай':
            speker('ура')
        if x['text'] == 'звук максимум' or x['text'] == 'поставь звук на максимум':
            for i in range(50):
                keyboard.send("volume up")
            speker('Звук увеличен до максимума')
        if x['text'] == 'звук минимум' or x['text'] == 'поставь звук на минимум' or x['text'] == 'звук в пол' or x['text'] == 'звук пол':
            for i in range(50):
                keyboard.send("volume down")
            speker('Звук уменьшен до минимума')
        for i in range(len(num)):
            if x['text'] == f'звук {num[i]} процентов' or x['text'] == f'звук {num[i]} процента' or x['text'] == f'звук {num[i]} процентов' or x['text'] == f'звук на {num[i]} процента'or x['text'] == f'звук на {num[i]} процентов' or x['text'] == f'поставь звук на {num[i]} процента' or x['text'] == f'поставь звук на {num[i]} процентов':
                for a in range(50):
                    keyboard.send("volume down")
                for b in range(int((i*2+2)/2)):
                    keyboard.send("volume up")
                speker(f'звук поставлен на {num[i]} процентов')
        if x['text'] == 'выключи звук' or x['text'] == 'включи звук' or x['text'] == 'убери звук' or x['text'] == 'верни звук':
            keyboard.send("volume mute")
            if x['text'] == 'выключи звук' or x['text'] == 'убери звук':
                speker('звук был выключен')
            elif x['text'] == 'включи звук' or x['text'] == 'верни звук':
                speker('звук был включен')
        if x['text'] == 'включить музыку' or x['text'] == 'включи музыку':
            speker('включаю музыку')
            song.play()
        if x['text'] == 'выключить компьютер' or x['text'] == 'выключи компьютер':
            speker('выключаю')
            os.system('shutdown -s')
        if x['text'] == 'выключить музыку' or x['text'] == 'выключи программу' or x['text'] == 'выключи музыку' or x['text'] == 'выключить программу' or x['text'] == 'пока' or x['text'] == 'до скорой встречи':
            # pyglet.app.exit()
            if x['text'] == 'выключить программу' or x['text'] == 'выключи программу' or x['text'] == 'пока' or x['text'] == 'до скорой встречи':
                speker('возвращайтесь')
                sys.exit()
            elif x['text'] == 'выключить музыку' or x['text'] == 'выключи музыку':
                speker('музыка была выключена')
                Player().pause()
                sys.exit()
    else:
        pass