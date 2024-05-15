====================================================
Games introduction
====================================================

Games using classes
--------------------

| The games in this section are built via the use of classes.
| The games use a class for the game object since it makes it easy to group together the game data and the game functions within the class.
| The game data are attributes. **Attributes** are variables belonging to a class.
| The game functions are methods. **Methods** are functions associated with a class.

| Modifying the game while keeping the original game intact is possible thanks to Polymorphism and Inheritance.
| **Inheritance**: Subclasses can be created which inherit the attributes and methods from the original game class.
| **Polymorphism**: Selected attributes or methods in the subclasses can be adjusted to create different versions of the game.
| **Composition**: Classes can be assigned to attributes in the main game class.

| See https://pc-microbit-extension.readthedocs.io/en/latest/games/magic_8.html for examples of using child classes derived from the original game in the parent class in order to make variations of the game.


| See: https://www.w3schools.com/python/python_classes.asp

.. admonition:: Tip
    
    **MicrobitGame** is written in camel case. This is the python naming convention for classes. Each word is capitalized and there are no underscores. This is different to the convention for a variable which would be written, in snake case, as **microbit_game**.

