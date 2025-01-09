import time
import requests
import threading
from bs4 import BeautifulSoup
import configparser
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'config.ini'), encoding='utf-8')
Web = config.get('news', 'Web')
maxMsgShow = config.getint('client', 'maxMsgShow')
linkDict = {}
threads = []
responses = []
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    }

def HandleUrl(url):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    linkDict[url].append(response)

def HandlePaperResponse():
    keyToDelete = []
    for key in linkDict.keys():
        text = ""
        value = linkDict[key]
        response = value[1]
        soup = BeautifulSoup(response.text, 'html.parser')
        
        try:
            body_div = soup.find("div", attrs={"class" : 'index_cententWrap__Jv8jK'})
            paragraphList = body_div.find_all('p')
        except AttributeError:
            keyToDelete.append(key)
            continue
        else:
            for paragraph in paragraphList:
                sentence = paragraph.get_text(strip=True)
                if sentence == "" or sentence == " " :
                    continue
                text += sentence + "\n"
            linkDict[key].append(text)
                
    for key in keyToDelete:
        print(f"删除无用链接: {key}")
        del linkDict[key]

def HandleCCTVResponse():
    keyToDelete = []
    for key in linkDict.keys():
        text = ""
        value = linkDict[key]
        response = value[1]
        soup = BeautifulSoup(response.text, 'html.parser')
        
        try:
            paragraphList = soup.find("div", attrs={"class" : 'content_area'}).find_all('p')
        except AttributeError as e:
            print(f"AttributeError {e}")
            keyToDelete.append(key)
            continue
        
        else:
            for paragraph in paragraphList:
                sentence = paragraph.get_text(strip=True)
                if sentence == "" or sentence == " " :
                    continue
                text += sentence + "\n"
            
            if text == "" or text == " " or text == "\n":
                keyToDelete.append(key)
            else:
                linkDict[key].append(text)
                
    for key in keyToDelete:
        print(f"删除无用链接: {key}")
        del linkDict[key]
        
def StartFetch():
    for url in linkDict.keys():
        thread = threading.Thread(target=HandleUrl, args=(url,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()   
    threads.clear()
          
    HandleResponse()

    for key in linkDict.keys():
        thread = threading.Thread(target=SaveToDisk, args=(key,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
        
def HandleResponse():
    match Web:
        case "澎湃网":
            HandlePaperResponse()
        case "央视网国内":
            HandleCCTVResponse()
        case "央视网国外":
            HandleCCTVResponse()
            
def SaveToDisk(key):
    if not os.path.exists(os.path.join(BASE_DIR, 'news')):
        os.mkdir(os.path.join(BASE_DIR, 'news'))
    
    filename = re.sub(r'[\\/:*?"<>|]', '', linkDict[key][0])
    with open(os.path.join(BASE_DIR, 'news', f"{filename}.txt"), 'w', encoding='utf-8') as f:
        f.write(linkDict[key][2])
    f.close()
    
def DealWebNameToUrl(web):
    match web:
        case "澎湃网":
            return 'https://tophub.app/n/wWmoO5Rd4E'
        case "央视网国内":
            return 'https://tophub.app/n/aqeEKPjv9R'
        case "央视网国外":
            return 'https://tophub.app/n/qndg1WxoLl'
def Parser(html):
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find("div", attrs={'class' : "jc-c"})
    div_tds = content_div.find_all("td", attrs={"class" : "al"}, limit=maxMsgShow)
    for div_td in div_tds:
        link_title = div_td.find("a").get_text(strip=True)
        linkDict[div_td.find("a").get('href')] = [link_title]      
 
if __name__ == "__main__":
    url = DealWebNameToUrl(Web)
    strat_time = time.time()
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    print(f"获取网页耗时: {time.time() - strat_time}")
    
    strat_time = time.time()
    Parser(response.text)
    print(f"解析界面耗时: {time.time() - strat_time}")
    
    strat_time = time.time()
    StartFetch()
    print(f"获取内容耗时: {time.time() - strat_time}")
