class Lift:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        
    def get_floor(self):
        return self.current_floor

    def move_to_floor(self, floor_number):
        self.current_floor = floor_number
