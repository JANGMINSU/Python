import table

class Bat:
    ### 생성자
    def __init__(self, table, width=15, height=100, x_posn=50, y_posn=50, color="green", x_speed=23, y_speed=23):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color
        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.rectangle = self.table.draw_rectangle(self)

    ### 메소드
    def move_up(self, master):
        self.y_posn = self.y_posn - self.y_speed
        if self.y_posn <= 0:
            self.y_posn = 0
        x1 = self.x_posn
        y1 = self.y_posn
        x2 = self.x_posn + self.width
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_down(self, master):
        self.y_posn = self.y_posn + self.y_speed
        if self.y_posn >= self.table.height - self.height:
            self.y_posn = self.table.height - self.height
        x1 = self.x_posn
        y1 = self.y_posn
        x2 = self.x_posn + self.width
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_left(self, master):
        self.x_posn = self.x_posn - self.x_speed
        if self.x_pson <= 0:
            self.x_posn = 0
        x1 = self.x_posn
        y1 = self.y_posn
        x2 = self.x_posn + self.width
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)
        
    def move_right(self, master):
        self.x_posn = self.x_posn + self.x_speed
        if self.x_posn >= self.table.width - self.width:
            self.x_posn = self.table.width - self.width
        x1 = self.x_posn
        y1 = self.y_posn
        x2 = self.x_posn + self.width
        y2 = self.y_posn + self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    def detect_collision(self, ball):
        collision_direction = ""
        collision = False
        feel = 5

        # 배트 변수
        top = self.y_posn
        bottom = self.y_posn + self.width
        left = self.x_posn
        right = self.x_posn + self.height
        v_centre = top + (self.height / 2)
        h_centre = left + (self.width / 2)

        # 볼 변수
        top_b = ball.y_posn
        bottom_b = ball.y_posn + ball.height
        left_b = ball.x_posn
        right_b = ball.x_posn + ball.width
        r = (right_b - left_b) / 2
        v_centre_b = top_b + r
        h_centre_b = left_b + r

        if ((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collision = True
            print("충돌")
