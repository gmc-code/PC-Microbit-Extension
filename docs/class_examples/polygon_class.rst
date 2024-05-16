====================================================
Polygon Class with \*args
====================================================
    
| Write a **Polygon** class.
| Set the Polygon's **sides** on calling the Polygon class.
| Since a polygon can have varying numbers of sides, use packing of positional arguments, via \*args.
| Use ``def __init__(self, *args)`` to pack the arguments.
| e.g. ``tri_1 = Polygon(3, 4, 5)``
| e.g. ``rect_1 = Polygon(6, 8, 6, 8)``

| Write a method to return the perimeter of a polygon.
| Write code to output:
| tri_1 with sides (3, 4, 5), has a perimeter of 12.
| rect_1 with sides (6, 8, 6, 8), has a perimeter of 28.

.. admonition:: Tasks

    #. Write a **Polygon** class using the scaffold below.

        .. code-block:: python

            class Polygon:

                def __init__(self, *args):
                    self.sides = args

                def perimeter(self):
                    return sum(           )

            tri_1 = Polygon( 3, 4, 5)
            print(f'tri_1 with sides {      }, has a perimeter of {            }.')
            rect_1 = Polygon( 6, 8, 6, 8)
            print(f'rect_1 with sides {      }, has a perimeter of {            }.')

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a Polygon class.

                .. code-block:: python

                    class Polygon:

                        def __init__(self, *args):
                            self.sides = args

                        def perimeter(self):
                            return sum(self.sides)

                    tri_1 = Polygon(3, 4, 5)
                    print(f'tri_1 with sides {tri_1.sides}, has a perimeter of {tri_1.perimeter()}.')
                    rect_1 = Polygon(6, 8, 6, 8)
                    print(f'rect_1 with sides {rect_1.sides}, has a perimeter of {rect_1.perimeter()}.')

