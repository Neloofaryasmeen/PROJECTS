# from turtle import*
# from colorsys import*
# bgcolor('black')
# tracer(10)
# h=0.6
# for i in range(1000):

#     c = hsv_to_rgb(h,1,1)
#     h+=1/3
#     fillcolor(c)
#     begin_fill()
#     circle(-50,150)
#     forward(i)
#     left(29)
#     end_fill()


#     done()

import turtle as t 
import colorsys 
t.bgcolor('black')
t.tracer(10)
t.pensize(1)
h=0
for i in range(300):
    c= colorsys.hsv_to_rgb(h,1,0.8)
    t.pencolor(c)
    h += 0.006
    t.right(119)
    t.circle(-i*0.3,120)
    t.circle(i*0.3,120)
    t.circle(-i*0.3,90)
    t.circle(i*0.3,90)
  