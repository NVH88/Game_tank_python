#Class tank của máy

import pygame
import random
import Tank
from pgzero.actor import Actor
import Explosion

pygame.init()
HEIGHT, WIDTH = 600, 800
SIZE_TANK = 25

class Tank_enemy(Tank.Tank):    #kế thừa từ lớp tank gốc
    def __init__(self, image, x, y, angle):  #(ảnh xe tăng, vị trí(x, y), hướng)
        super().__init__(image, x, y, angle)
        self.count = 0  #số bước đi
        self.explosion_wall_list = []   #list vụ nổ tường do xe tăng tạo ra
    
    def move(self, wall_list):  #hàm di chuyển
        orginal_x, orginal_y = self.x, self.y
        self.count -= 1
        if self.angle == 0:
            self.x += 1
        elif self.angle == 90:
            self.y -= 1
        elif self.angle == 180:
            self.x -= 1
        elif self.angle == 270:
            self.y += 1
        if self.x < SIZE_TANK or self.y < SIZE_TANK or self.x > WIDTH - SIZE_TANK or self.y > HEIGHT - SIZE_TANK: #không cho xe tăng đi ra ngoài màn hình
            self.x, self.y = orginal_x, orginal_y
            self.count = 0
        if self.collidelist(wall_list) != -1:   #không cho xe tăng đi xuyên tường
            self.x, self.y = orginal_x, orginal_y
            self.count = 0
            
    def set_count(self):    #đặt lại số bước đi của xe
        self.count = 30

    def set_angle(self):    #đặt lại hướng của xe
        self.angle = random.randint(0, 3) * 90

    def add_bullet(self, hold_off):   #thêm đạn vào list đạn
        if self.hold_off == 0:
            bullet = Actor('bulletred2')
            bullet.pos = self.pos
            bullet.angle = self.angle
            if bullet.angle == 0:
                bullet.x += SIZE_TANK
            elif bullet.angle == 90:
                bullet.y -= SIZE_TANK
            elif bullet.angle == 180:
                bullet.x -= SIZE_TANK
            elif bullet.angle == 270:
                bullet.y += SIZE_TANK
            self.bullet_list.append(bullet)
            self.hold_off = max(10, 30 - hold_off) #để giúp trong chế độ bắn theo level nạp đạn nhanh chậm
        else:
            self.hold_off -= 1

    def bullet_wall(self, wall_list):   #check xem có bắn vào tường không
        for bullet in self.bullet_list:
            wall_index = bullet.collidelist(wall_list)  
            if wall_index != -1:
                #nổ tường
                self.explosion_wall_list.append(Explosion.Explosion('images/explosion4.png',    
                                                (wall_list[wall_index].x - SIZE_TANK, wall_list[wall_index].y - SIZE_TANK)))
                wall_list.pop(wall_index)
                pygame.mixer.Sound('sounds/gun10.wav').play()
                self.bullet_list.remove(bullet)

    def bullet_tank(self, tank, status):    #check xem máy có bắn trúng xe tăng mình không
        for bullet in self.bullet_list:
            if bullet.colliderect(tank):  
                status.loss = True 
                pygame.mixer.Sound('sounds/gun10.wav').play()

    def upd(self, wall_list, tank, speed, hold_off, status):     #hàm update
        choice = random.randint(0, 2)
        if self.count > 0:  #di chuyển
            self.move(wall_list)
        elif choice == 0:   #đặt lại số bước đi
            self.set_count()
        elif choice == 1:   #đặt lại hướng
            self.set_angle()
        elif choice == 2:   #thêm đạn vào list
            self.add_bullet(hold_off)
        super().set_bullet(speed)    #bắn đạn
        self.bullet_tank(tank, status)  #máy bắn trúng người
        self.bullet_wall(wall_list) #máy bắn trúng tường

    def draw(self):
        super().draw()