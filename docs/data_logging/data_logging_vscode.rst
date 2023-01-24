====================================================
Data Logging vscode
====================================================

References for data logging
----------------------------------------

#. For byte decoding to a string see: https://docs.python.org/3/library/stdtypes.html#bytes.decode
#. For microbit uart see: https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html

----

Microbit code
----------------------------------------

| The uart (universal asynchronous receiver-transmitter) module lets you talk to a device connected to your board using a serial interface.
| Below is sample code to stream the accelerometer values to the serial port.
| This is for a microbit attached to a computer which will receive the data.

.. code-block:: python

    from microbit import *

        def send_data():
            x = accelerometer.get_x()
            y = accelerometer.get_y()
            z = accelerometer.get_z()
            acc_str = str(x) + ',' + str(y) + ',' + str(z)
            uart.write(acc_str)
            uart.write('\n')

        uart.init(9600)
        sending = False
        while True:
            if button_a.was_pressed():
                sending = True
            if button_b.was_pressed():
                sending = False
            if sending:
                send_data()
            sleep(100)

| Button pressing is used to control the sending of data.
| Press A to send data.
| Press B to stop sending data.
| In the code above, the accelerometer data is sent.

----

VScode
----------------------------------------

| The code below collects data from the microbit, saves it to a csv file and plots it.
| Adjust **data_count = 20** to the number of data points desired.
| Adjust **sleep_ms = 100** to the time in millisec between readings. Make sure that it is not shorter than teh sleep between sends on hte microbit.
| Adjust **ser.port = 'COM3'** to match the seerial port that is used when the micorbit is attached. It is usually 'COM3'.

| Adjust ``filename = 'microbit_data.csv'`` to suit.

.. code-block:: python

    import serial
    import time
    import csv
    import matplotlib.pyplot as plt

    data_count = 20
    sleep_ms = 100
    # Set up the Serial connection to capture the Microbit communications
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM3'
    ser.open()

    data = []
    # Loop until count reaches data_count
    count = 0
    while True:
        # Read in a line from the Microbit, decode the bytes string to a string
        microbitreaddata = ser.readline().decode('utf-8')
        # remove "\n" -- end of line from each line if present.
        data.append(microbitreaddata.rstrip())
        # print to terminal if wanted
        time.sleep(sleep_ms / 1000)
        count += 1
        if count > data_count:
            break

    # Close the serial connection
    ser.close()

    # convert lists of stings to lists of ints
    data_list = []
    for line in data:
        line_list = line.split(",")
        str_to_int = list(map(int, line_list))
        data_list.append(str_to_int)

    # save to csv

    myheaders = ['time','x','y', 'z']
    filename = 'microbit_data.csv'
    with open(filename, 'w', newline='') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(myheaders)
        writer.writerows(data_list)

    # convert data to 4 lists
    # [[21075, 36, 96, -1020]...]
    times = []
    x_vals = []
    y_vals = []
    z_vals = []
    for sublist in data_list:
        times.append(sublist[0])
        x_vals.append(sublist[1])
        y_vals.append(sublist[2])
        z_vals.append(sublist[3])

    xAxis = times
    plt.grid(True)
    plt.xlabel('times')
    plt.ylabel('acc')
    plt.title('acc v time')

    ## LINE GRAPH ##
    plt.plot(xAxis, x_vals, color='red', marker='x', label = "x_vals")
    plt.plot(xAxis, y_vals, color='blue', marker='o', label = "y_vals")
    plt.plot(xAxis, z_vals, color='green', marker='*', label = "z_vals")

    # format dates so they are angled to fit
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.show()

