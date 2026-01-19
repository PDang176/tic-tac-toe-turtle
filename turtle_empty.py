import turtle
t = turtle.Turtle()
t.speed(5)
screen = turtle.Screen()
GRID_LENGTH = 300
RADIUS = 40

def drawGrid():
  t.home()
  # TODO: Draw Top Line
  t.penup()

  t.pendown()

  # TODO: Draw Bottom Line
  t.penup()

  t.pendown()

  # TODO: Draw Left Line
  t.penup()

  t.pendown()

  # TODO: Draw Right Line
  t.penup()

  t.pendown()

# Call Draw Grid Function
drawGrid()

def drawO(x, y):
  # TODO: Draw Circle for O
  pass

def drawX(x, y):
  t.penup()
  # TODO: Draw first diagonal of X
  t.penup()
  # TODO: Draw second diagonal of X

working = False
turn = 0 # 0: O, 1: X



def clicked(x, y):
  global working
  if working:
    return

  screen.onclick(None)
  working = True

  t.setheading(0)
  t.penup()
  
  # TODO: Set turtle x coordinate
  # TODO: Set turtle y coordinate

  global turn
  # TODO: Draw either O or X depending on whose turn it is

  working = False
  screen.onclick(clicked)

# Add onclick event
screen.onclick(clicked)

def restart():
  # TODO: Clear screen, draw grid, reset turn to 0
  pass

# Add restart game functionality
screen.listen()
screen.onkey(restart, "r")

turtle.mainloop()