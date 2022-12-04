====================================================
Tilt Pixels game
====================================================

Game design
--------------------

| TiltPixels is a game to find hidden pixels on the display by titling the microbit.
| A class is used to run the game.
| A set will be used to keep track of the pixels visited by tilting.
| e.g. {(0, 0), (1, 0)} is the set of the two pixels in the top left.
| The (x,y) coordinates of each pixel are in the diagram below.

.. image:: images/microbit_coords.png
    :scale: 100 %
    :align: center
    :alt: coordinates


#. Set up the game object (initialize an instance of the class)
    #. Set between 2 and 4 random pixels to be found.
    #. Start from a random pixel and display it brightly then faintly.
#. Repeat the following steps:
    #. Use the accelerometer to detect a tilt and move the pixel.
    #. If all the pixels have been found then:
        #. Display the location of the hidden pixels as well as the visited pixels.
        #. Scroll the score.
        #. Play again if both buttons are pressed.

| The code uses the class, ``TiltPixels()``, for the game object.
| Only the ``set_game`` method is used outside the class itself.

| The code below omits the TiltPixels class for simplicity, but shows the rest of the game code.
| The while True loop repeats the game if both buttons have been pressed.

.. code-block:: python

    from microbit import *

    game = TiltPixels()
    game.run_game()
            while True:
        if button_a.was_pressed() and button_b.was_pressed():
            game.set_game()
            game.run_game()
        else:
            sleep(2000)

----

The TiltPixels class
------------------------

| The ``TiltPixels`` class groups together the game attributes and game methods.

.. py:class:: TiltPixels()

    | Set up the game object to control the game, including the hidden and visited pixels.
    | Initial x, y values for the initial pixel could be passed here as an argument.
    | ``game = TiltPixels(2,2)`` would place the initial pixel in the center of the 5 by 5 grid.
    | There is no need to do so since the game has a constructor method to start at a random pixel.

| The code below imports the random module and creates the game object by creating an instance of the TiltPixels class.

.. code-block:: python

    from microbit import *
    import random


    game = TiltPixels()

----

The TiltPixels outline
-------------------------------

.. admonition:: Tasks

    #. Here is the outline to the TiltPixels class. See if you can write code for each method to get the game working.


.. code-block:: python

    from microbit import *
    import random


    class TiltPixels:
        """TiltPixels game: tilt to find the hidden pixels"""

        def __init__(self, x_pos=random.randint(0, 4), y_pos=random.randint(0, 4)):
            # call set_game

        def set_game(self, x_pos=random.randint(0, 4), y_pos=random.randint(0, 4)):
            # sets or resets the game variables.

        def set_pixels_to_find():
            # creates a set of tuples of (x, y) coordinates for 2 to 4 hidden pixels.

        def acc_x_change(self):
            # returns -1 to move to the left, 0 for no change and 1 to move to the right.

        def acc_y_change(self):
            # returns -1 to move to the top, 0 for no change and 1 to move to the bottom.

        def tilt(self):
            # moves a bright pixel in the direction of tilt.

        def prepare_move(self, x_delta, y_delta):
            # updates the new pixel and adds it to the pixels_filled set.

        def show(self):
            # sets the brightness of the new pixel to bright, then dim.

        def are_all_found(self):
            # checks if all the hidden pixels have been visited by tilting.

        def answer(self):
            # displays the hidden pixels brightly and the visited pixels dimly.

        def set_score(self, time):
            # calculates the score.

        def show_score(self):
            # scrolls the score.

        def run_game(self):
            # runs the game.

    game = TiltPixels()
    game.run_game()
    while True:
        if button_a.was_pressed() and button_b.was_pressed():
            game.set_game()
            game.run_game()
        else:
            sleep(2000)

----

The TiltPixels constructor
---------------------------------

