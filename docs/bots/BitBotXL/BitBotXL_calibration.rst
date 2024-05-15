====================================================
BitBotXL Calibration
====================================================

See: https://4tronix.co.uk/blog/?p=2479

Calibrating the Motors on BitBot XL v1.2
----------------------------------------------

| Process: The calibration program starts at speed 3. You then set the left or right speeds until it is driving straight. Then give the robot a good shake and it will change to speed 6. Set this speed, shake again to change to speed 9. Once this speed is set correctly, shake again and it will return to speed 3. You can then switch off and all the values are stored. If you run the program again, you will start from the un-calibrated values and must follow all the steps again.

| Download the calibration file :download:`microbit-SetCalibration.hex <files/microbit-SetCalibration.hex>`.| Load the program into the Microbit by dragging it onto the drive icon for the microbit, then  plug the microbit into the bot, facing forward.
| Switch on the robot. It will display 5 (indicating a v1.2 BitBot XL), then change to show 3 (meaning speed 3)
| Press A or B buttons to affect the turning left or right, then press both A+B simultaneously and the robot will display the current calibration value, then move forwards for 2 seconds at speed 3.
| If it is still not moving straight, press the appropriate button one or more times to straighten it up, then press A+B again to test it
| When you're happy that it is moving straight, give the robot a shake and it will store the values for speed 3 and move onto Speed 6.
| Repeat for speed 6 and speed 9.
| When you're happy that all three speeds are set correctly, then switch off. Don't switch it back on again without changing the software in the Microbit, because the first action of the calibration program is to reset the calibration values.

