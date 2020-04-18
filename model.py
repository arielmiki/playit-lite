import enum
import pickle

class MouseEvent:
    class Type(enum.Enum):
        ON_MOVE = 0
        ON_SCROLL = 1
        ON_CLICK = 2

    @staticmethod
    def decode(byte):
        return pickle.loads(byte)

    @staticmethod
    def encode(obj):
        return pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)


    def __init__(self, type: Type, x, y, button = None, pressed = False, dx = 0, dy = 0):
        self.type = type
        self.x = x
        self.y = y
        self.button = button
        self.pressed = pressed
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return "<type: {0}, x: {1}, y:{2}, button:{3}, pressed:{4}, dx:{5}, dy:{6}>".format(self.type, self.x, self.y, self.button, self.pressed, self.dx, self.dy)    
