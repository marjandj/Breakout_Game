from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=750, height=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)


paddle = Paddle()
ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.move_right, key="Right")
screen.onkey(paddle.move_left, key="Left")


colors = ["red", "red", "green", "green", "yellow", "yellow"]  # Each row a different color
points = [7, 7, 5, 5, 3, 3]  # Each color have a different value
bricks = []

brick_width = 40 * 2  # Since stretch_len=2, the actual width is 40
brick_height = 20  # Default turtle square size is 20, so stretch_wid=1 keeps it at 20

rows = 6
cols = 14

column_spacing = -30

total_width = cols * brick_width + (cols - 1) * column_spacing
start_x = -(total_width // 2) + (brick_width // 2)
start_y = 250  # Adjust starting position

for row in range(rows):
    for col in range(cols):
        x = start_x + col * (brick_width + column_spacing)
        y = start_y - row * (brick_height + 5)
        brick = Brick(position=(x, y), color=colors[row], point=points[row])
        bricks.append(brick)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with left and right wall
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.bounce_x()

    # Collision with upper wall
    if ball.ycor() > 380:
        ball.bounce_y()

    # Collision with paddle
    if ball.distance(paddle) < 30 and ball.ycor() < -260:
        ball.bounce_y()

    # Collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 30 and ball.ycor() > 90:
            ball.bounce_y()
            brick.hideturtle()  # Hide the brick
            bricks.remove(brick)
            scoreboard.add_points(brick.point)
            if not bricks:
                game_is_on = False
                scoreboard.final_score("win")



    # Missed the paddle

    if ball.ycor() < -360:
        scoreboard.take_life()
        ball.reset_position()

    if scoreboard.lives == 0:
        game_is_on = False
        scoreboard.final_score("lose")


screen.mainloop()