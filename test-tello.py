from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()
print(tello.get_battery())

tello.move_left(100)
tello.rotate_clockwise(90)
tello.move_forward(100)

tello.land()