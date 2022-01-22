# WatchMan
This is a repository to contain the code for the Intelligent Surveillance system.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Introduction
* The idea of the project is to create an economical system that fulfills the need of a smart alarm system.
* The idea is to create a trip alarm system to capture video footage of intrusion once triggered.
* It is attempted that the system will capture and store the video in the system and the recording will persist unless there is no activity found in the camera feed.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Circuit Details & Code Functionality
The circuit is wired, and contains only an UNO, a HC-SR04 and a bluetooth module (HC-05). 
It is planned to make the communication between the arduino and system wireless using bluetooth module. Once we connect to the system, our code in the main.py file runs and UV sensor start detecting the intrusions. 
As soon as any Intrusion is detected, i.e., the camera detects some activity [status changes from Unoccupied to Occupied], the webcam start recording.
It'll keep recording until and unless the status changes back to Unoccuppied.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Real Life Applications
- Data and Storage saver.
- Enhanced security (while in the nearby proximity we can get feed of camera on any of the device which is connected to the bluetooth)
- Better and Cost efficient way of imporving your House security.
