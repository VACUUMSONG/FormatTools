#!/bin/python
#***********************************************
#
#      Filename: format.py
#
#        Author:
#   Description: ---
#        Create: 2020-05-30 12:32:44
# Last Modified: 2020-05-30 12:32:47
#***********************************************
import  pandas as pd 
import  requests 
from   lxml import etree

headers = {
    "user-agent":"mozilla/5.0 (macintosh; intel mac os x 10_7_0) applewebkit/535.11 (khtml, like gecko) chrome/17.0.963.56 safari/535.11"
}

# 中公网址
def get_vsgs_url(website):

    if website == "安徽":
        url = "http://ah.zgjsks.com/html/jiaozhao/ksgg/" 
    if website == "广东":
        url = "http://gd.zgjsks.com/html/jiaozhao/ksgg/" 
    if website == "福建":
        url = "http://fj.zgjsks.com/html/jiaozhao/ksgg/" 
    
    return url 

# 获取中公 最新公告
def get_vsgs_title(url):
    res = requests.get(url,headers)
    # 声明网页编码
    res.encoding = "gb2312"
    txt = res.text

    html = etree.HTML(txt)
    
    title_txt = html.xpath('//div[@class="notice_box_main"]/ul/li/span/font/../../p/a/text()')
    title_url = html.xpath('//div[@class="notice_box_main"]/ul/li/span/font/../../p/a/@href')
    # 只选择日期标红的title
    date = html.xpath('//div[@class="notice_box_main"]/ul/li/span/font/text()')

    return title_txt,title_url,date

def get_vsgs_txt(url):

    res = requests.get(url,headers)
    # 声明网页编码
    res.encoding = "gb2312"
    txt = res.text

    html = etree.HTML(txt)
    txt = html.xpath('//div/p/text()')

    return txt 

# 标题格式
def F_Title(str):
    
def main():
    
    website = "安徽"

    url = get_vsgs_url(website)
    txt_title , txt_url,txt_date = get_vsgs_title(url)
    print(txt_url[0])
    txt =  get_vsgs_txt(txt_url[0]) 

    for i in txt:
        print(i)



if __name__ == "__main__":
    main()