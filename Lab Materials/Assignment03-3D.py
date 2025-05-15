# For better understanding show the video: https://drive.google.com/drive/folders/1vti-n-EBm448Xkib9JjGxTsPnB9-ztNV?usp=drive_link

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Camera
camera_position = (0,500,500)

fovY = 120  
grid_length = 100  
grid_size = 14
rand_var = 423

# Game state
playerPos = [0, 0, 0]
playerAngle = 0
camMode = "third"  
gameStatus = False

# Bullets
bullets = []

# Enemies
enemies = []
numEnemies = 5

# Player stats
life = 5
missiedBullets = 0
score = 0
minBound = -grid_size * grid_length // 2
maxBound = grid_size * grid_length // 2

#cheat
cheat = False
gun = False
cheat_rotation = 0
can_fire = True
cheatMoveAngle = 0
cheatCamOffset = [-100, 0, 60]

lastx, lasty, lastz = 0,0,0

def draw_text(x, y, text, font = GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 600)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def drawFloor(GRID_SIZE):
    glBegin(GL_QUADS)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i + j) % 2 == 0:
                glColor3f(1, 1, 1) #white
            else:
                glColor3f(0.7, 0.5, 0.95) #light purple

            x = (i - GRID_SIZE // 2) * grid_length
            y = (j - GRID_SIZE // 2) * grid_length

            glVertex3f(x, y, 0) #bottom left
            glVertex3f(x + grid_length, y, 0) #bottom right
            glVertex3f(x + grid_length, y + grid_length, 0) #top right
            glVertex3f(x, y + grid_length, 0) #top left
    glEnd()

def drawWalls():
    wall_ref = grid_length * grid_size // 2
    wallHeight = 115
    colors = [[0.012, 1, 0.996],[0, 0, 1], [1, 1, 1], [0, 1, 0]]
    directions = [
        [(-1, -1), (1, -1), (1, -1), (-1, -1)],
        [(1, -1), (1, 1), (1, 1), (1, -1)],
        [(1, 1), (-1, 1), (-1, 1), (1, 1)],
        [(-1, 1), (-1, -1), (-1, -1), (-1, 1)]
        ]
    for i in range(4):
        glBegin(GL_QUADS)
        glColor3f(*colors[i])
        for j in range(4):
            if j < 2:
                glVertex3f(directions[i][j][0] * wall_ref, directions[i][j][1] * wall_ref, 0)
            else:
                glVertex3f(directions[i][j][0] * wall_ref, directions[i][j][1] * wall_ref, wallHeight)
        glEnd()

def drawPlayer():
    glPushMatrix()
    glTranslatef(*playerPos)
    glRotatef(playerAngle, 0, 0, 1)  

    if gameStatus:
        glRotatef(90,0,1,0)

    # Left foot
    glColor3f(0, 0, 1)
    glTranslatef(0,-20,-100)
    glRotatef(90, 0, 1, 0)
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 16, 8, 100, 10, 10)

    # Right foot
    glTranslatef(0,-80,0)
    gluCylinder(gluNewQuadric(), 16, 8, 100, 10, 10)

    # Body
    glColor3f(0.095, 0.350, 0.095)
    glTranslatef(0, 40, -30)
    glutSolidCube(80)

    # Gun
    glColor3f(0.6, 0.6, 0.6)
    glTranslatef(0, 0, 40)
    glTranslatef(30, 0, -90) 
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 20, 5, 120, 10, 10)

    # Left Hand
    glColor3f(1.0, 0.88, 0.65)
    glTranslatef(0, -25, 0)
    gluCylinder(gluNewQuadric(), 15, 6, 60, 10, 10)

    # Right Hand
    glTranslatef(0, 50, 0)
    gluCylinder(gluNewQuadric(), 15, 6, 60, 10, 10)

    # Head
    glColor3f(0, 0, 0)
    glTranslatef(40,-25, -25)
    gluSphere(gluNewQuadric(), 30, 10, 10)
    glPopMatrix()


