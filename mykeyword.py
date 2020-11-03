#!/bin/python
#***********************************************
#
#      Filename: KeyWord.py
#
#        Author:   VACUUMSONG@163.com
#   Description: ---
#        Create: 2020-07-05 08:50:22
# Last Modified: 2020-07-06 17:36:35
#***********************************************
from jieba.analyse import *
from pkg_resources import *

class Keyword:      

    def get_Keywords_IFIDF(s):
        k1 = list()
        with open('123.txt',encoding='utf-8') as f:
            data = f.read()
        # print("************TF-IDF******************")
        for keyword, weight in extract_tags(data,topK=12, withWeight=True):
            # print('%s %s' % (keyword, weight))
            k1.append(keyword)
        return k1

    def get_Keywords_TextRank(s):
        k2 = list()
        with open('123.txt',encoding='utf-8') as f:
            data = f.read()
        # print("***********TextRank******************")   
        for keyword, weight in textrank(data,topK=20, withWeight=True):
            print('%s %s' % (keyword, weight))
            k2.append(keyword)

        return k2

    def get_intersection(s,k1,k2):
        intersection =  (list(set(k1).intersection(set(k2)))) 
        # print (intersection)
        return intersection

    def get_keywords(s):
        kw = str()
        K = Keyword()
        # 获取文本
        k1 = K.get_Keywords_IFIDF()
        k2 = K.get_Keywords_TextRank()
        kws = K.get_intersection(k1,k2)
        for k in kws[:10]:
            kw += "     " + k + " \n\n" 
        return kw 
