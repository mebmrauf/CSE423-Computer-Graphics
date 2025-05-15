from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

points, directions, colors = [], [], []
speed, blink, freeze = 0.7, False, False

def convertCoordinate(x, y):
    global width, height
    a = x - (width / 2)
    b = (height / 2) - y
    return a, b

def mouseListener(button, state, x, y):
    global points, freeze, blink, directions, colors
    if freeze:
        return
    
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        blink = not blink
    
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        point = convertCoordinate(x, y)
        if -250 < point[0] < 250 and -250 < point[1] < 250:
            points.append(point)
            color = [random.random(), random.random(), random.random()]
            direction = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
            dirX, dirY = random.choice(direction)
            dirX *= speed
            dirY *= speed
            directions.append((dirX, dirY))
            colors.append(color)
    glutPostRedisplay()
    
def keyboardListener(key, x, y):
    global freeze
    if key == b' ':
        if freeze == False:
            freeze = True
            print("Freeze")
        else:
            freeze = False
            print("Unfreeze")
    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global freeze, speed, directions
    if not freeze:
        if key == GLUT_KEY_UP:
            speed *= 2
            print("Speed Increased")
            for i in range(len(directions)):
                directions[i] = (directions[i][0] * 2, directions[i][1] * 2)
        elif key == GLUT_KEY_DOWN:
            speed = max(0.1, speed / 2)
            print("Speed Decreased")
            for i in range(len(directions)):
                directions[i] = (directions[i][0] / 2, directions[i][1] / 2)
    glutPostRedisplay()

def showPoints():
    global points, blink, directions, colors
    for i in range(len(points)):
        if i < len(directions):
            glColor3f(colors[i][0], colors[i][1], colors[i][2])
            if blink:
                glColor3f(1, 1, 1)
            glPointSize(10)
            glBegin(GL_POINTS)
            glVertex2f(points[i][0], points[i][1])
            glEnd()
            points[i] = (points[i][0] + directions[i][0], points[i][1] + directions[i][1])
            if points[i][0] > 249:
                points[i] = (249, points[i][1])
                directions[i] = (-abs(directions[i][0]), directions[i][1])
            elif points[i][0] < -249:
                points[i] = (-249, points[i][1])
                directions[i] = (abs(directions[i][0]), directions[i][1])
            if points[i][1] > 249:
                points[i] = (points[i][0], 249)
                directions[i] = (directions[i][0], -abs(directions[i][1]))
            elif points[i][1] < -249:
                points[i] = (points[i][0], -249)
                directions[i] = (directions[i][0], abs(directions[i][1]))

    blink = False


def animate():
    global freeze
    if freeze == False:
        glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1, 1, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 250, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    showPoints()
    
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex2d(-250, -250)
    glVertex2d(250, -250)
    glVertex2d(250, -250)
    glVertex2d(250, 250)
    glVertex2d(250, 250)
    glVertex2d(-250, 250)
    glVertex2d(-250, 250)
    glVertex2d(-250, -250)
    glEnd()
    
    glutSwapBuffers()

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000)

width,height = 500, 500
glutInit()
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)  
wind = glutCreateWindow(b"The Amazing Box")
init()
glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()