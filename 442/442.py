import turtle
import random
CELL=120
OFFSET=CELL // 2
START=-CELL
class Figure:
    def __init__(self):
        self.x=0
        self.y=0
        self.visible=False
        self.pen=turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
    def setPosition(self, x, y):
        self.x=x
        self.y=y
    def show(self):
        self.visible=True
        self.draw("black")
    def hide(self):
        self.pen.clear()
        self.visible=False
    def draw(self, color):
        pass

class Cross(Figure):
    def draw(self, color):
        self.pen.clear()
        self.pen.color(color)
        self.pen.pensize(3)
        s = 40
        self.pen.penup()
        self.pen.goto(self.x-s, self.y-s)
        self.pen.pendown()
        self.pen.goto(self.x+s, self.y+s)

        self.pen.penup()
        self.pen.goto(self.x-s, self.y + s)
        self.pen.pendown()
        self.pen.goto(self.x + s, self.y - s)
class Nought(Figure):
    def draw(self, color):
        self.pen.clear()
        self.pen.color(color)
        self.pen.pensize(3)

        self.pen.penup()
        self.pen.goto(self.x, self.y - 40)
        self.pen.pendown()
        self.pen.circle(40)

class Board(Figure):
    def draw(self, color):
        self.pen.clear()
        self.pen.color(color)
        self.pen.pensize(3)
        for i in range(4):
            x = START + i*CELL
            self.pen.penup()
            self.pen.goto(x, START)
            self.pen.pendown()
            self.pen.goto(x, START + 3*CELL)
        for i in range(4):
            y = START + i*CELL
            self.pen.penup()
            self.pen.goto(START, y)
            self.pen.pendown()
            self.pen.goto(START + 3*CELL, y)
class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Хрестики-нулики")
        self.board = Board()
        self.board.draw("black")
        self.cells = {}
        self.turn = "X"
        self.play()
    def center(self, r, c):
        x = START + c * CELL + OFFSET
        y = START + r * CELL + OFFSET
        return x, y
    def random_move(self):
        empty = [(r, c) for r in range(3) for c in range(3)
                 if (r, c) not in self.cells]
        return random.choice(empty) if empty else None
    def move(self):
        move = self.random_move()
        if not move:
            return
        r, c = move
        x, y = self.center(r, c)
        if self.turn == "X":
            fig = Cross()
        else:
            fig = Nought()
        fig.setPosition(x, y)
        fig.show()
        self.cells[(r, c)] = self.turn
        self.turn = "O" if self.turn == "X" else "X"
        self.screen.ontimer(self.play, 300)
    def play(self):
        if len(self.cells) < 9:
            self.move()
Game()
turtle.listen()
turtle.mainloop()
