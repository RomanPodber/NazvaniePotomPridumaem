import os
import requests
import json

ok = False
with open("save.json", "r") as save:
    data = json.load(save)
if data["login"] == " ":
    while 1:
        mail = input("Ваша почта: ")
        requests.post("http://nonamegame.herokuapp.com/log", data={"mail": mail})
        res = requests.get("http://nonamegame.herokuapp.com/log")
        if res == "ok":
            os.startfile("волшебник маг властелин 2 игра.py")
            with open("save.json", "w") as dat:
                dat.write(json.dumps({"current_level": data["current_level"],
                                      "login": mail}, ensure_ascii=False))
            exit()
        else:
            print('Пользователь не найден')
else:
    os.startfile("волшебник маг властелин 2 игра.py")
    exit()