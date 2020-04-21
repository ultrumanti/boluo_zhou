
# heck special text labels

from tkinter import *
import tkinter.ttk
from sucaideal import XmlMaker
import os
from tkinter import filedialog
import linecache

path_check_list = []


# beigin position
beginlist = []
# end position
endlist = []
# type
typelist = []
# text vocabulary
vocalist = []

backgroundlist = ['white','CornflowerBlue','DarkViolet','Pink','Cyan','DarkGreen','Olive','Orange','OrangeRed','PapayaWhip','Indigo','LightCoral','RosyBrown']
foregroundlist = ['black','white','white','white','white','white','white','white','white','Chocolate','Aqua','PapayaWhip','BlanchedAlmond']
typeflaglist = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
flaglist = ['a','b','c','d','e','f','g','h','i','j','k','l','m']

file_path = []

va = []

# output dictionary
path_out_str = "xxxxx"
# input dictionary
read_str_path = "xxxxx"
# input dictionary
file_path_all = "xxxxx"

# Select text that contains a specific word
def getline(the_file_path):
    line_str = linecache.getline(the_file_path, 5)
    if(line_str.find("赤眼蜂")>-1):
        return True
    else:
        return False

def walkFile(file):
    files = os.listdir(file)
    files.sort()
    for file_ in files:
        f_name = str(file_)
        if (f_name[-4:].__eq__(".txt")):
            if(getline(file + f_name)):
                path_check_list.append(f_name)

def create_new(the_file_path):
    data_list = []
    for line in open(the_file_path, "r"):
        line = line.replace("\n", "")
        data_list.append(line)
    beginlist_1 = data_list[0].split("]--[")
    endlist_1 = data_list[1].split("]--[")
    typelist_1 = data_list[3].split("]--[")
    strtext_1 = data_list[4]
    flagtext(beginlist_1,endlist_1,typelist_1,strtext_1)

def remove_vo(deabeg,deen,index):
    vocabu = dejudge(deabeg,deen)
    vocabu = sorted(vocabu, reverse=True)
    if (len(vocabu) != 0):
        for i in range(0, len(vocabu)):
            Text_1.tag_add(flaglist[0], beginlist[vocabu[i]], endlist[vocabu[i]])
            Text_1.tag_config(flaglist[0], background=backgroundlist[0], foreground=foregroundlist[0])
            beginlist.pop(vocabu[i])
            endlist.pop(vocabu[i])
            typelist.pop(vocabu[i])
            vocalist.pop(vocabu[i])
    else:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        Text_1.tag_add(flaglist[index], first, last)
        Text_1.tag_config(flaglist[index], background=backgroundlist[index], foreground=foregroundlist[index])

def blodChangeA():
        try:
            debegin = Text_1.index(SEL_FIRST)
            deend = Text_1.index(SEL_LAST)
            deabeginarr = debegin.split(".")
            deendarr = deend.split(".")
            remove_vo(deabeginarr[1], deendarr[1],0)
        except TclError:
            pass

def clearlist():
    beginlist.clear()
    endlist.clear()
    typelist.clear()
    vocalist.clear()

def dejudge(debegin,deend):
    vocabu = []
    for i in range(0,len(beginlist)):
        deabeginarr = beginlist[i].split(".")
        deendarr = endlist[i].split(".")
        if((int(debegin)>int(deabeginarr[1])) and (int(debegin)<int(deendarr[1]))
        or (int(deend)>int(deabeginarr[1])) and (int(deend)<int(deendarr[1]))
        or (int(debegin)<int(deabeginarr[1])) and (int(deend)>int(deabeginarr[1]))
        or (int(debegin)<int(deendarr[1])) and (int(deend)>int(deendarr[1]))
        or (int(debegin) == int(deabeginarr[1])) and (int(deend) == int(deendarr[1]))
        ):
            vocabu.append(i)
    return vocabu

def flag_delete():
    strtext = Text_1.get('0.0', END)
    Text_1.delete(END)
    Text_1.insert(END, strtext)
    clearfourlist()

