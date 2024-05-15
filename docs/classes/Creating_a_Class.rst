====================================================
Creating a Class
====================================================
    

Naming Classes
----------------------

| By convention, the name of the class is in camel case. e.g. **LevelGame**. 
| Each word is capitalized and there are no underscores. 

----

Class Creation
----------------------

| The code below creates a class, ``LevelGame``.
| The keyword **class** is followed by the name of the class then a colon. e.g. ``class LevelGame:``

| ``pass`` is used as a placeholder for future code, since empty code is not allowed in a class.
| When the pass statement is executed, nothing happens, but getting an error is avoided. 

.. code-block:: python

    class LevelGame:
        pass

----

Object instantiation
----------------------

| An object is what is made from the class blueprint.
| Objects are **instances** of classes.
| The code below carries out object **instantiation** (making an instance).
| The ``game`` instance is created by calling the class, ``LevelGame()``, and assigning that to the variable ``game``.
| The object ``game`` is an instance of the class ``LevelGame``. 

.. code-block:: python

    class LevelGame:
        pass

    game = LevelGame()
