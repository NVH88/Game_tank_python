import pygame
import sys
import Button
import subprocess
# sử dụng nhiều màn hình trong pygame?
# mỗi một màn hình sử dụng nhiều hàm với các vòng lặp trò chơi riêng chúng
# thủ thuật ở đây là người chơi ảo tưởng về các màn hình khác nhau nhưng thực chất mình chỉ che đi nội dung cũ và phủ nội dung mới lên
pygame.init()
WIDTH_SCREEN=1600
HEIGHT_SCREEN=800
SCREEEN=pygame.display.set_mode((WIDTH_SCREEN,HEIGHT_SCREEN))

BG=pygame.image.load(r'D:\lerning-at-ptit\Kì 1 năm 3\python\pygame\BTL_tank\learn_Button\assets\tanktest.jpg')
BG=pygame.transform.scale(BG,(1600,800))

def get_font(size):
    return pygame.font.Font(r'D:\lerning-at-ptit\Kì 1 năm 3\python\pygame\BTL_tank\learn_menu\assets\font.ttf',size) #trả về kiểu font chữ and size

def play(): #play screen
    pygame.display.set_caption("Play")
    while True:
        PLAY_MOUSE_POS=pygame.mouse.get_pos()

        SCREEEN.fill("black")
        
        PLAY_TEXT= get_font(45).render("đây là màn hình Play Game",True,"white")
        PLAY_RECT=PLAY_TEXT.get_rect(center=(640,260))
        SCREEEN.blit(PLAY_TEXT,PLAY_RECT)

        PLAY_BACK=Button.Button(image=None, pos=(640,460),text_input="BACK",
                                font=get_font(75),base_color="white",hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEEN)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # kiểm tra nó là sự kiện click thì xem nó có click chúng nút nào không
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):                        
                    main_menu()
        pygame.display.update()

def solo(): #solo screen
    pygame.display.set_caption("SOLO")
    while True:
        SOLO_GET_POS=pygame.mouse.get_pos()

        SCREEEN.fill("violet")

        #hiển thị chữ SOLO 
        SOLO_TEXT=get_font(45).render("SOLO voi tao.",True,"Black")
        SOLO_TEXT_RECT=SOLO_TEXT.get_rect(center=(640,260))
        SCREEEN.blit(SOLO_TEXT,SOLO_TEXT_RECT)

        #Tạo đối tượng nút trở về menu
        SOLO_BACK=Button.Button(image=None,pos=(640,460),text_input="BACK",font=get_font(75),
                                    base_color="Black",hovering_color="green")
        SOLO_BACK.changeColor(SOLO_GET_POS)
        SOLO_BACK.update(SCREEEN)

        #sử lí sự kiện
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if SOLO_BACK.checkForInput(SOLO_GET_POS):
                    main_menu()
        pygame.display.update()

def train():
    pygame.display.set_caption("TRAIN")
    while True:
        TRAIN_GET_POS=pygame.mouse.get_pos()

        SCREEEN.fill("yellow")

        #hiển thị chữ TRAIN 
        TRAIN_TEXT=get_font(45).render("TRAIN.",True,"Black")
        TRAIN_TEXT_RECT=TRAIN_TEXT.get_rect(center=(640,260))
        SCREEEN.blit(TRAIN_TEXT,TRAIN_TEXT_RECT)

        #Tạo đối tượng nút trở về menu
        TRAIN_BACK=Button.Button(image=None,pos=(640,460),text_input="BACK",font=get_font(75),
                                    base_color="Black",hovering_color="green")
        TRAIN_BACK.changeColor(TRAIN_GET_POS)
        TRAIN_BACK.update(SCREEEN)

        #sử lí sự kiện
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if TRAIN_BACK.checkForInput(TRAIN_GET_POS):
                    main_menu()
        pygame.display.update()

