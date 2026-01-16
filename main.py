from turtle import Screen

#Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.getcanvas().winfo_toplevel().attributes("-topmost", True)
screen.title("Pong")














screen.exitonclick()