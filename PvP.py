#chế độ chơi 2 người

import pgzrun
import BackGround as BG
import Tank_player
import Status
import Explosion
global screen, Rect, clock

HEIGHT, WIDTH = 600, 800
SIZE_TANK = 25

status1 = Status.Status() #trạng thái thắng thua của người chơi 1
status2 = Status.Status() #trạng thái thắng thua của người chơi 2
bg = BG.BackGround('grass', 'wall')  #background
#tạo 2 xe tăng của 2 người chơi
tank1 = Tank_player.Tank_player('Player 1', 'tank_blue', SIZE_TANK, HEIGHT - SIZE_TANK, 0) 
tank2 = Tank_player.Tank_player('Player 2', 'tank_green', WIDTH - SIZE_TANK, SIZE_TANK, 180)

def draw():
    if status1.player: #Người chơi thứ nhất thắng
        screen.fill((0, 0, 0))
        screen.draw.text('Player 1 win', ((200, 250)), color = ((255, 255, 255)), fontsize = 100)
    elif status2.player: #Người chơi thứ hai thắng
        screen.fill((0, 0, 0))
        screen.draw.text('Player 2 win', ((200, 250)), color = ((255, 255, 255)), fontsize = 100)
    else: #Tiếp tục vẽ
        bg.draw() #vẽ background
        for wall in bg.wall_list: #vẽ gạch
            wall.draw()
        #vẽ 2 xe tăng
        tank1.draw()
        tank2.draw()
        #vẽ vụ nổ tường cho 2 xe tăng
        for w_expl in tank1.explosion_wall_list:
            w_expl.draw(screen, clock)
        for w_expl in tank2.explosion_wall_list:
            w_expl.draw(screen, clock)
        #vẽ cột hp cho 2 xe tăng
        screen.draw.filled_rect(Rect(tank1.x - SIZE_TANK, tank1.y - SIZE_TANK - 15, tank1.hp / 10, 10), "red")
        screen.draw.filled_rect(Rect(tank2.x - SIZE_TANK, tank2.y - SIZE_TANK - 15, tank2.hp / 10, 10), "red")

def update():
    #update xe tăng 1
    tank1.move('a', 'd', 'w', 's', bg.wall_list)    #di chuyển
    tank1.add_bullet('bulletblue2', 'q')            #nạp đạn
    tank1.set_bullet(2)                             #bắn đạn(tốc độ đạn)
    tank1.bullet_wall(bg.wall_list)                 #check bắn vào tường
    tank1.bullet_PvP(tank2, status1)                #check bắn trúng người chơi thứ 2
    
    #update xe tăng 2
    tank2.move('left', 'right', 'up', 'down', bg.wall_list)
    tank2.add_bullet('bulletred2', 'l')
    tank2.set_bullet(2)
    tank2.bullet_wall(bg.wall_list)
    tank2.bullet_PvP(tank1, status2)

    #đẩy vụ nổ ra khỏi list tránh làm nặng game
    while len(tank1.explosion_enemy_list) > 10:     
            tank1.explosion_enemy_list[0:1] = []
    while len(tank2.explosion_enemy_list) > 10:
            tank2.explosion_enemy_list[0:1] = []

pgzrun.go()