import os
from  pkg_resources   import *
import tkinter
from tkinter import ttk,IntVar
from tkinter import messagebox as mBox
from template import *
from header import Header
from mykeyword import Keyword



# 定义函数按键函数
# 清空文本输入框的内容
def format_clear():
    #定义一个变量，把e的值获取
    t.delete('1.0','end') 
    t2.delete('1.0','end') 
    t2.insert("insert"," 【文章关键字】 \n================\n\n")


def format_set():

    var_cls = str()
    var_f = str()
    # 落款行数
    var_end = radio.get()
    # 标题样式
    var_style = cmb3.get()
    #定义一个变量，获取用户输入的字符文本
    var = t.get("0.0",tkinter.END)
    # 除去字符串中的空行
    var_cls = "".join([s for s in var.splitlines(True) if s.strip()])
    t.delete('1.0','end')
    t.insert("insert",var_cls)
    t2.delete('1.0','end') 
    t2.insert("insert"," 【文章关键字】 \n================\n\n")

    # 去空格 预处理
    var_2 = t.get("0.0",tkinter.END)
    # var_f = "".join([s.strip("u\u3000") for s in var_cls.splitlines(True) if s.strip()])
    # 各种空白字符的Unicode编码
    # white_space = ["u\u0009", "u\u000A", "u\u000B", "u\u000C", "u\u000D", "u\u0020", "u\u0085", "u\u0020", "u\u1680", "u\u2002", "u\u2003", "u\u2002", "u\u2003", "u\u2004", "u\u2005", "u\u2009", "u\u2007", "u\u2008", "u\u2008", "u\u200A", "u\u2028", "u\u2029", "u\u2009", "u\u205F", "u\u3000"]
    white_space = ["u\u000a","u\u000d","u\u0009", "u\u000B",  "u\u1680", "u\u2002", "u\u2003", "u\u2002", "u\u2003", "u\u2004", "u\u2005", "u\u2009", "u\u2007", "u\u2008", "u\u2008", "u\u200A", "u\u2028", "u\u2029", "u\u2009", "u\u205F", "u\u3000"]
    for space in white_space: 
        var_f = "".join([s.strip(space) for s in var_cls.splitlines(True) if s.strip()])

    var_f = "".join([s.strip("u\u0020") for s in var_f.splitlines(True) if s.strip()])
    var_f = "".join([s.strip("u\u2002") for s in var_f.splitlines(True) if s.strip()])
    #var_f = "".join([s.strip("u\u000a") for s in var_f.splitlines(True) if s.strip()])
    #var_f = "".join([s.strip("u\u000d") for s in var_f.splitlines(True) if s.strip()])
    
    # 回显文字
    t.delete('1.0','end')
    t.insert("insert",var_f)

    if os.path.exists("./格式化文本.html"):
        os.remove("./格式化文本.html")
    if os.path.exists("./123.txt"):
        os.remove("./123.txt")

    # 生成一个txt文档，便于查询关键字
    with open("123.txt",'a',encoding='utf-8') as x:
        TXT = str()
        for l in var_f.splitlines(True):
            TXT += l
        x.write(TXT)
    # 获取文档关键字
    K = Keyword()
    keywords = K.get_keywords()
    t2.insert("insert",keywords)
    # 生成html文档，用于格式排版

    with open("格式化文本.html",'a',encoding='utf-8') as h:

        All = str()
        #标题
        H1 = str()
        #内容
        C = str()
        # 落款
        E = str()
        #表头
        Table = str()
        # 广告
        Ad = str()

        # write table
        # 时间
        RE_T = str()
        # 学历
        RE_D = str()
        # 学段
        RE_P = str()
        # 年龄
        RE_A = str()
        # 人数 
        RE_N = str() 


        T = Template() 
        # 需要落款
        if var_end !=0:
            # 正文排版
            for l in var_f.splitlines(True)[:-var_end]:
                # 是标题
                if T.is_H1(var_style,l):
                    H1 = T.H1(l)                   
                    All += H1
                # 其他正文
                else:
                    C = T.C(l)
                    All += C
            for l in var_f.splitlines(True)[-var_end:]:
                E = T.E(l)
                All += E
        else:
            # 正文排版
            for l in var_f.splitlines(True)[:]:
                # 是标题
                if T.is_H1(var_style,l):
                    H1 = T.H1(l)                   
                    All += H1
                # 其他正文
                else:
                    C = T.C(l)
                    All += C
                    
        #合并排版后的内容
        # 如果需要表头
        if yn_radio.get() == 1: 
            H = Header()
            RE_T, RE_D, RE_P, RE_A, RE_N = H.RE() 
            Table = T.T1(RE_T,RE_D,RE_P,RE_A,RE_N)
            # Ad = T.AD()
            h.write(Table+All)
        else:
            h.write(All)
        
        # 自定义广告
        # h.write(Table+All+Ad)

    mBox.showinfo("重要提示","排版文件已生成。\n\nPs:注意：\n\n1、文章开头的内容概述为机器生成，需进行人工核对！\n\n2 、表格、图片、附件等需手动上传！\n\n3、本软件仅为辅助性工具。\n    因编辑人员造成的文章错漏引发的后续问题，软件开发人员概不负责！")


    if os.path.exists("./123.txt"):
        os.remove("./123.txt")


