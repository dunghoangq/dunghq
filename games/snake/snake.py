# LIBRARIES
from turtle import Turtle, Screen
import time

# SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# The Snake itself
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)



game_is_on = True

while game_is_on:
    # Make the snake move smoothly
    screen.update()

    # Make the snake move faster
    time.sleep(.1)

    # Test the snake moving forward
    # for seg in segments:
    #     seg.forward(20)

    # Make the each segment follow the previous segment
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    # test
    segments[0].forward(20)


screen.exitonclick()
