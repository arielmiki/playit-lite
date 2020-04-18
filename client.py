from pynput import mouse
from model import MouseEvent
import pyautogui
import socket

class MouseListenerClient:
    def __init__(self, host: str = 'localhost', port: int = 5050):
        self.port = port
        self.host = host
        self.width, self.height = pyautogui.size()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def start(self):
        with mouse.Listener(on_move=self.__on_move, on_click=self.__on_click, on_scroll=self.__on_scroll) as listener:
            listener.join()

    def __on_click(self, x, y, button, pressed):
        e = MouseEvent(MouseEvent.Type.ON_CLICK, x/self.width, y/self.height, button=button, pressed=pressed)
        self.socket.sendto(MouseEvent.encode(e), (self.host, self.port))
        
    def __on_move(self, x, y):
        e = MouseEvent(MouseEvent.Type.ON_MOVE, x/self.width, y/self.height)
        self.socket.sendto(MouseEvent.encode(e), (self.host, self.port))

    def __on_scroll(self, x, y, dx, dy):
        e = MouseEvent(MouseEvent.Type.ON_SCROLL, x/self.width, y/self.height, dx=dx, dy=dy)
        print(dx, dy)
        self.socket.sendto(MouseEvent.encode(e), (self.host, self.port))



if __name__ == '__main__':
    client = MouseListenerClient(host = "localhost", port = 20071)
    client.start()    
