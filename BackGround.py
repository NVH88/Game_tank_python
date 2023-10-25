#Tạo background và tường(chướng ngại vật)

import random
from pgzero.actor import Actor

HEIGHT, WIDTH = 600, 800
SIZE_TANK = 25

class BackGround(Actor):
    def __init__(self, BGImage, WImage):#(ảnh background, ảnh tường)
        #Tạo ảnh nền
        super().__init__(BGImage)
        #Tạo tường chắn
        self.wall_list = [] #(list tường chắn)
        for i in range(16):
            for j in range(10):
                if random.randint(0, 100) < 50:
                    wall = Actor(WImage)
                    wall.pos = (i * 50 + SIZE_TANK, j * 50 + SIZE_TANK * 3)
                    self.wall_list.append(wall)
    #hàm vẽ
    def draw(self):
        super().draw()
        for wall in self.wall_list:
            wall.draw()