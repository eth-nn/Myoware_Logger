# Myoware_Logger
NodeMCU Amica Logging program for the Myoware EMG Muscle Sensor (AT-04-001)

# Pin Connections
D1: Stop Recording Button

D2: 1st Status LED 

D3: 2nd Status LED

D4: 3rd Status LED

D5: 4th Status LED

A0: Myoware Sensor SIG pin

# Note 
The code is setup for 3.3v mode. I.e. the sensor power pin is connected to the 3.3v rail of the NodeMCU. For 5v operation replace the value 3.3 to 5 in emgLogger.py on line 51. Additionally, the remFi() function may or may not work for you as I have experienced difficulty with using it.

# Usage
After loading code via USB or WebREPL gain access to the REPL of the controller, again either through USB or WebREPL. 
1. Type "start()" and enter desired filename to store. 
2. Modify the sample rate from default if prefered.
3. Logging starts automaticly after the previous choice.
4. Stop by grounding the D1 pin either by the Stop Recording Button or wire. It is IMPORTANT to stop this way or else you may experience file corruption of the file.
5. Repeat if memory allows, else CTRL + C to exit into the main REPL to either extract the file from the device or clean up the onboard memory for new recordings.
