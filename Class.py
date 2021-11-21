import turtle
class Pen:
    strength=100
    color="red"
    def info(self):
        return("Прочность",self.strength,"колир ",self.color)
    def __init__(self,strength,color,):
        self.strength=strength
        self.color=color

    def draw_human(self):
        a=10
        import turtle
        turtle.color("red")
        turtle.speed(0)
        turtle.left(90)
        turtle.forward(200)
        self.strength-=200/10
        turtle.right(90)
        turtle.forward(200)
        self.strength -= 200 / 10
        turtle.right(90)
        turtle.forward(200)
        self.strength -= 200 / 10
        turtle.right(90)
        turtle.forward(200)
        self.strength -= 200 / 10
        turtle.circle(200)
        self.strength -= 200 / 10
        if self.strength<0:
            return
        turtle.write(self.info(), font=("Arial", 10, "normal"))
        turtle.mainloop()