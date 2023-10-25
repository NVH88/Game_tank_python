import pygame
class Button():
    def __init__(self,image,pos,text_input,font,base_color,hovering_color):
        self.image=image #
        self.font=font #phông chữ
        self.x_pos,self.y_pos=pos[0],pos[1] #vị trí
        self.base_color,self.hovering_color=base_color,hovering_color 
        self.text_input=text_input #chữ trên nút
        self.text=self.font.render(self.text_input,True,self.base_color) #phương thức render tạo ra hình ảnh và vẽ lên bằng blit
        if self.image is None: #check có img hay không
            self.image=self.text
        self.img_rect=self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.text_rect=self.text.get_rect(center=(self.x_pos,self.y_pos))
    
    #hiển thị hình ảnh và văn bản
    def update(self,screen):
        # ở đây self.image luôn khác rỗng vì nếu không có hình ảnh ta sẽ in ra nguyên chữ vì đã gán nó ở dòng 12
        if self.image is not None: #kiểm tra xem nếu nó khác rỗng thì in ra hình ảnh
            screen.blit(self.image,self.img_rect)
        screen.blit(self.text,self.text_rect)
    
    #check click vào khu vực nút
    def checkForInput(self,position):
        if position[0] in range (self.img_rect.left,self.img_rect.right) and position[1] in range (self.img_rect.top,self.img_rect.bottom):
            return True
        return False
    
    #check click vào khu vực nút and Hover
    def changeColor(self,position):
        if position[0] in range (self.img_rect.left,self.img_rect.right) and position[1] in range (self.img_rect.top,self.img_rect.bottom):
            self.text=self.font.render(self.text_input,True,self.hovering_color)
        else:
            self.text=self.font.render(self.text_input,True,self.base_color)