import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Crawlies(Actor):
    """
    A food item.
    
    The responsibility of Crawlies is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Crawly."
        super().__init__()
        self._points = 0
        self.set_text("x")
        self.set_color(constants.RED)
        self.reset()
        
    def reset(self):
        x = random.randint(1, constants.MAX_X)
        y = random.randint(1, constants.MAX_Y)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
    
        
    def get_points(self):
        """Gets the points the Crawly is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points