def btuchange_removeall():
    strtext = Text_1.get('0.0', END)
    Text_1.delete('0.0',END)
    Text_1.insert(END, strtext)
    clearlist()

def clearfourlist():
    beginlist.clear()
    endlist.clear()
    typelist.clear()
    vocalist.clear()
    
def btuchange_up():
    nowindex = int(v.get()) - 1
    if(nowindex>=0):
        clearlist()
        Text_1.delete('0.0', END)
        v.set(nowindex)
        readtxt(str(nowindex))

def btuchange_next():
    clearlist()
    Text_1.delete('0.0', END)
    nowindex = int(v.get()) + 1
    v.set(nowindex)
    readtxt(str(nowindex))

def writetext(begin,end,voca,type,strtext):
    path = str(v.get())
    strpath = path_out_str + path_check_list[int(path)]
    print(strpath)
    f = open(strpath, 'w')
    f.write( begin +'\n')
    f.write( end +'\n')
    f.write( voca +'\n')
    f.write( type + '\n')
    f.write( strtext )
    f.close()
    nowindex = int(v.get()) + 1
    writetext_num(str(nowindex))
    Text_label.delete('0.0', END)
    Text_label.insert(END, voca)

# Where the sequence number has been carried out
def writetext_num(num):
    strpath = "./store_info/now_num.txt"
    f = open(strpath, 'w')
    f.write(num)
    f.close()

def btuchange_endout_next():
    btuchange_endout()
    btuchange_next()

def btuchange_endout():
    strbegin = ""
    strend = ""
    strvoca = ""
    strtype = ""
    strtext = ""
    if(len(beginlist)>1):
        num_list = []
        for i in range(0,len(beginlist)):
            beginarr = beginlist[i].split(".")
            num_list.append(int(beginarr[1]))
        num_list_end = sorted(num_list)
        num_arr = []
        for j in range(0, len(num_list_end)):
            for i in range(0,len(num_list)):
                if(num_list[i] == num_list_end[j]):
                    num_arr.append(i)
                    pass
        for i in range(0,len(num_arr)-1):
            beginarr = beginlist[num_arr[i]].split(".")
            strbegin = strbegin + beginarr[1] + "]--["
            endarr = endlist[num_arr[i]].split(".")
            strend = strend + endarr[1] + "]--["
            strvoca = strvoca + vocalist[num_arr[i]] + "]--["
            strtype = strtype + typelist[num_arr[i]] + "]--["
        beginarr = beginlist[num_arr[len(num_arr)-1]].split(".")
        strbegin = strbegin + beginarr[1]
        endarr = endlist[num_arr[len(num_arr)-1]].split(".")
        strend = strend + endarr[1]
        strvoca = strvoca + vocalist[num_arr[len(num_arr)-1]]
        strtype = strtype + typelist[num_arr[len(num_arr)-1]]
        strtext = Text_1.get('0.0', END)
        writetext(strbegin, strend, strvoca, strtype, strtext)

    if(len(beginlist)==1):
        beginarr = beginlist[len(beginlist) - 1].split(".")
        strbegin = strbegin + beginarr[1]
        endarr = endlist[len(beginlist) - 1].split(".")
        strend = strend + endarr[1]
        strvoca = strvoca + vocalist[len(beginlist) - 1]
        strtype = strtype + typelist[len(beginlist) - 1]
        strtext = Text_1.get('0.0', END)
        writetext(strbegin, strend, strvoca, strtype, strtext)
    if (len(beginlist) == 0):
        writetext(strbegin, strend, strvoca, strtype, strtext)

def btuchange_jump():
    nowindex= v.get()
    if (int(nowindex) >= 0 and int(nowindex) <= path_check_list.__len__()):
        clearlist()
        readtxt(str(v.get()))

def readtxt(path):
    print("read",path)
    strpath = read_str_path + path_check_list[int(path)]
    print(strpath)
    create_new(strpath)

