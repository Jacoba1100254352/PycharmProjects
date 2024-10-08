import sys

import pgzrun


mod = sys.modules['__main__']

WIDTH = 650
HEIGHT = 500

rocket = mod.Actor("small_rocket", (WIDTH / 2, HEIGHT - 50))
shields = []
x = 50

for i in range(3):
	shield = mod.Rect((x, 350), (120, 40))
	shields.append(shield)
	x += 210

enemies = []
aliens = ["alien2", "alien_ship2", "alien3"]
alienProjectiles = []

y = 80
index = 0
for j in range(3):
	x = 100
	row = []
	for i in range(5):
		alien = mod.Actor(aliens[index], (x, y))
		alien.xspeed = 4
		row.append(alien)
		x += 50
	
	enemies.append(row)
	index += 1
	y += 40

score = 0
lives = 3

fired = False
projectile = mod.Rect((rocket.x, rocket.y), (5, 10))

gameState = "start"

# pause buttons
pause = mod.Actor("pause", (630, 20))
restart = mod.Rect((WIDTH / 2 - 75, 230), (150, 50))
continueButton = mod.Rect((WIDTH / 2 - 75, 150), (150, 50))
quitButton = mod.Rect((WIDTH / 2 - 75, 310), (150, 50))

# music and sounds
sound = mod.Actor("volume", (WIDTH / 2 - 50, 100))
soundOn = True
musicPlayer = mod.Actor("music", (WIDTH / 2 + 50, 100))
musicOn = True

mod.music.play("tune.mp3")


def draw():
	mod.screen.clear()
	
	if gameState == "play":
		rocket.draw()
		pause.draw()
		
		for p in alienProjectiles:
			mod.screen.draw.filled_rect(p, (50, 255, 50))
		
		for e in range(len(enemies)):
			for s in range(len(enemies[e])):
				enemies[e][s].draw()
		
		for s in shields:
			mod.screen.draw.filled_rect(s, (255, 255, 255))
		
		if fired:
			mod.screen.draw.filled_rect(projectile, (255, 50, 50))
		
		mod.screen.draw.text("Lives: " + str(lives), center=(50, 20), fontsize=30, color=(255, 255, 255))
		mod.screen.draw.text("Score: " + str(score), center=(50, 50), fontsize=30, color=(255, 255, 255))
	
	elif gameState == "start":
		mod.screen.draw.text("Press Enter to Start the Game!", center=(WIDTH / 2, HEIGHT / 2), fontsize=40,
		                     color=(255, 255, 255))
	
	elif gameState == "end":
		mod.screen.draw.text("Game Over!\nPress Enter to Play Again \nor Escape to Quit!",
		                     center=(WIDTH / 2, HEIGHT / 2), fontsize=40, color=(255, 255, 255))
	
	else:
		sound.draw()
		musicPlayer.draw()
		mod.screen.draw.text("Pause", center=(WIDTH / 2, 50), fontsize=50, color=(255, 255, 255))
		mod.screen.draw.filled_rect(continueButton, (147, 112, 219))
		mod.screen.draw.text("Continue", center=(WIDTH / 2, 175), fontsize=30, color=(255, 255, 255))
		mod.screen.draw.filled_rect(restart, (147, 112, 219))
		mod.screen.draw.text("Restart", center=(WIDTH / 2, 255), fontsize=30, color=(255, 255, 255))
		mod.screen.draw.filled_rect(quitButton, (147, 112, 219))
		mod.screen.draw.text("Quit", center=(WIDTH / 2, 335), fontsize=30, color=(255, 255, 255))


def on_mouse_down(pos):
	global gameState, soundOn, musicOn
	
	if gameState == "play":
		if pause.collidepoint(pos):
			gameState = "pause"
	
	elif gameState == "pause":
		if continueButton.collidepoint(pos):
			gameState = "play"
		
		if restart.collidepoint(pos):
			gameState = "start"
		
		if quitButton.collidepoint(pos):
			quit()
		
		if sound.collidepoint(pos):
			if soundOn:
				sound.image = "no_volume"
			
			else:
				sound.image = "volume"
			
			soundOn = not soundOn
		
		if musicPlayer.collidepoint(pos):
			if musicOn:
				musicPlayer.image = "no_music"
				mod.music.pause()
			else:
				musicPlayer.image = "music"
				mod.music.unpause()
			musicOn = not musicOn


