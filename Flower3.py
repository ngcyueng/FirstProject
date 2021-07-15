import turtle

t1 = turtle.Turtle()
t1.shape("turtle")
t1.speed(0)
t1.color("yellow", "red")
t1.width(3)

def draw_box(t):
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.end_fill()

for petal in range(36):
    draw_box(t1)
    t1.right(10)