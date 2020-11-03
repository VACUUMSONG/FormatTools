#!/bin/python
#***********************************************
#
#      Filename: 123.py
#
#        Author:
#   Description: ---
#        Create: 2020-05-25 14:16:14
# Last Modified: 2020-06-03 14:48:39
##***********************************************

# 大致思路
#***********************************************
# 1、逐行读取文本文档
#       【0】已删除格式的纯文本文档
# 2、简单识别含有某些关键字的行
#      【0】时间：年 月 日 截止等
#      【1】学历：大专 本科 硕士  研究生等
#      【2】岗位：\d*人 \d*名
#      【3】学段：中学 小学 幼儿园
#      【4】年龄：\d*周岁以下
# 3、进一步信息筛选
#      【0】输出html格式的文本文档  
#      【1】直接复制到windows剪切板
# 4、复制文字到后台编辑器
# 5、提示编辑人员检查图片、表格、附件等细节
#      【0】表格、图片格式检查
#      【1】提示下载附件并上传到自己的服务器
#**********************************************************************************************
import re

class Header:

    def RE(s):
        # 报名时间
        l_time   = list()
        dic_time = dict()
        RE_T = str()
        # 学历要求
        l_degree = list()
        F_degree = list()
        RE_D = str()
        # 招聘学段
        l_period = list()
        F_period = list()
        RE_P = str()
        # 年龄要求
        l_age = list()
        F_age = list()
        RE_A = str()
        # 岗位要求
        l_num = list()
        F_num = list()
        RE_N = str()


        with open('123.txt','r',encoding="utf-8") as f:
            lines = f.readlines()
            # 逐行读取文件 
            for l in lines:
                # 报名时间
                time0 = re.findall(".*报名时间.*月.*日",l)
                time1 = re.findall(".*月.*日.*至.*",l)
                time2 = re.findall(".*月.*日截止",l)
                time3 = re.findall(".*至.*年.*月.*日",l)
                time4 = re.findall(".*月.*日前",l)
                time5 = re.findall(".*招满为止",l)
                time6 = re.findall(".*报考时间.*月.*日",l)
                time7 = re.findall(".*招聘时间.*月.*日",l)
                if time0 not in l_time:
                    l_time.extend(time0) 
                if time1 not in l_time:
                    l_time.extend(time1) 
                if time2 not in l_time:
                    l_time.extend(time2) 
                if time3 not in l_time:
                    l_time.extend(time3) 
                if time4 not in l_time:
                    l_time.extend(time4) 
                if time5 not in l_time:
                    l_time.extend(time5) 
                if time6 not in l_time:
                    l_time.extend(time6) 
                if time7 not in l_time:
                    l_time.extend(time7) 

                # 学历要求
                degree0 = re.findall(".*大专.*",l)
                degree1 = re.findall(".*专科.*",l)
                degree2 = re.findall(".*本科.*",l)
                degree3 = re.findall(".*硕士.*",l)
                degree4 = re.findall(".*博士.*",l)
                degree5 = re.findall(".*研究生.*",l)
                degree6 = re.findall(".*及以上学历",l)
                # degree
                if degree0:
                    l_degree.append(degree0) 
                if degree1:
                    l_degree.append(degree1) 
                if degree2:
                    l_degree.append(degree2) 
                if degree3:
                    l_degree.append(degree3) 
                if degree4:
                    l_degree.append(degree4) 
                if degree5:
                    l_degree.append(degree5) 
                if degree6:
                    l_degree.append(degree6) 

                # 学段
                period0 = re.findall(".*幼儿园.*",l)
                period1 = re.findall(".*小学.*",l)
                period2 = re.findall(".*中学.*",l)
                period3 = re.findall(".*中小学.*",l)
                period4 = re.findall(".*大学.*",l)
                period5 = re.findall(".*学院.*",l)
                # period
                if period0:
                    l_period.append(period0) 
                if period1:
                    l_period.append(period1) 
                if period2:
                    l_period.append(period2) 
                if period3:
                    l_period.append(period3) 
                if period4:
                    l_period.append(period4) 
                if period5:
                    l_period.append(period5) 

                # 年龄要求
                age0 = re.findall("\d*周岁以下.*",l)
                age1 = re.findall("\d*年龄.*",l)
                if age0:
                    l_age.append(age0) 
                if age1:
                    l_age.append(age1) 

                # 招聘岗位
                num0 = re.findall(".*\d+名",l)
                num1 = re.findall(".*\d+人",l)
                if num0:
                    l_num.append(num0) 
                if num1:
                    l_num.append(num1) 

            # 报名时间
            # print("______________") 
            if l_time:
                F_ti = re.findall("\d*月.*日.*",min(l_time,key=len))
                if F_ti:
                    try:
                        # print("报名时间："+min(F_ti,key=len)) 
                        RE_T= (min(F_ti,key=len)) 
                    except:
                        pass
                else:
                    # print(min(l_time,key = len))
                    RE_T= (min(l_time,key = len))
            else:            
                # print("报名时间：详见公告")
                RE_T= ("详见公告")


            # 招聘岗位
            # print("______________") 
            if l_degree:
                res_degree = min(l_degree[0])
                F_de0 = re.findall("专科",res_degree)
                F_de1 = re.findall("大专",res_degree)
                F_de2 = re.findall("本科",res_degree)
                F_de3 = re.findall("硕士",res_degree)
                F_de4 = re.findall("博士",res_degree)
                F_de5 = re.findall("研究生",res_degree)

                if F_de0:
                    F_degree.append(F_de0)
                if F_de1:
                    F_degree.append(F_de1)
                elif F_de2:
                    F_degree.append(F_de2)
                elif F_de3:
                    F_degree.append(F_de3)
                elif F_de4:
                    F_degree.append(F_de4)
                elif F_de5:
                    F_degree.append(F_de5)
                
            if F_degree:
                try:
                    # print("学历要求:"+min(F_degree)[0]+"及以上学历")
                    RE_D= (min(F_degree)[0]+"及以上学历")
                except:
                    pass
            else:            
                # print("学历要求：详见公告")
                RE_D= ("详见公告")

            # 招聘学段
            # print("______________") 
            if l_period:
                res_period = min(l_period[0])
                F_pr0 = re.findall("幼儿园",res_period)
                F_pr1 = re.findall("中小学",res_period)
                F_pr2 = re.findall("中学",res_period)
                F_pr3 = re.findall("小学",res_period)
                F_pr4 = re.findall("大学",res_period)
                F_pr5 = re.findall("学院",res_period)

                if F_pr0:
                    F_period.append(F_pr0)
                if F_pr1:
                    F_period.append(F_pr1)
                elif F_pr2:
                    F_period.append(F_pr2)
                elif F_pr3:
                    F_period.append(F_pr3)
                elif F_pr4:
                    F_period.append(F_pr4)
                elif F_pr5:
                    F_period.append(F_pr4)

            if F_period:
                try:
                    # print("招聘学段:"+min(F_period)[0])
                    RE_P= (min(F_period)[0])
                except:
                    pass
            else:            
                # print("招聘学段：详见公告")
                RE_P= ("详见公告")

            # 年龄要求
            # print("______________") 
            if l_age:
                res_age = min(l_age[0])
                F_age0 = re.findall("\d*周岁以下",res_age)
                F_age1 = re.findall("\d*周岁",res_age)

                if F_age0:
                    F_age.append(F_age0)
                elif F_age1:
                    F_age.append(F_age1)
            if F_age:
                try:
                    # print("年龄要求:"+min(F_age)[0])
                    RE_A= (min(F_age)[0])
                except:
                    pass
            else:            
                # print("年龄要求：详见公告")
                RE_A= ("详见公告")

            # 招聘人数
            # print("______________") 
            if l_num:
                res_num = min(l_num[0])
                F_num0 = re.findall(".*\d+名.*",res_num)
                F_num1 = re.findall(".*\d+人.*",res_num)

                if F_num0:
                    F_num.append(F_num0)
                elif F_num1:
                    F_num.append(F_num1)
            if F_num:
                try:
                    # print("招聘岗位:"+min(F_num)[0])
                    RE_N= (min(F_num)[0])
                except:
                    pass
            else:            
                # print("招聘岗位：详见公告")
                RE_N= ("详见公告")

        # 返回匹配的结果
        # 分别为时间，学历，学段，年龄，人数
        return RE_T,RE_D,RE_P,RE_A,RE_N