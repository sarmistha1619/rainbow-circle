import turtle

t=turtle.Turtle()
t.speed(10000)
t.hideturtle()
t.getscreen().bgcolor('white')

for j in range(1,6):
    for i in range(1, 50):
        t.circle(i)
        t.right(3)
        t.color('Purple')

    for i in range(50, 100):
        t.circle(i)
        t.right(3)
        t.color('MediumBlue')

    for i in range(100, 150):
        t.circle(i)
        t.right(3)
        t.color('MediumTurquoise')

    for i in range(150, 200):
        t.circle(i)
        t.right(3)
        t.color('Green')

    for i in range(200, 250):
        t.circle(i)
        t.right(3)
        t.color('Yellow')

    for i in range(250, 300):
        t.circle(i)
        t.right(3)
        t.color('OrangeRed')

    for i in range(300, 350):
        t.circle(i)
        t.right(3)
        t.color('red')