import time
import ftrobopy
import threading


txt = ftrobopy.ftrobopy('auto') # connect to txt

# lets configure our inputs
joystick_l = txt.joystick(0, 1, 1)
joystick_r = txt.joystick(1, 1, 1)

# and these are our outputs
motor_r = txt.motor(1)
motor_l = txt.motor(2)
motor_r.setDistance(0, syncto=None)
motor_l.setDistance(0, syncto=None)
txt.updateWait()
print("Wir sind startklar.")

# steering with your motors instead of using a steering axle allows for turning directly on your heel. I've made it so
# that pressing/depressing the right X-Axis stick will make the vehicle do a big u-turn like with a steering axle
# steering with the left X-Axis stick on the other hand allows for turning completely on your own heel 
# it takes a little getting used to but allows for more flexibility while steering.

def infiniteloop1():  # steering via BT Remote
    while True:
        if abs(joystick_r.leftright()) <= 0.1 and abs(joystick_l.leftright()) <= 0.4 and abs(joystick_l.updown()) >= 0.1:  # forward and backward
            motor_l.setSpeed(joystick_l.updown() * 508)
            motor_r.setSpeed(joystick_l.updown() * 508)
            motor_l.setDistance(0, syncto=motor_r)
            motor_r.setDistance(0, syncto=motor_l)

        elif abs(joystick_l.leftright()) > 0.4:  # turning on your heel
            motor_l.setSpeed(joystick_l.leftright() * 508)
            motor_r.setSpeed(joystick_l.leftright() * -508)
            motor_l.setDistance(0, syncto=None)
            motor_r.setDistance(0, syncto=None)

        # cornering fw/left:
        elif abs(joystick_l.leftright()) <= 0.80 and joystick_r.leftright() <= -0.1 and joystick_l.updown() >= 0.1:
            motor_l.setDistance(0, syncto=None)
            motor_r.setDistance(0, syncto=None)
            motor_r.setSpeed((2.6 + joystick_l.updown() + (3 * abs(joystick_r.leftright()))) * 76.5)
            motor_l.setSpeed((2.2 + joystick_l.updown() + (3 * ((abs(joystick_r.leftright()) - 0.1)**15))) * 76.5)

        # cornering fw/right:
        elif abs(joystick_l.leftright()) <= 0.80 and joystick_r.leftright() >= 0.1 and joystick_l.updown() >= 0.1:
            motor_l.setDistance(0, syncto=None)
            motor_r.setDistance(0, syncto=None)
            motor_l.setSpeed((2.6 + joystick_l.updown() + (3 * abs(joystick_r.leftright()))) * 76.5)
            motor_r.setSpeed((2.2 + joystick_l.updown() + (3 * ((abs(joystick_r.leftright()) - 0.1)**15))) * 76.5)

        # cornering backw/left:
        elif abs(joystick_l.leftright()) <= 0.80 and joystick_r.leftright() <= -0.1 and joystick_l.updown() <= -0.1:
            motor_l.setDistance(0, syncto=None)
            motor_r.setDistance(0, syncto=None)
            motor_l.setSpeed(-((2.6 + abs(joystick_l.updown()) + (3 * abs(joystick_r.leftright()))) * 76.5))
            motor_r.setSpeed(-((2.2 + abs(joystick_l.updown()) + (3 * ((abs(joystick_r.leftright()) - 0.1)**15))) * 76.5))

        # cornering backw/right:
        elif abs(joystick_l.leftright()) <= 0.80 and joystick_r.leftright() >= 0.1 and joystick_l.updown() <= -0.1:
            motor_l.setDistance(0, syncto=None)
            motor_r.setDistance(0, syncto=None)
            motor_r.setSpeed(-((2.6 + abs(joystick_l.updown()) + (3 * abs(joystick_r.leftright()))) * 76.5))
            motor_l.setSpeed(-((2.2 + abs(joystick_l.updown()) + (3 * ((abs(joystick_r.leftright()) - 0.1)**15))) * 76.5))


        else:  # deadzone between +-0.09 just incase stick doesn't center completely
            motor_l.stop()
            motor_r.stop()
            motor_r.setDistance(0, syncto=None)
            motor_l.setDistance(0, syncto=None)



# lets make this a thread incase we need to run something else from the same file
thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

