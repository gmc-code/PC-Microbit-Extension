====================================================
French numbers
====================================================


| Based on http://www.multiwingspan.co.uk/micro.php?page=french
| Press A to change the number (dots).
| Press B to show the matching french number.



.. code-block:: python

    from microbit import *

    def n_leds(value):
        """ function to create an image consisting of value LEDs """
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


    # List of French words
    french = [
        "zéro",
        "un",
        "deux",
        "trois",
        "quatre",
        "cinq",
        "six",
        "sept",
        "huit",
        "neuf",
        "dix",
        "onze",
        "douze",
        "treize",
        "quatorze",
        "quinze",
        "seize",
        "dix-sept",
        "dix-huit",
        "dix-neuf",
        "vingt",
        "vingt et un",
        "vingt-deux",
        "vingt-trois",
        "vingt-quatre",
        "vingt cinq",
    ]

    # Set and show the starting value for the display
    counter = 1
    display.show(n_leds(counter))

    while True:
        # Press A to change the number
        if button_a.is_pressed():
            counter += 1
            if counter == 26:
                counter = 1
            display.show(n_leds(counter))
            sleep(50)
        # Press B to show the French word
        if button_b.was_pressed():
            display.scroll(french[counter])
            display.show(n_leds(counter))
        sleep(100)


----

.. admonition:: Tasks

    #. Write the code to scroll the number before the french for the number of dots.

