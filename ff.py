import telebot
from telebot import types
import requests
import pyautogui as pag
import os
import sqlite3

pag.FAILSAFE = False
TOKEN = "1667255041:AAFuTpS2M594DhDCiYlDpA3B8E0GA3AJYwU"
CHAT_ID = "3779764"
client = telebot.TeleBot(TOKEN)
requests.post("https://api.telegram.org/bot{1667255041:AAFuTpS2M594DhDCiYlDpA3B8E0GA3AJYwU}/sendMessage?chat_id={"
              "3779764}&text=Online")


def su(h):
    if h == '5':
        s = open("надо.txt", "r+", encoding="UTF - 8")
        s = [elem.split() for elem in s]
        name, much, col_vo, date = [], [], [], []
        for elem in s:
            if h == '5':
                name.append(elem[0])
                much.append(elem[1])
                col_vo.append(elem[2])
                date.append(elem[3])

                h = '0'

            return name, much, col_vo, date


@client.message_handler(commands=["start"])
def start(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["/eat", "/water", "/eggs"]

    for btn in btns:
        rmk.add(types.KeyboardButton(btn))
        client.send_message(message.chat.id, "бот", reply_markup=rmk)


while True:
    os.system('cls')
    print('1 - для добавки')
    print('2 - для просмотра')
    print('3 - для обновлять')
    a = input('Напиши цифру: ')

    if a == '1':
        txt = input()
        s = open("надо.txt", "a", encoding="UTF - 8")
        s.write(txt)
        s.close()
    elif a == '2':
        s = open("надо.txt", encoding="UTF - 8")
        for i in s:
            print(i.split())
            q = i.split()
        # print(s.read)
        s.close()

    elif a == '3':
        txt = input()
        # перезаписывает файл и пишет Привет
        s = open("надо.txt", 'w', encoding="UTF - 8")
        s.write(txt)
        s.close()
    elif a == '4':
        a = "5"
        su(a)

# s = open("фигня какая-то.py", 'a')
# s.write('Привет')
# s.close()

# комбо дозаписи и считывания
# s = open("фигня какая-то.py", 'a')
# s.write('Привет')
# s.close()
# s = open("фигня какая-то.py")
# print(s.read())
# s.close()
