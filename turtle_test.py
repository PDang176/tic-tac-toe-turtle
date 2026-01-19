import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
screen = turtle.Screen()
RADIUS = 40

# Draw Grid
def drawGrid():
  # Top Line
  t.penup()
  t.goto(-150, 50)
  t.pendown()
  t.forward(300)
  # Bottom Line
  t.penup()
  t.goto(-150, -50)
  t.pendown()
  t.forward(300)
  # Left Line
  t.penup()
  t.goto(-50, 150)
  t.right(90)
  t.pendown()
  t.forward(300)
  # Right Line
  t.penup()
  t.goto(50, 150)
  t.pendown()
  t.forward(300)

drawGrid()

# Coordinates
# Top Left: x < -50, y > 50
# Middle Left: x < -50, -50 < y < 50
# Bottom Left: x < -50, y < -50

# Top Middle: -50 < x < 50, y > 50
# Middle Middle: -50 < x < 50, -50 < y < 50
# Bottom Middle: -50 < x < 50, y < -50

# Top Right: x > 50, y > 50
# Middle Right: x > 50, -50 < y < 50
# Bottom Right: x > 50, y < -50

def drawO(x, y):
  t.setheading(0)
  t.penup()
  # Set x
  if x < -50:
    x = -100
  elif x < 50:
    x = 0
  else:
    x = 100
  # Set y
  if y < -50:
    y = -100
  elif y < 50:
    y = 0
  else:
    y = 100
  
  t.goto(x, y - RADIUS)
  t.pendown()
  t.circle(40)

def drawX(x, y):
  t.penup()
  # Set x
  if x < -50:
    x = -100
  elif x < 50:
    x = 0
  else:
    x = 100
  # Set y
  if y < -50:
    y = -100
  elif y < 50:
    y = 0
  else:
    y = 100
  
  t.goto(x - RADIUS, y + RADIUS)
  t.pendown()
  t.setheading(-45)
  t.forward(113)

  t.penup()
    
  t.goto(x + RADIUS, y + RADIUS)
  t.pendown()
  t.setheading(-135)
  t.forward(113)

working = False
turn = 0 # 0: O, 1: X

def clicked(x, y):
  global working
  if working:
    return

  screen.onclick(None)
  working = True

  global turn
  if turn == 0:
    drawO(x, y)
    turn = 1
  else:
    drawX(x, y)
    turn = 0

  working = False
  screen.onclick(clicked)

screen.onclick(clicked)
turtle.mainloop()