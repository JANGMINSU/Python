class Student:
    def __init__(self, sname="", sage=0, shobby=""):
        self.sname = sname
        self.sage = sage
        self.shobby = shobby

    def student_info(self):
        print("Student Name : ", self.sname)
        print("Age : ", self.sage)
        print("Hobby : ", self.shobby)

    def sleep(self):
        print("ZZZ")

    def set_hobby(self, shobby):
        self.shobby = shobby

    def study(self):
        print("공부")
    
