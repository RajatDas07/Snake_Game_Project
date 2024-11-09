import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
bodies = []

# creating a screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width=600, height=600)

# creating a head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# creating a food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.ht()
food.goto(150, 200)
food.st()

# creating a score board
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score:0  |   Highest Score:0")

# creating a function for moving in all direction
def moveUp():
    if head.direction != "down":
        head.direction = "up"
def moveDown():
    if head.direction != "up":
        head.direction = "down"
def moveLeft():
    if head.direction != "right":
        head.direction = "left"
def moveRight():
    if head.direction != "left":
        head.direction = "right"
def moveStop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# event handling
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

# Update (Line 45): Add exit key handling so that game can exit safely.
s.onkey(s.bye, "Escape")  # Press 'Escape' key to close the game

# main loop
try:
    while True:  # Start of the main loop
        s.update()  # to update the screen
        
        # check collision with border
        if head.xcor() > 290:
            head.setx(-290)
        if head.xcor() < -290:
            head.setx(290)

        # Update (Line 82): Fix border collision handling for y-axis
        if head.ycor() > 290:
            head.sety(-290)
        if head.ycor() < -290:
            head.sety(290)  # Fix head.set() to head.sety() for proper boundary handling

        # check collision with food
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)
            
            # increase the body of snake
            body = turtle.Turtle()
            body.speed(0)
            body.penup()
            body.shape("square")
            body.color("red")
            bodies.append(body)  # append the new body in list

            sc = sc + 100  # increase the score
            
            # Update (Line 110): Adjust delay with a minimum limit to control snake speed
            delay = max(0.05, delay - 0.001)  # Set minimum delay to avoid excessive speed

            if sc > hs:
                hs = sc  # update the highest score
            sb.clear()
            sb.write("Score:{}   |    Highest Score:{}".format(sc, hs))

        # move snake body
        for i in range(len(bodies) - 1, 0, -1):
            x = bodies[i - 1].xcor()
            y = bodies[i - 1].ycor()
            bodies[i].goto(x, y)

        if len(bodies) > 0:
            x = head.xcor()
            y = head.ycor()
            bodies[0].goto(x, y)

        move()

        # check collision with snake body
        for body in bodies:
            if body.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                
                # hide bodies
                for body in bodies:
                    body.ht()
                bodies.clear()
                sc = 0
                delay = 0.1
                sb.clear()
                sb.write("Score:{}  |   Highest Score:{}".format(sc, hs))

        time.sleep(delay)

# Update (Lines 66 and below): Use try-except to handle `turtle.Terminator` error
except turtle.Terminator:
    pass  # Exit loop safely if screen is closed
