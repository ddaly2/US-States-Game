from turtle import Turtle

class StateName:
    def __init__(self):
        self.states = 0

    def fill_in_name(self, name, x, y):
        new_state = Turtle()
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(x, y)
        new_state.write(name)
        self.states += 1

    def is_finished(self):
        if self.states > 2:
            return True
        return False
