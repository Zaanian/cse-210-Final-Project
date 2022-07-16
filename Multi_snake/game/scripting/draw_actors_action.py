import constants
from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        secondScore = cast.get_first_actor("second-scores")
        food = cast.get_first_actor("foods")
        bugs = cast.get_first_actor("bugz")
        snake = cast.get_first_actor("snakes")
        secondSnake = cast.get_first_actor("second-snakes")
        segments = snake.get_segments()
        secondSegments = secondSnake.get_segments()
        messages = cast.get_actors("messages")
        crawly = cast.get_actors("crawly")
        flyBugg = cast.get_actors("fly-buggs")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actor(bugs)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(secondSegments)
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(secondScore)
        self._video_service.draw_actors(messages, True)
        self._video_service.draw_actors(crawly)
        self._video_service.draw_actors(flyBugg)
        self._video_service.flush_buffer()