# Read processed sequence number
def read_store_info_now():
    strpath = "./store_info/now_num.txt"
    strtxt = ""
    for line in open(strpath, 'r'):
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        strtxt = line
    return strtxt

def flag_change(first,last,index):
    Text_1.tag_add(flaglist[index], first, last)
    str = Text_1.get(first, last)
    typelist.append(typeflaglist[index])
    beginlist.append(Text_1.index(first))
    endlist.append(Text_1.index(last))
    vocalist.append(str)
    Text_1.tag_config(flaglist[index], background=backgroundlist[index], foreground=foregroundlist[index])

def remove_vo_change(deabeg,deen):
    vocabu = dejudge(deabeg,deen)
    vocabu = sorted(vocabu, reverse=True)
    if (len(vocabu) != 0):
        for i in range(0, len(vocabu)):
            Text_1.tag_add(flaglist[0], beginlist[vocabu[i]], endlist[vocabu[i]])
            Text_1.tag_config(flaglist[0], background=backgroundlist[0], foreground=foregroundlist[0])
            beginlist.pop(vocabu[i])
            endlist.pop(vocabu[i])
            typelist.pop(vocabu[i])
            vocalist.pop(vocabu[i])

def blodChangeB():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 1
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first,last,index)
    except TclError:
        pass

def blodChangeC():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 2
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeD():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 3
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeE():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 4
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeF():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 5
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeG():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 6
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeH():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 7
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeI():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 8
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeJ():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 9
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeK():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 10
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeL():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 11
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def blodChangeM():
    try:
        first = Text_1.index(SEL_FIRST)
        last = Text_1.index(SEL_LAST)
        index = 12
        deabeginarr = first.split(".")
        deendarr = last.split(".")
        remove_vo_change(deabeginarr[1], deendarr[1])
        flag_change(first, last, index)
    except TclError:
        pass

def flagtext(beginlist_1,endlist_1,typelist_1,strtext_1):
    tag = typelist_1
    Text_1.insert(END, strtext_1)
    for i in range(0,len(tag)):
        if((tag[i])=='1'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 1
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '2'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 2
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '3'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 3
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '4'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 4
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '5'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 5
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '6'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 6
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '7'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 7
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '8'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 8
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '9'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 9
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '10'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 10
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '11'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 11
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '12'):
            firststr = '1.' + beginlist_1[i]
            laststr = '1.' + endlist_1[i]
            index = 12
            flag_change(firststr, laststr, index)

# Special document No
def write_special_num():
    snum = int(v.get())
    strpath = "./store_info/special_num.txt"
    f = open(strpath, 'a')
    f.write('\n'+ path_check_list[snum])
    f.close()

