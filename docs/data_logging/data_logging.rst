====================================================
Data Logging V2 MICROBIT
====================================================

References for data logging to the microbit
--------------------------------------------

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/log.html
| See: https://python.microbit.org/v/3/api/log


----

Microbit log
----------------------------------------

To log data to the microbit for later viewing:

    #. First, add ``import log`` to the start of your program.
    #. Set your data log column headings using ``log.set_labels()``.
    #. Then add records to your data log with ``log.add()``
    #. When finished the activity that is being recorded, read your data. Once the data has been logged on the micro:bit, plug the micro:bit into a laptop or desktop computer. The micro:bit will appear like a USB drive called MICROBIT. Look in there and you'll see a file called MY_DATA: Double-click on MY_DATA to open it in a web browser and you'll see a table with your data. Only do this once finished since no more data can be written to teh file MY_DATA unless the mirobit is unplugged and reconnected or reset.
    #. You can now: Preview your data visually as a graph directly in the MY_DATA file on your micro:bit. You can isolate individual lines of data in the graph by clicking on the legend. Use the copy button to copy the data so you can paste it straight into a spreadsheet. Download the data as a CSV (comma separated values) file which you can also import into a spreadsheet.
    

----

Microbit code
----------------------------------------

.. py:module:: log

| This module lets you log data to a MY_DATA file saved on a micro:bit V2 MICROBIT USB drive.
| As of Jan 2023 Mu editor doesn't have the log module.





| Below is code to record data to the microbit
| Use https://python.microbit.org/v/3/reference/data-logging

.. code-block:: python

    from microbit import *
    import log

    log.set_labels("heading", timestamp=log.SECONDS)
    while True:
        heading = compass.heading()
        log.add(heading )
        sleep(1000)

