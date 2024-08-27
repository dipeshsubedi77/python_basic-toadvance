import turtle
turtle.setup(500, 600)
turtle.penup()
turtle.hideturtle()

LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# draw the star
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #left shoulder
turtle.dot()

turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #left shoulder
turtle.dot()

turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) #left shoulder
turtle.dot()

turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) #left shoulder
turtle.dot()

turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) #left shoulder
turtle.dot()

turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #left shoulder
turtle.dot()

turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) #left shoulder
turtle.dot()

# DISPLAY THE STAR NAME

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.write('Betegeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.write('Melssa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.write('Alintak')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.write('Alininam')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.write('Mintitaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.write('Saiph')

turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.write('Rigle')


# draw  aline from the left shoulder to left beltstar

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()
#  draw  aline from the right shoulder to right beltstar

turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()
#  draw  aline from the left beltstar to  middle beltstar


turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()
#  draw  aline from the   middle beltstar to right beltstar


turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()

turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()
#  draw  aline from the left beltstar to  left knee

turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

#  draw  aline from the right beltstar to left knee
turtle.goto(RIGHT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.done()








