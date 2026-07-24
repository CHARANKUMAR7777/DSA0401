import turtle

screen = turtle.Screen()
screen.title("Monthly Sales Charts")

t = turtle.Turtle()
t.speed(0)

months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]

sales = [120,150,180,170,200,220,250,240,260,280,300,320]

# Draw Axes
t.penup()
t.goto(-250, -150)
t.pendown()
t.forward(500)

t.penup()
t.goto(-250, -150)
t.setheading(90)
t.pendown()
t.forward(350)

# ---------------- Line Plot ----------------
t.color("blue")
t.penup()

for i in range(len(sales)):
    x = -220 + i * 40
    y = -150 + sales[i]
    if i == 0:
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

# ---------------- Scatter Plot ----------------
t.color("red")
for i in range(len(sales)):
    x = -220 + i * 40
    y = -150 + sales[i]
    t.penup()
    t.goto(x, y)
    t.dot(8)

# ---------------- Bar Plot ----------------
t.color("green")
for i in range(len(sales)):
    x = -220 + i * 40
    t.penup()
    t.goto(x, -150)
    t.setheading(90)
    t.pendown()
    t.forward(sales[i])

# Month Labels
t.color("black")
for i in range(len(months)):
    x = -220 + i * 40
    t.penup()
    t.goto(x, -170)
    t.write(months[i], align="center", font=("Arial", 8, "normal"))

t.hideturtle()
turtle.done()
