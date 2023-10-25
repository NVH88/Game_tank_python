# set up level: level càng cao máy càng mạnh

class Level:
    def __init__(self, level):
        self.level = level  
        self.tocDoDan = level   #tốc độ đạn bay theo level
        self.soLuongMay = level + 5 #số lượng máy theo level
        self.hold_off = level * 2   #tốc độ nạp đạn của máy giảm theo level