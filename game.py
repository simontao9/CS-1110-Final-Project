# Simon Tao (whx3pt) and Katie Chervenic (xsn2rz)
# Final Project

# Description: pac man style game where player's score increases as they move around a maze collecting coins
# Basic elements:
# - User input: up, down, left, and right arrows to move character
# - Game over: game ends when health bar is empty
# - Graphics/images: graphics for player, enemies, and coins
# Additional elements:
# - Restart from Game Over: give player the option to press space to restart the game
# - Enemies: randomly move around maze and reduce player's health when they contact
# - Collectibles: coins add to score, special item worth more
# - Sprite animation: sprite sheet to animate player

import random
import uvage
camera = uvage.Camera(800,600)

score = 0
tick = 0
lives = 3
game_on = False
game_over = False

# Maze
walls = [
uvage.from_color(0, 5, "blue", 10, 300),
uvage.from_color(0, 550, "blue", 10, 300),
uvage.from_color(50, 150,"blue",100,10),
uvage.from_color(50, 225,"blue",100,10),
uvage.from_color(50, 400,"blue",100,10),
uvage.from_color(50, 325,"blue",100,10),
uvage.from_color(100, 188,"blue",10,85),
uvage.from_color(100, 363,"blue",10,85),
uvage.from_color(750, 150,"blue",100,10),
uvage.from_color(750, 225,"blue",100,10),
uvage.from_color(750, 400,"blue",100,10),
uvage.from_color(750, 325,"blue",100,10),
uvage.from_color(700, 188,"blue",10,85),
uvage.from_color(700, 363,"blue",10,85),
uvage.from_color(800, 5, "blue", 10, 300),
uvage.from_color(800, 550, "blue", 10, 300),
uvage.from_color(400, 600, "blue", 1000, 10),
uvage.from_color(400, 0,"blue",1000,10),
uvage.from_color(400, 325,"blue",150,10),
uvage.from_color(475, 280,"blue",10,100),
uvage.from_color(325, 280,"blue",10,100),
uvage.from_color(400, 25,"blue",10,50),
uvage.from_color(400, 155,"blue",10,50),
uvage.from_color(400, 135,"blue",100,10),
uvage.from_color(200, 185,"blue",10,100),
uvage.from_color(600, 185,"blue",10,100),
uvage.from_color(225, 175,"blue",50,10),
uvage.from_color(575, 175,"blue",50,10),
uvage.from_color(200, 360,"blue",10,80),
uvage.from_color(600, 360,"blue",10,80),
uvage.from_color(400, 425,"blue",10,50),
uvage.from_color(400, 400,"blue",100,10),
uvage.from_color(400, 575,"blue",10,50),
uvage.from_color(200, 525,"blue",100,10),
uvage.from_color(600, 525,"blue",100,10),
uvage.from_color(200, 500,"blue",10,50),
uvage.from_color(600, 500,"blue",10,50),
uvage.from_color(400, 550,"blue",100,10),
uvage.from_color(90, 467,"blue",50,10),
uvage.from_color(68, 500,"blue",10,75),
uvage.from_color(710, 467,"blue",50,10),
uvage.from_color(732, 500,"blue",10,75),
uvage.from_color(290, 467,"blue",50,10),
uvage.from_color(515, 467,"blue",50,10),
uvage.from_color(270, 70,"blue",50,10),
uvage.from_color(535, 70,"blue",50,10),
uvage.from_color(270, 30,"blue",50,10),
uvage.from_color(535, 30,"blue",50,10),
uvage.from_color(100, 70,"blue",75,10),
uvage.from_color(700, 70,"blue",75,10),
uvage.from_color(100, 30,"blue",75,10),
uvage.from_color(700, 30,"blue",75,10),
uvage.from_color(60, 50,"blue",10,50),
uvage.from_color(140, 50,"blue",10,50),
uvage.from_color(740, 50,"blue",10,50),
uvage.from_color(660, 50,"blue",10,50),
uvage.from_color(240, 50,"blue",10,50),
uvage.from_color(300, 50,"blue",10,50),
uvage.from_color(565, 50,"blue",10,50),
uvage.from_color(505, 50,"blue",10,50),
]

