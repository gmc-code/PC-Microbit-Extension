====================================================
Dice Inheritance
====================================================

| One die, two dice.

| Write a child class,**LoadedDie**, of the parent class, **Die**.     
| Set the die's **sides**. 
| The parent class, Die, has a parameter: ``sides``.
| The child class, LoadedDie, has the parameters, ``sides``, ``bias``, ``bias_count``. 
| ``Bias`` is a die value with extra chances of getting it, set by ``bias_count``.
| Both classes have the instance variables: ``sides`` and ``face_list``.
| In the Die class, the die values, ``face_list``, start at 1 and go to the number of sides.  
| The Die class has the methods: ``make_face_list()``, ``get_die()`` and ``roll_die()``.
| The LoadedDie class has the method: ``make_face_list_biased()``.


.. admonition:: Tasks

    #. Write a **LoadedDie** class as a child class of the **Die** class using the scaffold below.

        .. code-block:: python

            from random import choice


            class Die:
                """dice simulator"""

                def __init__(self, sides=6):
                    self.sides = sides
                    self.face_list = self.make_face_list(sides)

                def make_face_list(self, sides):
                    face_list = [i for i in range(1, sides + 1)]
                    return face_list

                def get_die(self):
                    print(f"The die has sides: {self.             }")

                def roll_die(self):
                    return choice(self.           )


            class LoadedDie(Die):
                def __init__(self, sides=6,       =6,           =4):
                    super().__init__(sides=6)
                    self.face_list = self.make_face_list_biased(sides, bias, bias_count)

                def make_face_list_biased(self, sides,     ,            ):
                    biased_list = [i for i in range(1, sides + 1)] + [bias] * bias_count
                    return biased_list


            die0 = Die(sides=6)
            die0.get_die()
            for i in range(36):
                print(die0.roll_die(), end=" ")

            print("\n")
            die6 = LoadedDie(sides=6, bias=6, bias_count=4)
            die6.get_die()
            for i in range(36):
                print(die6.roll_die(), end=" ")


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a **LoadedDie** class as a child class of the **Die** class.

                .. code-block:: python

                    from random import choice


                    class Die:
                        """dice simulator"""

                        def __init__(self, sides=6):
                            self.sides = sides
                            self.face_list = self.make_face_list(sides)

                        def make_face_list(self, sides):
                            face_list = [i for i in range(1, sides + 1)]
                            return face_list

                        def get_die(self):
                            print(f"The die has sides: {self.face_list}")

                        def roll_die(self):
                            return choice(self.face_list)


                    class LoadedDie(Die):
                        def __init__(self, sides=6, bias=6, bias_count=4):
                            super().__init__(sides=6)
                            self.face_list = self.make_face_list_biased(sides, bias, bias_count)

                        def make_face_list_biased(self, sides, bias, bias_count):
                            biased_list = [i for i in range(1, sides + 1)] + [bias] * bias_count
                            return biased_list


                    die0 = Die(sides=6)
                    die0.get_die()
                    for i in range(36):
                        print(die0.roll_die(), end=" ")

                    print("\n")
                    die6 = LoadedDie(sides=6, bias=6, bias_count=4)
                    die6.get_die()
                    for i in range(36):
                        print(die6.roll_die(), end=" ")


