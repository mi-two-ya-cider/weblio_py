import webbrowser
import tkinter as tk
from tkinter import ttk
from time import sleep
import threading
import json

###############################
#ぼやけるの防止
#ソース:https://www.zacoding.com/post/wxpython-high-dpi/
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
###############################

"""
history_json = open('history.json')
print(history_json)
history_json2 = json.load(history_json)
print(history_json2)
"""

root = tk.Tk()
root.title(u'weblio単語検索')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height)
#print(str('200x100+')+str(screen_height)+str('+0'))
root.geometry(str('200x51+0+')+str(screen_height-140))

text = ttk.Label(text='調べたい語句を入力')
text.pack()
wordbox = ttk.Entry()
wordbox.pack()
wordbox.focus_set()

def openweblio(throw_away):
    word = wordbox.get()
    webbrowser.open('https://ejje.weblio.jp/content/'+str(word))
#    sleep(3)
    root.destroy()

root.attributes("-topmost", True)
wordbox.bind('<Key-Return>', openweblio)
root.mainloop()
