class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name+"가 야옹!")
        
    def drink(self):
        print(self.name + "가 우유를 마십니다.")
        print(self.name + "가 낮잠을 잡니다.")

class Lift:
    def __init__(self, current_floor=1):
        self.current_floor = current_floor

    def get_floor(self):
        return self.current_floor

    def move_to_floor(self, floor_number):
        self.current_floor = floor_number
