import lift

my_lift = lift.Lift()

floor = my_lift.get_floor()
print("현재 층 : ",floor)

my_lift.move_to_floor(5)

floor = my_lift.get_floor()
print("lift가 새로운 층으로 이동했습니다. : ",floor)