.. py:method:: __init__(x_pos=random.randint(0, 4), y_pos=random.randint(0, 4))

    | The __init__() method is the constructor called when the game object is created.
    | It calls ``self.set_game(x_pos, y_pos)``.
    | The starting pixel is at the coordinates: ``(x_pos, y_pos)``.
    | ``x_pos`` is the starting x value which by default will be a random integer from 0 to 4.
    | ``y_pos`` is the starting y value which by default will be a random integer from 0 to 4.

.. py:method:: def set_game(self, x_pos=random.randint(0, 4), y_pos=random.randint(0, 4))

    | Sets the following variables:
    | ``self.x_pos`` is the x position of the current pixel.
    | ``self.y_pos`` is the y position of the current pixel.
    | ``self.tilt_sensitivity`` is the amount of tilt needed to move the pixel.
    | ``self.game_speed`` is the sleep time between pixel moves.
    | ``self.score``is set to 0.
    | ``self.pixels_filled`` is initialized as a set with the starting pixel tuple: ``(x_pos, y_pos)``. A set is used to make it easy to keep track of the visited pixels. A set is used instead of a list because sets don't allow duplicate values to be stored. When the microbit is tilted, each pixel will be added to the set. 
    | ``self.pixels_to_get`` stores the set of hidden pixels created using ``set_pixels_to_find``. 

    | Calls the following methods:
    | ``self.show()`` displays the pixel at (x_pos, y_pos).

| The set up code is below:

.. code-block:: python

    class TiltPixels:
        """TiltPixels game: tilt to find the hidden pixels"""
        
        def __init__(self, x_pos=random.randint(0, 4), y_pos=random.randint(0, 4)):
            self.set_game(x_pos, y_pos)

        def set_game(self, x_pos=random.randint(0, 4), y_pos=random.randint(0, 4)):
            self.x_pos = x_pos
            self.y_pos = y_pos
            self.tilt_sensitivity = 100
            self.game_speed = 200
            self.score = 0
            self.pixels_filled = {(x_pos, y_pos)}
            self.pixels_to_get = self.set_pixels_to_find()
            self.show()

----

The hidden pixels
---------------------------------

.. py:method:: set_pixels_to_find()

    | Create a set of tuples of (x, y) coordinates for 2 to 4 hidden pixels.
    | e.g with 4 pixels: {(2, 1), (4, 1), (3, 4), (2, 0)}

| The decorator ``@staticmethod``, makes the function a static method. This utility function doesn't access any properties of the class. No reference to ``self`` is passed to it.
| ``pixels = set()`` creates an empty set.
| ``pixels.add((x, y))`` adds a tuple of x and y values to the set. These are the coordinates of each hidden pixel to find.
| ``for _ in range(random.randint(2, 4))`` controls the number of pixels to find. There will be a random number of pixels, from 2 to 4 pixels, to find. 
| ``_`` is used by convention when the iterator variable is not needed in the for-loop body.

.. code-block:: python

    class TiltPixels:
        ...

        @staticmethod
        def set_pixels_to_find():
            pixels = set()
            for _ in range(random.randint(2, 4)):
                x = random.randint(0, 4)
                y = random.randint(0, 4)
                pixels.add((x, y))
            return pixels

----

Accelerometer
---------------------------------

.. py:method:: acc_x_change()

    | Return an integer that will be used to move the pixel left or right.
    | Values are: -1 to move to the left, 0 for no change and 1 to move to the right.
    | A sensitivity of 100 can be exceeded with a small tilt.

.. code-block:: python

    class TiltPixels:
        ...

        def acc_x_change(self):
            sensitivity = self.tilt_sensitivity
            accx = accelerometer.get_x()
            if accx < -sensitivity:
                xd = -1
            elif accx > sensitivity:
                xd = 1
            else:
                xd = 0
            return xd

----

.. py:method:: acc_y_change()

    | Return an integer that will be used to move the pixel left to right.
    | Values are: -1 to move to the top, 0 for no change and 1 to move to the bottom.
    | A sensitivity of 100 can be exceeded with a small tilt.

