import socket
from model import MouseKeyboardEvent
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyoardController
import pyautogui
import threading

WIDTH, HEIGHT = pyautogui.size()


class MouseKeyboardThread(threading.Thread):
    def __init__(self, conn, addr):
        self.mouse = MouseController()
        self.keyboard = KeyoardController()
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print("Accepting connection from: {0}:{1} ".format(*self.addr))
    
    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                print("{0}:{1}: Connection closed".format(*self.addr))
                break
            self.__process_data(data)
        self.conn.close()
    
    def __process_data(self, data):
        try:
            e = MouseKeyboardEvent.decode(data)
        except:
            return
        print(e)
        if e.type == MouseKeyboardEvent.Type.MOUSE_ON_MOVE:
            self.mouse.position = (e.x * WIDTH, e.y * HEIGHT)
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


class MouseKeyboardListenerServer:
    def __init__(self, host = 'localhost', port = 5050):
        self.port = port
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        print("Starting TCP server at {0}:{1}".format(self.host, self.port))
        self.socket.bind((self.host, self.port))
        while True:
            self.socket.listen(1)
            conn, addr = self.socket.accept()
            thread = MouseKeyboardThread(conn, addr)
            thread.start()


if __name__ == '__main__':
    client = MouseKeyboardListenerServer(input("Host:"), int(input("Port:")))
    client.start() 

