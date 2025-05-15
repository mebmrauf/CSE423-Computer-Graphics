from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

width, height = 500, 500
pause, resume, terminate = False, True, False
points, speed = 0, 50

def convertCoordinate(x, y):
    global width, height
    a = x
    b = height - y
    return a, b

def drawPoints(x, y, color):
    glColor3f(*color)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def calculateZone(startPoint, endPoint):
    dx = endPoint[0] - startPoint[0]
    dy = endPoint[1] - startPoint[1]
    if abs(dx) > abs(dy): 
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx <= 0 and dy >= 0:
            zone = 3
        elif dx <= 0 and dy <= 0:
            zone = 4
        elif dx >= 0 and dy <= 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx <= 0 and dy >= 0:
            zone = 2
        elif dx <= 0 and dy <= 0:
            zone = 5
        elif dx >= 0 and dy <= 0:
            zone = 6 
    return zone

def convertZoneNto0(x, y, zone):
    if zone == 0:
        x, y = x, y
    elif zone == 1:
        x, y = y, x
    elif zone == 2:
        x, y = y, -x
    elif zone == 3:
        x, y = -x, y
    elif zone == 4:
        x, y = -x, -y
    elif zone == 5:
        x, y = -y, -x
    elif zone == 6:
        x, y = -y, x
    elif zone == 7:
        x, y = x, -y
    return (x, y)
    
def convertZone0toN(x, y, zone):
    if zone == 0:
        x, y = x, y
    elif zone == 1:
        x, y = y, x
    elif zone == 2:
        x, y = -y, x
    elif zone == 3:
        x, y = -x, y
    elif zone == 4:
        x, y = -x, -y
    elif zone == 5:
        x, y = -y, -x
    elif zone == 6:
        x, y = y, -x
    elif zone == 7:
        x, y = x, -y
    return (x, y)

def midpointLine(startPoint, endPoint, color, zone):
    dx = endPoint[0] - startPoint[0]
    dy = endPoint[1] - startPoint[1]
    d = 2 * dy - dx
    dNE = 2 * dy - 2 * dx
    dE = 2 * dy
    x = startPoint[0]
    y = startPoint[1]
    while x <= endPoint[0]:
        cx, cy = convertZone0toN(x, y, zone)
        drawPoints(cx, cy, color)
        if d <= 0:
            d += dE
        else:
            d += dNE
            y += 1
        x += 1

def eightWaySymmetry(startPoint, endPoint, color):
    zone = calculateZone(startPoint, endPoint)
    startPoint = convertZoneNto0(startPoint[0], startPoint[1], zone)
    endPoint = convertZoneNto0(endPoint[0], endPoint[1], zone)
    midpointLine(startPoint, endPoint, color, zone)

def drawCatcher():
    global catcherInfo
    if terminate: color = (1, 0, 0)
    else: color = (1, 1, 1)    
    for key in catcherInfo:
        eightWaySymmetry(catcherInfo[key][0], catcherInfo[key][1], color)

def drawArrow():
    arrow = {"straight": ((10,470),(50,470)), "up": ((10,470),(30,490)), "down": ((10,470),(30,450))}
    for key in arrow:
        eightWaySymmetry(arrow[key][0], arrow[key][1], (0, 0.859, 1))

def drawCross():
    cross = {"line1": ((450,450),(490,490)), "line2": ((450,490),(490,450))}
    for key in cross:
        eightWaySymmetry(cross[key][0], cross[key][1], (1, 0, 0))

def drawPauseResume():
    global pause, resume
    res = {"line1": ((230,450), (230, 490)), "line2": ((250,450), (250, 490))}
    pos = {"line1": ((225,450), (225, 490)), "line2": ((225,450), (255, 470)), "line3": ((225,490), (255, 470))}
    if resume:
        for key in res:
            eightWaySymmetry(res[key][0], res[key][1], (1, 0.69, 0))
    if pause:
        for key in pos:
            eightWaySymmetry(pos[key][0], pos[key][1], (1, 0.69, 0))

def drawDiamond():
    global diamondInfo
    for key in diamondInfo:
        if key != "color":
            eightWaySymmetry(diamondInfo[key][0], diamondInfo[key][1], diamondInfo["color"])

