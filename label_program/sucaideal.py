# 处理工具

from xml.dom.minidom import Document

class XmlMaker:
    def __init__(self,txtpath,xmlpath):
        self.txtPath = txtpath
        self.xmlPath = xmlpath
        self.txtList = []


    def readtxt(self):
        txtfile = open(self.txtPath,"r",encoding='utf-8',errors='ignore')
        self.txtList = txtfile.readlines()
        for i in self.txtList:
            oneline = i.strip().split(" ")
            if len(oneline) != 5:
                print("TxtError")

    def makexml(self,num,result,tag,line):
        doc = Document()

        dict1 = {'1':"Disease",'2':"Insect_pest",'3':"Pathogeny",'4':"Medicament",'5':"Plant_name"}

        begindoc = doc.createElement("doc")
        doc.appendChild(begindoc)

        pathinfo = "-------"
        objectpath = doc.createElement("path")
        objectcontenttext = doc.createTextNode(pathinfo)
        objectpath.appendChild(objectcontenttext)
        begindoc.appendChild(objectpath)

        objectoutput = doc.createElement("outputs")
        begindoc.appendChild(objectoutput)

        objectannotation = doc.createElement("annotation")
        objectoutput.appendChild(objectannotation)

        objectT = doc.createElement("T")
        objectannotation.appendChild(objectT)

        objectbeiginitem = doc.createElement("item")
        objectbeigintext = doc.createTextNode("")
        objectbeiginitem.appendChild(objectbeigintext)
        objectT.appendChild(objectbeiginitem)


        for i in range(0,num.__len__()-1):

            objectitem = doc.createElement("item")

            objecttype = doc.createElement("type")
            objecttypetext = doc.createTextNode("T")
            objecttype.appendChild(objecttypetext)
            objectitem.appendChild(objecttype)

            print(result[i])
            print(num[i])
            print(tag[i])
            objectname = doc.createElement("name")
            objectnametext = doc.createTextNode(dict1[str(tag[i])])
            objectname.appendChild(objectnametext)
            objectitem.appendChild(objectname)

            objectvalue= doc.createElement("value")
            objectvaluetext = doc.createTextNode(result[i])
            objectvalue.appendChild(objectvaluetext)
            objectitem.appendChild(objectvalue)

            array = num[i].split(":")
            objectstart = doc.createElement("start")
            objectstarttext = doc.createTextNode(array[0])
            objectstart.appendChild(objectstarttext)
            objectitem.appendChild(objectstart)

            objectend = doc.createElement("end")
            objectendtext = doc.createTextNode(array[1])
            objectend.appendChild(objectendtext)
            objectitem.appendChild(objectend)

            objectattributes = doc.createElement("attributes")
            objectattributestext = doc.createTextNode("")
            objectattributes.appendChild(objectattributestext)
            objectitem.appendChild(objectattributes)

            objectid = doc.createElement("id")
            objectidtext = doc.createTextNode(str(i))
            objectid.appendChild(objectidtext)
            objectitem.appendChild(objectid)

            objectT.appendChild(objectitem)

        objectE= doc.createElement("E")
        objectannotation.appendChild(objectE)

        objectseconditem = doc.createElement("item")
        objectsecondtext = doc.createTextNode("")
        objectseconditem.appendChild(objectsecondtext)
        objectE.appendChild(objectseconditem)

        objectR = doc.createElement("R")
        objectannotation.appendChild(objectR)

        objectthirditem = doc.createElement("item")
        objectthirdtext = doc.createTextNode("")
        objectthirditem.appendChild(objectthirdtext)
        objectR.appendChild(objectthirditem)

        objectA = doc.createElement("A")
        objectannotation.appendChild(objectA)

        objectforthitem = doc.createElement("item")
        objectforthtext = doc.createTextNode("")
        objectforthitem.appendChild(objectforthtext)
        objectA.appendChild(objectforthitem)

        tlinfo = "-------"
        objecttl = doc.createElement("time_labeled")
        objecttltext = doc.createTextNode(tlinfo)
        objecttl.appendChild(objecttltext)
        begindoc.appendChild(objecttl)

        labeledinfo = "-------"
        objectlabeled = doc.createElement("labeled")
        objectlabeledtext = doc.createTextNode(labeledinfo)
        objectlabeled.appendChild(objectlabeledtext)
        begindoc.appendChild(objectlabeled)

        objectcon = doc.createElement("content")
        objectcontext = doc.createTextNode(line)
        objectcon.appendChild(objectcontext)
        begindoc.appendChild(objectcon)

        f = open(self.xmlPath, 'w')
        doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()

# 逆向最大匹配
class IMM(object):
    def __init__(self, dic_path):
        self.dictionary = set()
        self.maximum = 0
        self.twodict = {}
        # 读取词典
        with open(dic_path, 'r', encoding='utf8') as f:
            for line in f:
                line = line.strip()
                data = line.split(" ")
                if not line:
                    continue
                self.dictionary.add(data[0])
                self.twodict[data[0]] = data[1]
                if len(data[0]) > self.maximum:
                    self.maximum = len(data[0])

    def cut(self, text):
        text=text.replace("\n","")
        # 词语
        result = []
        # 位置序号
        num = []
        # 标签
        tag = []
        copytext = text
        index = len(text)
        while index > 0:
            word = None
            for size in range(self.maximum, 0, -1):
                if index - size < 0:
                    continue
                piece = text[(index - size):index]
                if piece in self.dictionary:
                    word = piece
                    num.append(str(index - size)+':'+str(index))
                    result.append(word)
                    one = copytext[:index - size]
                    two = copytext[index - size:index]
                    three = copytext[index:]
                    copytext=one+"【--"+two+"--】"+three
                    tag.append(self.twodict[word])
                    index -= size
                    break
            if word is None:
                index -= 1
        return num[::-1],result[::-1],tag[::-1]
