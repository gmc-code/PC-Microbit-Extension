====================================================
Rectangle Inheritance 
====================================================

Square(Rectangle) Inheritance
-----------------------------------

| In the code below, the Square class uses the super() function to modify the __init__ method that would be inherited from the Rectangle class.

| Write code to ouput the area of a square of side length 3.

.. admonition:: Tasks

    #. Write a **Square(Rectangle)** class using the scaffold below.

        .. code-block:: python

            class Rectangle:

                def __init__(self, length, width):
                    self.length = length
                    self.width = width

                def area(self):
                    return self.length * self.width


            class Square(           ):

                def __init__(self, length):
                    super().__init__(       ,       )
                    
            square = Square(3)
            print(square.area())


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a **Square(Rectangle)** class.

                .. code-block:: python

                    class Rectangle:

                        def __init__(self, length, width):
                            self.length = length
                            self.width = width

                        def area(self):
                            return self.length * self.width


                    class Square(Rectangle):

                        def __init__(self, length):
                            super().__init__(length, length)
                            
                    square = Square(3)
                    print(square.area())

----

ColouredRectangle(Rectangle) Inheritance
-----------------------------------------

| In the code below, the ColouredRectangle class has its own ``__init__`` method that uses the super() function to reuse the ``__init__`` method from the Rectangle class and to allow other attributes to be set separately.

| Write could to output:
| Area of the red rectangle is 6.

.. admonition:: Tasks

    #. Write a **ColouredRectangle(Rectangle)** class using the scaffold below.

        .. code-block:: python

            class Rectangle:
                def __init__(self, length, width):
                    self.length = length
                    self.width = width

                def area(self):
                    return self.length * self.width

            class ColouredRectangle(          ):
                def __init__(self, length, width, colour):
                    super().__init__(       ,      )
                    self.colour =

            col_rect = ColouredRectangle(2, 3, 'red')
            print(f'Area of the {col_rect.colour} rectangle is {col_rect.area()}.')

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a **ColouredRectangle(Rectangle)** class.

                .. code-block:: python

                    class Rectangle:
                        def __init__(self, length, width):
                            self.length = length
                            self.width = width

                        def area(self):
                            return self.length * self.width

                    class ColouredRectangle(Rectangle):
                        def __init__(self, length, width, colour):
                            super().__init__(length, width)
                            self.colour = colour

                    col_rect = ColouredRectangle(2, 3, 'red')
                    print(f'Area of the {col_rect.colour} rectangle is {col_rect.area()}.')


