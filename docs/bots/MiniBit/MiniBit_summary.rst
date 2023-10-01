====================================================
MiniBit summary
====================================================

| A summary of the MiniBit methods is below.
| Speeds values are 0 to 10.
| Suggested tightness values are from 1 to 10.

.. code-block:: python

    from microbit import *
    import MiniBit

    buggy = MiniBit.MiniBitMotors()
    buggy.forwards(speed=2, duration=None)
    buggy.backwards(speed=2, duration=None)
    buggy.left(speed=2, tightness=2, duration=None)
    buggy.right(speed=2, tightness=2, duration=None)
    buggy.spin_left(speed=2, duration=None)
    buggy.spin_right(speed=2, duration=None)
    buggy.stop()


    distance_sensor = MiniBit.MiniBitDistanceSensor()
    dist = distance_sensor.distance()





=
=





