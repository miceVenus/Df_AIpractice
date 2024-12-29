import socket
import threading
import logging
HOST = '0.0.0.0' # 服务器的本地IP地址
PORT = 12345 # 服务器的端口号
CODING= "utf-8"

class Server:
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        self.StartServer()
        
    def HandleClient(self, clientSocket, clientAddress):
        try:
            logging.info(f"连接来自 {clientAddress}")
            dataRecv = clientSocket.recv(65536).decode(CODING)
            logging.info(f"接收到数据")
            dataHandled = self.DataProcess(dataRecv)
            clientSocket.sendall(dataHandled.encode(CODING))
            
        except Exception as e:
            logging.error(f"处理数据时发生错误: {e}")
            
        finally:
            clientSocket.close()
            logging.info(f"连接 {clientAddress} 已关闭")
            
        
    def StartServer(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
            serverSocket.bind((self.host, self.port))
            serverSocket.listen(5)
            print(f"服务器启动，监听端口 {self.port}...")
            
            while True:
                try:
                    clientSocket, clientAddress = serverSocket.accept()
                    clientHandler = threading.Thread(target=self.HandleClient, args=(clientSocket, clientAddress))
                    clientHandler.start()
                    
                except Exception as e:
                    logging.error(f"处理客户端连接时发生错误: {e}")

    def DataProcess(self, text):
        pass #todo:把text传给模型处理，然后返回处理结果
        data = "什么也没做"
        
        return data
    
if __name__ == "__main__":
    Server = Server()