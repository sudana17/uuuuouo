#!/usr/bin/env python
# coding: utf-8

# In[4]:


import turtle as tl

def draw_fractal(size):
    if size >= 5:
        tl.pensize(max(size / 50, 1))
        tl.forward(size)
        tl.left(45)
        draw_fractal(size / 1.5)
        tl.right(30)
        draw_fractal(size / 3)
        tl.right(30)
        draw_fractal(size / 6)
        tl.right(30)
        draw_fractal(size / 9)
      
     

        tl.left(45)
        tl.penup()
        tl.backward(size)
        tl.pendown()
    else:
        tl.pensize(3)
        tl.dot()
        
size = 300

tl.delay(1)  # уменьшение задержки для скорости
tl.penup()
tl.color('blue')
tl.goto(0, -size * 2)
tl.setheading(90)
tl.pendown()

draw_fractal(size)
tl.done()


# In[ ]:





# In[ ]:




