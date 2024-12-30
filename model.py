
from ast import arg
import socket
import os
from socketserver import DatagramRequestHandler
HOST = "192.168.120.183"
PROT = 12345
CODING = "utf-8"


class Model:
    
    def __init__(self):
        self.host = HOST # 服务器的ip地址 记得修改
        self.port = PROT # 服务器的端口号 记得修改
        
    def ProcessUploadFile(self, fileDirList, outputDir="output"): # 上传文件处理函数
        
        for fileDir in fileDirList:    
            content = self.GetContent(fileDir)
            dataRecv = self.TryInitSocketAndSendContentAndGetMessage(content)
            self.WriteAsFile(dataRecv, fileDirList, outputDir)

    def ProcessTextIn(self, text, *args) -> str: # 直接输入文本处理函数
        dataRecv = self.TryInitSocketAndSendContentAndGetMessage(text)
        return dataRecv
        
    def TryInitSocketAndSendContentAndGetMessage(self, content) -> str:
        s = self.InitSocket()
        try: 
            s.sendall(content.encode(CODING))
            dataRecv = s.recv(65536).decode(CODING)
            return dataRecv
        
        except socket.error as se:
            print(f"Socket 错误: {se}")
        
        except Exception as e:
            print(f"错误: {e}")
                    
        finally:
                if s is not None:
                    s.close()


    def WriteAsFile(self, content, fileDirList, outputDir="output"):
        if not os.path.exists(outputDir):
            os.mkdir(outputDir)
        
        for fileDir in fileDirList:
            fileName = self.GetFileName(fileDir)
            self.WriteContentToFile(content, fileName, outputDir)
            
    def GetFileName(self, fileDir):
        fileName = fileDir.split("/")[-1]
        return fileName
    
    
    def InitSocket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            return s
        
        except socket.error as e:
            print(f"Socket 错误: {e}")
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
    