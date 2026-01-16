from turtle import Screen, Turtle

#Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.getcanvas().winfo_toplevel().attributes("-topmost", True)
screen.title("Pong")
screen.tracer(0)



screen.listen()
# screen.onkey(go_up,"Up")
# screen.onkey(go_down,"Down")

game_is_on = True
while game_is_on:
    screen.update()















screen.exitonclick()