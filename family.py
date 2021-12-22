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


@client.message_handler(commands=["start"])
def start(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = []


def func1(sql):
    connection = sqlite3.connect(r"C:\Users\Степанчик\Desktop\скрипты\pythonProject\img\test.db")
    cursor = connection.cursor()
    cursor.execute(sql)
    a = cursor.fetchall()
    print(a)
    connection.commit()
    return (a)
    # connection.close()


while True:
    os.system('cls')
    print('1 - для добавки')
    print('2 - для просмотра')
    print('3 - для обновлять')
    a = input('Напиши цифру: ')

    if a == '1':
        text = input('Напиши текст: ')
        text1 = input()
        txt = f"INSERT INTO table_name (`column2`, `column3`) VALUES ('{text}', '{text1}');"
        print(func1(txt))
    elif a == '2':
        txt = "SELECT * FROM table_name;"
        func1(txt)
    elif a == '3':
        clm = input()
        text = input()
        txt = f"UPDATE table_name SET '{clm}' = '{text}' WHERE id = 1"
        func1(txt)
    else:
        print('Ты слепой')

        # Надо вбивать когда и в каком обьеме давалась вода и еда и расчитать сколько это стоило
        # потом надо вбивать дату время и кол во проданных яиц
        # Потом это расчитать насколько в месяц,неделю три месяца ,год мы в плюсе иди в минусе
