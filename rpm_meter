# This script will use the built in encoder in fischertechniks red motors to read the total revolutions counter 
# and calculate revolutions per minute as a floating average of the last 2 seconds.
# the rpm will be printed to the display and can be useful e.g. to run any code when certain rpm thresholds are reached

import time
import ftrobopy
import threading



txt=ftrobopy.ftrobopy('auto')

joystick1 = txt.joystick(0,1,1)
joystick2 = txt.joystick(1,1,1)
Motor1 = txt.motor(1)
Motor1.setDistance(0)
txt.updateWait()




def infiniteloop1():  # RPM-Meter
    while True:
        Motor1 = txt.motor(1)
        curRev = Motor1.getCurrentDistance()
        t0 = time.time()
        lastRev = 0
        

        while (curRev == Motor1.getCurrentDistance()):
            txt.updateWait()
            t1 = time.time()
            try:
                getriRev = (curRev - lastRev / (t1 - t0))
                rpm = getriRev / 3.18  # 1.59 * (duration of measurement interval in s) returns sensible results for red encoder motor
                print("RPM: " + "%.1f" % rpm)

            except ZeroDivisionError:
                pass
            time.sleep(2)  # this sets length of measurement interval
            t0 = t1
            lastRev = curRev 


thread1 = threading.Thread(target=infiniteloop1)
thread1.start()
