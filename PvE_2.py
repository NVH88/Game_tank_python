#chế độ theo level

import random
import pgzrun
import BackGround as BG
import Tank_player
import Tank_enemy
import Status
import Level
from pgzero.actor import Actor
global screen, Rect, clock

HEIGHT, WIDTH = 600, 800
SIZE_TANK = 25
stt = Status.Status()

with open('level.txt', 'r') as file:
    L = int(file.read())

print(L)
lev = Level.Level(L)    #Set up level: level càng cao máy càng mạnh
bg = BG.BackGround('grass', 'wall')  #background
tank = Tank_player.Tank_player('p1', 'tank_blue', WIDTH / 2, HEIGHT - SIZE_TANK, 90)  
enemy_list = []     #list tank máy

for i in range(lev.soLuongMay):     #thêm tank máy vào list
    enemy_list.append(Tank_enemy.Tank_enemy('tank_red', random.randint(SIZE_TANK, WIDTH - SIZE_TANK), SIZE_TANK, 270))

def draw(): 
    global enemy_list
    if stt.loss:    #màn hình khi thua
        enemy_list = []
        screen.fill((0, 0, 0))
        screen.draw.text('Loss', ((300, 250)), color = ((255, 255, 255)), fontsize = 100)   
    elif len(enemy_list) == 0:  #màn hình khi thắng
        screen.fill((0, 0, 0))
        screen.draw.text('Win', ((320, 250)), color = ((255, 255, 255)), fontsize = 100)  
    else:   #vẽ liên tục
        bg.draw()   #vẽ background
        tank.draw() #vẽ tank người chơi
        for enemy in enemy_list:
            enemy.draw()    #vẽ tank máy
            for w_expl in enemy.explosion_wall_list:    #vụ nổ khi máy bắn vào tường
                w_expl.draw(screen, clock)
        for w_expl in tank.explosion_wall_list: #vụ nổ khi người bắn vào tường
            w_expl.draw(screen, clock)
        for e_expl in tank.explosion_enemy_list:    #vụ nổ khi người vắn vào máy
            e_expl.draw(screen, clock)

def update():
    tank.move('left', 'right', 'up', 'down', bg.wall_list)  #hàm di chuyển, tránh xuyên tường
    tank.add_bullet('bulletblue2', 'space')     #hàm nạp đạn, bắn bằng nút space
    tank.set_bullet(2)      #tốc độ đạn, cho đạn bay
    tank.bullet_wall(bg.wall_list)      #bắn trúng tường
    tank.bullet_enemy(enemy_list)       #bắn trúng máy

    for enemy in enemy_list:
        while len(enemy.explosion_wall_list) > 10:  #giới hạn số vụ nổ (do máy bắn vào tường) trong list là 10, tránh nặng game
            enemy.explosion_wall_list[0:1] = []
    while len(tank.explosion_enemy_list) > 10:  #giới hạn số vụ nổ (do người chơi bắn vào tường) trong list là 10, tránh nặng game
            tank.explosion_enemy_list[0:1] = []

    for enemy in enemy_list:
        enemy.upd(bg.wall_list, tank, lev.tocDoDan, lev.hold_off, stt)  #update máy

pgzrun.go()