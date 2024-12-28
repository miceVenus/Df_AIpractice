
import socket
import os

class Model:
    
    def __init__(self):
        self.host = "192.168.120.183" # 服务器的ip地址 记得修改
        self.port = 12345
        self.dataSed = ""
        
    def InitSocket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            return s
        
        except socket.error as e:
            print(f"Socket 错误: {e}")
            return None
    
    def ProcessUploadFile(self, fileDirList):
        for fileDir in fileDirList:    
            with open(fileDir, mode='r', encoding='utf-8') as file:
                self.dataSed = file.read() 
            file.close()
            
            try: 
                s = self.InitSocket()
                if s is None:
                    print("Socket 初始化失败")
                    return
                s.sendall(self.dataSed.encode("utf-8"))
                dataRecv = s.recv(65536).decode("utf-8")
                self.WriteAsFile(dataRecv, fileDirList)
                print('Received')
                
            except socket.error as e:
                print(f"Socket 错误: {e}")
                
            finally:
                if s is not None:
                    s.close()
                
                
    def ProcessTextIn(self, text) -> str:
        s = self.InitSocket()
        if s is None:
            print("Socket 初始化失败")
            return ""
        
        try:
            s.sendall(text.encode("utf-8"))
            
            dataRecv = s.recv(65536).decode("utf-8")
            print('Received') 
            return dataRecv
        
        except Exception as e:
            print(f"Socket 错误: {e}")
            return ""
            
        finally:
            if s is not None:
                s.close()

    def WriteAsFile(self, text, fileDirList):
        if not os.path.exists("output"):
            os.mkdir("output")
        
        for fileDir in fileDirList:
            fileName = fileDir.split("/")[-1]
            with open(f"output/{fileName}.txt", mode='w', encoding='utf-8') as file:
                file.write(text) 
            file.close()