#enter side
while True:
    a,b = input('enter the length of each side').split()
    try:
        a = int(a)
        b = int(b)
    except:
        print ('enter integers only!')
        continue
    break
import turtle
t = turtle.Pen()
t.speed(1)
t.forward(a)
t.left(90)
t.forward(b)
t.left(90)
t.forward(a)
t.left(90)
t.forward(b)

input('enter to exist')