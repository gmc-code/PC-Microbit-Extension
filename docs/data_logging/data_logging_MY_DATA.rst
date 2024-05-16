====================================================
Data Logging MY_DATA
====================================================

References for data logging to the microbit: V2 MICROBIT
---------------------------------------------------------

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/log.html
| See: https://python.microbit.org/v/3/api/log
| For raising exemptions see: https://docs.python.org/3/tutorial/errors.html#raising-exceptions

----

Microbit log module
----------------------------------------

.. code-block:: python

    from microbit import *
    import log

| This module lets you log data to a MY_DATA file saved on a microbit V2 MICROBIT USB drive.
| As of Jan 2023 Mu editor doesn't have the log module.
| Use the online editor at https://python.microbit.org/v/3.
| See online info for data logging: https://python.microbit.org/v/3/reference/data-logging

----

Microbit log
----------------------------------------

To log data to the microbit for later viewing:

#. First, add ``import log`` to the start of your program.
#. Set the data log column headings using ``log.set_labels()``.
#. Then add records to your data log with ``log.add()``
#. If you want to view the data from the serial port as it is being recorded on the microbit use ``log.set_mirroring(True)``, otherwise the serial port will be off by default.

    .. image:: images/online_serial.png
        :scale: 50 %
        :align: center
        :alt: online_serial

#. When finished the activity that is being recorded, read your data. Connect the microbit to a computer. The microbit will appear like a USB drive called MICROBIT. Double-click on MY_DATA file to open it in a web browser. Your data will be displayed in a table. Only do this once finished since no more data can be written to the file MY_DATA unless the microbit is unplugged and reconnected or reset.

    .. image:: images/microbit_drive.png
        :scale: 100 %
        :align: center
        :alt: microbit_drive

    .. image:: images/data_table.png
        :scale: 75 %
        :align: center
        :alt: data_table

#. Click **Visual Preview** to preview the data a graph directly in the MY_DATA file on your microbit.

    .. image:: images/my_data_buttons.png
        :scale: 75 %
        :align: center
        :alt: microbit_drive

    .. image:: images/data_graph.png
        :scale: 35 %
        :align: center
        :alt: data_graph

#. Click **the legend keys** to isolate individual lines of data in the graph. 

    .. image:: images/data_graph_brightness.png
        :scale: 35 %
        :align: center
        :alt: data_graph_brightness

#. Use the **Copy** button to copy the data so you can paste it straight into a spreadsheet. 
#. Use the **Download** button to download the data as a CSV (comma separated values) file which you can also import into a spreadsheet.

----

Data log
---------------

| Below is code to record brightness and accelerometer data to the microbit.


.. code-block:: python

    from microbit import *
    import log

    # Configure the labels and select a time unit for the timestamp
    log.set_labels('brightness', 'x', 'y', 'z', timestamp=log.SECONDS)

    # Send each data row to the serial output
    log.set_mirroring(True)


    def log_data():
        """Log the light level, press A to delete, press B to stop."""
        if button_a.is_pressed():
            display.show(Image.NO)
            # Delete the log file using the "full" options, which takes
            # longer but ensures the data is wiped from the device
            log.delete(full=True)
            display.show(Image.HAPPY)
        elif button_b.is_pressed():
            raise Exception("log finished")
        else:
            x = accelerometer.get_x()
            y = accelerometer.get_y()
            z = accelerometer.get_z()
            brightness=display.read_light_level()
            try:
                log.add(brightness=brightness, x=x, y=y, z=z)
            except OSError:
                # display.scroll("Log full")
                raise Exception("log full")


    run_every(log_data, ms=100)
    while True:
        display.show(Image.HAPPY)
        sleep(10000) #10 seconds


| ``log.set_labels('brightness', 'x', 'y', 'z', timestamp=log.SECONDS)`` sets the column headings for the data, which automatically includes a time stamp in the first column.  
| See: https://microbit-micropython.readthedocs.io/en/v2-docs/log.html#log.set_labels

| ``log.set_mirroring(True)`` sends the data to the serial port for monitoring the data. 
| See: https://microbit-micropython.readthedocs.io/en/v2-docs/log.html#log.set_mirroring

| ``run_every(log_data, ms=100)`` runs the function **log_data** every 100 milli-secs. 
| See: https://microbit-micropython.readthedocs.io/en/v2-docs/microbit.html#microbit.run_every.

| The log_data function records the readings via ``log.add(brightness=brightness, x=x, y=y, z=z)``. 
| See: https://microbit-micropython.readthedocs.io/en/v2-docs/log.html#log.add

| Pressing the A button deletes the log in full. It may take a few seconds. A no image is shown at the start of the deletion and a happy image is shown when done, and recording data starts again.
| Pressing the B button raises an exemption. This is the only way to stop the run_every process from continuing.
| A try-except block is used to take account of the error that occurs when the log is full. The normal practice would be to use ``display.scroll("Log full")`` in the except block. Doing so would result in repeated scrolling of this message. THat may be desirable in some cases. Instead ``raise Exception("log full")`` has been used to cause the run_every process to be stopped. A blank screen is then interpreted as if logging has finished.
| To restart logging, including deleting the log, hold down the A button while pressing the black reset button on the top back of the microbit.
| To restart logging, without deleting the log, press the black reset button on the top back of the microbit and new logging data will be appended to the log.

| A long sleep, ``sleep(10000)``, 10 seconds, has been set to cover the anticipated reading period. Adjust to suit the activity.

