import turtle
import numpy as np
import matplotlib.pyplot as plt


t = turtle.Turtle()


for i in range(5):
    t.circle(20 * i)
    t.sety((10*i)*(-1))
    t.setx((10*i)*(-1))

for i in range(5):
    t.circle(-20*i)
    t.sety((10 * i) *(-1))

# for i in range(5):
#     t.circle(10*i)
#     t.up()
#     t.sety((10*i)*(-1))
#     t.down()

