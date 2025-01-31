import configparser
import socket
import os
import shutil
import time
from urllib import response
import requests
import threading
from bs4 import BeautifulSoup
import re


class Model:

    def __init__(self):
        self.config = Model.Config()
        self.scraper = Model.Scraper(self)
        self.clientSocket = None
        self.modelType = None
    
    # 上传文件处理函数
    def ProcessUploadFile(self, fileDirList, modelType): 
        self.modelType = modelType
        for fileDir in fileDirList:    
            content = self.GetContent(fileDir)
            dataRecv = self.TryInitSocketAndSendGetMessage(content)
            self.WriteAsFile(dataRecv, fileDir)
            
    # 直接输入文本处理函数
    def ProcessTextIn(self, text, modelType) -> str:
        self.modelType = modelType
        dataRecv = self.TryInitSocketAndSendGetMessage(text)
        return dataRecv
    
    def ProcessHTML(self, fileList, modelType) -> list:
        self.modelType = modelType
        dataRecvList = []
        for file in fileList:
            fileDir = os.path.join(self.config.basicDir, 'news', file+'.txt')    
            content = self.GetContent(fileDir)
            dataRecv = self.TryInitSocketAndSendGetMessage(content)
            dataRecvList.append(dataRecv)
        return dataRecvList
        
    
    def TryInitSocketAndSendGetMessage(self, content) -> str:
        self.TryInitSocket()
        if self.clientSocket is None:
            print("Warning : Socket 被初始化为None")
            return None
        else:
            return self.TrySendGetMessage(content)
    
    # 传递数据构成：ModelType?text在服务端以字符串操作进行分离 
    def TrySendGetMessage(self, text) -> str:
        try: 
            content = self.modelType + "?" + text
            self.clientSocket.sendall(content.encode(self.config.coding))
            print(f"发送{self.config.host}数据:\n {content}")
            dataRecv = self.clientSocket.recv(65536).decode(self.config.coding)
            print(f"接收到来自{self.config.host}的数据:\n {dataRecv}")
            self.clientSocket.close()
            return dataRecv
        except socket.error as se:
            print(f"Socket 发送或接受信息错误 返回NONE: {se}")
            return None
        finally:
            self.clientSocket.close()

    def WriteAsFile(self, content, fileDir):
        if not os.path.exists(self.config.outputDir):
            os.mkdir(self.config.outputDir)
        fileName = self.GetFileName(fileDir)
        self.WriteContentToFile(content, fileName)
            
    def GetFileName(self, fileDir):
        fileName = fileDir.split("/")[-1]
        return fileName
    
    def TryInitSocket(self):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((self.config.host, self.config.port))
        except socket.error as e:
            print(f"Socket 初始化错误 返回None: {e}")
            return None
    
                        
    def GetContent(self, fileDir) -> str:
        with open(fileDir, mode='r', encoding=self.config.coding) as file:
            content = file.read() 
            file.close()
            
        return content
    
    def WriteContentToFile(self, content, fileName):
        with open(f"{self.config.outputDir}/{fileName}.txt", mode='w', encoding=self.config.coding) as file:
            file.write(content) 
        file.close()
    
    def ClearResource(self):
        newsDir = os.path.join(self.config.basicDir, 'news')
        if os.path.exists(newsDir):
            shutil.rmtree(newsDir)
            
    class Scraper:
        def __init__(self, outerInstance : 'Model'):
            self.config = outerInstance.config
            self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}
            self.linkDict = {}
            self.threads = []
            self.responseCache = self.GetResponseCached()
            self.GetLinkDictCached()
        
        
        def StartFetch(self):
            for url in self.linkDict.keys():
                thread = threading.Thread(target=self.HandleUrl, args=(url,))
                thread.start()
                self.threads.append(thread)
                
            for thread in self.threads:
                thread.join()   
            self.threads.clear()
                
            self.HandleResponse()

            for key in self.linkDict.keys():
                thread = threading.Thread(target=self.SaveToDisk, args=(key,))
                thread.start()
                self.threads.append(thread)
            
            for thread in self.threads:
                thread.join()
                
        def HandleUrl(self, url):
            response = self.GetResponse(url)
            self.linkDict[url].append(response)    
            
        def HandleResponse(self):
            keyToDelete = []
            for key in self.linkDict.keys():
                text = ""
                try:
                    paragraphList = self.GetParasFromWeb(key)
                except AttributeError:
                    keyToDelete.append(key)
                    continue
                else:
                    for paragraph in paragraphList:
                        sentence = paragraph.get_text(strip=True)
                        if sentence == "" or sentence == " " :
                            continue
                        text += sentence + "\n"
                    self.linkDict[key].append(text)
                        
            for key in keyToDelete:
                print(f"删除无用链接: {key}")
                del self.linkDict[key]
                
        def SaveToDisk(self, key):
            if not os.path.exists(os.path.join(self.config.basicDir, 'news')):
                os.mkdir(os.path.join(self.config.basicDir, 'news'))
            
            filename = re.sub(r'[\\/:*?"<>|]', '', self.linkDict[key][0])
            with open(os.path.join(self.config.basicDir, 'news', f"{filename}.txt"), 'w', encoding='utf-8') as f:
                f.write(self.linkDict[key][2])
            f.close()
            
        def GetParasFromWeb(self, key) -> list:
            response = self.linkDict[key][1]
            soup = BeautifulSoup(response.text, 'html.parser')
            match self.config.web:
                case "澎湃网":
                    return soup.find("div", attrs={"class" : 'index_cententWrap__Jv8jK'}).find_all('p')
                case "央视网国内":
                    return soup.find("div", attrs={"class" : 'content_area'}).find_all('p')
                case "央视网国外":
                    return soup.find("div", attrs={"class" : 'content_area'}).find_all('p')
                case _:
                    return []  
            
        def GetUrl(self, web):
            match web:
                case "澎湃网":
                    return 'https://tophub.app/n/wWmoO5Rd4E'
                case "央视网国内":
                    return 'https://tophub.app/n/aqeEKPjv9R'
                case "央视网国外":
                    return 'https://tophub.app/n/qndg1WxoLl'
                case _:
                    return ''
                
        def Parser(self, html):
            soup = BeautifulSoup(html, 'html.parser')
            content_div = soup.find("div", attrs={'class' : "jc-c"})
            div_tds = content_div.find_all("td", attrs={"class" : "al"}, limit=self.config.maxMsgShow)
            for div_td in div_tds:
                link_title = div_td.find("a").get_text(strip=True)
                self.linkDict[div_td.find("a").get('href')] = [link_title]
                
        def GetResponseCached(self):
            url = self.GetUrl(self.config.web)
            return self.GetResponse(url)
        
        def GetLinkDictCached(self):
            self.run()
                    
        def GetResponse(self, url):
            response = requests.get(url=url, headers=self.headers)
            response.encoding = self.config.coding
            return response
        
        def run(self):
            print("开始爬取")
            response = self.responseCache
            
            strat_time = time.time()
            self.Parser(response.text)
            print(f"解析界面耗时: {time.time() - strat_time}")
            
            strat_time = time.time()
            self.StartFetch()
            print(f"获取内容耗时: {time.time() - strat_time}")
            
    class Config:
        def __init__(self):
            self.config = configparser.ConfigParser()
            self.basicDir = os.path.dirname(os.path.abspath(__file__))
            self.config.read(os.path.join(self.basicDir, "config.ini"), encoding="utf-8")
            
            self.host = self.config.get("server", "HOST")
            self.port = self.config.getint("server", "PORT")
            self.coding = self.config.get("basic", "CODING")
            self.outputDir = self.config.get("basic", "OUTPUT_DIR")
            if self.outputDir is None:
                self.outputDir = "./output"
                
            self.web = self.config.get('scraper', 'WEB')
            self.maxMsgShow = self.config.getint('scraper', 'maxMsgShow')
            
            self.default_host = self.config.get("default", "default_host")
            self.default_port = self.config.getint("default", "default_port")
            self.default_coding = self.config.get("default", "default_coding")
            self.default_output_dir = self.config.get("default", "default_output_dir")
            self.default_web = self.config.get("default", "default_web")
            self.default_maxMsgShow = self.config.getint("default", "default_maxmsgshow")
        
        def GetConfig(self):
            return (self.host, str(self.port), self.coding, self.outputDir, self.web, str(self.maxMsgShow))

        def WriteConfig(self, settingTuple):
            self.host, port, self.coding, self.outputDir, self.web, maxMsgShow = settingTuple
            self.port = int(port)
            self.maxMsgShow = int(maxMsgShow)
            
            self.config.set("server", "HOST", self.host)
            self.config.set("server", "PORT", str(self.port))
            self.config.set("basic", "CODING", self.coding)
            self.config.set("basic", "OUTPUT_DIR", self.outputDir)
            self.config.set("scraper", "web", self.web)
            self.config.set("scraper", "maxmsgshow", str(self.maxMsgShow))
            
            with open(os.path.join(self.basicDir, "config.ini"), mode='w', encoding=self.coding) as file:
                self.config.write(file)
            file.close()
            
        def GetDefaultConfig(self):
            return (self.default_host, str(self.default_port), self.default_coding, self.default_output_dir, 
                    self.default_web, str(self.default_maxMsgShow))
    