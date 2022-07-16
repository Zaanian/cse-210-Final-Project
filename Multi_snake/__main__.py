import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.bugs import Bugs
from game.casting.crawlies import Crawlies
from game.casting.score import Score
from game.casting.second_score import SecondScore
from game.casting.snake import Snake
from game.casting.second_snake import SecondSnake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.control_second_actors_action import ControlSecondActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("bugz", Bugs())
    cast.add_actor("crawly", Crawlies())
    cast.add_actor("snakes", Snake())
    cast.add_actor("second-snakes", SecondSnake())
    cast.add_actor("scores", Score())
    cast.add_actor("second-scores", SecondScore())
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", ControlSecondActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()