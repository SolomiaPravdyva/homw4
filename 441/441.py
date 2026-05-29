import turtle
from datetime import datetime
import math

class Watch:
    def update(self):
        pass
class Digit:
    def __init__(self, number, angle, radius):
        self.number=number
        self.angle=angle
        self.radius=radius
    def draw(self, t):
        x=self.radius * math.cos(math.radians(self.angle))
        y=self.radius * math.sin(math.radians(self.angle))
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.write(self.number, align="center", font=("Arial", 14, "normal"))
class ClockFace:
    def __init__(self, radius=200):
        self.radius=radius
        self.digits=[Digit(i, 90 - i * 30, radius - 30) for i in range(1, 13)]
    def draw(self, t):
        t.penup()
        t.goto(0, -self.radius)
        t.pendown()
        t.circle(self.radius)
        for d in self.digits:
            d.draw(t)
class Hand:
    def __init__(self, length, width, color):
        self.length=length
        self.width=width
        self.color=color
    def draw(self, t, angle):
        t.penup()
        t.goto(0, 0)
        t.setheading(90 - angle)
        t.pendown()
        t.color(self.color)
        t.width(self.width)
        t.forward(self.length)

class AnalogWatch(Watch):
    def __init__(self, screen):
        self.screen=screen
        self.face_t=turtle.Turtle()
        self.face_t.hideturtle()
        self.face_t.speed(0)

        self.hand_t=turtle.Turtle()
        self.hand_t.hideturtle()
        self.hand_t.speed(0)

        self.face=ClockFace()
        self.face.draw(self.face_t)

        self.hour_hand=Hand(80, 6, "black")
        self.minute_hand=Hand(120, 4, "blue")
        self.second_hand=Hand(150, 2, "red")
    def update(self):
        self.hand_t.clear()
        now=datetime.now()
        hour=now.hour % 12
        minute=now.minute
        second=now.second
        hour_angle= (hour + minute / 60) * 30
        minute_angle= (minute + second / 60) * 6
        second_angle= second * 6
        self.hour_hand.draw(self.hand_t, hour_angle)
        self.minute_hand.draw(self.hand_t, minute_angle)
        self.second_hand.draw(self.hand_t, second_angle)

class DigitalWatch(Watch):
    def __init__(self, screen, mode="24"):
        self.screen= screen
        self.mode= mode
        self.writer= turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(0, -250)
    def set_mode(self, mode):
        self.mode= mode
    def update(self):
        self.writer.clear()
        now = datetime.now()
        if self.mode =="12":
            hour = now.hour % 12
            hour = 12 if hour == 0 else hour
            ampm= "AM" if now.hour < 12 else "PM"
            time_str = f"{hour:02d}:{now.minute:02d}:{now.second:02d} {ampm}"
        else:
            time_str = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
        self.writer.write(time_str, align="center", font=("Arial", 28, "bold"))

screen = turtle.Screen()
screen.bgcolor("white")
screen.tracer(0)
analog = AnalogWatch(screen)
digital = DigitalWatch(screen, mode="24")

def update():
    analog.update()
    digital.update()
    screen.update()
    screen.ontimer(update, 1000)

update()
turtle.done()
