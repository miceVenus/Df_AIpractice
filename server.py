import socket
import threading
import logging
import time

# 服务器的本地IP地址
HOST = '0.0.0.0'
 
# 服务器的端口号
PORT = 12345 
CODING= "utf-8"
MAX_CONNECTIONS = 3

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
            except Exception as ret:
                time.sleep(0.01)
            else:
                self.clientQueue.append((clientSocket, clientAddress))
                logging.info(f"Socket服务端与IP地址为{clientAddress}的客户端连接")
            
            for CS, CA in self.clientQueue:
                clientTh = threading.Thread(target=self.DealRecvAndSend, args=(CS, CA))
                clientTh.start()


    def DealRecvAndSend(self, clientSocket, clientAddress):
        try:
            dataRecv = clientSocket.recv(65536).decode(CODING)
            dataHandled = self.DataProcess(dataRecv)
            clientSocket.sendall(dataHandled.encode(CODING))
        except Exception as e:
            logging.error(f"Error receiving or sending data : {e}")
        finally:
            self.clientQueue.remove((clientSocket, clientAddress))
            clientSocket.close()
        
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
                    
    #todo:把text传给模型处理，然后返回处理结果
    def DataProcess(self, text):
        pass 
        data = "什么也没做"
        
        return data
    
if __name__ == "__main__":
    Server = Server()