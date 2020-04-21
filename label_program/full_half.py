# -*- coding: cp936 -*-

import linecache
import os
import shutil

#


def strQ2B(ustring):
    # Half to full
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # Half space direct conversion
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):
        # Half width characters (except space) converted according to relationship
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring

def strB2Q(ustring):
    # Half to full
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 32:  # Half space
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:
        # Half width characters (except space) converted according to relationship
            inside_code += 65248
        rstring += chr(inside_code)
    return rstring

path_check_list = []

def walkFile(file):
    files = os.listdir(file)
    files.sort()
    for file_ in files:
        f_name = str(file_)
        if (f_name[-4:].__eq__(".txt")):
            path_check_list.append(f_name)

def create_new(the_folder_path,file_path):
    data_list = []
    for line in open(the_folder_path+file_path, "r"):
        line = line.replace("\n", "")
        data_list.append(line)
    beginlist_1 = strQ2B(data_list[0])
    endlist_1 = strQ2B(data_list[1])
    vocalist_1 = strQ2B(data_list[2])
    typelist_1 = strQ2B(data_list[3])
    strtext_1 = strQ2B(data_list[4])
    flagtext(beginlist_1, endlist_1,vocalist_1, typelist_1, strtext_1,file_path)

# Destination folder
file_path_all= "xxxxx/re_output/"
# Output folder
path_out_str="xxxxx/trans_yuan/"

def flagtext(beginlist_1, endlist_1,vocalist_1, typelist_1, strtext_1,file_path):
    strpath = path_out_str + file_path
    print(strpath)
    f = open(strpath, 'w')
    f.write(beginlist_1 + '\n')
    f.write(endlist_1 + '\n')
    f.write(vocalist_1 + '\n')
    f.write(typelist_1 + '\n')
    f.write(strtext_1)
    f.close()
    
walkFile(file_path_all)

for i in range(0,path_check_list.__len__()):
    create_new(file_path_all , path_check_list[i])

