import turtle
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
screen = turtle.Screen()
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

working = False

def drawO(x, y):
  global working
  if working:
    return

  screen.onclick(None)
  working = True

  t.setheading(-90)
  t.penup()
  # Set x
  if x < -50:
    x = -140
  elif x < 50:
    x = -40
  else:
    x = 60
  # Set y
  if y < -50:
    y = -100
  elif y < 50:
    y = 0
  else:
    y = 100
  
  t.goto(x, y)
  t.pendown()
  t.circle(40)

  working = False
  screen.onclick(clicked)

def drawX(x, y):
  global working
  if working:
    return

  screen.onclick(None)
  working = True

  t.penup()
  # Set x
  if x < -50:
    x = -140
  elif x < 50:
    x = -40
  else:
    x = 60
  # Set y
  if y < -50:
    y = -60
  elif y < 50:
    y = 40
  else:
    y = 140
  
  t.goto(x, y)
  t.pendown()
  t.setheading(-45)
  t.forward(113)

  t.penup()
  # Set x
  if x < -50:
    x = -60
  elif x < 50:
    x = 40
  else:
    x = 140
  # Set y
  if y < -50:
    y = -60
  elif y < 50:
    y = 40
  else:
    y = 140
    
  t.goto(x, y)
  t.pendown()
  t.setheading(-135)
  t.forward(113)

  working = False
  screen.onclick(clicked)

turn = 0 # 0: O, 1: X

def clicked(x, y):
  global turn
  if turn == 0:
    drawO(x, y)
    turn = 1
  else:
    drawX(x, y)
    turn = 0

screen.onclick(clicked)
turtle.mainloop()