#===================================================================          
from datetime import datetime
from easygui import msgbox
#构造一个将来的时间
#截止日期:
future = datetime.strptime('2021-06-01 08:00:00','%Y-%m-%d %H:%M:%S')
#当前时间
now = datetime.now()
#求时间差
delta = future - now

print("倒计时:" + str(delta.days))
#===================================================================          
if(delta.days>0):
    # 创建窗口
    window = tkinter.Tk()
else:
    info='''
                     _______________
                    / 哥走了，      \\
                    \\ 有缘江湖再见。/
                     ---------------
                      \\
                       \  ^^___^^
                        \  (o o)\_______
                           (___)\        )\/\\
                               ||        |
                               ||------W |
                               ||       ||
   '''   
    msgbox(info,"温馨提示")

window.title("排版助手_V3.0")
window.geometry("880x560")
# GUI 界面编辑 

# 创建滚动条
scroll = tkinter.Scrollbar()
# 创建文本框text，设置宽度100，high不是高度，是文本显示的行数设置为3行
t = tkinter.Text(window,width=56)
t2 = tkinter.Text(window,width=18)
# 将滚动条填充
# side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
# scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
t2.pack(side="left",fill=tkinter.Y) # 将文本框填充进window窗口的左侧，
t.pack(side=tkinter.LEFT,fill=tkinter.Y) # 将文本框填充进window窗口的左侧，
t.pack(side="left",fill=tkinter.Y) # 将文本框填充进window窗口的左侧，
scroll.pack(side="left", fill=tkinter.Y)
# 将滚动条与文本框关联
scroll.config(command=t.yview) # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
t.config(yscrollcommand=scroll.set) # 将滚动条关联到文本框

## 创建按钮
b1 = tkinter.Button(window,text='清空文本',width = 15,height= 2,command = format_clear)
b2 = tkinter.Button(window,text='自动排版',width = 15,height= 2,command = format_set)
b1.pack(side='top')
b2.pack(side='bottom')

# 落款行数
lab = ttk.Label(window, width=15,text="")
lab.pack(side='bottom')
# 创建下拉菜单
# cmb = ttk.Combobox(window,width=15,height=2)
# cmb.pack(side='bottom')
# cmb['value'] = ('0','2','3','4')
# cmb.current(1)

radio = IntVar()

PS = [
    ("【 -4- 】",4),
    ("【 -3- 】",3),
    ("【 -2- 】",2),
    ("【 -0- 】",0)
]
for lab,num in PS: 
    R = ttk.Radiobutton(text=lab, variable=radio, value=num)
    R.pack(side="bottom")
# 默认两行落款
radio.set(2)

# 落款行数
lab = ttk.Label(window, width=15,text="\n【 设置落款行数 】")
lab.pack(side='bottom')

yn_radio = IntVar()

YN = [
    ("【 -是- 】",1),
    ("【 -否- 】",0)
]
for lab2,num2 in YN: 
    X = ttk.Radiobutton(text=lab2, variable=yn_radio, value=num2,)
    X.pack(side="bottom")
# 落款行数
lab2 = ttk.Label(window, width=15,text="\n【 是否生成表格 】")
lab2.pack(side='bottom')
# 文章标题样式
cmb3 = ttk.Combobox(window,width=15,height=2)
cmb3.pack(side='bottom')
cmb3['value'] = ('一、二、三、','1、2、3、')
cmb3.current(0)
# 落款行数
lab2 = ttk.Label(window, width=15,text="【 设置标题样式 】")
lab2.pack(side='bottom')
# 设置文本框内容
txt = "请在此处粘贴需要排版的文字。" 
# 将文本内容插入文本框
input_txt = t.insert("insert",txt)
t2.insert("insert"," 【文章关键字】 \n================\n\n")
window.mainloop()
