
import configparser
import socket
import os
from socketserver import DatagramRequestHandler

config = configparser.ConfigParser()
config.read("config.ini")

HOST = config.get("server", "HOST")
PORT = config.getint("server", "PORT")
CODING = config.get("basic", "CODING")


class Model:
    
    def __init__(self):
        self.host = HOST
        self.port = PORT 
        self.clientSocket = None
        
    def ProcessUploadFile(self, fileDirList, outputDir="output"): # 上传文件处理函数
        
        for fileDir in fileDirList:    
            content = self.GetContent(fileDir)
            dataRecv = self.TryInitSocketAndSendGetMessage(content)
            self.WriteAsFile(dataRecv, fileDirList, outputDir)

    def ProcessTextIn(self, text) -> str: # 直接输入文本处理函数
        dataRecv = self.TryInitSocketAndSendGetMessage(text)
        return dataRecv
        
    def TryInitSocketAndSendGetMessage(self, content) -> str:
        self.TryInitSocket()
        if self.clientSocket is None:
            print("Warning : Socket 被初始化为None")
            return None
        else:
            return self.TrySendGetMessage(content)
    
    def TrySendGetMessage(self, content) -> str:
        try: 
            self.clientSocket.sendall(content.encode(CODING))
            dataRecv = self.clientSocket.recv(65536).decode(CODING)
            self.clientSocket.close()
            return dataRecv
        except socket.error as se:
            print(f"Socket 发送或接受信息错误 返回NONE: {se}")
            return None
        finally:
            self.clientSocket.close()

    def WriteAsFile(self, content, fileDirList, outputDir="output"):
        if not os.path.exists(outputDir):
            os.mkdir(outputDir)
        
        for fileDir in fileDirList:
            fileName = self.GetFileName(fileDir)
            self.WriteContentToFile(content, fileName, outputDir)
            
    def GetFileName(self, fileDir):
        fileName = fileDir.split("/")[-1]
        return fileName
    
    
    def TryInitSocket(self):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((self.host, self.port))
        except socket.error as e:
            print(f"Socket 初始化错误 返回None: {e}")
            return None
    
                        
    def GetContent(self, fileDir) -> str:
        with open(fileDir, mode='r', encoding=CODING) as file:
            content = file.read() 
            file.close()
            
        return content
    
    def WriteContentToFile(self, content, fileName, outputDir):
        with open(f"{outputDir}/{fileName}.txt", mode='w', encoding=CODING) as file:
            file.write(content) 
        file.close()
    