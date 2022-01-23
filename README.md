# WatchMan

An intelligent survelliance system that uses sonars and cv to save power and footage space

[![Setup Image]("https://raw.githubusercontent.com/Kaushikdey647/WatchMan/main/assets/images/img1.jpeg")]("https://github.com/Kaushikdey647/WatchMan/")
## Introduction
* The idea of the project is to create an economical system that fulfills the need of a smart alarm system.
* The idea is to create a trip alarm system to capture video footage of intrusion once triggered.
* It is attempted that the system will capture and store the video in the system and the recording will persist unless there is no activity found in the camera feed.

## How to use
1. If you don't have python yet, install it from [here]("https://www.python.org/downloads/").
2. Clone this repository using the instructions above.
3. Now navigate to the /python subdirectory, and install necessary python dependencies using: `pip install -r requirements.txt`
4. Finally make sure the camera is accessible and run the script using `python main.py`

## Circuit Details & Code Functionality
1. The circuit is wired, and contains only an UNO, a HC-SR04 and a bluetooth module (HC-05). 
2. It is planned to make the communication between the arduino and system wireless using bluetooth module. Once we connect to the system, our code in the main.py file runs and UV sensor start detecting the intrusions. 
3. As soon as any Intrusion is detected, i.e., the camera detects some activity [status changes from Unoccupied to Occupied], the webcam start recording.
4. It'll keep recording until and unless the status changes back to Unoccuppied.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Real Life Applications
- Data and Storage saver.
- Enhanced security (while in the nearby proximity we can get feed of camera on any of the device which is connected to the bluetooth)
- Better and Cost efficient way of imporving your House security.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hardware Arrangement
Image - https://github.com/Kaushikdey647/WatchMan/blob/main/hardware.jpeg
