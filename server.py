import socket

class MouseListenerServer:
    def __init__(self, host = 'localhost', port = 5050):
        self.port = port
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def __process_data(self, data):
         print( "Recieve message {0}".format(data.decode()))

    def start(self):
        self.socket.bind((self.host, self.port))
        while True:
                data, addr = self.socket.recvfrom(1024)
                self.__process_data(data)


if __name__ == '__main__':
    client = MouseListenerServer()
    client.start() 

