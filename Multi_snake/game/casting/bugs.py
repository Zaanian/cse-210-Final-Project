import constants
import random
from game.casting.actor import Actor
from game.shared.point import Point

class Bugs(Actor):
    def __init__(self):
        "Constructs a new Bug(insect/food)."
        super().__init__()
        self._points = 0
        self.set_text("B")
        self.reset()
        
    def reset(self):
        """resets bugs"""
        self._points = random.randint(5, 12)
        x = random.randint(1, constants.MAX_X)
        y = random.randint(1, constants.MAX_Y)
        velocity = Point(0, 1 * constants.CELL_SIZE)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_color(constants.RED)
        self.set_position(position)
        self.set_velocity(velocity)
        
    def get_bugs_points(self):
        return self._points