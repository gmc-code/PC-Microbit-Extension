====================================================
Clock Reflexes
====================================================

| Reflexes is based on http://www.multiwingspan.co.uk/micro.php?page=concentrate2
| Press A when the hand is about to reach 12 o'clock.

.. code-block:: python

    from microbit import *

    clocks = [
        Image.CLOCK1,
        Image.CLOCK2,
        Image.CLOCK3,
        Image.CLOCK4,
        Image.CLOCK5,
        Image.CLOCK6,
        Image.CLOCK7,
        Image.CLOCK8,
        Image.CLOCK9,
        Image.CLOCK10,
        Image.CLOCK11,
        Image.CLOCK12,
    ]

    counter = 0
    start = 200
    sleep_delay = start
    score = 0

    while True:
        display.show(clocks[counter])
        # extra help on the last tick
        if counter == 11:
            sleep(sleep_delay / 10)
        if button_a.was_pressed():
            sleep(500)
            if counter == 11:
                display.show(Image.HAPPY)
                score += 1
                sleep_delay = sleep_delay - 10
                sleep_delay = max(10, sleep_delay)
                sleep(500)
            else:
                display.show(Image.SAD)
                display.scroll(str(score))
                sleep(500)
                score = 0
                sleep_delay = start
        counter += 1
        if counter > 11:
            counter = 0
        sleep(sleep_delay)



----

.. admonition:: Tasks

    #. Adjust the code to keep track of the highest score and update it when a new score is higher.

