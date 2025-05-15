from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def drawHome():
    homeBackground()
    homeRoof()
    homeBase()
    homeDoor()
    homeWindow1()
    homeWindow2()

def homeBackground():
    points = [(0, 0), (500, 0), (0, 350), (500, 0), (0, 350), (500, 350)]
    glBegin(GL_TRIANGLES)
    glColor3f(0.412, 0.498, 0.314)
    for point in points:
        glVertex2f(*point)
    glEnd()

def homeRoof():
    points = [(35, 200), (415, 200), (225, 300)]
    glBegin(GL_TRIANGLES)
    glColor3f(0.361, 0.459, 0.439)
    for point in points:
        glVertex2f(*point)
    glEnd()

def homeBase():
    points = [(50, 50), (400, 50), (50, 200), (400, 50), (50, 200), (400, 200)]
    glBegin(GL_TRIANGLES)
    glColor3f(0.165, 0.286, 0.263)
    for point in points:
        glVertex2f(*point)
    glEnd()

def homeDoor():
    points = [(195, 50), (255, 50), (195, 150), (255, 50), (195, 150), (255, 150)]
    glBegin(GL_TRIANGLES)
    glColor3f(0.816, 0.769, 0.643)
    for point in points:
        glVertex2f(*point)
    glEnd()
    glColor3f(0, 0, 0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex2f(247, 100)
    glEnd()

def homeWindow1():
    points = [(100, 100), (150, 100), (100, 150), (150, 100), (100, 150), (150, 150)]
    glBegin(GL_TRIANGLES)
    glColor3f(0.929, 1, 0.969)
    for point in points:
        glVertex2f(*point)
    glEnd()

    points = [(125, 100), (125, 150), (100, 125), (150, 125)]
    glLineWidth(2)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for point in points:
        glVertex2f(*point)
    glEnd()

def homeWindow2():
    points = [(290, 100), (340, 100), (290, 150), (340, 100), (290, 150), (340, 150)]
    glBegin(GL_TRIANGLES)
    glColor3f(0.929, 1, 0.969)
    for point in points:
        glVertex2f(*point)
    glEnd()

    points = [(315, 100), (315, 150), (290, 125), (340, 125)]
    glLineWidth(2)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for point in points:
        glVertex2f(*point)
    glEnd()

def drawRain():
    global rainDrops, rainAngle
    glColor3f(0.239, 0.592, 0.922)
    glBegin(GL_LINES)
    for drop in rainDrops:
        x, y = drop
        glVertex2f(x, y)
        glVertex2f(x + rainAngle, y - 15)
    glEnd()

def animate():
    global rainDrops
    for drop in rainDrops:
        drop[0] += rainAngle
        drop[1] -= 3
        if drop[0] < 0:
            drop[0] = width + drop[0]
        elif drop[0] > width:
            drop[0] = drop[0] - width
        if drop[1] < 0:
            drop[0] = random.uniform(0, width)
            drop[1] = height
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global brightness
    if key == b'd':
        brightness = max(0.0, brightness - 0.1)
    elif key == b'l':
        brightness = min(0.8, brightness + 0.1)
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global rainAngle
    if key == GLUT_KEY_LEFT and rainAngle > -10:
        rainAngle -= 1
    elif key == GLUT_KEY_RIGHT and rainAngle < 10:
        rainAngle += 1
    glutPostRedisplay()

def iterate():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(brightness, brightness, brightness, 0) 
    glLoadIdentity()
    iterate()
    drawHome()
    drawRain()
    glutSwapBuffers()

width,height = 500, 500
brightness = 0.9

rainDrops, rainAngle = [], 0.0
for i in range(350):
    x = random.uniform(0, width)
    y = random.uniform(0,height)
    rainDrops.append([x, y])

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"A home in Rainfall")
glutDisplayFunc(display)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()