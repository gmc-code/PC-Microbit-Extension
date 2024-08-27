# MOVEMotor bot code, change radio group to match bot number
# MOVEMotor_v31 200 + bot number
# MOVEMotor v2 150 + bot number

from microbit import *
import radio

radio.config(group=151)  # 0-255
radio.on()
dec_left = 0
dec_right = 0
biaslist =['decleft', 'resetbias', 'decright']

while True:
    sleep(50)
    msg = ""
    if pin0.is_touched():
        #dec_left +=20
        msg = "decleft"
    elif pin1.is_touched():
        #dec_left = 0
        #dec_right = 0
        msg = "resetbias"
    elif pin2.is_touched():
        #dec_right +=20
        msg = "decright"  
    elif button_a.is_pressed() and button_b.is_pressed():
        # stop
        msg = "X"
    elif button_a.is_pressed():
        # spin
        msg = "sL"
    elif button_b.is_pressed():
        # spin
        msg = "sR"
    else:
        y_reading = accelerometer.get_y()
        x_reading = accelerometer.get_x()
        # level
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
    if msg in biaslist:
        display.show(biaslist.index(msg))
    else:
        display.show(msg)
