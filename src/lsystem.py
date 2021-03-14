from src.turtle import TurtleDrawing

class LSystem:
    def __init__(
        self,
        symbols,
        start,
        production_rules,
        pos=(0, 0),
        angle=0,
        turning_angle_increment=0,
        length_scale_factor=1,
        swap_plus_minus=False,
    ):
        self.symbols = symbols
        self.start = start
        self.production_rules = production_rules
        self.turtle = TurtleDrawing(
            pos, angle, turning_angle_increment, length_scale_factor, swap_plus_minus
        )

    def __repr__(self):
        return f"Symbols: {self.symbols}\nStart: {self.start}\nProduction Rules: {self.production_rules}"

    def save(self, path):
        self.turtle.save(path)


