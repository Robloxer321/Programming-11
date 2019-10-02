import turtle 

screen = turtle.Screen()
screen.setup(500,500)
screen.title("Oval with 4 Arcs - PythonTurtle.Academy")
turtle.speed(50)
turtle.shape('turtle')
turtle.bgcolor("black")
turtle.hideturtle()

#Draw backround web
t = turtle.Turtle()
t.hideturtle()
t.speed(500)
turtle.shape('turtle')
turtle.pensize(2)
turtle.pencolor("grey")

for i in range(6):
  t.forward(150)
  t.backward(150)
  t.right(60)

side = 150
side1 = 300
for i in range(50):
  t.penup()
  t.pd()
  t.goto(0,0)
  t.color("grey")
  t.pendown()
  t.setheading(0)
  t.forward(side)
  t.right(120)
  for j in range(6):
    t.forward(side)
    t.right(60)
  side = side - 10
#Draw face

turtle.pensize(2)
turtle.begin_fill()
turtle.up()
turtle.goto(120,-170)
turtle.down()
turtle.seth(45)
turtle.color('black', 'red')
turtle.circle(270,90)
turtle.color('black', 'red')
turtle.circle(170,90)
turtle.color('black', 'red')
turtle.circle(270,90)
turtle.color('black', 'red')
turtle.circle(170,90)
turtle.end_fill()


#Draw web pattern

t = turtle.Turtle()
t.hideturtle()
t.speed(500)
turtle.shape('turtle')
turtle.pensize(2)
 
#Code for building radical thread
for i in range(6):
  t.forward(200)
  t.backward(200)
  t.right(60)
 
#Code for building spiral thread
side = 150
for i in range(50):
  t.penup()
  t.goto(0,0)
  t.pendown()
  t.setheading(0)
  t.forward(side)
  t.right(120)
  for j in range(6):
    t.forward(side)
    t.right(60)
  side = side - 10

#Draw left eye

turtle.shape('turtle')
turtle.speed (50)

turtle.pensize(2)
turtle.begin_fill()
turtle.up()
turtle.goto(-10,40)
turtle.down()
turtle.seth(90)
turtle.color('black', 'black')
turtle.circle(100,90)
turtle.color('black', 'black')
turtle.circle(60,90)
turtle.color('black', 'black')
turtle.circle(100,90)
turtle.color('black', 'black')
turtle.circle(60,90)
turtle.end_fill()

#Draw left pupil

turtle.shape('turtle')
turtle.speed (500)

turtle.pensize(2)
turtle.begin_fill()
turtle.up()
turtle.goto(-30,40)
turtle.down()
turtle.seth(90)
turtle.color('white', 'white')
turtle.circle(80,90)
turtle.color('white', 'white')
turtle.circle(40,90)
turtle.color('white', 'white')
turtle.circle(80,90)
turtle.color('white', 'white')
turtle.circle(40,90)
turtle.end_fill()

#Draw right eye

turtle.shape('turtle')
turtle.speed (500)

turtle.pensize(2)
turtle.begin_fill()
turtle.up()
turtle.goto(100,140)
turtle.down()
turtle.seth(-180)
turtle.color('black', 'black')
turtle.circle(100,90)
turtle.color('black', 'black')
turtle.circle(60,90)
turtle.color('black', 'black')
turtle.circle(100,90)
turtle.color('black', 'black')
turtle.circle(60,90)
turtle.end_fill()

#Draw right pupil

turtle.shape('turtle')
turtle.speed (500)

turtle.pensize(2)
turtle.begin_fill()
turtle.up()
turtle.goto(100,120)
turtle.down()
turtle.seth(-180)
turtle.color('white', 'white')
turtle.circle(80,90)
turtle.color('white', 'white')
turtle.circle(40,90)
turtle.color('white', 'white')
turtle.circle(80,90)
turtle.color('white', 'white')
turtle.circle(40,90)
turtle.end_fill()