# Player

player = uvage.from_image(400,363, "pacman.png")
player.scale_by(0.03)

left = True
right = False
up = False
down = False
def player_move():
    global right
    global left
    global up
    global down
    if uvage.is_pressing('right arrow'):
        player.x += 5
    if uvage.is_pressing('left arrow'):
        player.x += -5
    if uvage.is_pressing('up arrow'):
        player.y += -5
    if uvage.is_pressing('down arrow'):
        player.y += 5
    for wall in walls:
        player.move_to_stop_overlapping(wall)
    if player.x < 0:
        player.x = 800
    if player.x > 800:
        player.x = 0
    if uvage.is_pressing('right arrow') and right == False:
        if left == True:
            player.flip()
            right = True
            left = False
            up = False
            down = False
        if up == True:
            player.rotate(-90)
            right = True
            left = False
            up = False
            down = False
        if down == True:
            player.rotate(90)
            right = True
            left = False
            up = False
            down = False
    if uvage.is_pressing('left arrow') and left == False:
        if right == True:
            player.flip()
            left = True
            right = False
            up = False
            up = False
        if up == True:
            player.rotate(90)
            left = True
            right = False
            up = False
            up = False
        if down == True:
            player.rotate(-90)
            left = True
            right = False
            up = False
            up = False
    if uvage.is_pressing('up arrow') and up == False:
        if right == True:
            player.rotate(90)
            up = True
            right = False
            left = False
            down = False
        if left == True:
            player.rotate(-90)
            up = True
            right = False
            left = False
            down = False
        if down == True:
            player.rotate(180)
            up = True
            right = False
            left = False
            down = False
    if uvage.is_pressing('down arrow') and down == False:
        if right == True:
            player.rotate(-90)
            down = True
            right = False
            left = False
            up = False
        if left == True:
            player.rotate(90)
            down = True
            right = False
            left = False
            up = False
        if up == True:
            player.rotate(180)
            down = True
            right = False
            left = False
            up = False


# Enemies
enemy1 = uvage.from_image(400,299,'orange_enemy.png')
enemy1.scale_by(0.06)
enemy2 = uvage.from_image(350,300,'red_enemy.png')
enemy2.scale_by(0.1)
enemy3 = uvage.from_image(451,300,'pink_enemy.png')
enemy3.scale_by(0.1)
enemies_sized = [enemy1, enemy2, enemy3]
for e in enemies_sized:
    e.speedy = -5
    e.speedx = 5

def enemy_move():
    for e in enemies_sized:
        for wall in walls:
            e.move_to_stop_overlapping(wall)
            if e.left_touches(wall):
                e.speedx = random.randint(5,8)
            if e.right_touches(wall):
                e.speedx = -random.randint(5,8)
            if e.top_touches(wall):
                e.speedy = random.randint(5,8)
            if e.bottom_touches(wall):
                e.speedy = -random.randint(5,8)
            if e.top_touches(wall) and (e.left_touches(wall) or e.right_touches(wall)):
                e.speedx = 0
                e.speedy = 5
        e.move_speed()
        if e.x < 0:
            e.x = 800
        if e.x > 800:
            e.x = 0