def drawBullets():
    glColor3f(1, 0, 0)
    for bullet in bullets:
        glPushMatrix()
        glTranslatef(*bullet['bulletPosition'])
        glutSolidCube(10)
        glPopMatrix()

def drawEnemies(e):
        glPushMatrix()
        glTranslatef(*e['enemy_pos'])
        glScalef(e["scale"], e["scale"], e["scale"]) 

        #body
        glColor3f(1, 0, 0)
        glPushMatrix()
        glTranslatef(0, 0, 40)
        gluSphere(gluNewQuadric(), 40, 20, 20)
        glPopMatrix()

        #haed
        glColor3f(0,0,0)
        glPushMatrix()
        glTranslatef(0, 0, 80)
        gluSphere(gluNewQuadric(), 30, 20, 20)
        glPopMatrix()

        glPopMatrix()

def generateEnemyPosition():
    while True: # avoiding center
        x = random.randint(-600, 500)
        y = random.randint(-600, 500)
        
        if abs(x) > 200 or abs(y) > 200:
            break

    return {
        'enemy_pos': [x, y, 0], #position
        'scale': 1.0, #size
        'scale_dir': 0.005 #pulse
    }
    
for n in range(numEnemies):
    enemy = generateEnemyPosition()
    enemy["collide"] = False 
    enemies.append(enemy)

def mouseListener(button, state, x, y):
    global camMode

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if not gameStatus:
            rad = math.radians(playerAngle)
            dirX = -math.cos(rad)
            dirY = -math.sin(rad)
            gunLength = 140 
            gunRight = 50
            gunUp = 10
            bulletStart = [playerPos[0] + gunRight * math.sin(rad) + dirX * gunLength,
                            playerPos[1] - gunRight * math.cos(rad) + dirY * gunLength,
                            playerPos[2] + gunUp]
            bullets.append({'bulletPosition': bulletStart, 'dir': (dirX, dirY)})
            print("Player bullet fired!")

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and not gameStatus:
        if camMode == "third":
            camMode = "first"
        else:
            camMode = "third"
        print(f"Switched to {camMode}-person mode")
        glutPostRedisplay()
  

def keyboardListener(key, x, y):
    global playerPos, playerAngle, camMode, minBound, maxBound, cheatMoveAngle, cheatCamOffset, life, missiedBullets, score, gameStatus, cheat, gun 
    if cheat:
        speed = 50
    else:
        speed = 20
    angleStep = 5
    if not gameStatus:
        if key == b'w':
            angle = math.radians(playerAngle)
            dx = -math.cos(angle) * speed
            dy = -math.sin(angle) * speed
            newX = playerPos[0] + dx
            newY = playerPos[1] + dy
            if minBound <= newX <= maxBound and minBound <= newY <= maxBound:
                playerPos[0] = newX
                playerPos[1] = newY
                if camMode == "first" and cheat and not gun:
                    cheatCamOffset[0] += dx
                    cheatCamOffset[1] += dy

        elif key == b's':
            angle = math.radians(playerAngle)
            dx = math.cos(angle) * speed
            dy = math.sin(angle) * speed
            newX = playerPos[0] + dx
            newY = playerPos[1] + dy
            if minBound <= newX <= maxBound and minBound <= newY <= maxBound:
                playerPos[0] = newX
                playerPos[1] = newY
                if camMode == "first" and cheat and not gun:
                    cheatCamOffset[0] += dx
                    cheatCamOffset[1] += dy
        elif key == b'a' and not cheat:
            playerAngle += angleStep
        elif key == b'd' and not cheat:
            playerAngle -= angleStep
        elif key == b"c":
            cheat = not cheat
            if cheat:
                cheat_mode()
            else:
                gun = False
        elif key == b"v":
            if camMode == "first" and cheat:
                gun = not gun
            if not cheat:
                gun = False
                
    if key == b'r' and gameStatus:
        bullets.clear()
        enemies.clear()
        cheat = False
        camMode = "third"
        for i in range(numEnemies):
            enemy = generateEnemyPosition()
            enemy['collide'] = False
            enemies.append(enemy)        
        score = 0
        missiedBullets = 0
        life = 5
        gameStatus = False
        playerPos[:] = [0, 0, 0]
        playerAngle = 0
        print("Game restarted!")
        glutPostRedisplay()

