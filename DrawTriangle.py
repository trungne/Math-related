import turtle
#triangle sides
while True:
    a,b,c = input('Insert 3 sides of your triangle: ').split()
    try:
        a= int(a)
        b= int(b)
        c= int(c)
    except ValueError:
        print('Please insert numbers for your sides.')
        continue
    if a+b > c and a+c > b and b+c > a:
        break
    else:
        print('These 3 sides cannot make a triangle, please try again.')
        continue
#draw
import math
cosC = (a**2+ b**2 - c**2)/(2*a*b)
cosB = (a**2+ c**2 - b**2)/(2*a*c)
cosA = (b**2+ c**2 - a**2)/(2*b*c)
angleOppositeC = math.acos(cosC)
angleOppositeB = math.acos(cosB)
angleOppositeA = math.acos(cosA)


t = turtle.Pen()
t.forward(a)
t.left(180 - math.degrees(angleOppositeC))
t.forward(b)
t.left(180 - math.degrees(angleOppositeA))
t.forward(c)
t.left(180 - math.degrees(angleOppositeB))
turtle.mainloop()