====================================================
French numbers quiz
====================================================


| Words based on based on http://www.multiwingspan.co.uk/micro.php?page=french
| Press A to change the number (dots) to match the french number.


.. code-block:: python

    from microbit import *
    import random


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


    def SelectNumber():
        counter = 1
        display.show(nleds(counter))
        while button_b.was_pressed() == False:
            if button_a.is_pressed():
                counter += 1
                if counter == 26:
                    counter = 1
                display.show(nleds(counter))
                sleep(100)
            sleep(100)
        return counter


    while True:
        question = random.randint(1, 25)
        display.scroll(french[question])
        answer = SelectNumber()
        if answer == question:
            display.show(Image.YES)
        else:
            display.show(Image.NO)
        sleep(3000)






----

.. admonition:: Tasks

    #. Write the code to scroll the number after guessing the number of dots.

