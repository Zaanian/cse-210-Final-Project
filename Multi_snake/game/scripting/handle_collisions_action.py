import constants
import random
from game.casting.actor import Actor
from game.scripting.action import Action
from game.casting.crawlies import Crawlies
from game.casting.bugs import Bugs
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake(players) collides
    with the food, or the snake(players) collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision_player_one(cast)
            self._handle_food_collision_player_two(cast)
            
            self._handle_bugs_collision_player_one(cast)
            self._handle_bugs_collision_player_two(cast)
            
            self._handle_fly_collision_player_one(cast)
            self._handle_fly_collision_player_two(cast)
            
            self._handle_crawly_collision_player_one(cast)
            
            self._handle_segment_collision_player_one(cast)
            self._handle_segment_collision_player_two(cast)
            
            self._handle_player_collision(cast)
            self._handle_game_over(cast)

# PLAYER ONE 
    def _handle_food_collision_player_one(self, cast):
        """Updates the score and moves the food if player one collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        head = snake.get_head()

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()
            
            #Crawlies and fly-bugs spawn
            for i in range(constants.DEFAULT_NUMBER):
                crawly = Crawlies()
                cast.add_actor("crawly", crawly)
            for i in range(constants.DEFAULT_NUMBER):
                flyBugs = Bugs()
                flyBugs.set_text("y")
                flyBugs.set_color(constants.YELLOW)
                cast.add_actor("fly-buggs", flyBugs)
            
    def _handle_bugs_collision_player_one(self, cast):
        """Updates the score and moves the bugs if the snake collides with the bugs.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        bugs = cast.get_first_actor("bugz")
        snake = cast.get_first_actor("snakes")
        head = snake.get_head()

        if head.get_position().equals(bugs.get_position()):
            points = bugs.get_bugs_points()
            snake.grow_tail(points)
            score.add_points(points)
            bugs.reset()
            
    def _handle_fly_collision_player_one(self, cast):
        flyBugs = cast.get_actors("fly-buggs")
        score = cast.get_first_actor("second-scores")
        snake = cast.get_first_actor("second-snakes")
        head = snake.get_head()
        
        for i in flyBugs:
            if head.get_position().equals(i.get_position()):
                points = 3
                snake.grow_tail(points)
                score.add_points(points)
                i.reset()
        
    def _handle_crawly_collision_player_one(self,cast):
        crawly = cast.get_actors("crawly")
        score = cast.get_first_actor("second-scores")
        snake = cast.get_first_actor("second-snakes")
        head = snake.get_head()
        
        for i in crawly:
            if head.get_position().equals(i.get_position()):
                points = 1
                snake.grow_tail(points)
                score.add_points(points)
                i.reset()
        
            
    def _handle_segment_collision_player_one(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
# PLAYER TWO    
    def _handle_food_collision_player_two(self, cast):
        """Updates the score and moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        secondScore = cast.get_first_actor("second-scores")
        food = cast.get_first_actor("foods")
        secondSnake = cast.get_first_actor("second-snakes")
        head = secondSnake.get_head()
        
        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            secondSnake.grow_tail(points)
            secondScore.add_points(points)
            food.reset()
            
            for i in range(constants.DEFAULT_NUMBER):
                #Crawlies and bugs spawn
                crawly = Crawlies()
                crawly.set_text("x")
                cast.add_actor("crawly", crawly)
            for i in range(constants.DEFAULT_NUMBER):
                flyBugs = Bugs()
                flyBugs.set_text("y")
                flyBugs.set_color(constants.YELLOW)
                cast.add_actor("fly-buggs", flyBugs)
            
    def _handle_bugs_collision_player_two(self, cast):
        """Updates the score and moves the bugs if the snake collides with the bugs.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        secondScore = cast.get_first_actor("second-scores")
        bugs = cast.get_first_actor("bugz")
        secondSnake = cast.get_first_actor("second-snakes")
        head = secondSnake.get_head()

        if head.get_position().equals(bugs.get_position()):
            points = bugs.get_bugs_points()
            secondSnake.grow_tail(points)
            secondScore.add_points(points)
            bugs.reset()
        
    def _handle_fly_collision_player_two(self, cast):
        flyBugs = cast.get_actors("fly-buggs")
        secondScore = cast.get_first_actor("second-scores")
        secondSnake = cast.get_first_actor("second-snakes")
        head_two = secondSnake.get_head()
        
        for i in flyBugs:
            if head_two.get_position().equals(i.get_position()):
                points = 3
                secondSnake.grow_tail(points)
                secondScore.add_points(points)
                    
            
    def _handle_segment_collision_player_two(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        secondSnake = cast.get_first_actor("second-snakes")
        head_two = secondSnake.get_segments()[0]
        segments_two = secondSnake.get_segments()[1:]
        
        for segment in segments_two:
            if head_two.get_position().equals(segment.get_position()):
                self._is_game_over = True
            
# player collide with other player
    def _handle_player_collision(self, cast):
        """Sets the game over flag if a player collides with another players segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        secondSnake = cast.get_first_actor("second-snakes")
        score = cast.get_first_actor("scores")
        secondScore = cast.get_first_actor("second-scores")
        head_1 = snake.get_head()
        head_2 = secondSnake.get_head()
        segments = snake.get_segments()[1:]
        segments_twos = secondSnake.get_segments()[1:]
        
        for segment in segments:
            if head_2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                point = 3
                score.add_points(point)
                
        for segment in segments_twos:
            if head_1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                point = 3
                secondScore.add_points(point)
    
    
       
# GAME OVER 
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            
            snake = cast.get_first_actor("snakes")
            secondSnake = cast.get_first_actor("second-snakes")
            
            score = cast.get_first_actor("scores")
            secondScore = cast.get_first_actor("second-scores")
            
            segments = snake.get_segments()
            secondSegments = secondSnake.get_segments()
            
            food = cast.get_first_actor("foods")
            bugs = cast.get_first_actor("bugz")
            
            flyBugs = cast.get_actors("fly-buggs")
            crawly = cast.get_actors("crawly")
            
            player_one_score = score
            player_two_score = secondScore

            

            #player scores
            player_one_score.end_game_points()
            player_two_score.end_game_points()
            
            #message
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            
            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            #color change
            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in secondSegments:
                segment.set_color(constants.WHITE)
            for i in flyBugs:
                i.set_color(constants.WHITE)
            for i in crawly:
                i.set_color(constants.WHITE)
            bugs.set_color(constants.WHITE)
            food.set_color(constants.WHITE)