def on_key_down(key):
	global fired
	
	if key == mod.keys.SPACE and not fired:
		fired = True
		
		if soundOn:
			mod.sounds.laser.play()


def alienFire1():
	if len(enemies) >= 1:
		p1 = mod.Rect((enemies[0][0].x, enemies[0][0].y), (5, 10))
		alienProjectiles.append(p1)
		
		if soundOn:
			mod.sounds.laser2.play()
	
	mod.clock.schedule_unique(alienFire2, 1.0)


def alienFire2():
	if len(enemies) >= 2:
		p2 = mod.Rect((enemies[1][0].x, enemies[1][0].y), (5, 10))
		alienProjectiles.append(p2)
		
		if soundOn:
			mod.sounds.laser2.play()
	
	mod.clock.schedule_unique(alienFire3, 1.0)


def alienFire3():
	if len(enemies) >= 3:
		p3 = mod.Rect((enemies[2][0].x, enemies[2][0].y), (5, 10))
		alienProjectiles.append(p3)
		
		if soundOn:
			mod.sounds.laser2.play()


def updateAlienProjectiles():
	global lives
	
	for p in alienProjectiles:
		p.y += 5
		
		if rocket.colliderect(p):
			lives -= 1
			alienProjectiles.remove(p)
		
		if p.bottom >= HEIGHT:
			alienProjectiles.remove(p)


def resetAliens():
	enemies.clear()
	
	y = 80
	index = 0
	for _ in range(3):
		x = 100
		row = []
		for _ in range(5):
			alien = mod.Actor(aliens[index], (x, y))
			alien.xspeed = 4
			row.append(alien)
			x += 50
		
		enemies.append(row)
		index += 1
		y += 40


def moveRocket():
	if mod.keyboard.left and rocket.left > 0:
		rocket.x -= 10
	
	if mod.keyboard.right and rocket.right < WIDTH:
		rocket.x += 10


def moveAliens():
	for e in range(len(enemies)):
		for s in range(len(enemies[e])):
			enemies[e][s].x += enemies[e][s].xspeed


def checkCollision():
	for e in enemies:
		if e[0].left <= 0:
			changeDirection()
		
		if e[len(e) - 1].right >= WIDTH:
			changeDirection()


def changeDirection():
	for e in range(len(enemies)):
		for s in range(len(enemies[e])):
			enemies[e][s].xspeed *= -1
			enemies[e][s].y += 1


def moveProjectile():
	projectile.y -= 10


def checkProjectileCollision():
	global fired, score
	
	for e in range(len(enemies)):
		for s in range(len(enemies[e])):
			if enemies[e][s].colliderect(projectile):
				fired = False
				enemies[e].pop(s)
				score += 5
				
				if len(enemies[e]) == 0:
					enemies.pop(e)
				return
	
	if projectile.top <= 0:
		fired = False


def checkShieldCollision():
	global fired
	
	for s in shields:
		if s.colliderect(projectile):
			s.inflate_ip(-3, -1)
			fired = False
		
		for p in alienProjectiles:
			if p.colliderect(s):
				s.inflate_ip(-3, -1)
				alienProjectiles.remove(p)


def update():
	global gameState, lives
	
	if gameState == "start" or gameState == "end":
		if mod.keyboard.RETURN or mod.keyboard.kp_enter:
			gameState = "play"
			lives = 3
			alienProjectiles.clear()
			resetAliens()
			mod.clock.schedule_interval(alienFire1, 3.0)
		
		if mod.keyboard.escape:
			quit()
	
	elif gameState == "play":
		moveRocket()
		moveAliens()
		checkCollision()
		checkShieldCollision()
		updateAlienProjectiles()
		
		if len(enemies) == 0:
			resetAliens()
		
		if lives <= 0:
			gameState = "end"
		
		if fired:
			moveProjectile()
			checkProjectileCollision()
		else:
			projectile.x = rocket.x
			projectile.y = rocket.y - 20


pgzrun.go()
