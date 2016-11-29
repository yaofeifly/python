#!/usr/bin/env python27
# coding=utf-8
from bs4 import BeautifulSoup
import urllib
import os


def get_img(url):
    # os.mkdir(r'photos')
    finally_path = os.path.join(r'photos')
    if os.path.exists(finally_path):
        pass
    else:
        os.makedirs(finally_path)
    t = 1  # 记录图片张数
    html_doc = urllib.urlopen(url)
    soup = BeautifulSoup(html_doc, "lxml")
    # print soup.find_all('img')
    for myimg in soup.find_all('img'):
        pic_name = str(t) + '.jpg'
        img_src = myimg.get('src')
        dirss = os.path.join(finally_path, pic_name)
        new_file = open(dirss, "wb")
        if "http://" in img_src:
            f = urllib.urlopen(img_src)
        else:
            f = urllib.urlopen("http://www.nyist.net/"+img_src)
        f = f.read()
        new_file.write(f)
        print("Success!" + img_src)
        t += 1
        new_file.close()
    print("Exit")

if __name__ == '__main__':
    get_img("http://www.nyist.net/")