# Coins
coins = [
uvage.from_image(30,50,'coin.png'),
uvage.from_image(200,50,'coin.png'),
uvage.from_image(350,50,'coin.png'),
uvage.from_image(450,50,'coin.png'),
uvage.from_image(600,50,'coin.png'),
uvage.from_image(770,50,'coin.png'),
uvage.from_image(50,100,'coin.png'),
uvage.from_image(100,100,'coin.png'),
uvage.from_image(150,100,'coin.png'),
uvage.from_image(200,100,'coin.png'),
uvage.from_image(250,100,'coin.png'),
uvage.from_image(300,100,'coin.png'),
uvage.from_image(350,100,'coin.png'),
uvage.from_image(400,100,'coin.png'),
uvage.from_image(450,100,'coin.png'),
uvage.from_image(500,100,'coin.png'),
uvage.from_image(550,100,'coin.png'),
uvage.from_image(600,100,'coin.png'),
uvage.from_image(650,100,'coin.png'),
uvage.from_image(700,100,'coin.png'),
uvage.from_image(750,100,'coin.png'),
uvage.from_image(150,145,'coin.png'),
uvage.from_image(250,145,'coin.png'),
uvage.from_image(300,145,'coin.png'),
uvage.from_image(500,145,'coin.png'),
uvage.from_image(550,145,'coin.png'),
uvage.from_image(650,145,'coin.png'),
uvage.from_image(150,210,'coin.png'),
uvage.from_image(250,210,'coin.png'),
uvage.from_image(300,210,'coin.png'),
uvage.from_image(350,210,'coin.png'),
uvage.from_image(400,210,'coin.png'),
uvage.from_image(450,210,'coin.png'),
uvage.from_image(500,210,'coin.png'),
uvage.from_image(550,210,'coin.png'),
uvage.from_image(650,210,'coin.png'),
uvage.from_image(50,280,'coin.png'),
uvage.from_image(100,280,'coin.png'),
uvage.from_image(150,280,'coin.png'),
uvage.from_image(200,280,'coin.png'),
uvage.from_image(250,280,'coin.png'),
uvage.from_image(300,280,'coin.png'),
uvage.from_image(500,280,'coin.png'),
uvage.from_image(550,280,'coin.png'),
uvage.from_image(600,280,'coin.png'),
uvage.from_image(650,280,'coin.png'),
uvage.from_image(700,280,'coin.png'),
uvage.from_image(750,280,'coin.png'),
uvage.from_image(150,363,'coin.png'),
uvage.from_image(250,363,'coin.png'),
uvage.from_image(300,363,'coin.png'),
uvage.from_image(350,363,'coin.png'),
uvage.from_image(450,363,'coin.png'),
uvage.from_image(500,363,'coin.png'),
uvage.from_image(550,363,'coin.png'),
uvage.from_image(650,363,'coin.png'),
uvage.from_image(50,433,'coin.png'),
uvage.from_image(100,433,'coin.png'),
uvage.from_image(150,433,'coin.png'),
uvage.from_image(200,433,'coin.png'),
uvage.from_image(250,433,'coin.png'),
uvage.from_image(300,433,'coin.png'),
uvage.from_image(350,433,'coin.png'),
uvage.from_image(450,433,'coin.png'),
uvage.from_image(500,433,'coin.png'),
uvage.from_image(550,433,'coin.png'),
uvage.from_image(600,433,'coin.png'),
uvage.from_image(650,433,'coin.png'),
uvage.from_image(700,433,'coin.png'),
uvage.from_image(750,433,'coin.png'),
uvage.from_image(770,493,'coin.png'),
uvage.from_image(700,493,'coin.png'),
uvage.from_image(650,493,'coin.png'),
uvage.from_image(550,493,'coin.png'),
uvage.from_image(500,493,'coin.png'),
uvage.from_image(450,493,'coin.png'),
uvage.from_image(400,493,'coin.png'),
uvage.from_image(350,493,'coin.png'),
uvage.from_image(300,493,'coin.png'),
uvage.from_image(250,493,'coin.png'),
uvage.from_image(150,493,'coin.png'),
uvage.from_image(100,493,'coin.png'),
uvage.from_image(30,493,'coin.png'),
uvage.from_image(30,563,'coin.png'),
uvage.from_image(100,563,'coin.png'),
uvage.from_image(150,563,'coin.png'),
uvage.from_image(200,563,'coin.png'),
uvage.from_image(250,563,'coin.png'),
uvage.from_image(300,563,'coin.png'),
uvage.from_image(500,563,'coin.png'),
uvage.from_image(550,563,'coin.png'),
uvage.from_image(600,563,'coin.png'),
uvage.from_image(650,563,'coin.png'),
uvage.from_image(700,563,'coin.png'),
uvage.from_image(770,563,'coin.png'),
]

