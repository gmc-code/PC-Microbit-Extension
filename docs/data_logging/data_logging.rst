====================================================
Excel Data Logging
====================================================

References for data logging
----------------------------------------

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/log.html

#. https://microbit.org/get-started/user-guide/data-logging/
#. https://microbit.org/projects/make-it-code-it/python-wireless-data-logger/
#. https://www.hackster.io/HackingSTEM/visualize-data-in-excel-with-micro-bit-and-makecode-be21fb

----

Microbit log
----------------------------------------

To log data to the microbit for later viewing:

    #. First, add ``import log`` to the start of your program.
    #. Set your data log column headings using ``log.set_labels()``.
    #. Then add records to your data log with ``log.add()``
    #. Read your data. Once the data has been logged on the micro:bit, plug the micro:bit into a laptop or desktop computer. The micro:bit will appear like a USB drive called MICROBIT. Look in there and you'll see a file called MY_DATA: Double-click on MY_DATA to open it in a web browser and you'll see a table with your data.
    #. You can now: Preview your data visually as a graph directly in the MY_DATA file on your micro:bit. You can isolate individual lines of data in the graph by clicking on the legend. Use the copy button to copy the data so you can paste it straight into a spreadsheet. Download the data as a CSV (comma separated values) file which you can also import into a spreadsheet.
    

----

Create microbit code first
----------------------------------------

| Below is sample code to stream the accelerometer x values to the serial port to Excel.

.. code-block:: python

    from microbit import *
    import log

    log.set_labels("heading", timestamp=log.SECONDS)
    while True:
        heading = compass.heading()
        log.add(heading )
        sleep(1000)

