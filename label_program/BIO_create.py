
import linecache
import os

# Convert data file to specified format

# Tag category: BIO
flag_list = ["O",
             "B-DISE", "I-DISE",
             "B-PEST", "I-PEST",
             "B-PATH", "I-PATH",
             "B-DRUG", "I-DRUG",
             "B-PLAN", "I-PLAN",
             "B-WEED", "I-WEED",

            "B-CHEM", "I-CHEM",
            "B-BIOL", "I-BIOL",
            "B-TYPE", "I-TYPE",
            "B-AUXI", "I-AUXI",
            "B-PAST", "I-PAST",
            "B-BIST", "I-BIST"
             ]



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
    for i in range(0,str_text.__len__()):
        char_text = str_text[i:i+1]
        end_type, flag_result = flag_judge(i, str_begin, str_end)
        num_inde = int(str_type[end_type])
        if(num_inde == 6):
            num_inde = 5
        if(num_inde >6):
            flag_result = 0
        if( flag_result == 1):
            if(behind_flage.__eq__("O")):
                char_text = char_text + " " +flag_list[num_inde*2-1]
                if(str(i+1) in str_end):
                    behind_flage = flag_list[0]
                else:
                    behind_flage = flag_list[num_inde *2-1]
            else:
                char_text = char_text + " " + flag_list[num_inde*2]
                if (str(i + 1) in str_end):
                    behind_flage = flag_list[0]
                else:
                    behind_flage = flag_list[num_inde*2]
        else:
            char_text = char_text + " " + flag_list[0]
            behind_flage = flag_list[0]
        data_flag.append(char_text)
    return data_flag

def flag_judge(index, str_begin,str_end):
    end_type = 0
    flag_result = 0
    for i in range(0,str_begin.__len__()):
        if(index >= int(str_begin[i]) and index < int(str_end[i])):
            end_type = i
            flag_result = 1
    return end_type, flag_result

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
file_path_all = "xxxxx/train/"
# Store files after conversion
file_path = "xxxxx/train.txt"

va = []
walkFile(file_path_all)
for i in range(0,va.__len__()):
    data_flag = getdata(va[i])
    writetext(data_flag, file_path)


