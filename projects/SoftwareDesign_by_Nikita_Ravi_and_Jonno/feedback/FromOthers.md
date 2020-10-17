## notes

complicated with the installation files, could be prepackaged in a zip  
**This could indeed be done, be would need to be redone everytime a file changes. So for now we will leave it like this.**  

labphew installation caused many issues, but we managed to get it working on one machine.  
**Nice you at least got it working on one machine.**  

Then a second readme about the usage start with "once you get the BIMBO up and running", it feels like some intermediate steps are missing that connect the two files.  
**Added meaning of BIMBO to the first README.**  

Could use some additional steps for the installation of the arduino or make it clear if its necesary or not, given the pre-installed arduino  
**We do not really know how to make it cleared, as there is already an explanation of how to upload a simulation program to an Arduino. We could have more clearer stated that the Arduino's given to you were already preinstalled. Also, the issue of data output is more something for the sensor people.**  

Steps for finding COM port are seperated, even though they are a single step. was slightly confusing.  
**Yes good point. Edited this in the README to make it one step.**  

unclear where the savefile goes for AD2, it says a path, which does not exist on the user's PC. Browse button does not work, gives error in spyder 'model labphew has no attribute 'parent_path''.  
when trying to save to a new path by writing it, it gets permission denied or no such file or directory.
**We were not able to reproduce this bug. For us the browse button works. There is also a default path already written, which you can edit to you own path by typing. You can also change the default path in the config file if you want (though this was not stated anywhere)**  

BIMBO can only be run once per spyder instance, only restarting spyder enables to run the script again.
replugging arduino does the job as well, or use a different IDE. Doesn't happen on MAC  
**This seems to be a spyder issue. Also does not happen on every machine. We do not really know how to fix this. We could in the future change the installation guide to use pycharm but we are not sure this will not happen there either.**  

the fixes for arduino read-out are using: 

In command prompt: 

ls /dev/*

To find the com port in the form /dev/tty.usbmodem* where * is the number. 

Change in the ArduinoWidget line 17: 

arduinoData = serial.Serial(port='/dev/tty.usbmodem14201', baudrate=9600)  #Rename the 'COMX' here to whatever COM is used by your device.  

**Added this to the README, thanks!**  
