import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Temperature and Rainfall Graphs")

t = turtle.Turtle()
t.speed(0)

# Data
months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

temperature = [22,24,28,31,34,36,35,34,32,29,25,23]
rainfall = [15,20,30,45,80,150,220,200,160,90,40,20]

# Draw axes
t.penup()
t.goto(-250, -150)
t.pendown()
t.forward(500)

t.penup()
t.goto(-250, -150)
t.setheading(90)
t.pendown()
t.forward(300)

# Line plot for temperature
t.color("blue")
t.penup()
for i in range(len(temperature)):
    x = -220 + i * 40
    y = -150 + temperature[i] * 5
    if i == 0:
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

# Scatter plot for rainfall
t.color("red")
for i in range(len(rainfall)):
    x = -220 + i * 40
    y = -150 + rainfall[i]
    t.penup()
    t.goto(x, y)
    t.dot(8)

# Month labels
t.color("black")
for i in range(len(months)):
    x = -220 + i * 40
    t.penup()
    t.goto(x, -170)
    t.write(months[i], align="center", font=("Arial", 8, "normal"))

t.hideturtle()
turtle.done()
