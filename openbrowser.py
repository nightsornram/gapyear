import pyautogui
import time
import webbrowser
import pyperclip as cp
#edge = (899,1069)
#pyautogui.click(edge)
url = 'https://www.google.com/'
webbrowser.open(url)
time.sleep(3)
pyautogui.write('thailand')
pyautogui.press('Enter')

def Search(word):
	th = cp.copy(word)
	time.sleep(3)
	for i in range(7):
		pyautogui.press('Tab')
	pyautogui.press('backspace')
	pyautogui.write(th)
	pyautogui.press('Enter')
	time.sleep(3)

def SearchTH(word):
	cp.copy(word)
	time.sleep(3)
	for i in range(7):
		pyautogui.press('Tab')
	pyautogui.press('backspace')
	pyautogui.hotkey('ctrl','v')
	pyautogui.press('Enter')
	time.sleep(3)

#Search('Japan')
#Search('Singapore')
#Search('USA')
#Search('China')
SearchTH('ไทย')
