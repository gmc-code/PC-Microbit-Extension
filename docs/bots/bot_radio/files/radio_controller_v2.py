from microbit import *
import radio

radio.config(group=8)  # 0-255
radio.on()


msg=""
while True:
    sleep(50)
    y_reading = accelerometer.get_y()
    x_reading = accelerometer.get_x()
    # level sideways only
    if -200 <= y_reading <= 200 and -200 <= x_reading <= 200:
        msg = "X"
    # level sideways only
    elif -200 <= x_reading <= 200:
        if y_reading > 700:
            msg = "D"
        elif y_reading > 500:
            msg = "C"
        elif y_reading > 200:
            msg = "B"
        elif y_reading < -700:
            msg = "H"
        elif y_reading < -500:
            msg = "G"
        elif y_reading < -200:
            msg = "F"
    else:
        if x_reading > 700:
            msg = "T"
        elif x_reading > 500:
            msg = "S"
        elif x_reading > 200:
            msg = "R"
        elif x_reading < -700:
            msg = "N"
        elif x_reading < -500:
            msg = "M"
        elif x_reading < -200:
            msg = "L"
    radio.send(msg)
    display.show(msg)