#tạo vụ nổ khi bắn trúng

import pygame
global clock

class Explosion:
    def __init__(self, image, pos): #ảnh vụ nổ, vị trí vụ nổ
        self.image = pygame.image.load(image)   #ảnh
        self.pos = pos  #vị trí

    def clear(self):    #đặt về none khi xuất hiện đủ thời gian
        self.image = None

    def display(self, clock):   #chỉ cho xuất hiện 0.05s
        clock.schedule(self.clear, 0.05)
        
    def draw(self, screen, clock):
        if self.image:  #khi là none thì không xuất hiện vụ nổ
            self.display(clock)
            screen.blit(self.image, self.pos)