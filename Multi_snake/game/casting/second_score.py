import constants
from game.casting.actor import Actor
from game.shared.point import Point


class SecondScore(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points that player two has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)
        #position
        x = int(constants.MAX_X + 830)
        y = int(constants.MAX_Y + 0)
        self._position = Point(x, y)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")
        
    def end_game_points(self):
        #up = (0,-1) down = (0,1) left = (-1,0) right = (1,0)
        x = int(constants.MAX_X + 500)
        y = int(constants.MAX_Y + 250)
        self._position = Point(x, y)
        
        self._points
        self.set_text(f"Player Two: {self._points}")
        
        