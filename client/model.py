
import configparser
from email.policy import default
import socket
import os

BASIC_DIR = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()

config.read(os.path.join(BASIC_DIR, "config.ini"))

HOST = config.get("server", "HOST")
PORT = config.getint("server", "PORT")
CODING = config.get("basic", "CODING")
OUTPUT_DIR = config.get("basic", "OUTPUT_DIR")
if OUTPUT_DIR == "None":
    OUTPUT_DIR = "output"

default_host = config.get("default", "default_host")
default_port = config.getint("default", "default_port")
default_coding = config.get("default", "default_coding")
default_output_dir = config.get("default", "default_output_dir")

class Model:
    
    def __init__(self):
        self.host = HOST
        self.port = PORT 
        self.outputDir = OUTPUT_DIR
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
    
    def ProcessHTML(self, html) -> str:
        # convert html to text
        pass
        dataRecv = self.TryInitSocketAndSendGetMessage(html)
        return dataRecv
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
            self.clientSocket.sendall(content.encode(CODING))
            dataRecv = self.clientSocket.recv(65536).decode(CODING)
            print(f"接收到来自{self.host}的数据:\n {dataRecv}")
            self.clientSocket.close()
            return dataRecv
        except socket.error as se:
            print(f"Socket 发送或接受信息错误 返回NONE: {se}")
            return None
        finally:
            self.clientSocket.close()

    def WriteAsFile(self, content, fileDir):
        if not os.path.exists(self.outputDir):
            os.mkdir(self.outputDir)
        fileName = self.GetFileName(fileDir)
        self.WriteContentToFile(content, fileName)
            
    def GetFileName(self, fileDir):
        fileName = fileDir.split("/")[-1]
        return fileName
    
    def GetConfig(self):
        
        return (self.host, str(self.port), CODING, self.outputDir)
    
    def WriteConfig(self, settingTuple):
        self.host, port, CODING, self.outputDir = settingTuple
        self.port = int(port)
        
        config.set("server", "HOST", self.host)
        config.set("server", "PORT", str(self.port))
        config.set("basic", "CODING", CODING)
        config.set("basic", "OUTPUT_DIR", self.outputDir)
        
        with open(os.path.join(BASIC_DIR, "config.ini"), mode='w') as file:
            config.write(file)
        file.close()
    
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
    
    def GetDefaultConfig(self):
        return (default_host, str(default_port), default_coding, default_output_dir)
    
    def WriteContentToFile(self, content, fileName):
        with open(f"{self.outputDir}/{fileName}.txt", mode='w', encoding=CODING) as file:
            file.write(content) 
        file.close()
    