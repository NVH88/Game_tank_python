#dùng để xác định trạng thái của game(thua máy, thắng máy, người vs người thì ai thắng)

class Status: 
    def __init__(self):
        self.loss = False #người chơi thua máy
        self.player = False #người chơi thắng trong chế độ pvp

#không cần thuộc tính thắng máy vì có thể check bằng cách đếm số máy còn lại