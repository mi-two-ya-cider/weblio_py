import webbrowser
import tkinter as tk
from time import sleep
import threading

root = tk.Tk()
root.title(u'weblio単語検索')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height)
print(str('200x100+')+str(screen_height)+str('+0'))
root.geometry(str('200x50+0+')+str(screen_height-120))
wordbox = tk.Entry()
wordbox.pack()
wordbox.focus_set()

def openweblio(throw_away):
    word = wordbox.get()
    webbrowser.open('https://ejje.weblio.jp/content/'+str(word))
    sleep(5)
    root.destroy()
    
root.attributes("-topmost", True)
wordbox.bind('<Key-Return>', openweblio)
root.mainloop()
