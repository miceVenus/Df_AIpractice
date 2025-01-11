import socket
import threading
import logging
import time

# 服务器的本地IP地址
HOST = '0.0.0.0'
 
# 服务器的端口号
PORT = 12345 
CODING= "utf-8"
MAX_CONNECTIONS = 6

class Server:
    def __init__(self, host=HOST, port=PORT, maxConnection=MAX_CONNECTIONS):
        self.host = host
        self.port = port
        self.serverSocket = None
        self.maxConnection = maxConnection
        self.serverTh = None
        self.clientQueue = list()
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.StartServer()
        
    def HandleClient(self):
        while True:
            try:
                clientSocket, clientAddress = self.serverSocket.accept()
                logging.info(f"accept, clientSocket:{clientSocket}, Address:{clientAddress}")
                clientSocket.setblocking(True)
            except Exception as ret:
                time.sleep(0.01)
            else:
                if clientSocket and clientAddress:
                    self.clientQueue.append((clientSocket, clientAddress))
                logging.info(f"Socket服务端与IP地址为{clientAddress}的客户端连接")
            
                clientTh = threading.Thread(target=self.DealRecvAndSend, args=(clientSocket, clientAddress))
                clientTh.start()


    def DealRecvAndSend(self, clientSocket, clientAddress):
        try:
            dataRecv = clientSocket.recv(65536).decode(CODING)
            logging.info(f"接收到来自{clientSocket}的数据:\n {dataRecv}")
            dataHandled = self.DataProcess(dataRecv)
            logging.info(f"处理后的数据:\n {dataHandled}")
            clientSocket.sendall(dataHandled.encode(CODING))
        
        except socket.error as e:
                logging.error(f"Error receiving or sending data : {e}")
            
        finally:
            if (clientSocket, clientAddress) in self.clientQueue:
                self.clientQueue.remove((clientSocket, clientAddress))
            
            try:
                clientSocket.close()
            except Exception as e:
                logging.error(f"Error closing socket: {e}")
        
    def StartServer(self):
        try :
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.serverSocket.setblocking(False)
            self.serverSocket.bind((self.host, self.port))
        
        except socket.error as e:
            logging.error(f"服务器创建socket失败: {e}")
        
        else:
            self.serverSocket.listen(self.maxConnection)
            self.serverTh = threading.Thread(target=self.HandleClient)
            self.serverTh.start()
            logging.info(f"服务器启动，监听端口 {self.port}...")
                    
    def DataProcess(self, text: str):
        modelType, content = tuple(text.split("?", maxsplit=1))
        if modelType == "MT5文本摘要模型":
            return modelType + " " +self.TextModel(content)
        else:
            return modelType + " " + self.DialogModel(content)
    
    
    #todo:把text传给模型处理，然后返回处理结果
    def TextModel(self, text):
        time.sleep(1)
        data = str(randint(0, 100))
        return data
    
    def DialogModel(self, text):
        time.sleep(2)
        data = "什么也没做"
        return data
    
    
if __name__ == "__main__":
    Server = Server()