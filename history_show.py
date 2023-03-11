#参考文献
#https://stackoverflow.com/questions/1602106/in-pythons-tkinter-how-can-i-make-a-label-such-that-you-can-select-the-text-wi

import tkinter as tk
from tkinter import ttk
import json

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

history_wordtext = str(history_wordlist)
history_wordtext = history_wordtext.replace(', ', u"\n")
history_wordtext = history_wordtext.replace('[', '')
history_wordtext = history_wordtext.replace(']', '')
history_wordtext = history_wordtext.replace("'", "")
#history_wordtext = 'words\n-----------------------------------\n'+str(history_wordtext)
print(history_wordtext)


#history_timetext = str(history_timelist)

def history_time_func(ht_list):
    all_timetext = ''
    for i in range(len(ht_list)):
        ht = history_timelist[i]
        ot = '' #「onetime_timetext」の略　このfor文一回のみ使い、次のループになると初期化される変数
        year = str(ht[0])+'年'
        ot += year
        month = str(ht[1])+'月'
        ot += month
        day = str(ht[2])+'日'
        ot += day
        ot += '　'
        time = str(ht[3])+'時'
        ot += time
        minute = str(ht[4])+'分'
        ot += minute
        second = str(ht[5])+'秒'
        ot += second
        print(ot)
        all_timetext += ot
        all_timetext += '\n'
    print(all_timetext)
    return all_timetext

#history_timetext = 'time\n-----------------------------------\n'+history_time_func(history_timelist)
history_timetext = history_time_func(history_timelist)

"""
history_timetext = history_timetext.replace('\n', '')
history_timetext = history_timetext.replace('[[', '[')
history_timetext = history_timetext.replace('[20', u"\n20")
#history_timetext = history_timetext.replace('[20', '20')
history_timetext = history_timetext.replace(']', '')
history_timetext = history_timetext.replace(", \n", "\n")
history_timetext = 'times\n-----------------------------------'+str(history_timetext)
#history_timetext = history_timetext.replace('times:\n', 'times:')
"""

#https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQ7vdaT9kFCj2IdhHfGaykAvgBITKtXBYDaB-perce_p_JmIloo1w0a9zEK3A&usqp=CAI
#https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSDMptVK4hOXvuDwLb2BWuBywi_e8lmAY-r_H9a8mjDeHbmrrqNTOE6Do9Ipw&usqp=CAI

root = tk.Tk()
root.title('history -quick weblio search')
root.geometry('600x'+str(len(history_wordlist)*30+30))
root.iconphoto(False, tk.PhotoImage(file="weblio_icon.png"))
#history_text_ins = tk.StringVar()
#history_time_sv = tk.StringVar()
#history_text_sv.set(str(history_wordtext))
#history_time_sv.set(str(history_timetext))


#メモ
#下の二つのヘッダーを左揃えにしてスタイルを整える
history_word_header = tk.Label(font=("MS Gothic", "15", "bold"), justify="left", anchor="e", text="words\n-----------------------------------")
history_time_header = tk.Label(font=('MS Gothic', '15', 'bold'), justify="left", anchor="e", text='times\n-----------------------------------')
history_word_header.place(x=0, y=0)
history_time_header.place(x=300, y=0)

history_word_tt = tk.Text(font=("MS Gothic", "15", "bold"), relief='flat')
history_word_tt.insert('1.0', str(history_wordtext))
history_word_tt.place(x=0, y=40, height=1000)
history_word_tt.configure(state="disabled")

history_time_tt = tk.Text(font=("MS Gothic", "15", "bold"), relief='flat')
history_time_tt.insert('1.0', str(history_timetext))
history_time_tt.place(x=300, y=40)
history_time_tt.configure(state='disabled')
root.mainloop()
