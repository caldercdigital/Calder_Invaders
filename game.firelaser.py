import pgzrun
player = Actor("player", (400, 550)) # Load in the player Actor image

def draw(): 
    screen.blit('background', (0, 0))
    player.draw()
    drawLasers()

def update():
    global player,lasers
    checkKeys()
    updateLasers()

def drawLasers():
    for l in range(len(lasers)): lasers[l].draw()

def checkKeys():
    global player, lasers
    if keyboard.left:
        if player.x > 40: player.x -= 5
    if keyboard.right:
        if player.x < 760: player.x += 5
    if keyboard.space:
        if player.laserActive == 1:
            player.laserActive = 0
            clock.schedule(makeLaserActive, 1.0)
            l = len(lasers)
            lasers.append(Actor("laser2", (player.x,player.y-32)))
            lasers[l].status = 0
            lasers[l].type = 1

def makeLaserActive():
    global player
    player.laserActive = 1

def updateLasers():
    global lasers
    for l in range(len(lasers)):
        if lasers[l].type == 1:
            lasers[l].y -= 5
            if lasers[l].y < 10: lasers[l].status = 1

def init():
    global lasers
    lasers = [] 
    player.laserActive = 1

init()
pgzrun.go()
