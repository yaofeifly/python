__author__ = 'feifei'
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import os


def get_books(url):
    # 设置中文字符正确显示
    reload(sys)                         # 2
    sys.setdefaultencoding('utf-8')
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    rep = requests.get(url, headers=header)
    # 设置响应内容编码格式
    rep.encoding = 'utf-8'
    soup = BeautifulSoup(rep.text, "lxml")
    # 获取《西游记》文章的所有目录章节
    mulu_list = soup.find_all(id="mulu")
    # 将BeautifulSoup获取的目录以字符串的形式拼接起来
    values = ','.join(str(item) for item in mulu_list)
    soup2 = BeautifulSoup(values, 'lxml')
    # 利用BeautifulSoup爬取所有的章节
    soup2 = soup2.ul
    # 获取书名
    book_name = soup.h1.string
    # 以书名在当前路径创建文件夹
    finally_path = os.path.join(book_name)
    if os.path.exists(finally_path):
        pass
    else:
        os.makedirs(finally_path)
    bookMenu = []
    bookMenuUrl = []
    urlBegin = "http://www.shicimingju.com"
    # 获取所有章节的url并做拼接
    for i in range(1, len(soup2.contents)-1):
        bookMenu.append(soup2.contents[i].string)
        bookMenuUrl.append(soup2.contents[i].a['href'])
    # 爬取每一章节的内容
    for i in range(0, len(bookMenuUrl)):
        req = requests.get(urlBegin + bookMenuUrl[i])
        req.encoding = 'utf-8'
        chaptercode = req.text
        chapterSoup = BeautifulSoup(chaptercode, 'lxml')
        chapterResult = chapterSoup.find_all(id='con2')
        chapterResult = ','.join(str(v) for v in chapterResult)
        chapterSoup2 = BeautifulSoup(chapterResult, 'lxml')
        chapterSoup2 = chapterSoup2.find_all('p')
        # 在书名文件夹下以章节名作为文件名创建文件
        file_path = os.path.join(finally_path, bookMenu[i]+'.txt')
        with open(file_path, 'w') as f:
            # 将页面中每一章节具体内容存入文件中
            for j in chapterSoup2:
                if j.string is not None:
                    f.write(j.string + '\n')

if __name__ == '__main__':
    get_books("http://www.shicimingju.com/book/xiyouji.html")
