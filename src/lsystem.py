from src.turtle import TurtleDrawing

class LSystem:
    def __init__(
        self,
        symbols,
        start,
        production_rules,
        pos=(500,500),
        length=10,
        angle=0,
        turning_angle=0,
        turning_angle_increment=0,
        length_scale_factor=1,
    ):
        self.symbols = symbols
        self.start = start
        self.production_rules = production_rules
        self.turtle = TurtleDrawing(
            pos, length, angle, turning_angle, turning_angle_increment, length_scale_factor
        )

    def __repr__(self):
        return f"Symbols: {self.symbols}\nStart: {self.start}\nProduction Rules: {self.production_rules}"

    def save(self, path):
        print(f"Saving to {path}")
        self.turtle.save(path)


