
import drawSvg as draw
import math

class TurtleDrawing:
    def __init__(
        self,
        pos=(0, 0),
        length=1,
        angle=0,
        turning_angle=0,
        turning_angle_increment=0,
        length_scale_factor=1,
    ):
        self.pos = pos
        self.angle = angle
        self.length = length
        self.turning_angle = turning_angle
        self.turning_angle_increment = turning_angle_increment
        self.length_scale_factor = length_scale_factor
        self.stack = []
        self.drawing = draw.Drawing(1000, 1000)
        self.lines = []

    def draw(self, string):
        for char in string:
            if char in CHAR_TO_DRAW_FN: # Ignore variables
                getattr(self, CHAR_TO_DRAW_FN[char])()

        all_x_0, all_y_0, all_x_1, all_y_1 = zip(*self.lines)
        min_x = min(all_x_0 + all_x_1)
        max_x = max(all_x_0 + all_x_1)
        min_y = min(all_y_0 + all_y_1)
        max_y = max(all_y_0 + all_y_1)

        length_x = max_x - min_x
        length_y = max_y - min_y
        longer = max(length_x, length_y)
        shift_x = (1000 - (length_x * 1000 / longer)) / 2 # take half of remaining white space
        shift_y = (1000 - (length_y * 1000 / longer)) / 2

        new_x0 , new_x1 , new_y0 , new_y1 = [],[],[],[]
        for old_x0, old_y0, old_x1, old_y1 in self.lines:
            new_x0.append((old_x0 - min_x)*1000/longer + shift_x)
            new_x1.append((old_x1 - min_x)*1000/longer + shift_x)
            new_y0.append((old_y0 - min_y)*1000/longer + shift_y)
            new_y1.append((old_y1 - min_y) * 1000 / longer + shift_y)

        new_points = zip(new_x0, new_y0, new_x1, new_y1)

        for p in new_points:
            self.drawing.append(draw.Line(*p, stroke='black'))


    def save(self, path):
        # self.drawing.saveSvg(path)
        self.drawing.savePng(path)

    # ===== Helpers for drawing =======
    # http://paulbourke.net/fractals/lsys/
    # TODO

    def move(self):
        curr_x, curr_y = self.pos
        new_x = curr_x + self.length * math.cos(self.angle * math.pi / 180)
        new_y = curr_y + self.length * math.sin(self.angle * math.pi / 180)
        self.pos = (new_x, new_y)

        # want to calculate self.length units in the self.angle direction
        # move in x direction: length * cos(angle)
        # move in y direction: length * sin(angle)
        print("Move")


    def draw_and_move(self):
        curr_x, curr_y = self.pos
        new_x = curr_x + self.length * math.cos(self.angle * math.pi / 180)
        new_y = curr_y + self.length * math.sin(self.angle * math.pi / 180)
        self.lines.append([curr_x, curr_y, new_x, new_y])
        self.pos = (new_x, new_y)


    def turn_left(self):
        self.angle = (self.angle + self.turning_angle) % 360
        # print(self.angle)


    def turn_right(self):
        self.angle = (self.angle - self.turning_angle) % 360


    def reverse(self):
        self.angle = (180 + self.angle) % 360
        pass


    def push(self):
        self.stack.append(
            {'pos' : self.pos
            , 'angle' : self.angle
            , 'length' : self.length
            , 'turning_angle' : self.turning_angle
            , 'length_scale_factor' : self.length_scale_factor
            }
        )


    def pop(self):
        params = self.stack.pop(-1)
        self.pos = params['pos']
        self.angle = params['angle']
        self.length = params['length']
        self.turning_angle = params['turning_angle']
        self.length_scale_factor = params['length_scale_factor']


    def multiply_line_length(self):
        self.length *= self.length_scale_factor


    def divide_line_length(self):
        self.length /= self.length_scale_factor


    def decrement_turning_angle(self):
        self.turning_angle -= self.turning_angle_increment
        pass


    def increment_turning_angle(self):
        self.turning_angle += self.turning_angle_increment
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
    "(": 'decrement_turning_angle',
    ")": 'increment_turning_angle',
}

CONSTS = list(CHAR_TO_DRAW_FN.keys())