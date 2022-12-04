====================================================
Excel Data Logging
====================================================

References for data logging
----------------------------------------

#. https://microbit.org/get-started/user-guide/data-logging/
#. https://microbit.org/projects/make-it-code-it/python-wireless-data-logger/
#. https://www.hackster.io/HackingSTEM/visualize-data-in-excel-with-micro-bit-and-makecode-be21fb
#. https://www.microsoft.com/en-us/education/hackingstem/datastreamer

----

Excel Data Streamer Add-In
----------------------------------------

To connect live data with the Data Streamer add-in for Excel, first enable the Data Streamer add-in.

    #. Open Excel.
    #. Go to File > Options > Add-Ins.
    #. In the Manage box at the bottom, select COM Add-ins, and click Go.
    #. In the COM add-Ins dialog box, select the box next to Microsoft Data Streamer for Excel add-in, then click OK.
    #.The Data Streamer tab will now be in the tabs at the top of the ribbon.

----

Create microbit code first
----------------------------------------

| Below is sample code to stream the accelerometer x values to the serial port to Excel.

.. code-block:: python

    from microbit import *


    uart.init(9600)
    while True:
        x = accelerometer.get_x()
        acc_str = str(x)
        uart.write(acc_str)
        uart.write('\n')
        sleep(100)

There are two ways to send data via the serial port.
#. The ``print`` statement sends a string via the USB connected serial port. 
#. The ``uart.write`` method sends data via the USB connected serial port when the tx and rx pins are not specified.

The ``uart`` module lets you talk to a device connected to your board using a serial interface.
----

Using Excel Data Streamer
----------------------------------------

Excel's Data Streamer Add-in gathers data from external devices via the USB serial port on the computer. 

    #. Open Excel and select the **Data Streamer tab** a the top of the ribbon.
    #. Click “**connect your device**” to select the micro:bit USB device.
    #. Click “**start data**” in the Data Streamer tab. 
    #. 4 sheets will be created: Sheet1, Data In, Data Out, Settings.
    #. Click “**stop data**” in the Data Streamer tab.
    #. Choose the Settings Sheet. Adjust the settings: 
        #. Set Data rows to 10 
        #. Set Data channels to 1
        #. Set Data orientation to Newest first using the drop down.
    #. navigate to the **Data In** sheet to see micro:bit data.


