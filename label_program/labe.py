# Text annotation

from tkinter import *
import tkinter.ttk
from sucaideal import IMM,XmlMaker
import os
from tkinter import filedialog

# 删除保存位置
indexlist = []
# 删除保存字符串
stringlist = []
# 开始位置
beginlist = []
# 结束位置
endlist = []
# 分类
typelist = []
# 文本词汇
vocalist = []

backgroundlist = ['white','CornflowerBlue','DarkViolet','Pink','Cyan','DarkGreen','Olive','Orange','OrangeRed','PapayaWhip']
foregroundlist = ['black','white','white','white','white','white','white','white','white','Chocolate']
typeflaglist = ['0','1','2','3','4','5','6','7','8','9']
flaglist = ['a','b','c','d','e','f','g','h','i','j']
file_path = []

va = []

# 输入文件夹
file_path_all = "xxxx"


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
    # 删除保存位置
    indexlist.clear()
    # 删除保存字符串
    stringlist.clear()
    # 开始位置
    beginlist.clear()
    # 结束位置
    endlist.clear()
    # 分类
    typelist.clear()
    # 文本词汇
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
    Text_1.tag_add("flag_del", '0.0', END)
    Text_1.tag_config("flag_del", background=backgroundlist[0], foreground=foregroundlist[0])
    clearfourlist()

def btuchange_removeall():
    Text_1.tag_add("flag_del", '0.0', END)
    Text_1.tag_config("flag_del", background=backgroundlist[0], foreground=foregroundlist[0])
    clearlist()

def btuchange_delete():
    try:
        indexlist.append(Text_1.index(SEL_FIRST))
        str = Text_1.get(SEL_FIRST, SEL_LAST)
        stringlist.append(str)
        Text_1.delete(SEL_FIRST, SEL_LAST)
        flag_delete()
    except TclError:
        pass

def btuchange_undo():
    try:
        if(indexlist.__len__() != 0):
            Text_1.mark_set("undo", indexlist[indexlist.__len__()-1])
            Text_1.insert("undo", stringlist[stringlist.__len__()-1])
            indexlist.pop()
            stringlist.pop()
            flag_delete()
    except TclError:
        pass

def clearfourlist():
    # 开始位置
    beginlist.clear()
    # 结束位置
    endlist.clear()
    # 分类
    typelist.clear()
    # 文本词汇
    vocalist.clear()

def btuchange_del_bla():
    textstr = Text_1.get('0.0', END)
    Text_1.delete('0.0', END)
    clearlist()
    textstr=textstr.replace(" ","")
    textinsert(textstr)

def btuchange_recheck():
    textstr = Text_1.get('0.0', END)
    Text_1.delete('0.0', END)
    clearlist()
    textinsert(textstr)

def btuchange_up():
    nowindex = int(v.get()) - 1
    if(nowindex>=0):
        clearlist()
        Text_1.delete('0.0', END)
        v.set(nowindex)
        textstring = readtxt(str(nowindex))
        textinsert(textstring)
        
def btuchange_next():
    clearlist()
    Text_1.delete('0.0', END)
    nowindex = int(v.get()) + 1
    v.set(nowindex)
    textstring = readtxt(str(nowindex))
    textinsert(textstring)

# 输出位置
def writetext(begin,end,voca,type,strtext):
    path = int(v.get())
    strpath = "xxxx"+path_check_list[path]
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

# 字典
def writedic(dic_list_data):
    path="./data/total_dict.utf8"
    f = open(path, 'a')
    for i in range(0,dic_list_data.__len__()):
        f.write(dic_list_data[i]+'\n')
    f.close()


def writetext_num(num):
    strpath = "./store_info/now_num.txt"
    f = open(strpath, 'w')
    f.write(num)
    f.close()

def write_special_num():
    snum = str(v.get())
    strpath = "./store_info/special_num.txt"
    f = open(strpath, 'a')
    f.write('\n'+snum)
    f.close()

def btuchange_endout_next():
    dic_list_data = []
    for i  in range(0,beginlist.__len__()):
        dic_list_data.append(vocalist[i]+" "+str(typelist[i]))
    writedic(dic_list_data)
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
    if (int(nowindex) >= 0):
        clearlist()
        textstring = readtxt(str(v.get()))
        Text_1.delete('0.0', END)
        textinsert(textstring)

def textinsert(textstr):
    textstr = textstr.replace("\n", "")
    textstr = textstr.replace(" ", "")
    Text_1.insert(END, textstr)
    flagtext(textstr)

def readtxt(path):
 strpath = file_path_all + path_check_list[int(path)]
    strtxt = ""
    for line in open(strpath ,'r'):
        line = line.replace("\n", "")
        strtxt=strtxt+line
    return strtxt

