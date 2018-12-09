# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle, os, pygame, random, sys
from pygame.locals import *

def pong_game():
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Score
    score_a = 0
    score_b = 0

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = -3
    ball.dy = 3

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player: 0  COM: 0", align="center", font=("Courier", 24, "normal"))

    # Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 25
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 25
        paddle_a.sety(y)

    def paddle_b_move(dy):
        y = paddle_b.ycor()
        if paddle_b.ycor() > 300:
            y += dy*(-.8)
        elif paddle_b.ycor() < -300:
            y += dy*(-.81)
        else:
            y += dy*.78
        paddle_b.sety(y)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(paddle_a_up, "Up")
    wn.onkeypress(paddle_a_down, "Down")

    flag = True

    # Main game loop
    while flag == True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        paddle_b_move(ball.dy)

        # Border checking

        # Top and bottom
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")

        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")

        # Left and right
        if ball.xcor() > 350:
            score_a += 1
            pen.clear()
            pen.write("Player: {}  COM: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            paddle_b.goto(350, 0)
            ball.goto(0, 0)
            ball.dx *= -1

            if score_a >= 3:
                flag = False

        elif ball.xcor() < -350:
            score_b += 1
            pen.clear()
            pen.write("Player: {}  COM: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            paddle_b.goto(350, 0)
            ball.goto(0, 0)
            ball.dx *= -1

            if score_b >= 3:
                flag = False

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1
            os.system("afplay bounce.wav&")

        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
            os.system("afplay bounce.wav&")


def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:return True
	else:return False

def die(screen, score):
	f=pygame.font.SysFont('Arial', 30);t=f.render('Your score was: '+str(score), True, (0, 0, 0));screen.blit(t, (10, 270));pygame.display.update();pygame.time.wait(2000);pygame.quit()

def snake():
    running = True
    xs = [290, 290, 290, 290, 290];ys = [290, 270, 250, 230, 210];dirs = 0;score = 0;applepos = (random.randint(0, 590), random.randint(0, 590));pygame.init();s=pygame.display.set_mode((600, 600));pygame.display.set_caption('Snake');appleimage = pygame.Surface((10, 10));appleimage.fill((0, 255, 0));img = pygame.Surface((20, 20));img.fill((255, 0, 0));f = pygame.font.SysFont('Arial', 20);clock = pygame.time.Clock()
    while running == True:
    	clock.tick(10)
    	for e in pygame.event.get():
    		if e.type == QUIT:
    			running == False
    		elif e.type == KEYDOWN:
    			if e.key == K_UP and dirs != 0:dirs = 2
    			elif e.key == K_DOWN and dirs != 2:dirs = 0
    			elif e.key == K_LEFT and dirs != 1:dirs = 3
    			elif e.key == K_RIGHT and dirs != 3:dirs = 1
    	i = len(xs)-1
    	while i >= 2:
    		if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):die(s, score)
    		i-= 1
    	if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):score+=1;xs.append(700);ys.append(700);applepos=(random.randint(0,590),random.randint(0,590))
    	if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580: die(s, score)
    	i = len(xs)-1
    	while i >= 1:
    		xs[i] = xs[i-1];ys[i] = ys[i-1];i -= 1
    	if dirs==0:ys[0] += 20
    	elif dirs==1:xs[0] += 20
    	elif dirs==2:ys[0] -= 20
    	elif dirs==3:xs[0] -= 20
    	s.fill((255, 255, 255))
    	for i in range(0, len(xs)):
    		s.blit(img, (xs[i], ys[i]))
    	s.blit(appleimage, applepos);t=f.render(str(score), True, (0, 0, 0));s.blit(t, (10, 10));pygame.display.update()
