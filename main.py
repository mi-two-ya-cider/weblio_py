import webbrowser
import tkinter as tk
from tkinter import ttk
from time import sleep
import threading
import json
import win32gui
import subprocess
import history_view
import os
import cython
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
stop = False
window_title = "quick weblio search"

###################################################################
#ぼやけるの防止
#ソース:https://www.zacoding.com/post/wxpython-high-dpi/
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
###################################################################

with open('history.json') as history_json:
    history_list = json.load(history_json)
    print(history_list)
    print(history_list[0])
    print(history_list[0][0])
    history_wordlist = history_list[0]
    history_timelist = history_list[1]
    print(history_wordlist)
    print(history_timelist)

def updtfile(word, time):
#    try:
        with open('history.json') as hist_mat:
            print("word:"+str(word))
            print('time:'+str(time))
            hist_list = json.load(hist_mat)
            hist_word = []
            hist_time = []
            hist_word = hist_list[0]
            hist_time = hist_list[1]
            hist_word.append(word)
            hist_time.append(time)
            print(hist_mat)
            print(hist_word)
#            try:
            #os.remove("history.json")
#            except:
#                messagebox.showwarning('file error', "history.json file was not found\nIf you want to fix it, you can search the file by yourself or creat new history.json file")
#                raise ValueError('history.json was not found')
#        with open('history.json', 'w') as file:
            all_list = []
            all_list.append(hist_word)
            all_list.append(hist_time)
            print(all_list)
            #print(list(str(list(all_list)[1:][:-1])))
            json.dump(all_list, open('history.json', 'w'))
#    except:
#        print('error')


def gettime():
    dt = datetime.now()
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    dt_list = [year, month, day, day, hour, minute, second]
    print(dt_list)
    return dt_list

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
    updtfile(word, list(gettime()))
    if word == '':
        print('blank value')
        messagebox.showwarning('search value error', "Cannot search for blank values")
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
