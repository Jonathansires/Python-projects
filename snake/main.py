import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
s = Screen()
s.listen()
s.setup(600,600)
s.bgcolor('black')
s.title("Snake game")
s.tracer(0)


snake= Snake()
food= Food()
scoreboard = Scoreboard()
game_on = True

s.onkey(snake.up, "w")
s.onkey(snake.down, "s")
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")

yes=.1
def up():
    global yes
    yes = yes+.01

s.onkey(up,"Up")
def down():
    global yes    
    wyes = yes-.01
s.onkey(down,"Down")


while game_on:
    s.update()
    time.sleep(yes)
    
    snake.move()

    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        print("nom")
        scoreboard.increase_score()

    if snake.head.xcor() >290 or snake.head.xcor() <-290 or snake.head.ycor() > 300 or snake.head.ycor()< -290:
        scoreboard.reset()
        snake.reset()
    
    for segment in snake.segments:
        if segment == snake.head:
            pass
    
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
s.exitonclick()