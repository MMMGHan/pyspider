# coding : UTF-8
import httplib
import requests
import time
import random
import socket
from bs4 import BeautifulSoup
def getHtml(url):
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'prov=cn010; city=010; weather_city=bj; region_ip=124.193.181.x; region_ver=1.2; ifengRotator_AP536=1; ifengRotator_iis3=4; ifengRotator_AP544=0; ifengRotator_Ap1527=0; ifengRotator_AP2712=1; ifengRotator_Ap1139=0; userid=1497490226836_2fbqxd5129; ifengRotator_ArpAdPro_1019=0; ifengRotator_iis3_c=9; ifengRotator_AP573=0; ifengRotator_AP6443=0; ifengRotator_AP940=0; ifengRotator_AP1998=0',
        'Host':'news.ifeng.com',
        'Pragma':'no-cache',
        'Referer':'http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url, headers=header, timeout=timeout)
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except httplib.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except httplib.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))

    return rep.text
def getData(html):
    bs = BeautifulSoup(html,'html.parser')
    body = bs.body
    newsLists = body.find('div', class_='newsList')
    newsUl = newsLists.findAll('ul')
    content = []
    counter = 0
    for new in newsUl:
        newTime = new.li.h4.get_text()
        newTitle = new.li.a.get_text()
        link = new.li.a
        newUrl = link['href']
        temp = [newTime[1:],newTitle[1:],newUrl[1:]]
        content.append(temp)
        counter+=1
    return content
text = getHtml('http://news.ifeng.com/listpage/11502/20170615/2/rtlist.shtml')    
content = getData(text)
print content,