#chế độ vô tận

import random
import pgzrun
import BackGround as BG
import Tank_player
import Tank_enemy
import Status
from pgzero.actor import Actor
global screen, Rect, clock

HEIGHT, WIDTH = 600, 800
SIZE_TANK = 25
stt = Status.Status()

bg = BG.BackGround('grass', 'wall')  
tank = Tank_player.Tank_player('p1', 'tank_blue', WIDTH / 2, HEIGHT - SIZE_TANK, 90)
enemy_list = []     #list xe tăng của máy
for i in range(5):  #có 5 máy ban đầu
    enemy_list.append(Tank_enemy.Tank_enemy('tank_red', random.randint(SIZE_TANK, WIDTH - SIZE_TANK), SIZE_TANK, 270))

def draw():
    global enemy_list
    if stt.loss:    #Nếu bị máy bắn trúng thì hết game
        enemy_list = [] #Xóa hết máy
        screen.fill((0, 0, 0))
        screen.draw.text('Loss', ((300, 250)), color = ((255, 255, 255)), fontsize = 100)   
    else:
        bg.draw() 
        tank.draw()             #vẽ xe tăng mình
        for enemy in enemy_list: #vẽ xe tăng địch
            enemy.draw()
            for w_expl in enemy.explosion_wall_list:    #vẽ vụ nổ tường do máy gây ra
                w_expl.draw(screen, clock)
        for w_expl in tank.explosion_wall_list:     #vẽ vụ nổ tường do xe tăng mình gây ra
            w_expl.draw(screen, clock)
        for e_expl in tank.explosion_enemy_list:    #vẽ vụ nổ của xe tăng địch
            e_expl.draw(screen, clock)
        screen.draw.text(str(tank.score), (10, 10), color = ((255, 255, 255)), fontsize = 40)  #in điểm số lên màn hình

def update():
    global enemy_list
    tank.move('left', 'right', 'up', 'down', bg.wall_list) #di chuyển xe tăng mình
    tank.add_bullet('bulletblue2', 'space') #nạp đạn(màu đạn, nút để bắn)
    tank.set_bullet(2)  #tốc độ đạn bay
    tank.bullet_wall(bg.wall_list)  #đạn trúng tường
    tank.bullet_enemy(enemy_list)   #đạn trúng tank máy

    for enemy in enemy_list:
        while len(enemy.explosion_wall_list) > 10:  #giới hạn số vụ nổ (do máy bắn vào tường) trong list là 10, tránh nặng game
            enemy.explosion_wall_list[0:1] = []
    while len(tank.explosion_enemy_list) > 10:  #giới hạn số vụ nổ (do người chơi bắn vào tường) trong list là 10, tránh nặng game
            tank.explosion_enemy_list[0:1] = []

    for enemy in enemy_list:    #update tank máy
        enemy.upd(bg.wall_list, tank, 2, 0, stt)

    while len(enemy_list) < 5:  #luôn để số tank máy là 5
        enemy_list.append(Tank_enemy.Tank_enemy('tank_red', random.randint(SIZE_TANK, WIDTH - SIZE_TANK), SIZE_TANK, 270))

pgzrun.go()