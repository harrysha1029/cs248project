
import drawSvg as draw

class TurtleDrawing:
    def __init__(
        self,
        pos=(0, 0),
        angle=0,
        turning_angle_increment=0,
        length_scale_factor=1,
        swap_plus_minus=False,
    ):
        self.pos = pos
        self.angle = angle
        self.turning_angle_increment = turning_angle_increment
        self.length_scale_factor = length_scale_factor
        self.swap_plus_minus = swap_plus_minus
        self.stack = []
        self.drawing = draw.Drawing(1000, 1000)

    def draw(self, string):
        for char in string:
            if char in CHAR_TO_DRAW_FN: # Ignore variables
                f = getattr(self, CHAR_TO_DRAW_FN[char])()

    def save(self, path):
        self.drawing.saveSvg(path)

    # ===== Helpers for drawing =======
    # http://paulbourke.net/fractals/lsys/
    # TODO

    def move(self):
        print("Move")
        pass


    def draw_and_move(self):
        print("Draw and Move")
        pass


    def turn_left(self):
        print("Turn left")
        pass


    def turn_right(self):
        print("Turn right")
        pass


    def reverse(self):
        print("Reverse")
        pass


    def push(self):
        print("Push")
        pass


    def pop(self):
        print("Pop")
        pass


    def multiply_line_length(self):
        print("Multiply line lengths")
        pass


    def divide_line_length(self):
        print("Divide line lengths")
        pass


    def swap_pm(self):
        print("Swap pm")
        pass


    def decrement_turning_angle(self):
        print("Decrement turning angle")
        pass


    def increment_turning_angle(self):
        print("Increment turning angle")
        pass



CHAR_TO_DRAW_FN = {
    "F": 'draw_and_move',
    "f": 'move',
    "+": 'turn_left',
    "-": 'turn_right',
    "|": 'reverse',
    "[": 'push',
    "]": 'pop',
    # "#": "increment_line_width",
    # "!": "decrement_line_width",
    # "@": "draw_dot",
    # "{": "open_polygon",
    # "}": "close_polygon",
    ">": 'multiply_line_length',
    "<": 'divide_line_length',
    "&": 'swap_pm',
    "(": 'decrement_turning_angle',
    ")": 'increment_turning_angle',
}

CONSTS = list(CHAR_TO_DRAW_FN.keys())