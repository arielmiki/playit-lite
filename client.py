from pynput import mouse, keyboard
from pynput.keyboard import Key
from model import MouseKeyboardEvent
import pyautogui
import socket

class MouseKeyboardListenerClient:
    def __init__(self, host: str = 'localhost', port: int = 5050):
        self.port = port
        self.host = host
        self.width, self.height = pyautogui.size()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.keyboard_listener = keyboard.Listener(on_press=self.__keyboard_on_press, on_release=self.__keyboard_on_release)
        self.mouse_listener =  mouse.Listener(on_move=self.__mouse_on_move, on_click=self.__mouse_on_click, on_scroll=self.__mouse_on_scroll)
    
    def start(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def join(self):
        self.keyboard_listener.join()
    
    def stop(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()

    def __mouse_on_click(self, x, y, button, pressed):
        e = MouseKeyboardEvent(MouseKeyboardEvent.Type.MOUSE_ON_CLICK, x/self.width, y/self.height, button=button, pressed=pressed)
        print(e)
        self.socket.sendto(MouseKeyboardEvent.encode(e), (self.host, self.port))
        
    def __mouse_on_move(self, x, y):
        e = MouseKeyboardEvent(MouseKeyboardEvent.Type.MOUSE_ON_MOVE, x = x/self.width, y = y/self.height)
        print(e)
        self.socket.sendto(MouseKeyboardEvent.encode(e), (self.host, self.port))

    def __mouse_on_scroll(self, x, y, dx, dy):
        e = MouseKeyboardEvent(MouseKeyboardEvent.Type.MOUSE_ON_SCROLL, dx=dx, dy=dy)
        print(e)
        self.socket.sendto(MouseKeyboardEvent.encode(e), (self.host, self.port))
    
    def __keyboard_on_press(self, key):
        e = MouseKeyboardEvent(MouseKeyboardEvent.Type.KEYBOARD_ON_PRESSED, key=key)
        print(e)
        self.socket.sendto(MouseKeyboardEvent.encode(e), (self.host, self.port))
    
    def __keyboard_on_release(self, key):
        e = MouseKeyboardEvent(MouseKeyboardEvent.Type.KEYBOARD_ON_RELEASED, key=key)
        print(e)
        self.socket.sendto(MouseKeyboardEvent.encode(e), (self.host, self.port))
    



if __name__ == '__main__':
    listener =  MouseKeyboardListenerClient(host = "localhost", port = 20071)
    listener.start()
    listener.join()
