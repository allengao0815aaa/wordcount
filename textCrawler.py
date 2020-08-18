#-*- coding:utf-8 -*-
# author:高梓瑞
# datetime:2019-12-28 22:40
# software: PyCharm
# environment:
# packages:BeautifulSoup；requests

import requests
from bs4 import BeautifulSoup

urls = ['https://www.globaltimes.cn/content/','.shtml']


for i in range(10000):

    k = 1165772;

    r = requests.get(urls[0] + str(k + i) + urls[1], timeout = 30)
    #爬取环球网英文版10000个新闻页面

    soup = BeautifulSoup(r.text, 'html.parser')

    #爬取text并剔除js内容
    for script in soup(["script", "style"]):
        script.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines
    	for phrase in line.split(" "))
        #text = '\n'.join(chunk for chunk in chunks if chunk)

    #print(text)

    file=open('result.txt',"a")
    for i in range (len(text)):
        file.write(text[i])
    file.close()





