#rule1: variables should start with an alphabet or underscore
#rule2: don't use integers at the beginning of the variable
#rule3: No spaces inbetween
#rule4: shouldn't exceed 8 characters
#string concatenation: adding two strings
import time
import turtle
t = turtle.Turtle()
t.speed(0)

pencolor = input("Enter the pencolor:")
t.pencolor(pencolor)

bgcolor = input("Enter the background color:")
sc = turtle.Screen()
sc.bgcolor(bgcolor)

i = 0

while i<40:
    t.forward(100)
    t.right(190)
    i+=1
time.sleep(10)