def read_store_info_now():
    strpath = "./store_info/now_num.txt"
    strtxt = ""
    for line in open(strpath, 'r'):
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        strtxt = strtxt + line
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

def flagtext(textstr):
    tokenizer = IMM('./data/total_dict.utf8')
    num,result,tag = tokenizer.cut(textstr)
    for i in range(0,len(tag)):
        if((tag[i])=='1'):
            strnum = num[i]
            numarr = strnum.split(":")
            firststr = '1.' + numarr[0]
            laststr = '1.' + numarr[1]
            index = 1
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '2'):
            strnum = num[i]
            numarr = strnum.split(":")
            firststr = '1.' + numarr[0]
            laststr = '1.' + numarr[1]
            index = 2
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '3'):
            strnum = num[i]
            numarr = strnum.split(":")
            firststr = '1.' + numarr[0]
            laststr = '1.' + numarr[1]
            index = 3
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '4'):
            strnum = num[i]
            numarr = strnum.split(":")
            firststr = '1.' + numarr[0]
            laststr = '1.' + numarr[1]
            index = 4
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '5'):
            strnum = num[i]
            numarr = strnum.split(":")
            firststr = '1.' + numarr[0]
            laststr = '1.' + numarr[1]
            index = 5
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '6'):
            strnum = num[i]
            numarr = strnum.split(":")
            firststr = '1.' + numarr[0]
            laststr = '1.' + numarr[1]
            index = 6
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '7'):
            strnum = num[i]
            numarr = strnum.split(":")
            firststr = '1.' + numarr[0]
            laststr = '1.' + numarr[1]
            index = 7
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '8'):
            strnum = num[i]
            numarr = strnum.split(":")
            firststr = '1.' + numarr[0]
            laststr = '1.' + numarr[1]
            index = 8
            flag_change(firststr, laststr, index)
        if ((tag[i]) == '9'):
            strnum = num[i]
            numarr = strnum.split(":")
            firststr = '1.' + numarr[0]
            laststr = '1.' + numarr[1]
            index = 9
            flag_change(firststr, laststr, index)

path_check_list = []

def walkFile(file):
    files = os.listdir(file)
    files.sort()
    for file_ in files:
        f_name = str(file_)
        if (f_name[-4:].__eq__(".txt")):
                path_check_list.append(f_name)

def filefound():
    file_pa = filedialog.askdirectory()
    file_path.append(file_pa)
    walkFile(file_path[0])

master = Tk()
master.geometry('650x600')
frame_6 = Frame(master)
frame_6.pack()
label_6 = Label(frame_6, text="选择文本序号")
label_6.grid(row=1, column=0)
walkFile(file_path_all)
value_list = tkinter.StringVar()
label_out = tkinter.StringVar()
v=tkinter.StringVar()
number = Spinbox(frame_6, textvariable=v, from_=0, to=15789)
number.grid(row=1, column=1)
number_ok = Button(frame_6, text="确定", command=btuchange_jump)
number_ok.grid(row=1, column=2)
btu_file_check = Button(frame_6, text="选择文件目录" , command=filefound)
btu_file_check.grid(row=1, column=3, padx=5, pady=5)
frame_7 = Frame(master)
frame_7.pack(fill=X)
label_5 = Label(frame_7, text='文本标记')
label_5.grid(row=1, column=0)
frame_4 = Frame(master)
frame_4.pack()
label_4 = Label(frame_4, text='   ')
de = Button(frame_4, text="删除",command=btuchange_delete)
undo = Button(frame_4, text="撤销删除",command =btuchange_undo)
recheck = Button(frame_4, text="重新识别",command =btuchange_recheck)
removeall = Button(frame_4, text="删除所有标签",command =btuchange_removeall)
special_all = Button(frame_4, text="添加特殊页码",command =write_special_num)
de.grid(row=3, column=5, padx=5, pady=5)
undo.grid(row=3, column=6, padx=5, pady=5)
label_4.grid(row=3, column=7, padx=5, pady=5)
recheck.grid(row=3, column=8, padx=5, pady=5)
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
btn_nine = Button(frame_5, text="生物药剂",fg= backgroundlist[8], command= blodChangeI)
btn_ten = Button(frame_5, text="类 药剂",fg= backgroundlist[9], command= blodChangeJ)
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
dele_bla = Button(frame_2, text="删除空格",command=btuchange_del_bla)
dele_bla.grid(row=2, column=6, padx=5, pady=5)
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
strtext = ""
if(strtxt_num.__eq__("")):
    strtext = readtxt(str(0))
    writetext_num("0")
    v.set("0")
else:
    strtext = readtxt(strtxt_num)
    v.set(strtxt_num)
textinsert(strtext)
master.mainloop()