coins_sized = []
for coin in coins:
    coin.scale_by(0.03)
    coins_sized.append(coin)

coin_total = 95

def coin_mechanics():
    global score
    global coin_total
    for coin in coins_sized:
        if player.touches(coin):
            score += 10
            coin.x += 50000
            coin_total -= 1
    if coin_total == 0:
        for coin in coins_sized:
            coin.x -= 50000

# Lives
life1 = uvage.from_image(775, 20, 'heart.png')
life1.scale_by(0.05)
life2 = uvage.from_image(728, 20, 'heart.png')
life2.scale_by(0.05)
life3 = uvage.from_image(680, 20, 'heart.png')
life3.scale_by(0.05)

def lives_function():
    global game_on
    global game_over
    global lives
    for enemy in enemies_sized:
        if player.touches(enemy) and lives == 3:
            life1.x += 50000
            lives -= 1
            game_on = False
            player.x = 400
            player.y = 363
            enemy1.x = 400
            enemy1.y = 299
            enemy2.x = 350
            enemy2.y = 300
            enemy3.x = 451
            enemy3.y = 300
    for enemy in enemies_sized:
        if player.touches(enemy) and lives == 2:
            lives -= 1
            life2.x += 50000
            game_on = False
            player.x = 400
            player.y = 363
            enemy1.x = 400
            enemy1.y = 299
            enemy2.x = 350
            enemy2.y = 300
            enemy3.x = 451
            enemy3.y = 300
    for enemy in enemies_sized:
        if player.touches(enemy) and lives == 1:
            life3.x += 50000
            game_on = False
            game_over = True

#Start message
start_message = uvage.from_text(400, 525, 'Press Space Bar to Start', 30, "Gray", bold=True)

#reset
def reset():
    global game_on
    global game_over
    global score
    global lives
    global tick
    global coins
    global enemy1
    global enemy2
    global enemy3
    global player
    global life1
    global life2
    global life3

    game_on = False
    game_over = False
    score = 0
    lives = 3
    tick = 0

    for coin in coins_sized:
        if coin.x > 50000:
            coin.x -= 50000

    player.x = 400
    player.y = 363

    enemy1.x = 400
    enemy1.y = 299
    enemy2.x = 350
    enemy2.y = 300
    enemy3.x = 451
    enemy3.y = 300

    life1.x = 775
    life2.x = 728
    life3.x = 680



# Tick
def tick():
    global game_on
    global score
    global lives

    camera.clear("black")

    camera.draw(start_message)

    for wall in walls:
        camera.draw(wall)

    for coin in coins_sized:
        camera.draw(coin)

    for e in enemies_sized:
        camera.draw(e)

    camera.draw(player)

    camera.draw(uvage.from_color(100, 20, 'pink', 200, 40))
    camera.draw(uvage.from_color(755, 20, 'pink', 200, 40))
    camera.draw(uvage.from_text(100, 23, str(int(score)), 50, "black", bold=False))
    camera.draw(life1)
    camera.draw(life2)
    camera.draw(life3)

    if uvage.is_pressing('space'):
        game_on = True
        start_message.x += 5000

    if game_on == True:
        player_move()
        enemy_move()
        coin_mechanics()

    lives_function()

    if game_over == True:
        camera.clear('black')
        camera.draw(uvage.from_text(400, 300, 'GAME OVER!', 100, 'red', bold=True))
        camera.draw(uvage.from_text(400, 500, 'Press R Key to Restart', 30, 'red', bold=True))
        if uvage.is_pressing('r'):
            reset()

    camera.display()

uvage.timer_loop(30, tick)
