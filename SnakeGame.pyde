from snake import snake
from food import food
from game import game

game = game()
food = food(game)
snake = snake(game)

def setup():
    size(game.SCREEN_WIDTH, game.SCREEN_HEIGHT)
    background(0)
    frameRate(game.speed)

def keyPressed():
  if key == CODED and not game.pause == -1:
    snake.turn(keyCode)
    
def mousePressed():
    
    if not game.over:
        game.pause *= -1
    else:
        game.reset(snake, food)

def draw():
    if not game.pause == -1:
        background(0)
        food.update(snake)
        snake.update()
        game.displayScore(snake.tailLength)
    else:
        pass
    
