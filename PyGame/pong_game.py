'''
Created on Jul 7, 2021

@author: sohamdigambar
'''
import turtle as my_turtle
import random

#creating objects to run the game

#variables to keep track of scores
player_A_score = 0
player_B_score = 0


#creates the screen using the turtle object
window = my_turtle.Screen()
window.title("Simple Pong Game")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

    
#creating left paddle
left_paddle = my_turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
left_paddle.penup()
left_paddle.goto(-350, 0)


#creating right paddle
right_paddle = my_turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
right_paddle.penup()
right_paddle.goto(350, 0)


#creating the ball
ball = my_turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5, 5)
ball_x_dir = 1.75
ball_y_dir = 1.75


#creating the pen to update scores
pen = my_turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align = "center", font = ('Arial', 24, 'normal'))


#creating methods to run the logistics of the game

#moving the left paddle
def left_paddle_up():
    y_cord = left_paddle.ycor()
    y_cord = y_cord + 90
    left_paddle.sety(y_cord)

def left_paddle_down():
    y_cord = left_paddle.ycor()
    y_cord = y_cord - 90
    left_paddle.sety(y_cord)


#moving the right paddle
def right_paddle_up():
    y_cord = right_paddle.ycor()
    y_cord = y_cord + 90
    right_paddle.sety(y_cord)
    

def right_paddle_down():
    y_cord = right_paddle.ycor()
    y_cord = y_cord - 90
    right_paddle.sety(y_cord)
    
    
#Assigning the keyboard keys to play the game
window.listen()
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')

while True:
    window.update()
    
    #moving the ball
    ball.setx(ball.xcor() + ball_x_dir)
    ball.sety(ball.ycor() + ball_y_dir) 
 
    #making sure the ball doesn't go past the border of the screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y_dir = (ball_y_dir) * -1
    if ball.ycor() <  -290:
        ball.sety(-290)
        ball_y_dir = (ball_y_dir) * -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_x_dir = ball_x_dir
        player_A_score = player_A_score + 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(player_A_score, player_B_score), align = 'center', font = ('Arial', 24, 'normal'))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_x_dir = ball_x_dir * -1
        player_B_score = player_B_score + 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(player_A_score, player_B_score), align = 'center', font = ('Arial', 24, 'normal'))
        
        
    #Handling the collisions of the ball
    if (ball.xcor() > 340) and (ball.xcor() < 350) and ((ball.ycor() < right_paddle.ycor() + 40) and (ball.ycor() > right_paddle.ycor() - 40)):
        ball.setx(340)
        ball_x_dir = ball_x_dir * -1
    if (ball.xcor() < -340) and (ball.xcor() > -350) and ((ball.ycor() < left_paddle.ycor() + 40) and (ball.ycor() > left_paddle.ycor() - 40)):
        ball.setx(-340)
        ball_x_dir = ball_x_dir * -1