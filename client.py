from pynput import mouse
import socket

class MouseListenerClient:
    def __init__(self, host: str = 'localhost', port: int = 5050):
        self.port = port
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def start(self):
        with mouse.Listener(on_move=self.__on_move, on_click=self.__on_click) as listener:
            listener.join()

    def __on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        # if not pressed:
        #     # Stop listener
        #     return False

    def __on_move(self, x, y):
        # print('Pointer moved to {0}'.format((x, y)))
        self.socket.sendto("{0};{1}".format(x, y).encode(), (self.host, self.port))



if __name__ == '__main__':
    client = MouseListenerClient()
    client.start()    
