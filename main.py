import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("skyblue")
drawing_board.title("Python Turtle")

'''
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance1 = turtle.Turtle()
turtle_instance1.left(90)
turtle_instance1.forward(100)
'''

#square
# turtle_instance = turtle.Turtle()
# for i in range(4):
#     turtle_instance.forward(200)
#     turtle_instance.left(90)
''' 
#star
turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.left(144)
    turtle_instance.forward(200)
'''
#polygon
turtle_instance = turtle.Turtle()
num_sides = 6
angle = 360 / num_sides
side_length = 150

for i in range(6):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)


turtle.done()