def specialKeyListener(key, x, y):
    global camera_position
    x, y, z = camera_position
    if not gameStatus:
        if key == GLUT_KEY_UP:
            y += 3
        if key == GLUT_KEY_DOWN:
            y-= 3
        if key == GLUT_KEY_LEFT:
            x -= 3
        if key == GLUT_KEY_RIGHT:
            x += 3
    camera_position = (x, y, z)


def setupCamera():
    glMatrixMode(GL_PROJECTION)  
    glLoadIdentity()  
    gluPerspective(fovY, 1.25, 0.1, 1500)
    glMatrixMode(GL_MODELVIEW)  
    glLoadIdentity()

    global lastx, lasty, lastz
    if camMode == "third":
        x, y, z = camera_position
        gluLookAt(x,y,z, 0,0,0, 0,0,1)
    if camMode == "first":
        angle = math.radians(playerAngle)
        gunLength = 50
        gunRight = 30
        gunUp = 40
        camX = playerPos[0] + gunRight * math.sin(angle) - math.cos(angle) * gunLength
        camY = playerPos[1] - gunRight * math.cos(angle) - math.sin(angle) * gunLength
        camZ = playerPos[2] + gunUp

        if camMode == "first" and cheat and gun:
            lookX = camX + (-math.cos(angle)) * 100
            lookY = camY + (-math.sin(angle)) * 100
            lookZ = camZ

            lastx = lookX
            lasty = lookY
            lastz = lookZ
        
        elif cheat and not gun:
            camX = cheatCamOffset[0] + 160
            camY = cheatCamOffset[1] 
            camZ = (playerPos[2] + cheatCamOffset[2]) -10
            lookX = playerPos[0] 
            lookY = playerPos[1] 
            lookZ = playerPos[2] 
        else:
            lookX = camX + (-math.cos(angle)) * 100
            lookY = camY + (-math.sin(angle)) * 100
            lookZ = camZ
        gluLookAt(camX, camY, camZ, lookX, lookY, lookZ, 0, 0, 1)  

def enemiesVsPlayer():
    global bullets, missiedBullets, score, life, gameStatus
    
    for e in enemies:
        dx = playerPos[0] - e['enemy_pos'][0]
        dy = playerPos[1] - e['enemy_pos'][1]
        
        dist = math.sqrt(dx**2 + dy**2)
        
        if dist > 1:
            e['enemy_pos'][0] += dx / dist * 0.05
            e['enemy_pos'][1] += dy / dist * 0.05
        e['scale'] += e['scale_dir']
        if e['scale'] >= 1.2 or e['scale'] <= 0.8:
            e['scale_dir'] *= -1
    
    if not gameStatus:
        for e in enemies:
            ex, ey, ez = e["enemy_pos"]
            px, py, pz = playerPos
    
            # Collision detection
            collision = abs(px - ex) < 100 and abs(py - ey) < 100 and abs(pz - ez) < 100
    
            if collision:
                if life > 0:
                    life -= 1
                    print(f"Remaining Player life: {life}")
                    enemies.remove(e)     
                    enemies.append(generateEnemyPosition()) 
                else:
                    gameStatus = True
                    enemies.clear()  
                break  

def shoot():
    global bullets, missiedBullets, gameStatus

    # fire bullets
    for bullet in bullets:
        bullet['bulletPosition'][0] += bullet['dir'][0] * 10
        bullet['bulletPosition'][1] += bullet['dir'][1] * 10

    b = 0
    while b < len(bullets):
        x, y, z = bullets[b]['bulletPosition']
        if abs(x) >= 600 or abs(y) >= 600:
            missiedBullets += 1
            print(f"Bullet missed: {missiedBullets}")
            bullets.pop(b)
        else:
            b += 1

    if missiedBullets >= 10 or life == 0:
        gameStatus = True
        enemies.clear()

