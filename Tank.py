#class tank gốc

from pgzero.actor import Actor

HEIGHT, WIDTH = 600, 800
SIZE_TANK = 25

class Tank(Actor): #lớp xe tăng gốc
    def __init__(self, image, x, y, angle): #(ảnh, x, y, hướng xe tăng)
        super().__init__(image)
        self.x = x
        self.y = y
        self.angle = angle
        self.bullet_list = []  #list đạn
        self.hold_off = 0  #thời gian chờ để nạp đạn

    def set_bullet(self, speed):  #hàm bắn đạn (speed: tốc độ đạn)
        for bullet in self.bullet_list:
            if bullet.angle == 0:
                bullet.x += speed
            elif bullet.angle == 90:
                bullet.y -= speed
            elif bullet.angle == 180:
                bullet.x -= speed
            elif bullet.angle == 270:
                bullet.y += speed
            if bullet.x < 0 or bullet.y < 0 or bullet.x > WIDTH or bullet.y > HEIGHT:   #đạn đi ra ngoài màn hình thì xóa
                self.bullet_list.remove(bullet)

    def draw(self):
        super().draw()  #vẽ xe tăng
        for bullet in self.bullet_list:     #vẽ đạn
            bullet.draw()