import socket
from model import MouseEvent
from pynput.mouse import Button, Controller
import pyautogui

class MouseListenerServer:
    def __init__(self, host = 'localhost', port = 5050):
        self.port = port
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.mouse = Controller()
        self.width, self.height = pyautogui.size()
    
    def __process_data(self, data):
        e = MouseEvent.decode(data)
        if e.type == MouseEvent.Type.ON_MOVE:
            self.mouse.position = (e.x * self.width, e.y * self.height)
        elif e.type == MouseEvent.Type.ON_CLICK:
            if e.pressed:
                self.mouse.press(e.button)
            else:
                self.mouse.release(e.button)
        elif e.type == MouseEvent.Type.ON_SCROLL:
            print(e.dx, e.dy)
            self.mouse.scroll(e.dx, e.dy)

    def start(self):
        self.socket.bind((self.host, self.port))
        while True:
                data, addr = self.socket.recvfrom(1024)
                self.__process_data(data)


if __name__ == '__main__':
    client = MouseListenerServer("0.0.0.0", 20071)
    client.start() 

