from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects 
    is to update the game state when actor collides.
    
    Stereotype:
        Controller
    """

    def __init__(self, output_service):

        self._output_service = output_service


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle= cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        ball = cast["ball"][0] # there's only one

        #Check if the ball is bouncing against any of the 4 walls:
        if ball.get_x >= 80:
            ball.x *= -1
        if ball.x <= -80:
            ball.velocity *= -1
        if ball.y >= 20:
            ball.velocity *= -1
        if ball.y <= -20:
            self._output_service.game_over()

        #Check if there is the ball collides with any of bricks
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                self._output_service.delete_brick()

        
        #Detect collisions between the ball and the paddles
        if ball.get_position().equals(paddle.get_position()):
            ball -= ball.velocity[0]
            ball -= ball.velocity[1]
            ball.bounce()
