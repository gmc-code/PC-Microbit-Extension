====================================================
Fill the grid
====================================================


| See: http://www.multiwingspan.co.uk/micro.php?page=shut
| Press A to start.
| Press B to roll dice.
| The aim is to get to 25 to fill screen and win game.
| Overthrows at the end end lead to bounce backs. e.g. If a 2 is needed but a 6 is thrown, it bounces back 4 to 21 with the last 4 pixels off.


.. code-block:: python

    from microbit import *
    import random

    faces = [
        Image("00000:00000:00900:00000:00000:"),
        Image("00009:00000:00000:00000:90000:"),
        Image("00009:00000:00900:00000:90000:"),
        Image("90009:00000:00000:00000:90009:"),
        Image("90009:00000:00900:00000:90009:"),
        Image("90009:00000:90009:00000:90009:"),
    ]


    def nleds(value):
        img = Image("00000:" * 5)
        sp = img.set_pixel
        counter = 0
        for row in range(0, 5):
            for col in range(0, 5):
                if counter < value:
                    sp(col, row, 9)
                else:
                    sp(col, row, 0)
                counter += 1
        return img


    def RandomImages(n, delay):
        for i in range(0, n):
            display.show(random.choice(faces))
            sleep(delay)
            #display.clear()
            #sleep(delay // 2)
        display.clear()

    def PlayGame():
        counter = 0
        while counter != 25:
            if button_b.was_pressed():
                display.clear()
                sleep(250)
                roll = random.randint(1, 6)
                RandomImages(5, 100)
                display.show(faces[roll - 1])
                sleep(500)
                if counter + roll == 25:
                    # won
                    counter = counter + roll
                elif counter + roll < 25:
                    # add on
                    counter = counter + roll
                else:
                    # go to end and come back
                    counter = 50 - (counter + roll)
            display.show(nleds(counter))
            sleep(10)
        for i in range(0, 10):
            display.show(nleds(25))
            sleep(200)
            display.clear()
            sleep(200)


    while True:
        display.show(Image.ARROW_W)
        if button_a.is_pressed():
            PlayGame()
        sleep(1000)

----

.. admonition:: Tasks

    #. Adding scoring based on the number of dice rolls.

