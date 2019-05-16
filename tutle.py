import turtle, math
bob = turtle.Turtle()
#bob.delay = 0.01

def square(f, length):
    for i in range(4):
        f.fd(length)
        f.lt(90)

def polygon(f, length, n):
    for i in range(n):
        f.fd(length)
        f.lt(360/n)

def circle(t, r):
    n = 100
    length = 2 * math.pi * r / n
    polygon(t, length, n)

def arc(t, r, angle):
    n = 100
    length = (2 * math.pi * r * angle) / (360 * n)
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

arc(bob, 100, 360)
#circle(bob, 200)
#square(bob, 200)
turtle.mainloop()