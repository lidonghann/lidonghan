# coding=utf-8
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
web_url = 'http://www.fengup.com/phb/qiyephb/1441.html'
r = requests.get(web_url, headers=headers, verify=False)
all_td = BeautifulSoup(r.content.decode('gbk'), 'lxml').find_all(name='tr')
for tr in all_td:
    tds = tr.find_all('td')
    if len(tds) == 3:
        print tds[0].text, tds[1].text, tds[2].text
# all_td = BeautifulSoup(r.content.decode('gbk'), 'lxml').find_all(name='td')
# w = 0
# for i in all_td:
#     s = str(i)
#     a = s[4:-5]
#     w+=1
#     print a,
#     if w%3==0:
#         print
#     if w>1500:
#         if w%5==0:
#             print

