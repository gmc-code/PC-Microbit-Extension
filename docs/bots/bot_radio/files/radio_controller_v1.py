from microbit import *
import radio


radio.config(group=8)  # 0-255
radio.on()

msg=""
while True:
    y_reading = accelerometer.get_y()
    x_reading = accelerometer.get_x()
    # flat
    if -200 <= y_reading <= 200 and -200 <= x_reading <= 200:
        msg = "X"
    # level sideways
    elif -200 <= x_reading <= 200:
        # forwards and back tilting
        if y_reading > 200:
            msg = "B"
        elif y_reading < -200:
            msg = "F"
        else:
            msg = "X"
    else:
        # sideways tilting
        if x_reading > 200:
            msg = "R"
        elif x_reading < -200:
            msg = "L"
        else:
            msg = "X"
    radio.send(msg)
    display.show(msg)