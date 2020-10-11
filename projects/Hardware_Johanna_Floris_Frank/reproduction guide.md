**Setting up Arduino software**

- If you haven't already, download the Arduino [IDE](https://www.arduino.cc/en/Main/Software) software for your relevant operating system
- Open the Arduino program. Within the program, open the library manager (sketch -> include library -> manage library, or press Ctrl+shift+I), look for the Adafruit_BME280 library
- Install the Adafruit_BME280 library. The program should request to also install other libraries necessary for the Adafruit_BME280 library to function. Accept this request.
- Check if the Wire, SoftwareSerial and Adafruit_Sensor libraries are installed. The first two should be installed by default, the last one should be included if you have correctly followed the previous step. If any of them are not installed, do so.

**Hardware required**

- Two Arduino UNO (other Arduino types would work, but the connection pins will be different than described here) with USB connecting cables
- Breadboard
- GybMep BME/BMP280 sensor
- Connecting wires
- PC with USB port (preferably 2, but one is also possible)
- Multimeter
- Two banana connector electric cables, two alligator connection clips

- If you do not receive a signal following these instructions, it is possible this is due to a non-function wire. This can be checked using a multimeter with two cables with alligator clip connections attached. With the multimeter in diode mode and the clips are not into contact, the multimeter should read a voltage of typically 2-3 V. Clamping each connecting end of the wire in one of the clips, the voltage difference should vanish (like what happens if you directly hold the clamps together). If it doesn't 

I2C communication via 
- If you only have a single USB port, connect the 5V power output pin on your master Arduino with the Vin pin on the slave Arduino