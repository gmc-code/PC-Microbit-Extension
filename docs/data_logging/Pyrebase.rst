====================================================
Pyrebase
====================================================

This allows one microbit to communicate to another microbit over the internet with google firebase as the database.

References for python data communication
-----------------------------------------------

#. See https://www.youtube.com/watch?v=8IWalfRUk1M
#. https://github.com/codefirstio/Python-Firebase-Realtime-Database-CRUD-Series/blob/master/createdata.py
#. https://github.com/nhorvath/Pyrebase4

----

Set up Firebase database
-------------------------------

#. Log into a google account
#. Go to firebase: https://firebase.google.com/
#. Click **Go to console** on top right.
#. Click **Create a project**.
#. Enter a title such as: **microbit-acc**.
#. Modify or use the default Project ID such as **microbit-acc**.
#. Turn on Google Analytics for the project.
#. Click **Continue**.
#. Set the Google Analytics location.
#. Click to accept Google Analytics terms.
#. Click **Create Project**.
#. When the project is ready, click **Continue**.

#. In the left sidebar, click **Build**.
#. In the left sidebar, click **Realtime Database**.
#. Click **Create Database**.
#. Choose the Realtime Database location from the dropdown.
#. Choose **Start in test mode** which gives 30 days to lock it.
#. Click **Enable**.

#. In the Realtime Database window choose the **Rules** tab.
#. Edit the read and write rules to a future date for convenience such as "now < 2556144000",  // 2051-01-01
#. (For getting a suitable epoch timestamp see: https://www.epochconverter.com/)
#. Click **Publish**.

#. Choose the **Data** tab.
#. Copy the url for the database from the link shown.
#. Paste the url into the python code to the connect to the database.

----

Install python **pyrebase** library
----------------------------------------

* Type cmd in windows search to open the Command Prompt. Type (and press Enter):

    ``pip install Pyrebase4``

| This installs pyrebase. Pyrebase4 is a wrapper to install the recent libraries that pyrebase requires.

.. admonition:: Tip
    
    #. If using Mu editor:
    #. Click on the **Mu Administrator** gear icon in bottom right corner of the Mu editor window.
    #. Click on the **Third Party packages** tab.
    #. Paste in **Pyrebase4** at bottom of the list.
    #. Click OK

----

Register Web App to get config details
----------------------------------------

#. Continue on the firebase website. 
#. In the left sidebar, click **Project Overview**.
#. Click the Web icon **</>**
#. Enter the project name to register: e.g. **microbit-acc**.
#. Click **Register app**.
#. Copy the code in the **const firebaseConfig** dictionary. and paste that into the python code. Add quotes to the keys to make them work in python.
#. 







