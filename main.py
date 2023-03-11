import webbrowser
import tkinter as tk
from tkinter import ttk
from time import sleep
import threading
import json
import win32gui

root = tk.Tk()
stop = False
window_title = "quick weblio search"

###############################
#ぼやけるの防止
#ソース:https://www.zacoding.com/post/wxpython-high-dpi/
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
###############################


history_json = open('history.json')
history_list = json.load(history_json)
print(history_list)
print(history_list[0])
print(history_list[0][0])
history_wordlist = history_list[0]
history_timelist = history_list[1]
print(history_wordlist)
print(history_timelist)
history_json.close()

def activewindowfunc():
    try:
        awf_count = 0
        while True:
            awf_count += 1
            global stop
            if stop:
                raise ValueError('stop vatiable was true')
            activeWindow = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            print(activeWindow)
            if activeWindow != window_title and awf_count > 10:
                root.quit()
                stop = True
            sleep(0.1)
    finally:
        print('the activeWindowfunc thread was killed because of stop variable that was True')


actvwin_thread = threading.Thread(target=activewindowfunc)
actvwin_thread.start()

#root.iconphoto(False, tk.PhotoImage(file="weblio_icon.png"))
root.title(window_title)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height)
#print(str('200x100+')+str(screen_height)+str('+0'))
root.geometry(str('200x51+0+')+str(screen_height-140))
root.iconphoto(False, tk.PhotoImage(file="weblio_icon.png"))


text = ttk.Label(text='調べたい語句を入力')
text.pack()
wordbox = ttk.Entry()
wordbox.pack()
wordbox.focus_set()

def openweblio(throw_away):
    word = wordbox.get()
    webbrowser.open('https://ejje.weblio.jp/content/'+str(word))
#    sleep(3)
    stop = True
    root.destroy()

root.attributes("-topmost", True)
wordbox.bind('<Key-Return>', openweblio)
root.mainloop()

stop = True