.. code-block:: python

    class TiltPixels:
        ...

        def acc_y_change(self):
            sensitivity = self.tilt_sensitivity
            accy = accelerometer.get_y()
            if accy < -sensitivity:
                yd = -1
            elif accy > sensitivity:
                yd = 1
            else:
                yd = 0
            return yd

----

Tilt
---------------------------------

| The ``while True`` loop calls ``game.tilt()``
| This gets the change in the x and y coordinates from tilting.
| The new pixel is stored in the set, ``pixels_filled``.
| The new pixel is then shown brightly, then dimly.

.. py:method:: tilt()

    | Calls the **prepare_move** method and the **show** method.

.. code-block:: python

    class TiltPixels:
        ...

        def tilt(self):
            self.prepare_move(self.acc_x_change(),self.acc_y_change())
            self.show()

----

Prepare move
~~~~~~~~~~~~~~~~

.. py:method:: prepare_move(x_delta, y_delta)

    | Updates the x_pos and y_pos values for the new pixel and adds it to the pixels_filled set.
    | x_delta is the integer returned from ``acc_x_change()``.
    | y_delta is the integer returned from ``acc_y_change()``.

| The min and max functions are used to restrict the new x and y values to 0 to 4.
| ``pixels_filled.add((self.x_pos, self.y_pos)`` adds the new tuple (x, y) to the set ``pixels_filled``. Because sets can't include duplicate values, any previously visited pixels are only stored once.

.. code-block:: python

    class TiltPixels:
        ...

        def prepare_move(self, x_delta, y_delta):
            self.x_pos = min(4, max(0, self.x_pos + x_delta))
            self.y_pos = min(4, max(0, self.y_pos + y_delta))
            self.pixels_filled.add((self.x_pos, self.y_pos))

----

Show
~~~~~~~~~~~~~~~~

.. py:method:: show()

    | Set the brightness of the new pixel to 9, then 2.

.. code-block:: python

    class TiltPixels:
        ...

        def show(self):
            display.set_pixel(self.x_pos, self.y_pos, 9)
            sleep(50)
            display.set_pixel(self.x_pos, self.y_pos, 2)

----

are_all_found
---------------------------------

| After moving to a new pixel, check to see if all the hidden pixels have been found.


.. py:method:: are_all_found()

    | Returns True if all the hidden pixels have been visited, or False if not.
    | It uses the **issubset** method to check if all the values in the set pixels_to_get are in the set pixels_filled.

.. code-block:: python

    class TiltPixels:
        ...

        def are_all_found(self):
            return self.pixels_to_get.issubset(self.pixels_filled)
    
----

Answer and score
---------------------------------

| If all the hidden pixels have been found, display the hidden pixels brightly while keeping all the visited pixels displayed dimly.

.. py:method:: answer()

    | Loop through the set of hidden pixels and set their brightness to 9.

.. py:method:: set_score()

    | Calculate the game score by finding the difference between the number of pixels visited and the number of hidden pixels, subtracting that from 100 and subtracting the time taken.
    | The higher the number the better. Scores above 90 are very difficult to achieve.

.. py:method:: show_score()

    | Scrolls the score.


.. code-block:: python

    class TiltPixels:
        ...

        def answer(self):
            # display.clear()
            for i in self.pixels_to_get:
                display.set_pixel(i[0], i[1], 9)
            sleep(2000)
        
        def set_score(self, time):
            self.score = (100 - (len(self.pixels_filled) - 
                            len(self.pixels_to_get)) - int(time / 1000))

        def show_score(self):
            scores = "score = " + str(self.score)
            display.scroll(scores, delay=80)
----

Run game
---------------------------------

| Use the accelerometer to detect a tilt and move the pixel.
| If all the pixels have been found then display the location of the hidden pixels as well as the visited pixels and scroll the score.


.. py:method:: run_game()

    | Turn on pixels as the microbit is tilted until the hidden pixels are found.

.. code-block:: python

    class TiltPixels:
        ...

    def run_game(self):
        start_time = running_time()
        game_over = False
        while game_over is False:
            self.tilt()
            sleep(self.game_speed)
            if self.are_all_found():
                now = running_time()
                game_over = True
                self.answer()
                self.set_score(now - start_time)
                self.show_score()
    
----

Game code
---------------------------------

| The game code is below.

.. code-block:: python

    from microbit import *
    import random


    class TiltPixels:
        """TiltPixels game: tilt to find the hidden pixels"""

        def __init__(self, x_pos=random.randint(0, 4), y_pos=random.randint(0, 4)):
            self.set_game(x_pos, y_pos)

        def set_game(self, x_pos=random.randint(0, 4), y_pos=random.randint(0, 4)):
            self.x_pos = x_pos
            self.y_pos = y_pos
            self.tilt_sensitivity = 100
            self.game_speed = 200
            self.score = 0
            self.pixels_filled = {(x_pos, y_pos)}
            self.pixels_to_get = self.set_pixels_to_find()
            self.show()

        @staticmethod
        def set_pixels_to_find():
            pixels = set()
            for _ in range(random.randint(2, 4)):
                x = random.randint(0, 4)
                y = random.randint(0, 4)
                pixels.add((x, y))
            return pixels

        def answer(self):
            # display.clear()
            for i in self.pixels_to_get:
                display.set_pixel(i[0], i[1], 9)
            sleep(2000)

        def are_all_found(self):
            return self.pixels_to_get.issubset(self.pixels_filled)
        
        def set_score(self, time):
            self.score = (100 - (len(self.pixels_filled) - 
                            len(self.pixels_to_get)) - int(time / 1000))

        def show_score(self):
            scores = "score = " + str(self.score)
            display.scroll(scores, delay=80)

        def prepare_move(self, x_delta, y_delta):
            self.x_pos = min(4, max(0, self.x_pos + x_delta))
            self.y_pos = min(4, max(0, self.y_pos + y_delta))
            self.pixels_filled.add((self.x_pos, self.y_pos))

        def show(self):
            display.set_pixel(self.x_pos, self.y_pos, 9)
            sleep(50)
            display.set_pixel(self.x_pos, self.y_pos, 2)

        def acc_x_change(self):
            sensitivity = self.tilt_sensitivity
            accx = accelerometer.get_x()
            if accx < -sensitivity:
                xd = -1
            elif accx > sensitivity:
                xd = 1
            else:
                xd = 0
            return xd

        def acc_y_change(self):
            sensitivity = self.tilt_sensitivity
            accy = accelerometer.get_y()
            if accy < -sensitivity:
                yd = -1
            elif accy > sensitivity:
                yd = 1
            else:
                yd = 0
            return yd
            
        def tilt(self):
            self.prepare_move(self.acc_x_change(),self.acc_y_change())
            self.show()

        def run_game(self):
            start_time = running_time()
            game_over = False
            while game_over is False:
                self.tilt()
                sleep(self.game_speed)
                if self.are_all_found():
                    now = running_time()
                    game_over = True
                    self.answer()
                    self.set_score(now - start_time)
                    self.show_score()

    game = TiltPixels()
    game.run_game()
    while True:
        if button_a.was_pressed() and button_b.was_pressed():
            game.set_game()
            game.run_game()
        else:
            sleep(2000)

----

.. admonition:: Tasks

    Use subclasses to complete the following:

    #. Modify the code to use a button press to peek at the answer for half a second while still playing the game.
    #. Modify the code so that the A and B buttons move the pixel left to right instead of tilting left to right. Keep the tilting in the y-direction.
    #. Write code to use the A and B buttons to adjust the game speed in steps of 100 with a minimum of 100 and a maximum of 800.
    #. Add a default parameter for the game speed to the __init__ method and set_game method to enable setting of the game speed. Run the first game with a game speed of 1000. Use a for-loop to decrement (lower) the game speed down to 200 in steps of 200 so that 5 games are played.

