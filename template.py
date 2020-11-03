#!/bin/python
#***********************************************
#
#      Filename: template.py
#
#        Author:
#   Description: ---
#        Create: 2020-05-30 12:32:44
#***********************************************
# 大致思路
#***********************************************
# 1、选择文本来源
#       【0】已删除格式的纯文本文档
#       【1】输入url爬去的文档
# 2、标注文本类别
#      【0】标题  
#      【1】正文
#      【2】描红
#      【3】尾注
# 3、应用格式进行排版
#      【0】输出html格式的文本文档  
#      【1】直接复制到windows剪切板
# 4、复制文字到后台编辑器
# 5、提示编辑人员检查图片、表格、附件等细节
#      【0】表格、图片格式检查
#      【1】提示下载附件并上传到自己的服务器
#***********************************************
import re

class Template:

    # 广告
    def AD(s):
        # 广告文件存放路径
        Ad_path = "./AD.html"

        F_AD = str()
        # 默认推荐：空白
        # 默认广告：当前
        ad ='<p style="text-indent: 0em; margin-bottom: 10px; line-height: 2em;"> <span style="font-family: 宋体, SimSun; font-size: 16px;"><strong>【推荐阅读】</strong></span> </p><p style="padding: 0px; margin-top: 0px; font-family: &quot;Microsoft YaHei&quot;; font-size: 14px; text-indent: 0em; white-space: normal; background-color: rgb(255, 255, 255); margin-bottom: 10px; line-height: 2em;"> <span style="color: #000000; font-family: 宋体, SimSun; font-size: 16px;"><strong>【推荐资料】</strong></span> </p>' 

        F_AD += ad
        with open(Ad_path,encoding='utf-8') as f:
            lines = f.readlines()
            for l in lines:
                print(l)
                F_AD += l
        return F_AD

    # 公告表头
    # 参数以及格式化文本
    def T1(s,time,degree,peroid,age,num):
        
        b1 = '<p style="padding: 0px; font-family: &quot;Microsoft YaHei&quot;; font-size: 14px; white-space: normal; background-color: rgb(255, 255, 255); text-indent: 0em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;"><strong>【内容摘要】</strong></span> </p> <table width="1000" style="width: 962px;"> <tbody> <tr class="firstRow"> <td width="280" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="text-indent: 0em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;">报名时间</span> </p> </td> <td width="720" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="color: #FF0000; text-indent: 32px; font-size: 16px; font-family: 宋体, SimSun;">'
        # 报名时间
        t = time 
        b2='</span> </p> </td> </tr> <tr> <td width="280" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="text-indent: 0em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;">学历要求</span> </p> </td> <td width="720" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="white-space: normal; text-indent: 2em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;">'
        # 学历要求
        d = degree
        b3='</span> </p> </td> </tr> <tr> <td width="280" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="text-indent: 0em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;">招聘学段</span> </p> </td> <td width="720" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="white-space: normal; text-indent: 2em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;">'
        # 招聘学段
        p = peroid
        b4='</span><br/> </p> </td> </tr> <tr> <td width="280" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="text-indent: 0em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;">年龄要求</span> </p> </td> <td width="720" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="white-space: normal; text-indent: 2em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;">'
        # 年龄要求
        a = age
        b5='</span> </p> </td> </tr> <tr> <td width="280" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="text-indent: 0em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-family: 宋体, SimSun; text-align: -webkit-center;">招聘岗位</span> </p> </td> <td width="720" valign="middle" align="center" style="padding: 0px; margin: 0px; border-style: solid; word-break: break-all; border-width: 1px;"> <p style="white-space: normal; text-indent: 2em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;">'
        # 招聘岗位人数
        n = num
        b6='</font> </p> </td> </tr> </tbody> </table> <p style="padding: 0px; font-family: &quot;Microsoft YaHei&quot;; font-size: 14px; white-space: normal; background-color: rgb(255, 255, 255); text-indent: 0em; margin-bottom: 10px; line-height: 2em; margin-top: 5px;"> <span style="font-size: 16px; font-family: 宋体, SimSun;"><strong>【公告详情】</strong></span> </p>'
        T = b1 + t + b2 + d + b3 + p + b4 + a + b5 + n + b6 
        return T

    # 文章标题
    # 加粗 顶格 宋体 16号 
    def H1(s,txt):
        b1 = ' <p style="padding: 0px; margin-top: 0px; margin-bottom: 10px; font-family: &quot; Microsoft YaHei&quot;; font-size: 14px; text-indent: 0em; white-space: normal; background-color: rgb(255, 255, 255); line-height: 2em;"> <span style="font-family: 宋体, SimSun; font-size: 16px;"> <strong>'
        t = txt
        b2 = '</strong></span> </p>'

        H1 = b1 + t +b2
        return H1 
    
    # 正文内容
    # 首行缩进 2 段前5 段后 10 
    # 宋体 16号 
    def C(s,txt):
        b1 = ' <p style="text-indent: 2em; margin-bottom: 10px; line-height: 2em;"> <span style="font-family: 宋体, SimSun; font-size: 16px;"> '
        t = txt
        b2 = '</span> </p>'

        C =  b1 + t + b2
        return  C

    # 落款内容
    # 宋体 16号 
    # 右对齐   
    def E(s,txt):
        b1 = ' <p style="text-indent: 2em; margin-bottom: 10px; line-height: 2em;text-align: right;"> <span style="font-family: 宋体, SimSun; font-size: 16px;"> '
        t = txt
        b2 = '</span> </p>'

        E =  b1 + t + b2
        return  E

    # 关键信息标红
    def C_red(s,txt):

        b1 = '<span style="font-family: 宋体, SimSun; font-size: 16px; color: #FF0000;">'
        t  = txt 
        b2 = '</span>'

        C_red = b1 + t + b2 
        return C_red

    # 文章表头
    # 提取文章关键信息
    def T(s,txt):
        pass
    
    # 是否为标题
    def is_H1(s,style,txt):
        H1=str()
        H2=str()
        #　以【一二三四五六七八九十】开头
        if style =="一、二、三、":
            H1 = len(re.findall("^[一二三四五六七八九十]",txt))
        #　以【1234567890】开头
        if style == "1、2、3、":
            H2 = len(re.findall("^[1234567890]",txt))
        if H1:
            res = True 
        elif H2:
            res = True
        else:
            res = False

        return  res

def open_txt(path):
    # 传入纯文本文档
    txt = path
    # 逐行读取 
    with open(txt,encoding='utf-8') as f:
        lines = f.readlines()
        for l in lines:
            # print(l)
            yield l
    


def main(path):

    # 传入纯文本文档
    txt = path
    # 逐行读取 
    with open(txt,encoding='utf-8') as f:
        lines = f.readlines()
        for l in lines:
            # 准备html模版
            with open("Demo.html",'a',encoding='utf-8') as h:
                All = str()
                H1 = str()
                C = str()
                T = Template() 
                # 排版
                if is_H1(l):
                    H1 = T.H1(l)                   
                    All += H1
                else:
                    C = T.C(l)
                    All += C

                #合并排版后的内容
                # 保存写入
                h.write(All)

    
if __name__ == "__main__":

    txt = "./text.txt" 
    main(txt)