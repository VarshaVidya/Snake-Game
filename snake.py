from turtle import Turtle
STARTING_POS = [(-20,0),(-40,0),(-60,0)]
UP=90
DOWN =270
RIGHT=0
LEFT=180
class Snake:
    # create snake
    def __init__(self):
        self.every_segment = []
        self.draw_snake()
        self.head = self.every_segment[0]

    def draw_snake(self):
        for i in STARTING_POS:
            self.add_to_snake(i)

    def add_to_snake(self,position):
        my_turtle = Turtle("square")
        my_turtle.color("white")
        my_turtle.penup()
        my_turtle.goto(position)
        self.every_segment.append(my_turtle)


    def extend_snake(self):
        self.add_to_snake(self.every_segment[-1].position())

    def snake_move(self):
        for i in range(len(self.every_segment) - 1, 0, -1):
            x_pos = self.every_segment[i - 1].xcor()
            y_pos = self.every_segment[i - 1].ycor()
            self.every_segment[i].goto(x_pos, y_pos)
        self.head.forward(20)
    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def move_left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)