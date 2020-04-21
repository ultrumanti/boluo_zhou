
import linecache
import os

# Convert data file to specified format

# Tag category: BIEO
flag_list = [ "O",
             "B-DISE", "I-DISE", "E-DISE",
             "B-PEST", "I-PEST", "E-PEST",
             "B-PATH", "I-PATH", "E-PATH",
             "B-DRUG", "I-DRUG", "E-DRUG",
             "B-PLAN", "I-PLAN", "E-PLAN",
             "B-WEED", "I-WEED", "E-WEED" ]


def getdata(the_file_path):
    data_list = []
    for line in open(the_file_path, "r"):
        line = line.replace("\n", "")
        data_list.append(line)
    str_begin = data_list[0].split("]--[")
    str_end = data_list[1].split("]--[")
    str_info = data_list[2].split("]--[")
    str_type = data_list[3].split("]--[")
    str_text = data_list[4]
    data_flag = []
    behind_flage = flag_list[0]
    i=0
    while(True):
        char_text = str_text[i:i+1]
        end_type, flag_result = flag_judge(i, str_begin, str_end)
        if(end_type == -1):
            info_len = 1
        else:
            info_len = len(str_info[end_type])
        inden = int(str_type[end_type])
        if( flag_result == 1):
            if(inden < 7):
                if (inden == 6):
                    inden = 5
                if (info_len == 1):
                    char_text =  char_text + " W"
                    data_flag.append(char_text)
                if (info_len == 2):
                    char_text = char_text + " " +flag_list[inden * 3 - 2 ]
                    data_flag.append(char_text)
                    char_text = str_text[i + 1:i + 2]
                    char_text = char_text + " " + flag_list[inden * 3 ]
                    data_flag.append(char_text)
                if (info_len > 2):
                    char_text = char_text + " " + flag_list[inden * 3 - 2]
                    data_flag.append(char_text)
                    for j in range(0,info_len-2):
                        char_text = str_text[i+1+j:i+2+j]
                        char_text = char_text + " " + flag_list[inden * 3-1]
                        data_flag.append(char_text)
                    char_text = str_text[i + info_len - 1:i + info_len ]
                    char_text = char_text + " " + flag_list[inden * 3]
                    data_flag.append(char_text)
            else:
                char_text = char_text + " O"
                data_flag.append(char_text)
        else:
            char_text = char_text + " O"
            data_flag.append(char_text)
        i = i + info_len
        if(i >= len(str_text)):
            break
    return data_flag

def flag_judge(index, str_begin,str_end):
    end_type = -1
    flag_result = 0
    for i in range(0,str_begin.__len__()):
        if(index >= int(str_begin[i]) and index < int(str_end[i])):
            end_type = i
            flag_result = 1
    return end_type, flag_result

va = []
def walkFile(file):
    files = os.listdir(file)
    files.sort()
    for file_ in files:
        f_name = str(file_)
        if (f_name[-4:].__eq__(".txt")):
            va.append(file + "/" + f_name)

def writetext(data_flag, file_path):
    f = open(file_path, 'a')
    for i in range(0,len(data_flag)):
        f.write(data_flag[i] + "\n")
    f.write("\n")
    f.close()


# Folders to convert
file_path_all = "xxxxx/train"
# Store files after conversion
file_path = "xxxxx/train.txt"


va.clear()
walkFile(file_path_all)
for i in range(0,va.__len__()):
    data_flag = getdata(va[i])
    writetext(data_flag, file_path)


