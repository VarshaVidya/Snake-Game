from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")

my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard=ScoreBoard()
my_screen.listen()
my_screen.onkey(snake.move_up,"Up")
my_screen.onkey(snake.move_down,"Down")
my_screen.onkey(snake.move_left,"Left")
my_screen.onkey(snake.move_right,"Right")

# move snake
Game_on = True
while Game_on:
    time.sleep(0.1)
    my_screen.update()
    snake.snake_move()
    # food collision
    if snake.head.distance(food)<15:
        food.generate_food()
        scoreboard.add_score()
        snake.extend_snake()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        Game_on=False
        scoreboard.gameover()

        #detect collision with tail
    for seg in snake.every_segment:
        if snake.head.distance(seg)<10 and seg!=snake.head:
            Game_on=False
            scoreboard.gameover()
my_screen.exitonclick()