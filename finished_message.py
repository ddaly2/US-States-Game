from turtle import Turtle

FONT = ('Courier', 20, 'normal')


class FinishedMessage:

    def __init__(self):
        self.states = 0

    def show_message(self):
        message = Turtle()
        message.penup()
        message.hideturtle()
        message.goto(-150, 250)
        message.write("You Finished The Quiz!", font=FONT)
