import pygame
import sys
import Button
import subprocess
import os
pygame.init()
WIDTH_SCREEN=1150
HEIGHT_SCREEN=700
SCREEEN=pygame.display.set_mode((WIDTH_SCREEN,HEIGHT_SCREEN))
def get_font(size):
    return pygame.font.Font(r'images/font.ttf',size) #trả về kiểu font chữ and size
pygame.display.set_caption("end")
MENU_MOUSE_POS=pygame.mouse.get_pos() 
# final = False
END_BG_Screen=pygame.image.load(r'images/grass.png')
END_BG_Screen=pygame.transform.scale(END_BG_Screen,(WIDTH_SCREEN,HEIGHT_SCREEN))
path = ''
while True:

    END_GET_POS=pygame.mouse.get_pos()
    SCREEEN.blit(END_BG_Screen,(0,0))
    image_button=pygame.image.load(r'images/Tutorial_Rect.png')
    image_button=pygame.transform.scale(image_button,(400,100))
    ENDPV1_Replay=Button.Button(image_button,pos=(WIDTH_SCREEN/2,280),text_input="Replay",font=get_font(50),
                                base_color="#d7fcd4",hovering_color="yellow")
    ENDPV2_Replay=Button.Button(image_button,pos=(WIDTH_SCREEN/2,460),text_input="MENU",font=get_font(50),
                                base_color="#d7fcd4",hovering_color="yellow")
    
    LIST_OPTION=list()
    LIST_OPTION.append(ENDPV1_Replay)
    LIST_OPTION.append(ENDPV2_Replay)
    for button in LIST_OPTION: 
        button.changeColor(END_GET_POS) #truyền vị trí chuột để thay đổi màu
        button.update(SCREEEN)
    END_TEXT=get_font(100).render("END",True,"#d7fcd4")
    END_TEXT_RECT=END_TEXT.get_rect(center=(WIDTH_SCREEN/2,100))
    SCREEEN.blit(END_TEXT,END_TEXT_RECT)

    #sử lí sự kiện
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if ENDPV1_Replay.checkForInput(END_GET_POS):
                path = 'PvP.py'
                break
            if ENDPV2_Replay.checkForInput(END_GET_POS):
                path = 'Main.py'
                break
    if path != '':
        break
                
    pygame.display.update()
subprocess.Popen(["python", "exit_pygame.py"])
subprocess.Popen(["python", path])