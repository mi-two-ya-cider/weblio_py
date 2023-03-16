#参考文献
#https://stackoverflow.com/questions/1602106/in-pythons-tkinter-how-can-i-make-a-label-such-that-you-can-select-the-text-wi






import tkinter as tk
from tkinter import ttk
import json
import pyautogui

menu = 0
rightclick_offset = []
history_wordlist_mat = []
history_timelist_mat = []
rclick_tarword = 0
rclick_tartime = 0
y_off = 0
window_x = 0
window_y = 0


def hv_main():
    global history_wordlist_mat
    global history_timelist_mat
    history_json = open('history.json')
    history_list = json.load(history_json)
    print(history_list)
    print(history_list[0])
    print(history_list[0][0])
    history_wordlist_mat = history_list[0]
    history_timelist_mat = history_list[1]
    print(history_wordlist_mat)
    print(history_timelist_mat)
    history_json.close()

    history_wordtext = str(list(reversed(history_wordlist_mat)))
    history_wordtext = history_wordtext.replace(', ', u"\n")
    history_wordtext = history_wordtext.replace('[', '')
    history_wordtext = history_wordtext.replace(']', '')
    history_wordtext = history_wordtext.replace("'", "")
    #history_wordtext = 'words\n-----------------------------------\n'+str(history_wordtext)
    print(history_wordtext)


    #時間のリストを新しい順に並び変える
    #単語のリストは新しい順に並び変えてある

    #history_timetext = str(history_timelist)

    def history_time_func(ht_list):
        print("ht_list:"+str(ht_list))
        all_timetext = ''
        for i in range(len(ht_list)):
            ht = ht_list[i]
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
    history_timetext = history_time_func(list(reversed(history_timelist_mat)))

    history_wordlist_show = list(reversed(history_wordlist_mat))
    history_timelist_show = list(reversed(history_timelist_mat))

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

    master = tk.Tk()
    master.title('history -quick weblio search')
    master.geometry('600x'+str(len(history_wordlist_mat)*30+30))
    icon = tk.PhotoImage(file="weblio_icon.jpg")
    #master.iconphoto(False, icon)
    #history_text_ins = tk.StringVar()
    #history_time_sv = tk.StringVar()
    #history_text_sv.set(str(history_wordtext))
    #history_time_sv.set(str(history_timetext))


    #メモ
    #下の二つのヘッダーを左揃えにしてスタイルを整える
    history_word_header = tk.Label(master, font=("MS Gothic", "15", "bold"), bg="#f0f0f0", justify="left", anchor="e", text="words\n-----------------------------------")
    history_time_header = tk.Label(master, font=('MS Gothic', '15', 'bold'), bg="#f0f0f0", justify="left", anchor="e", text='times\n-----------------------------------')
    history_word_header.place(x=0, y=0)
    history_time_header.place(x=300, y=0)

    history_word_tt = tk.Text(master, font=("MS Gothic", "15", "bold"), relief='flat', bg="#f0f0f0")
    history_word_tt.insert('1.0', str(history_wordtext))
    history_word_tt.place(x=0, y=40, height=1000)
    history_word_tt.configure(state="disabled")

    history_time_tt = tk.Text(master, font=("MS Gothic", "15", "bold"), relief='flat', bg="#f0f0f0")
    history_time_tt.insert('1.0', str(history_timetext))
    history_time_tt.place(x=300, y=40, height=1000)
    history_time_tt.configure(state='disabled')

    def showmenu(event):
        global menu
        global rightclick_offset
        global rclick_tarword
        global rclick_tartime
        global y_off
        global window_x
        global window_y
        x_off_mat, y_off_mat = pyautogui.position()
        print(rightclick_offset)
        """
        if event.y >=400:
            #y_off = event.y-8
            y_off = y_off_mat - y_off_mat%20 #y_offを20の倍数にする
            y_off = y_off/20
            rclick_tarword = history_wordlist_mat[int(y_off)]
            rclick_tartime = history_timelist_mat[int(y_off)]
        """
        window_x = master.winfo_x()
        window_y = master.winfo_y()
        print(window_x)
        print(window_y)

        local_x = x_off_mat-window_x
        local_y = y_off_mat-window_x
        
        menu.post(x_off_mat, y_off_mat)


    
    def rclick_delete():
        #history_wordlist_mat[y_off]を削除
        global rclick_tarword
        global rclick_tartime
        global history_wordlist_mat
        global history_timelist_mat

        print(rclick_tarword)
        print(rclick_tartime)

        history_wordlist_deleted = history_wordlist_mat.remove(rclick_tarword)
        history_timelist_deleted = history_timelist_mat.remove(rclick_tartime)
        print(history_wordlist_deleted)
        print(history_timelist_deleted)
        with open('history.json') as hist_mat_json:
#            print("word:"+str(word))
#            print('time:'+str(time))
            hist_list = json.load(hist_mat_json)
            all_list = []
            all_list.append(history_wordlist_deleted)
            all_list.append(history_timelist_deleted)
            print(all_list)
            json.dump(all_list, open('history.json', 'w'))

    global menu
    global rightclick_offset
    menu = tk.Menu(master, tearoff=0)
    menu.add_command(label="削除", command=rclick_delete)


    master.bind('<Button-3>', showmenu)

    master.mainloop()

if __name__ == '__main__':
    hv_main()
