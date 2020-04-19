import enum
import pickle

class MouseKeyboardEvent:
    class Type(enum.Enum):
        MOUSE_ON_MOVE = 0
        MOUSE_ON_SCROLL = 1
        MOUSE_ON_CLICK = 2
        KEYBOARD_ON_PRESSED = 3
        KEYBOARD_ON_RELEASED = 4

    @staticmethod
    def decode(byte):
        return pickle.loads(byte)

    @staticmethod
    def encode(obj):
        return pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)


    def encode(self):
        return pickle.dumps(self, pickle.HIGHEST_PROTOCOL)

    def __init__(self, type: Type, x = 0, y = 0, button = None, pressed = False, dx = 0, dy = 0, key = None):
        self.type = type
        self.x = x
        self.y = y
        self.button = button
        self.pressed = pressed
        self.dx = dx
        self.dy = dy
        self.key = key

    def __repr__(self):
        return "{0}: x={1}, y={2}, button={3}, pressed={4}, dx={5}, dy={6}, key={7}>".format(self.type, self.x, self.y, self.button, self.pressed, self.dx, self.dy, self.key)    
