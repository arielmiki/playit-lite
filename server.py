import socket
from model import MouseKeyboardEvent
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyoardController
import pyautogui

class MouseKeyboardListenerServer:
    def __init__(self, host = 'localhost', port = 5050):
        self.port = port
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.mouse = MouseController()
        self.keyboard = KeyoardController()
        self.width, self.height = pyautogui.size()
    
    def __process_data(self, data):
        e = MouseKeyboardEvent.decode(data)
        print(e)
        if e.type == MouseKeyboardEvent.Type.MOUSE_ON_MOVE:
            self.mouse.position = (e.x * self.width, e.y * self.height)
        elif e.type == MouseKeyboardEvent.Type.MOUSE_ON_CLICK:
            if e.pressed:
                self.mouse.press(e.button)
            else:
                self.mouse.release(e.button)
        elif e.type == MouseKeyboardEvent.Type.MOUSE_ON_SCROLL:
            self.mouse.scroll(e.dx, e.dy)
        elif e.type == MouseKeyboardEvent.Type.KEYBOARD_ON_PRESSED:
            self.keyboard.press(e.key)
        elif e.type == MouseKeyboardEvent.Type.KEYBOARD_ON_RELEASED:
            self.keyboard.release(e.key)

    def start(self):
        self.socket.bind((self.host, self.port))
        while True:
            data, addr = self.socket.recvfrom(1024)
            self.__process_data(data)


if __name__ == '__main__':
    client = MouseKeyboardListenerServer("localhost", 20071)
    client.start() 

