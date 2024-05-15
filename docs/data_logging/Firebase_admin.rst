====================================================
Python Data communication
====================================================

This allows one microbit to communicate to another microbit over the internet with google firebase as the database.

References for python data communication
-----------------------------------------------

#. See https://www.youtube.com/watch?v=J2hqqx__IY4
#. https://www.youtube.com/watch?v=fzMVV7ZMyvE&t=3s
#. https://www.youtube.com/watch?v=fzMVV7ZMyvE&t=3s
#. https://www.youtube.com/watch?v=fzMVV7ZMyvE&t=3s
#. https://www.youtube.com/watch?v=fzMVV7ZMyvE&t=3s
#. https://github.com/LCCompSci/FirebaseComplete
#. https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/


----

Get the microbit communication port
--------------------------------------

#. Connect the microbit to a laptop.
#. Type ``cmd`` in the window search to open the command prompt.
#. At the prompt, type ``chgport``.
#. At typical response might be: ``COM6 = \Device\thcdcacm0``
#. So the microbit would be on **COM6** port.


----

Set up Firebase database
-------------------------------

#. Log into a google account
#. Go to firebase: https://firebase.google.com/
#. Click **Go to console** on top right.
#. Click **Create a project**.
#. Enter a title such as: **Microbit-data**.
#. Modify or use the default Project ID such as **microbit-data-2021**.
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

Install python library: firebase-admin
----------------------------------------

pip install firebase-admin

.. admonition:: Tip
    
    #. If using Mu editor:
    #. Click on the **Mu Administrator** gear icon in bottom right corner of the Mu editor window.
    #. Click on the **Third Part packages** tab.
    #. Paste in **firebase-admin** at bottom of the list.
    #. Click OK
    #. 
----

Authenticate the Google Service Account
----------------------------------------

#. Firebase will allow access to Firebase server APIs from Google Service Accounts. 
#. To authenticate the Google Service Account, a private key in JSON format is required.
#. To generate the key, in the left sidebar, go to **Project Overview**, click **Project settings**, click **Service Accounts**, click **Generate new private key**, click **Generate key** to download the file, and move it from the downloads folder to the folder with the python files for using it.
#. The path to this JSON file must be provided to create the credentials object. 


