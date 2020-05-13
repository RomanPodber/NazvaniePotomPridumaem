import sqlite3
import os
import requests


ok = False
while 1:
    login = input("Логин: ")
    conn = sqlite3.connect("userstable.sqlite")
    cur = conn.cursor()
    box = []
    res = cur.execute(f"""SELECT email from users WHERE email = '{login}'""").fetchall()
    if bool(res):
        password = input('Пароль: ')
        res = cur.execute(f"""SELECT hashed_password from users where email = '{login}'""")
        if res[0] == password:
            print('ok')
            ok = True
        else:
            print('неверный пароль')
    else:
        print('Пользователь не найден')
    if ok is True:
        os.startfile("npp.py")
        exit()