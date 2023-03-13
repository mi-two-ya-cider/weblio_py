import webbrowser
import tkinter as tk
from tkinter import ttk
from time import sleep
import threading
import json
import win32gui
import subprocess
import history_view

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

history_wordlist_show = list(reversed(history_wordlist))
history_timelist_show = list(reversed(history_timelist))

def hv_run():
    subprocess.Popen('history_view.exe')

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
            if (activeWindow != (window_title or 'history -quick weblio search') and (awf_count > 10)):
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
root.geometry(str('200x60+0+')+str(screen_height-140))
root.iconphoto(False, tk.PhotoImage(file="weblio_icon.jpg"))


text = ttk.Label(text='調べたい語句を入力')
text.place(x=4, y=0)
wordbox = ttk.Entry()
wordbox.place(width=140, x=4, y=16)
wordbox.focus_set()

def openweblio(throw_away=None):
    word = wordbox.get()
    if word == '':
        print('blank value')
        tk.messagebox.showwarning('search value error', "Cannot search for blank values")
    else:
        webbrowser.open('https://ejje.weblio.jp/content/'+str(word))
#    sleep(3)
    stop = True
    root.destroy()

runbutton = ttk.Button(text='open', command=openweblio)
runbutton.place(x=145, y=15, width=40)
history_label = ttk.Label(text="履歴を開く")
history_label.place(x=4, y=40)
history_button = ttk.Button(text="view history", command=hv_run)
history_button.place(x=60, y=38)

root.attributes("-topmost", True)
wordbox.bind('<Key-Return>', openweblio)
root.mainloop()

stop = True
