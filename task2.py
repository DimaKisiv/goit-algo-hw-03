import turtle

def draw_koch_segment(t, ln, deep):
    if (deep == 0):
        t.fd(ln)
        return
    ln = ln/3
    deep = deep-1
    draw_koch_segment(t, ln, deep)
    t.left(60)
    draw_koch_segment(t, ln, deep)
    t.right(120)
    draw_koch_segment(t, ln, deep)
    t.left(60)
    draw_koch_segment(t, ln, deep)

deep = int(input("Введіть глибину:"))
t = turtle.Turtle()
t.speed(10 * (deep ** deep ** deep))
for _ in range(3):
    draw_koch_segment(t, 300, deep)
    t.right(120)
turtle.done()