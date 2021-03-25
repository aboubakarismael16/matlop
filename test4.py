import turtle
import numpy as np
import matplotlib.pyplot as plt


t = turtle.Turtle()
t.pensize(3)

t = turtle.Turtle()      #instantiate a new turtle object called 'a'
t.hideturtle()           #make the turtle invisible
t.penup()                #don't draw when turtle moves
t.goto(0, 20)            #move the turtle to a location
t.showturtle()           #make the turtle visible
t.pendown()              #draw when the turtle moves
t.goto(0, 20)

for i in range(5):
    t.circle(20 * i)

t = turtle.Turtle()      #instantiate a new turtle object called 'a'
t.hideturtle()           #make the turtle invisible
t.penup()                #don't draw when turtle moves
t.goto(0, 0)           #move the turtle to a location
t.showturtle()           #make the turtle visible
t.pendown()              #draw when the turtle moves
t.goto(0, 0)           #move the turtle to a new location

for i in range(5):
    t.circle(-20*i)

for i in range(10):
    t.circle(10*i)
    t.up()
    t.sety((10*i)*(-1))
    t.down()


angle = np.linspace(0, 2 * np.pi, 150)
radius = 0.4
x = radius * np.cos(angle)
y = radius * np.sin(angle)
figure, axes = plt.subplots(1)

axes.plot(x, y)
axes.set_aspect(1)

plt.title('Parametric Equation Circle')
plt.show()