#class tank của người chơi

import pygame
import Tank
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
import Explosion

pygame.init()
HEIGHT, WIDTH = 600, 800
SIZE_TANK = 25

class Tank_player(Tank.Tank):   #kế thừa từ lớp tank gốc
    def __init__(self, name, image, x, y, angle): #(tên người chơi, ảnh, vị trí(x, y), hướng)
        super().__init__(image, x, y, angle)
        self.name = name #Tên của người chơi
        self.hp = 500   #hp, trong chế độ PvP
        self.score = 0 #số điểm trong chế độ vô tận
        self.explosion_wall_list = []   #list những vụ nổ tường do xe người chơi tạo ra
        self.explosion_enemy_list = []  #list những vụ nổ xe tăng của máy do người chơi tạo ra

    def move(self, left, right, up, down, wall_list):   #hàm di chuyển 
            #(nút ấn để sang trái, phải, lên, xuống, list tường chắn)
        original_x = self.x
        original_y = self.y
        if keyboard[left]:
            self.x -= 2
            self.angle = 180
        elif keyboard[right]:
            self.x += 2
            self.angle = 0
        elif keyboard[up]:
            self.y -= 2
            self.angle = 90
        elif keyboard[down]:
            self.y += 2   
            self.angle = 270 
        
        if self.x < SIZE_TANK or self.y < SIZE_TANK or self.x > WIDTH - SIZE_TANK or self.y > HEIGHT - SIZE_TANK:   
            #không cho xe tăng di chuyển ra ngoài màn hình
            self.x, self.y = original_x, original_y
        if self.collidelist(wall_list) != -1:   #không cho xe tăng đi xuyên tường 
            self.x, self.y = original_x, original_y
            
    def add_bullet(self, image, push):  #hàm nạp đạn (ảnh đạn, nút bấm để nạp đạn)
        if self.hold_off == 0:
            if keyboard[push]:
                bullet = Actor(image)
                bullet.angle = self.angle
                #đặt vị trí đạn ở đầu nòng súng
                bullet.pos = self.pos
                if bullet.angle == 0:
                    bullet.x += SIZE_TANK
                if bullet.angle == 90:
                    bullet.y -= SIZE_TANK
                if bullet.angle == 180:
                    bullet.x -= SIZE_TANK
                if bullet.angle == 270:
                    bullet.y += SIZE_TANK
                self.bullet_list.append(bullet)
                self.hold_off = 20 #chờ nạp đạn
        else:
            self.hold_off -= 1

    def bullet_wall(self, wall_list): #kiểm tra xem đạn có trúng tường hay không?
        for bullet in self.bullet_list:
            wall_index = bullet.collidelist(wall_list) 
            if wall_index != -1:
                #Tạo vụ nổ, phải - SIZE_TANK vì pygame vẽ theo top left
                self.explosion_wall_list.append(Explosion.Explosion('images/explosion4.png', 
                                                (wall_list[wall_index].x - SIZE_TANK, wall_list[wall_index].y - SIZE_TANK)))
                wall_list.pop(wall_index)
                self.bullet_list.remove(bullet)
                pygame.mixer.Sound('sounds/gun9.wav').play()   

    def bullet_enemy(self, enemy_list): #kiểm tra xem đạn có bắn trúng máy hay không?
        for bullet in self.bullet_list:
            enemys_index = bullet.collidelist(enemy_list) 
            if enemys_index != -1:
                self.score += 1
                #Tạo vụ nổ, phải - SIZE_TANK vì pygame vẽ theo top left
                self.explosion_enemy_list.append(Explosion.Explosion('images/explosion3.png', 
                                                (enemy_list[enemys_index].x - SIZE_TANK, enemy_list[enemys_index].y - SIZE_TANK)))
                enemy_list.pop(enemys_index)
                self.bullet_list.remove(bullet)
                pygame.mixer.Sound('sounds/exp.wav').play()

    def bullet_PvP(self, tank, status): #check bắn trúng đối thủ hay không? (trong chế độ PvP)
        for bullet in self.bullet_list:
            if bullet.colliderect(tank): 
                tank.hp -= 100
                self.bullet_list.remove(bullet)
                pygame.mixer.Sound('sounds/exp.wav').play()
                if tank.hp == 0:
                    status.player = True
                    self.bullet_list = []

    def draw(self):
        super().draw()