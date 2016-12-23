# -*- coding: utf-8 -*-
__author__ = 'feifei'
import requests
from bs4 import BeautifulSoup
import sys


def get_content(url, page):
    reload(sys)                         # 2
    sys.setdefaultencoding('utf-8')
    problem_list_all = set()
    for i in range(1, page+1):
        header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
        }
        rep = requests.get(url+'?page='+str(i), headers=header)
        rep.encoding = 'utf-8'
        soup = BeautifulSoup(rep.text, "lxml")
        problem_list = soup.find_all('td', 'probname tal')

        for item in problem_list:
            problem_list_all.add(item.get_text())
    with open('problem.txt', 'wb') as f:
        for detail in problem_list_all:
            f.write(detail+'\n')
if __name__ == '__main__':
    get_content("http://acm.nyist.edu.cn/JudgeOnline/problemset.php", 12)


