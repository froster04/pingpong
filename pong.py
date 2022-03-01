import turtle
import os

#screen
wd = turtle.Screen() #seting up the screen
wd.title("pingpong by @froster04") #title for the screen
wd.bgcolor("grey") #bg colour of the screen
wd.setup(width=800, height=600) #screen dimensinons
wd.tracer(0)


#paddle a
paddle_a = turtle.Turtle() #creating paddle(object)
paddle_a.speed(0) #animation speed
paddle_a.shape("square") #giving shape
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white") #giving colour
paddle_a.penup()
paddle_a.goto(-350, 0) #start position on screen


#paddel b
paddle_b = turtle.Turtle() #creating paddle(object)
paddle_b.speed(0) #animation speed
paddle_b.shape("square") #giving shape
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white") #giving colour
paddle_b.penup()
paddle_b.goto(350, 0) #start position on screen

#ball
ball = turtle.Turtle() #creating ball(object)
ball.speed(0) #animation speed
ball.shape("square") #giving shape
ball.color("black") #giving colour
ball.penup()
ball.goto(0, 0) #start position on screen
ball.dx = 0.25
ball.dy = 0.25

#scoreboard (pen)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Plyaer B: 0", align="center", font=("Courier", 24, "normal"))

#score
score_a = 0
score_b = 0


#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

#keybinding
wd.listen()
wd.onkeypress(paddle_a_up, "w")
wd.onkeypress(paddle_a_down, "s")
wd.onkeypress(paddle_b_up, "Up")
wd.onkeypress(paddle_b_down, "Down")


#Main game loop
while True:
    wd.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #screen border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce_wall.wav&")
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce_wall.wav&")


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        os.system("aplay point.wav&")
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Plyaer B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        os.system("aplay point.wav&")
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Plyaer B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    #paddle and ball colision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay paddle_hit.wav&")

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay paddle_hit.wav&")