def hit_enemy():
    global bullets, missiedBullets, score, life, gameStatus
    new_enemies = []
    hit_bullets = []

    for e in enemies:
        hit = False
        for b in bullets:
            bx, by, bz = b['bulletPosition']
            ex, ey, ez = e['enemy_pos']
            if abs(bx - ex) < 30 and abs(by - ey) < 30 and abs(bz - ez) < 30:
                hit = True
                score += 1
                hit_bullets.append(b)
                break
       
        if hit:
            new_enemies.append(generateEnemyPosition())  
        else:
            new_enemies.append(e)
    for b in hit_bullets:
        if b in bullets:
            bullets.remove(b) 
    enemies[:] = new_enemies

def cheat_mode():
    global playerAngle, playerPos, enemies, cheat_rotation, can_fire, score, bullets, missiedBullets

    if cheat and not gameStatus:
        # Rotate player slowly 
        rotate_speed = 1
        playerAngle = (playerAngle + rotate_speed) % 360
        cheat_rotation += rotate_speed

        if cheat_rotation >= 30:
            cheat_rotation = 0
            can_fire = True

        rad = math.radians(playerAngle)
        dirX = -math.cos(rad)
        dirY = -math.sin(rad)

        # Gun tip position
        gunLength = 140
        gunRight = 50
        gunUp = 10

        bx = playerPos[0] + gunRight * math.sin(rad) + dirX * gunLength
        by = playerPos[1] - gunRight * math.cos(rad) + dirY * gunLength
        bz = playerPos[2] + gunUp

        if can_fire:
            for e in enemies:
                ex, ey, ez = e["enemy_pos"]
                dx, dy = ex - bx, ey - by
                dist_xy = math.sqrt(dx ** 2 + dy ** 2)
                if dist_xy == 0:
                    continue
                
                dot = (dx * dirX + dy * dirY) / dist_xy

                if dot > 0.998:
                    dz = ez - bz
                    dist_total = math.sqrt(dx**2 + dy**2 + dz**2)
                    enemy_direction = [dx / dist_total, dy / dist_total, dz / dist_total]

                    # Fire bullet
                    bullets.append({
                        'bulletPosition': [bx, by, bz],
                        'dir': enemy_direction,
                        'cheat': True 
                    })

                    can_fire = False
                    print("Player bullet fired!")
                    break

    glutPostRedisplay()


def idle():
    shoot()
    hit_enemy()
    enemiesVsPlayer()
    cheat_mode()
    glutPostRedisplay()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  
    glViewport(0, 0, 1000, 700)  

    setupCamera()

    drawFloor(grid_size)
    drawWalls()

    # game info text
    if not gameStatus:
        draw_text(10, 460, f"Player Life Remaining: {life} ")
        draw_text(10, 440, f"Game Score: {score}")
        draw_text(10, 420, f"Player Bullet Missed: {missiedBullets}")
    else:
        draw_text(10, 460, f"Game is Over. Your score is {score}.")
        draw_text(10, 440, f'Press "R" to RESTART the Game.')

    drawPlayer()
    drawBullets()
    for e in enemies:
        drawEnemies(e)

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Double buffering, RGB color, depth test
    glutInitWindowSize(1000, 600)  # Window size
    glutInitWindowPosition(250, 0)  # Window position
    glutCreateWindow(b"3D OpenGL Intro")  #window
    
    glutDisplayFunc(showScreen)  #display function
    glutKeyboardFunc(keyboardListener)  #keyboard listener
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)  #idle function to move the bullet automatically

    glutMainLoop()  #GLUT main loop

if __name__ == "__main__":
    main()