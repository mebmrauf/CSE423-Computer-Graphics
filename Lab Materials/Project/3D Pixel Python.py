from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
import math

# Game state variables
gridSize = 14
cellSize = 40
halfCellSize = cellSize/2
gridLength = gridSize * cellSize
gridOffset = gridLength / 2

# Camera-related variables
cameraDistance = 500
cameraHeight = 400
cameraAngle = 180
fovY = 60

# Controls for camera movement
zoomSpeed = 20
rotationSpeed = 2

# Snake variables
snakePositions = [(gridSize//2, gridSize//2)]
snakeDirection = (1, 0)
snakeSpeed = 0.2
snakeLastMoveTime = 0
foodCount = 0
specialActive = False

# Food variables
foodPosition = None
specialFoodPosition = None
foodSizeMultiplier = 1.3
specialFoodSizeMultiplier = 1.5
doublePointsActive = False
doublePointsStartTime = 0
doublePointsDuration = 10
doublePointsElapsedTime = 0
doublePointsLastUpdateTime = 0

# Bomb variables
bombs = []
bombLastSpawnTime = 0
bombSpawnInterval = 10
bombLifetime = 5
# Pause-aware Bomb Timing
# Track bomb elapsed time
bombelapsedTime = 0
lastUpdateTime = 0

# Obstacles
obstaclesPositions = []

# Background color
backgroundColor = (0.5, 0.8, 0.9)

# Game state
gameState = "START"
difficultyLevel = ""
score = 0

buttons = {
    "play": {"x": 900, "y": 750, "width": 80, "height": 30, "text": "Play", "active": True},
    "pause": {"x": 900, "y": 750, "width": 80, "height": 30, "text": "Pause", "active": False},
    "easy": {"x": 360, "y": 350, "width": 120, "height": 40, "text": "Easy", "active": True, "selected": False},
    "medium": {"x": 360, "y": 300, "width": 120, "height": 40, "text": "Medium", "active": True, "selected": False},
    "hard": {"x": 360, "y": 250, "width": 120, "height": 40, "text": "Hard", "active": True, "selected": False},
    "start": {"x": 350, "y": 190, "width": 200, "height": 50, "text": "Start Game", "active": False},
}

def changeBackgroundColor():
    global backgroundColor
    backgroundColor = (random.uniform(0.4, 1.0), random.uniform(0.4, 1.0), random.uniform(0.4, 1.0))
    glClearColor(*backgroundColor, 1.0)

def convertCoordinate(x, y):
    a = x
    b = 800 - y
    return a, b

def convertWorldCoordinate(x, y):
    actualX = x * cellSize - gridOffset + halfCellSize
    actualY = y * cellSize - gridOffset + halfCellSize
    return actualX, actualY

def getAvailablePositions(otherFoodPosition, minDistFromObstacles):
    global snakePositions, obstaclesPositions
    availablePositions = []
    for x in range(gridSize):
        for y in range(gridSize):
            position = (x, y)
            if position in snakePositions:
                continue
            if position in obstaclesPositions:
                continue
            if position == otherFoodPosition:
                continue
            isValidDistance = True
            for obstacleX, obstacleY in obstaclesPositions:
                distance = abs(x - obstacleX) + abs(y - obstacleY)
                if distance < minDistFromObstacles:
                    isValidDistance = False
                    break
            if isValidDistance:
                availablePositions.append(position)
    return availablePositions

def generateFood():
    global foodPosition, specialFoodPosition
    minDistFromObstacles = 2
    availablePositions = getAvailablePositions(specialFoodPosition, minDistFromObstacles)
    if availablePositions:
        foodPosition = random.choice(availablePositions)
    else:
        foodPosition = None

def generateSpecialFood():
    global specialFoodPosition, foodPosition
    minDistFromObstacles = 4
    availablePositions = getAvailablePositions(specialFoodPosition, minDistFromObstacles)
    if availablePositions:
        specialFoodPosition = random.choice(availablePositions)
    else:
        specialFoodPosition = None
       
def generateObstacles():
    global obstaclesPositions, snakePositions, foodPosition, specialFoodPosition
    numOfObstacleGroups = 3
    blocksPerGroup = 5
    if difficultyLevel == "MEDIUM":
        numOfObstacleGroups = 5
    elif difficultyLevel == "HARD":
        numOfObstacleGroups = 8

    obstaclesPositions = []
    availablePositions = []

    headX, headY = snakePositions[0]
    directionX, directionY = snakeDirection
    positionInFrontOfSnake = (headX + directionX, headY + directionY)

    for x in range(gridSize):
        for y in range(gridSize):
            position = (x, y)
            if position in snakePositions:
                continue
            if position == foodPosition:
                continue
            if position == specialFoodPosition:
                continue
            if position == positionInFrontOfSnake:
                continue
            availablePositions.append(position)

    for i in range(numOfObstacleGroups):
        if not availablePositions:
            break
        positionX, positionY = random.choice(availablePositions)
        groupPositions = [(positionX, positionY)]
        for i in range(blocksPerGroup - 1):
            neighbors = []
            lastX, lastY = groupPositions[-1]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                neighbor = (lastX + dx, lastY + dy)
                if neighbor in availablePositions:
                    neighbors.append(neighbor)
            if neighbors:
                nextBlock = random.choice(neighbors)
                groupPositions.append(nextBlock)
                availablePositions.remove(nextBlock)
            else:
                break
        obstaclesPositions.extend(groupPositions)

def generateBombs():
    global bombs, bombLastSpawnTime
    maximumNoOfBombs = 1
    if difficultyLevel == "MEDIUM":
        maximumNoOfBombs = 2
    elif difficultyLevel == "HARD":
        maximumNoOfBombs = 3
    bombs = []
    # Generate new bombs
    for i in range(maximumNoOfBombs):
        occupiedPositions = snakePositions.copy()
        if foodPosition:
            occupiedPositions.append(foodPosition)
        if specialFoodPosition:
            occupiedPositions.append(specialFoodPosition)
        occupiedPositions.extend(bombs)
        occupiedPositions.extend(obstaclesPositions)
        availablePositions = []
        for x in range(gridSize):
            for y in range(gridSize):
                position = (x, y)
                if position not in occupiedPositions:
                    availablePositions.append(position)
        if availablePositions:
            bombs.append(random.choice(availablePositions))
    bombLastSpawnTime = time.time()

def updateBombs():
    global bombs, bombLastSpawnTime, gameState, bombelapsedTime, lastUpdateTime
    if gameState == "GAME_OVER":
        bombs = []
        return
    currentTime = time.time()
    if gameState == "PLAYING":
        if lastUpdateTime == 0:
            lastUpdateTime = currentTime
        deltaTime = currentTime - lastUpdateTime
        bombelapsedTime += deltaTime
        lastUpdateTime = currentTime
        if bombelapsedTime > bombSpawnInterval:
            generateBombs()
            bombelapsedTime = 0
        if bombs and bombelapsedTime > bombLifetime:
            bombs = []

def drawBombs():
    global bombs
    for bombPosition  in bombs:
        x, y = bombPosition
        actualX, actualY = convertWorldCoordinate(x, y)
        glPushMatrix()
        glTranslatef(actualX, actualY, halfCellSize)
        glColor3f(0.0, 0.0, 0.0)
        gluSphere(gluNewQuadric(), cellSize * 0.35, 16, 16)
        glPushMatrix()
        glTranslatef(0, 0, cellSize * 0.25)
        glColor3f(1.0, 0.0, 0.0)  # Red
        gluSphere(gluNewQuadric(), cellSize * 0.15, 8, 8)
        glPopMatrix()
        glPopMatrix()
         
def resetGame():
    global snakePositions, snakeDirection, foodPosition, specialFoodPosition, foodCount, score, gameState, snakeSpeed, specialActive, snakeLastMoveTime, obstaclesPositions, bombs, bombLastSpawnTime, bombelapsedTime, lastUpdateTime, doublePointsActive, doublePointsStartTime, doublePointsElapsedTime, doublePointsLastUpdateTime
    doublePointsActive = False
    doublePointsStartTime = 0
    doublePointsElapsedTime = 0
    doublePointsLastUpdateTime = 0  
    bombs = []
    bombLastSpawnTime = time.time()
    bombelapsedTime = 0
    lastUpdateTime = 0
    while True:
        snakePositions = [(gridSize // 2, gridSize // 2)]
        snakeDirection = (1, 0)
        generateObstacles()
        headX, headY = snakePositions[0]
        nextX = headX + snakeDirection[0]
        nextY = headY + snakeDirection[1]
        isValid = True
        positionsToCheck = [snakePositions[0], (nextX, nextY)]
        for pos in positionsToCheck:
            if pos in obstaclesPositions:
                isValid = False
                break
        if isValid:
            break
    foodPosition = None
    specialFoodPosition = None
    generateFood()
    foodCount = 0
    specialActive = False
    score = 0
    if difficultyLevel == "EASY":
        snakeSpeed = 0.3
    elif difficultyLevel == "MEDIUM":
        snakeSpeed = 0.2
    else:
        snakeSpeed = 0.1
    snakeLastMoveTime = 0
    gameState = "PAUSED"

def moveSnake():
    global snakePositions, foodPosition, specialFoodPosition, score, foodCount, gameState, doublePointsActive, doublePointsStartTime, snakeSpeed, specialActive, obstaclesPositions
    if gameState != "PLAYING":
        return
    headX, headY = snakePositions[0]
    directionX, directionY = snakeDirection
    newHead = ((headX + directionX) % gridSize, (headY + directionY) % gridSize)
    if newHead in snakePositions:
        gameOver()
        return
    if newHead in bombs:
        bombs.clear()
        gameOver()
        return
    if newHead in obstaclesPositions:
        gameOver()
        return
    snakePositions.insert(0, newHead)
    if newHead == foodPosition:
        pointsToAdd = 2 if doublePointsActive else 1
        score += pointsToAdd
        foodCount += 1
        foodPosition = None
        generateFood()
        if foodCount == 5:
            generateSpecialFood()
            foodCount = 0
        if score % 5 == 0:
            generateObstacles()
        if score % 7 == 0:
            changeBackgroundColor()
    elif newHead == specialFoodPosition:
        doublePointsActive = True
        doublePointsStartTime = time.time()
        snakeSpeed *= 0.8
        specialFoodPosition = None
        specialActive = False
    elif foodPosition is not None:
        snakePositions.pop()

def gameOver():
    global gameState, foodPosition, specialFoodPosition, specialActive, doublePointsActive
    gameState = "GAME_OVER"
    foodPosition = None
    specialFoodPosition = None
    specialActive = False
    doublePointsActive = False

def gameStateChange(oldState, newState):
    global lastUpdateTime, doublePointsLastUpdateTime
    if oldState != "PLAYING" and newState == "PLAYING":
        lastUpdateTime = time.time()
        if doublePointsActive:
            doublePointsLastUpdateTime = time.time()
    elif oldState == "PLAYING" and newState != "PLAYING":
        lastUpdateTime = 0
        if doublePointsActive:
            doublePointsLastUpdateTime = 0

def drawObstacles():
    for x, y in obstaclesPositions:
        actualX, actualY = convertWorldCoordinate(x, y)
        glPushMatrix()
        glTranslatef(actualX, actualY, halfCellSize)
        glColor3f(0.5, 0.5, 0.5)
        glutSolidCube(cellSize * 0.8)
        glPopMatrix()

def drawGrid():
    glPushMatrix()
    for x in range(gridSize):
        for y in range(gridSize):
            if (x + y) % 2 == 0:
                glColor3f(0.8, 0.7, 0.9)
            else:
                glColor3f(0.4, 0.2, 0.5)
            actualX = x * cellSize - gridOffset
            actualY = y * cellSize - gridOffset
            glPushMatrix()
            glTranslatef(actualX + halfCellSize, actualY + halfCellSize, -3)
            glBegin(GL_QUADS)
            glVertex3f(-halfCellSize, -halfCellSize, 3)
            glVertex3f(halfCellSize, -halfCellSize, 3)
            glVertex3f(halfCellSize, halfCellSize, 3)
            glVertex3f(-halfCellSize, halfCellSize, 3)
            glEnd()
            if (x + y) % 2 == 0:
                glColor3f(0.7, 0.7, 0.3)
            else:
                glColor3f(0.2, 0.4, 0.2)
            glBegin(GL_QUADS)
            glVertex3f(-halfCellSize, -halfCellSize, 0)
            glVertex3f(halfCellSize, -halfCellSize, 0)
            glVertex3f(halfCellSize, -halfCellSize, 3)
            glVertex3f(-halfCellSize, -halfCellSize, 3)

            glVertex3f(halfCellSize, -halfCellSize, 0)
            glVertex3f(halfCellSize, halfCellSize, 0)
            glVertex3f(halfCellSize, halfCellSize, 3)
            glVertex3f(halfCellSize, -halfCellSize, 3)

            glVertex3f(halfCellSize, halfCellSize, 0)
            glVertex3f(-halfCellSize, halfCellSize, 0)
            glVertex3f(-halfCellSize, halfCellSize, 3)
            glVertex3f(halfCellSize, halfCellSize, 3)

            glVertex3f(-halfCellSize, halfCellSize, 0)
            glVertex3f(-halfCellSize, -halfCellSize, 0)
            glVertex3f(-halfCellSize, -halfCellSize, 3)
            glVertex3f(-halfCellSize, halfCellSize, 3)
            glEnd()
           
            glPopMatrix()
    glPopMatrix()

def drawSnake():
    if not snakePositions:
        return
    headX, headY = snakePositions[0]
    drawSnakeBodyParts(headX, headY, "head")
    for i in range(1, len(snakePositions)-1):
        x, y = snakePositions[i]
        drawSnakeBodyParts(x, y, "body")
    if len(snakePositions) > 1:
        tailX, tailY = snakePositions[-1]
        drawSnakeBodyParts(tailX, tailY, "tail")

def drawSnakeBodyParts(x, y, partsType):
    actualX, actualY = convertWorldCoordinate(x, y)
    glPushMatrix()
    glTranslatef(actualX, actualY, halfCellSize)
    if partsType == "head":
        drawSnakeHead()
    elif partsType == "body":
        if doublePointsActive:
            glColor3f(0.369, 0.604, 0.737)
        else:
            glColor3f(0.0, 0.8, 0.2)
        gluSphere(gluNewQuadric(), cellSize * 0.5, 16, 16)
    elif partsType == "tail":
        if doublePointsActive:
            glColor3f(0.369, 0.604, 0.737)
        else:
            glColor3f(0.0, 0.6, 0.1)
        gluSphere(gluNewQuadric(), cellSize * 0.4, 16, 16)
    glPopMatrix()

def drawSnakeHead():
    if doublePointsActive:
        glColor3f(0.369, 0.604, 0.737)
    else:
        glColor3f(0.0, 0.9, 0.2)
    gluSphere(gluNewQuadric(), cellSize * 0.55, 16, 16)
    directionX, directionY = snakeDirection
    if directionX == 1:
        headAngle = 0
    elif directionX == -1:
        headAngle = 180
    elif directionY == 1:
        headAngle = 90
    else:
        headAngle = 270
    glRotatef(headAngle, 0, 0, 1)

    glPushMatrix()
    glTranslatef(cellSize * 0.3, cellSize * 0.25, cellSize * 0.3)
    glColor3f(1.0, 1.0, 1.0)
    gluSphere(gluNewQuadric(), cellSize * 0.12, 8, 8)
   
    glTranslatef(cellSize * 0.06, 0, cellSize * 0.06)
    glColor3f(0.0, 0.0, 0.0)
    gluSphere(gluNewQuadric(), cellSize * 0.06, 8, 8)
    glPopMatrix()
   
    glPushMatrix()
    glTranslatef(cellSize * 0.3, -cellSize * 0.25, cellSize * 0.3)
    glColor3f(1.0, 1.0, 1.0)
    gluSphere(gluNewQuadric(), cellSize * 0.12, 8, 8)
   
    glTranslatef(cellSize * 0.06, 0, cellSize * 0.06)
    glColor3f(0.0, 0.0, 0.0)
    gluSphere(gluNewQuadric(), cellSize * 0.06, 8, 8)
    glPopMatrix()

    glColor3f(0.9, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(cellSize * 0.45, 0, 0)
    glRotatef(90, 0, 1, 0)
    gluSphere(gluNewQuadric(), cellSize * 0.12, 12, 8)
    glPopMatrix()

def drawFood():
    if foodPosition:
        x, y = foodPosition
        actualX, actualY = convertWorldCoordinate(x, y)
        glPushMatrix()
        glTranslatef(actualX, actualY, halfCellSize)
        glColor3f(1.0, 0.1, 0.1)
        glutSolidSphere(cellSize * 0.35 * foodSizeMultiplier, 16, 16)

        glPushMatrix()
        glColor3f(0.5, 0.25, 0.0)
        glTranslatef(0, 0, cellSize * 0.25 * foodSizeMultiplier)
        glRotatef(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), cellSize * 0.05 * foodSizeMultiplier, cellSize * 0.05 * foodSizeMultiplier, cellSize * 0.15 * foodSizeMultiplier, 8, 2)
        glPopMatrix()
        glPopMatrix()

def drawSpecialFood():
    if specialFoodPosition:
        x, y = specialFoodPosition
        actualX, actualY = convertWorldCoordinate(x, y)
        glPushMatrix()
        glTranslatef(actualX, actualY, halfCellSize)
        glRotatef(time.time() * 60 % 360, 0, 0, 1)
   
        blueGlow = 0.5 + 0.5 * math.sin(time.time() * 3.0)
        glColor3f(0.1, blueGlow, 1.0)
        starPoints = 5
        outerRadius = cellSize * 0.4 * specialFoodSizeMultiplier
        innerRadius = cellSize * 0.2 * specialFoodSizeMultiplier
        height = cellSize * 0.2 * specialFoodSizeMultiplier
        glBegin(GL_TRIANGLES)
        for i in range(starPoints * 2):
            angle1 = math.pi * i / starPoints
            angle2 = math.pi * (i + 1) / starPoints
           
            radius1 = outerRadius if i % 2 == 0 else innerRadius
            radius2 = outerRadius if (i + 1) % 2 == 0 else innerRadius
           
            # Top face vertices (center to outer points)
            x1Top = radius1 * math.cos(angle1)
            y1Top = radius1 * math.sin(angle1)
            x2Top = radius2 * math.cos(angle2)
            y2Top = radius2 * math.sin(angle2)
           
            # Bottom face vertices (center to outer points)
            x1Bottom = radius1 * math.cos(angle1)
            y1Bottom = radius1 * math.sin(angle1)
            x2Bottom = radius2 * math.cos(angle2)
            y2Bottom = radius2 * math.sin(angle2)
           
            # Top face triangle (center to adjacent points)
            glVertex3f(0, 0, height)
            glVertex3f(x1Top, y1Top, height / 2)
            glVertex3f(x2Top, y2Top, height / 2)
           
            # Bottom face triangle (center to adjacent points)
            glVertex3f(0, 0, -height)
            glVertex3f(x1Bottom, y1Bottom, -height / 2)
            glVertex3f(x2Bottom, y2Bottom, -height / 2)
           
            # Side faces (top to bottom)
            # First side triangle (top and bottom)
            glVertex3f(x1Top, y1Top, height / 2)
            glVertex3f(x1Bottom, y1Bottom, -height / 2)
            glVertex3f(x2Top, y2Top, height / 2)

            # Second side triangle (top and bottom)
            glVertex3f(x2Top, y2Top, height / 2)
            glVertex3f(x1Bottom, y1Bottom, -height / 2)
            glVertex3f(x2Bottom, y2Bottom, -height / 2)
        glEnd()
        glPopMatrix()


def updateDoublePointsStatus():
    global doublePointsActive, doublePointsStartTime, doublePointsElapsedTime, doublePointsLastUpdateTime, snakeSpeed
    if doublePointsActive and gameState == "PLAYING":
        currentTime = time.time()
        if doublePointsLastUpdateTime == 0:
            doublePointsLastUpdateTime = currentTime
        deltaTime = currentTime - doublePointsLastUpdateTime
        doublePointsElapsedTime += deltaTime
        doublePointsLastUpdateTime = currentTime
        if doublePointsElapsedTime > doublePointsDuration:
            doublePointsActive = False
            doublePointsElapsedTime = 0
            doublePointsLastUpdateTime = 0
            if difficultyLevel == "EASY":
                snakeSpeed = 0.3
            elif difficultyLevel == "MEDIUM":
                snakeSpeed = 0.2
            else:
                snakeSpeed = 0.1

def drawButtons():
    global buttons, difficultyLevel
    visibleButtons = []
   
    if gameState == "START":
        visibleButtons = ["easy", "medium", "hard"]
        if buttons["easy"]["selected"] or buttons["medium"]["selected"] or buttons["hard"]["selected"]:
            visibleButtons.append("start")
    elif gameState == "PLAYING":
        visibleButtons = ["pause"]
    elif gameState == "PAUSED":
        visibleButtons = ["play"]
    elif gameState == "GAME_OVER":
        visibleButtons = ["start"]
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    for buttonName in visibleButtons:
        button = buttons[buttonName]
        isSelected = button.get("selected", False)
        if isSelected:
            glColor3f(0.0, 1.0, 0.0)
            glLineWidth(3.0)
        else:
            glColor3f(0.0, 0.0, 0.0)
            glLineWidth(2.0)
           
        glBegin(GL_LINES)
        # upper line
        glVertex2f(button["x"], button["y"])
        glVertex2f(button["x"] + button["width"], button["y"])
        # bottom line
        glVertex2f(button["x"] + button["width"], button["y"] - button["height"])
        glVertex2f(button["x"], button["y"] - button["height"])
        # left line
        glVertex2f(button["x"], button["y"])
        glVertex2f(button["x"], button["y"] - button["height"])
        # right line
        glVertex2f(button["x"] + button["width"], button["y"])
        glVertex2f(button["x"] + button["width"], button["y"] - button["height"])
        glEnd()

        glColor3f(0.0, 0.0, 0.0)
        textX = button["x"] + (button["width"] - len(button["text"]) * 8) / 2
        textY = button["y"] - button["height"]/2 - 5
        drawText(textX, textY, button["text"])
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
 

def drawText(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(0.0, 0.0, 0.0)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))

def drawScore():
    global cameraAngle, gameState
    if gameState in ["PLAYING", "PAUSED", "GAME_OVER"]:
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, 1000, 0, 800)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        if cameraAngle % 90 == 0:
            angle_status = f"Camera Angle: {cameraAngle % 360}° (Exact)"
        else:
            angle_status = f"Camera Angle: {cameraAngle % 360}° (Not Exact)"
        if doublePointsActive:
            # Calculate remaining time based on elapsed time instead of wall clock time
            remainingTime = doublePointsDuration - doublePointsElapsedTime
            if remainingTime > 0 and gameState != "GAME_OVER":
                drawText(10, 680, f"DOUBLE POINTS: {remainingTime:.1f}s")
       
        if gameState == "GAME_OVER":
            drawText(400, 650, "GAME OVER", GLUT_BITMAP_TIMES_ROMAN_24)
            drawText(410, 620, f"Final Score: {score}")
       
        glColor3f(0.0, 0.0, 0.0)
        if gameState != "GAME_OVER":
            drawText(10, 770, f"Score: {score}")
            drawText(10, 740, f"Difficulty: {difficultyLevel}")
            drawText(10, 710, angle_status)
            drawText(400, 760, "Please rotate the board", GLUT_BITMAP_HELVETICA_18)
            drawText(380, 740, "to an exact 0, 90, 180 or 270", GLUT_BITMAP_HELVETICA_18)
            drawText(350, 720, "degree angle to control the snake properly", GLUT_BITMAP_HELVETICA_18)
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

def drawStartScreen():
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glColor3f(0.0, 0.0, 0.0)
    drawText(400, 700, "3D SNAKE GAME", GLUT_BITMAP_TIMES_ROMAN_24)
    glColor3f(0.0, 0.0, 0.0)
    drawText(350, 650, "Instructions:", GLUT_BITMAP_HELVETICA_18)
    drawText(350, 620, "- Use Arrow Keys to control the snake", GLUT_BITMAP_HELVETICA_12)
    drawText(350, 600, "- Eat apples to grow longer", GLUT_BITMAP_HELVETICA_12)
    drawText(350, 580, "- Collect special blue stars for speed boost", GLUT_BITMAP_HELVETICA_12)
    drawText(350, 560, "- Press P or Space to pause/resume", GLUT_BITMAP_HELVETICA_12)
    drawText(350, 540, "- Press R to restart the game", GLUT_BITMAP_HELVETICA_12)
    drawText(350, 520, "- Please select a difficulty level to enable the Start Game button", GLUT_BITMAP_HELVETICA_12)
    drawText(350, 490, "Camera Controls:", GLUT_BITMAP_HELVETICA_18)
    drawText(350, 460, "- X/Y keys: Zoom in/out", GLUT_BITMAP_HELVETICA_12)
    drawText(350, 440, "- W/S keys: Adjust camera height", GLUT_BITMAP_HELVETICA_12)
    drawText(350, 420, "- A/D keys: Rotate camera", GLUT_BITMAP_HELVETICA_12)
    drawText(350, 370, "Select Difficulty:", GLUT_BITMAP_HELVETICA_18)
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def setup_camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 2000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    angleRad = math.radians(cameraAngle)

    cameraX = cameraDistance * math.sin(angleRad)
    cameraY = cameraDistance * math.cos(angleRad)
    cameraZ = cameraHeight

    gluLookAt(cameraX, cameraY, cameraZ,
              0, 0, 0,
              0, 0, 1)

def keyboardListener(key, x, y):
    global gameState, buttons, cameraDistance, cameraAngle, cameraHeight, snakeDirection
    oldState = gameState
    if key == b'r':
        resetGame()
    elif key == b'p' or key == b' ':
        if gameState == "PLAYING":
            gameState = "PAUSED"
            buttons["play"]["active"] = True
            buttons["pause"]["active"] = False
        elif gameState == "PAUSED":
            gameState = "PLAYING"
            buttons["play"]["active"] = False
            buttons["pause"]["active"] = True
    elif key == b'x':
        cameraDistance = max(100, cameraDistance - zoomSpeed)
    elif key == b'y':
        cameraDistance = min(1000, cameraDistance + zoomSpeed)
    elif key == b'w':
        cameraHeight = min(800, cameraHeight + zoomSpeed)
    elif key == b's':
        cameraHeight = max(100, cameraHeight - zoomSpeed)
    elif key == b'a':
        cameraAngle = (cameraAngle + rotationSpeed) % 360
    elif key == b'd':
        cameraAngle = (cameraAngle - rotationSpeed) % 360
    elif key == b'\x1b':
        glutLeaveMainLoop()
    if oldState != gameState:
        gameStateChange(oldState, gameState)

def specialKeyListener(key, x, y):
    global snakeDirection
    if gameState != "PLAYING":
        return
    normalizedAngle = (cameraAngle % 360) // 90 * 90
    if normalizedAngle == 0:
        up = (0, -1)
        down = (0, 1)
        left = (1, 0)
        right = (-1, 0)
    elif normalizedAngle == 90:
        up = (-1, 0)
        down = (1, 0)
        left = (0, -1)
        right = (0, 1)
    elif normalizedAngle == 180:
        up = (0, 1)
        down = (0, -1)
        left = (-1, 0)
        right = (1, 0)
    elif normalizedAngle == 270:
        up = (1, 0)
        down = (-1, 0)
        left = (0, 1)
        right = (0, -1)
    if key == GLUT_KEY_UP and snakeDirection != down:
        snakeDirection = up
    elif key == GLUT_KEY_DOWN and snakeDirection != up:
        snakeDirection = down
    elif key == GLUT_KEY_LEFT and snakeDirection != right:
        snakeDirection = left
    elif key == GLUT_KEY_RIGHT and snakeDirection != left:
        snakeDirection = right

def mouseListener(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        global gameState, difficultyLevel, buttons
        oldState = gameState
        mouseX, mouseY = convertCoordinate(x, y)
        visibleButtons = []
        if gameState == "START":
            visibleButtons = ["easy", "medium", "hard"]
            if difficultyLevel != "":
                visibleButtons.append("start")
        elif gameState == "PLAYING":
            visibleButtons = ["pause"]
        elif gameState == "PAUSED":
            visibleButtons = ["play"]
        elif gameState == "GAME_OVER":
            visibleButtons = ["start"]
        for buttonName in visibleButtons:
            button = buttons[buttonName]
            if (button["x"] <= mouseX <= button["x"] + button["width"] and
                button["y"] - button["height"] <= mouseY <= button["y"]):
                if buttonName == "play":
                    gameState = "PLAYING"
                    buttons["play"]["active"] = False
                    buttons["pause"]["active"] = True
                elif buttonName == "pause":
                    gameState = "PAUSED"
                    buttons["play"]["active"] = True
                    buttons["pause"]["active"] = False
                elif buttonName == "start":
                    resetGame()
                elif buttonName in ["easy", "medium", "hard"]:
                    buttons["easy"]["selected"] = False
                    buttons["medium"]["selected"] = False
                    buttons["hard"]["selected"] = False
                    buttons[buttonName]["selected"] = True
                    difficultyLevel = buttonName.upper()
                    buttons["start"]["active"] = True
                    print(f"Difficulty set to {difficultyLevel}")
                glutPostRedisplay()
                if oldState != gameState:
                    gameStateChange(oldState, gameState)
                return True
        return False

def idle():
    global snakeLastMoveTime, gameState
    currentTime = time.time()
    if gameState == "PLAYING" and currentTime - snakeLastMoveTime > snakeSpeed:
        moveSnake()
        snakeLastMoveTime = currentTime
        if foodPosition is None:
            generateFood()
    updateBombs()
    updateDoublePointsStatus()
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    setup_camera()
    if gameState == "START":
        drawStartScreen()
    elif gameState != "START":
        drawGrid()
        drawObstacles()
        drawFood()
        drawSpecialFood()
        drawBombs()
        drawSnake()
    drawButtons()
    drawScore()
    glutSwapBuffers()

def initialize():
    global difficultyLevel
    glClearColor(*backgroundColor, 1.0)
    generateFood()
    difficultyLevel = ""

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutCreateWindow(b"3D Snake Game")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)
    initialize()
    glutMainLoop()
   
if __name__ == "__main__":
    main()