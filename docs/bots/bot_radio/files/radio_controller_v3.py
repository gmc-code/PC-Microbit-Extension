from microbit import *
import music
import radio

radio.config(group=8)  # 0-255
radio.on()


# Class to drive Kitronik :GAME Controller
class KitronikGameController:

    # This function will be called when a class instance is created
    def __init__(self):
        self.musicPin = pin2
        self.Up = pin8
        self.Down = pin14
        self.Left = pin12
        self.Right = pin13
        self.Fire_1 = pin15
        self.Fire_2 = pin16

    # Determines whether a particular button has been pressed
    #  (returns True or False)
    def onButtonPress(self, button):
        if button.read_digital() == 0:
            return True
        else:
            return False

controller = KitronikGameController()
while True:
    msg=""
    if button_a.is_pressed():
        msg = "X"
    elif button_b.is_pressed():
        msg = "X"
    elif controller.onButtonPress(controller.Fire_2) is True:
        if controller.onButtonPress(controller.Up) is True:
            msg = "H"
        elif controller.onButtonPress(controller.Down) is True:
            msg = "D"
        elif controller.onButtonPress(controller.Left) is True:
            msg = "N"
        elif controller.onButtonPress(controller.Right) is True:
            msg = "T"
    elif controller.onButtonPress(controller.Fire_1) is True:
        if controller.onButtonPress(controller.Up) is True:
            msg = "G"
        elif controller.onButtonPress(controller.Down) is True:
            msg = "C"
        elif controller.onButtonPress(controller.Left) is True:
            msg = "M"
        elif controller.onButtonPress(controller.Right) is True:
            msg = "S"
    else:
        if controller.onButtonPress(controller.Up) is True:
            msg = "F"
        elif controller.onButtonPress(controller.Down) is True:
            msg = "B"
        elif controller.onButtonPress(controller.Left) is True:
            msg = "L"
        elif controller.onButtonPress(controller.Right) is True:
            msg = "R"
    radio.send(msg)
    display.show(msg)