master = Tk()
master.geometry('650x600')
walkFile(file_path_all)
print(path_check_list.__len__())
frame_6 = Frame(master)
frame_6.pack()
label_6 = Label(frame_6, text="选择文本序号")
label_6.grid(row=1, column=0)
value_list = tkinter.StringVar()
label_out = tkinter.StringVar()
v=tkinter.StringVar()
v.set("-1")
number = Spinbox(frame_6, textvariable=v, from_=0, to=path_check_list.__len__())
number.grid(row=1, column=1)
number_ok = Button(frame_6, text="确定", command=btuchange_jump)
number_ok.grid(row=1, column=2)
frame_7 = Frame(master)
frame_7.pack(fill=X)
label_5 = Label(frame_7, text='文本标记')
label_5.grid(row=1, column=0)
frame_4 = Frame(master)
frame_4.pack()
label_4 = Label(frame_4, text='   ')
removeall = Button(frame_4, text="删除所有标签",command =btuchange_removeall)
special_all = Button(frame_4, text="添加特殊页码",command =write_special_num)
removeall.grid(row=3, column=9, padx=5, pady=5)
special_all.grid(row=3, column=10, padx=5, pady=5)
frame_5 = Frame(master)
frame_5.pack()
btn_first = Button(frame_5,  text='取消标记', fg='black',command = blodChangeA)
btn_second = Button(frame_5, text="病  害", fg= backgroundlist[1], command = blodChangeB)
btn_third = Button(frame_5, text="虫  害",fg= backgroundlist[2], command =blodChangeC)
btn_forth = Button(frame_5, text="病  原",fg= backgroundlist[3], command = blodChangeD)
btn_fifth = Button(frame_5, text="药  剂",fg= backgroundlist[4], command = blodChangeE)
btn_sixth = Button(frame_5, text="植  物",fg= backgroundlist[5], command = blodChangeF)
btn_seven = Button(frame_5, text="草  害",fg= backgroundlist[6], command=blodChangeG)
btn_eight = Button(frame_5, text="化  肥",fg= backgroundlist[7], command= blodChangeH)
btn_nine = Button(frame_5, text="生防菌",fg= backgroundlist[8], command= blodChangeI)
btn_ten = Button(frame_5, text="类 药剂",fg= backgroundlist[9], command= blodChangeJ)
btn_eleven = Button(frame_5, text="助  剂",fg= backgroundlist[10], command= blodChangeK)
btn_yuan = Button(frame_5, text="病原菌株",fg= backgroundlist[11], command= blodChangeL)
btn_yao = Button(frame_5, text="生防菌株",fg= backgroundlist[12], command= blodChangeM)
btn_first.grid(row=2, column=1, padx=5, pady=5)
btn_second.grid(row=2, column=2, padx=5, pady=5)
btn_third.grid(row=2, column=3, padx=5, pady=5)
btn_forth.grid(row=2, column=4, padx=5, pady=5)
btn_fifth.grid(row=2, column=5, padx=5, pady=5)
btn_sixth.grid(row=2, column=6, padx=5, pady=5)
btn_seven.grid(row=2, column=7, padx=5, pady=5)
btn_eight.grid(row=2, column=8, padx=5, pady=5)
btn_nine.grid(row=2, column=9, padx=5, pady=5)
btn_ten.grid(row=2, column=10, padx=5, pady=5)
btn_eleven.grid(row=2, column=11, padx=5, pady=5)
btn_yuan.grid(row=3, column=5, padx=5, pady=5)
btn_yao.grid(row=3, column=6, padx=5, pady=5)
frame_3 = Frame(master)
frame_3.pack()
Text_1 = Text(master=frame_3,height=15,width=50,
           highlightthickness=2,highlightcolor='black',
           highlightbackground='black',
            relief = "groove",font=('Verdana', 15) )
Text_1.pack()
frame_2 = Frame(master)
frame_2.pack()
btn_up = Button(frame_2, text="上一个",command=btuchange_up)
btn_next = Button(frame_2, text="下一个",command=btuchange_next)
btu_end = Button(frame_2, text="输出结果",fg= backgroundlist[7],command=btuchange_endout)
btu_end_next = Button(frame_2, text="输出结果+next", fg= backgroundlist[8],command=btuchange_endout_next)
btn_up.grid(row=2, column=1, padx=5, pady=5)
btn_next.grid(row=2, column=4, padx=5, pady=5)
btu_end.grid(row=2, column=2, padx=5, pady=5)
btu_end_next.grid(row=2, column=3, padx=5, pady=5)
frame_1 = Frame(master)
frame_1.pack()
label_3 = Label(frame_1, text = "输出样例：")
label_3.grid(row=1, column=1, padx=5, pady=5)
frame_0 = Frame(master)
frame_0.pack()
Text_label = Text(master=frame_0,height=5,width=50,
           highlightthickness=2,highlightcolor='black',
           highlightbackground='black',
            relief = "groove",font=('Verdana', 15) )
Text_label.pack()
strtxt_num = read_store_info_now()
if(strtxt_num.__eq__("")):
    readtxt(str(0))
    writetext_num("0")
    v.set("0")
else:
    readtxt(strtxt_num)
    v.set(strtxt_num)
master.mainloop()