lastTime = time.time()
def animate():
    global terminate, resume, catcherInfo, diamondInfo, diamondPositionX, p1, speed, points, lastTime
    if not terminate and resume:
        currentTime = time.time()
        deltaTime = currentTime - lastTime
        lastTime = currentTime
        catcherBox = {"x": p1[0], "y": p1[1], "width": 140, "height": 30}
        for key in diamondInfo:
            if key != "color":
                diamondInfo[key] = ((diamondInfo[key][0][0], diamondInfo[key][0][1] - speed * deltaTime), (diamondInfo[key][1][0], diamondInfo[key][1][1] - speed * deltaTime))
        diamondBox = {"x": diamondInfo["bottomLeft"][1][0], "y": diamondInfo["bottomLeft"][1][1], "width": 30, "height": 40}
        if hasCollided(diamondBox, catcherBox):
            print("Diamond caught!")
            diamondPositionX = random.randint(25, 475)
            diamondInfo = generateDiamond(diamondPositionX)
            points += 1
            speed += 5
            print("Points:", points)
        elif diamondInfo["topRight"][0][1] < 0:
            print("Game Over! Final Points:", points)
            terminate = True
    glutPostRedisplay()
    time.sleep(0.01)

def generateCatcher(p1, p2, p3, p4):
    return {"base": (p1, p2), "leftDiagonal": (p4, p1), "rightDiagonal": (p2, p3), "above": (p4, p3)}

def generateDiamond(diamondPositionX):
    return {"topRight": ((diamondPositionX, 445), (diamondPositionX + 15, 425)), "topLeft": ((diamondPositionX, 445), (diamondPositionX - 15, 425)), "bottomRight": ((diamondPositionX + 15, 425),(diamondPositionX, 405)), "bottomLeft": ((diamondPositionX - 15, 425), (diamondPositionX, 405)), "color": (random.uniform(0.4, 1), random.uniform(0.4, 1), random.uniform(0.4, 1))}

def hasCollided(box1, box2):
    return (box1['x'] < box2['x'] + box2['width'] and
            box1['x'] + box1['width'] > box2['x'] and
            box1['y'] < box2['y'] + box2['height'] and
            box1['y'] + box1['height'] > box2['y'])

def specialKeyListener(key, x, y):
    global resume, terminate, p1, p2, p3, p4
    if key == GLUT_KEY_RIGHT:
        if p3[0] <= 470 and not terminate and resume:
            p1[0], p2[0], p3[0], p4[0] = p1[0] + 10, p2[0] + 10, p3[0] + 10, p4[0] + 10
    elif key == GLUT_KEY_LEFT:
        if p4[0] >= 20 and not terminate and resume:
            p1[0], p2[0], p3[0], p4[0] = p1[0] - 10, p2[0] - 10, p3[0] - 10, p4[0] - 10
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    global pause, resume, terminate, p1, p2, p3, p4, speed, points, diamondInfo, catcherInfo
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        x, y = convertCoordinate(x, y)
        if 10 <= x <= 50 and 450 <= y <= 490:
            print("Starting Over!")
            points, speed = 0, 50
            diamondPositionX = random.randint(25, 475)
            diamondInfo = generateDiamond(diamondPositionX)
            catcherInfo = generateCatcher(p1, p2, p3, p4)
            resume, pause, terminate = True, False, False
            print("Game Restarted")

        elif 230 <= x <= 250 and 450 <= y <= 490 and resume:
                resume, pause = False, True
                print("Game Paused")
        elif 225 <= x <= 255 and 450 <= y <= 490 and pause:
                resume, pause = True, False
                print("Game Resumed")
        elif 450 <= x <= 490 and 450 <= y <= 490:
            print(f"Goodbye! Final Points: {points}")
            terminate = True
            glutLeaveMainLoop()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    drawCatcher()
    drawDiamond()
    drawArrow()
    drawCross()
    drawPauseResume()
    glutSwapBuffers()

p1, p2, p3, p4 = [200, 10], [280, 10], [310, 40], [170, 40]
catcherInfo = generateCatcher(p1, p2, p3, p4)
diamondPositionX = 75
diamondInfo = generateDiamond(diamondPositionX)

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Midpoint Line Drawing Algorithm")
glutDisplayFunc(display)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()