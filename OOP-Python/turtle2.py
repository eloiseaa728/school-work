import turtle

class turtleyas:
    def __init__(self, setColour, setSize, setStartAng):
        self.colour = setColour
        self.size = float(setSize)
        self.startAngle = float(setStartAng)
        self.t = turtle.Turtle()


    def star(self):
        self.t.right(90)
        self.t.forward(100)
        self.t.left(90)
        self.t.backward(100)

    def rectangle(self):
        self.t.right(self.startAngle)
        for self.i in range(0,2,1):
            self.t.right(90*self.size)
            self.t.forward(100*self.size)
            self.t.left(90*self.size)
            self.t.backward(100*self.size)
            self.t.shape(square,self.size)

turtle1 = turtleyas("blue", 1, 35.2)
turtle2 = turtleyas("green", 4, 100.4)

turtle1.rectangle()
turtle2.rectangle()
