## notes

complicated with the installation files, could be prepackaged in a zip

labphew installation caused many issues, but we managed to get it working on one machine.

Then a second readme about the usage start with "once you get the BIMBO up and running", it feels like some intermediate steps are missing that connect the two files.

Could use some additional steps for the installation of the arduino or make it clear if its necesary or not, given the pre-installed arduino

Steps for finding COM port are seperated, even though they are a single step. was slightly confusing.

unclear where the savefile goes for AD2, it says a path, which does not exist on the user's PC. Browse button does not work, gives error in spyder 'model labphew has no attribute 'parent_path''.
when trying to save to a new path by writing it, it gets permission denied or no such file or directory.

BIMBO can only be run once per spyder instance, only restarting spyder enables to run the script again.
replugging arduino does the job as well, or use a different IDE. Doesn't happen on MAC

the fixes for arduino read-out are using: 

In command prompt: 

ls /dev/*

To find the com port in the form /dev/tty.usbmodem* where * is the number. 

Change in the ArduinoWidget line 17: 

arduinoData = serial.Serial(port='/dev/tty.usbmodem14201', baudrate=9600)  #Rename the 'COMX' here to whatever COM is used by your device.
