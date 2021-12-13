import turtle

class Yem():
    def __init__(self,renk,konum1,konum2):
        self.yem = turtle.Turtle()
        self.yem.color(renk)
        self.yem.penup()
        self.yem.shape("circle")
        self.yem.goto(konum1,konum2)
        self.deneme = renk
    
    def goto(self,konum1,konum2):
        self.yem.goto(konum1,konum2)