def tutorial(): #tutorial screen
    pygame.display.set_caption("Tutorial")
    while True:
        TUTORIAL_GET_POS=pygame.mouse.get_pos()

        SCREEEN.fill("white")

        #hiển thị chữ hướng dẫn 
        TUTORIAL_TEXT=get_font(45).render("TUTORIAL.",True,"Black")
        TUTORIAL_TEXT_RECT=TUTORIAL_TEXT.get_rect(center=(640,260))
        SCREEEN.blit(TUTORIAL_TEXT,TUTORIAL_TEXT_RECT)

        #Tạo nút trở về menu
        TUTORIAL_BACK=Button.Button(image=None,pos=(640,460),text_input="BACK",font=get_font(75),
                                    base_color="Black",hovering_color="green")
        TUTORIAL_BACK.changeColor(TUTORIAL_GET_POS)
        TUTORIAL_BACK.update(SCREEEN)

        #sử lí sự kiện
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if TUTORIAL_BACK.checkForInput(TUTORIAL_GET_POS):
                    main_menu()
        pygame.display.update()


def main_menu(): #menu screen
    pygame.display.set_caption("Menu")
    while True:
        SCREEEN.blit(BG,(0,0))
        
        #lấy vị trí của chuột,để kiểm tra xem có nhấn vào hoặc di chuyển qua nó
        MENU_MOUSE_POS=pygame.mouse.get_pos() 
       
        #tạo đối tượng văn bản main menu lên màn hình
        MENU_TEXT=get_font(100).render("MAIN MENU",True,"#b68f40")
        MENU_TEXT_RECT=MENU_TEXT.get_rect(center=(WIDTH_SCREEN/2,100))

        LIST_OPTIONS=[]

        #tạo ra n nút bằng cách tạo ra n lớp nút
        image_button=pygame.image.load(r'D:\lerning-at-ptit\Kì 1 năm 3\python\pygame\BTL_tank\learn_menu\assets\Tutorial_Rect.png')
        image_button=pygame.transform.scale(image_button,(450,80))
        PLAY_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,250),text_input="PLAY",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white") #(ảnh botton,vị trí,text trên buton,đối tượng font chữ và size, màu chưa di chuột vào,màu hover chuột)
        LIST_OPTIONS.append(PLAY_BUTTON)
        SOLO_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,350),text_input="SOLO vs FRIEND",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white") #(ảnh botton,vị trí,text trên buton,đối tượng font chữ và size, màu chưa di chuột vào,màu hover chuột)
        LIST_OPTIONS.append(SOLO_BUTTON)
        TRAIN_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,450),text_input="TRAIN",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white")
        LIST_OPTIONS.append(TRAIN_BUTTON)
        TUTORIAL_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,550),text_input="TUTORIAL",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white")
        LIST_OPTIONS.append(TUTORIAL_BUTTON)
        QUIT_BUTTON=Button.Button(image_button,pos=(WIDTH_SCREEN/2,650),text_input="QUIT GAME",font=get_font(28),
                           base_color='#d7fcd4',hovering_color="white")
        LIST_OPTIONS.append(QUIT_BUTTON)
        #vẽ văn bản Main Menu
        SCREEEN.blit(MENU_TEXT,MENU_TEXT_RECT)

        #truyền liên tục vị trí chuột xem nó có qua các nút bằng cách duyệt qua mọi nút chúng ta có 
        # vẽ các nút chế độ trên màn hình menu
        for button in LIST_OPTIONS: 
            button.changeColor(MENU_MOUSE_POS) #truyền vị trí chuột để thay đổi màu
            button.update(SCREEEN)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # kiểm tra nó là sự kiện click thì xem nó có click chúng nút nào không
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if SOLO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # solo()
                    subprocess.run(["python",r'D:\lerning-at-ptit\Kì 1 năm 3\python\pygame\BTL_tank\learn_menu\testt.py'])
                if TRAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    train()
                if TUTORIAL_BUTTON.checkForInput(MENU_MOUSE_POS):
                    tutorial()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main_menu()



        