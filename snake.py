from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.setpos(position)
        self.body.append(new_turtle)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for el in range(len(self.body)-1, 0, -1):
            new_x = self.body[el - 1].xcor()
            new_y = self.body[el - 1].ycor()
            self.body[el].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_right(self):
        self.head.right(90)

    def turn_left(self):
        self.head.left(90)