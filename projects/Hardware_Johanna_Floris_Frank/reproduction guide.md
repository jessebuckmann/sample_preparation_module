**Setting up Arduino software**

- If you haven't already, download the Arduino [IDE](https://www.arduino.cc/en/Main/Software) software for your relevant operating system
- Open the Arduino program. Within the program, open the library manager (sketch -> include library -> manage library, or press Ctrl+Shift+I), look for the Adafruit_BME280 library
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

- If you do not receive a signal following the instructions, it is possible this is due to a non-function wire. This can be checked using a multimeter with two cables with alligator clip connections attached. With the multimeter in diode mode and the clips not in contact with each other, the multimeter should read a voltage of typically 2-3 V. Clamping each connecting end of the wire in one of the clips, the voltage difference should vanish (like what happens if you directly hold the clamps together). If the voltage doesn't drop, the wire is broken, which you can then throw in the bin.

**Single master-single slave text-based I2C communication via analog ports, Arduino basics**
- Connect both Arduino's  to your PC (on seperarte USB ports) using the USB cables. Make sure you know the adress of the USB port each Arduino is connected to
- Pick one Arduino as the slave, the other as the master
- Connect the (analog) ground pins and the analog A4 and A5 pins on one Arduino to the same pins on the other Arduino
- Open the [master sketch](link) and the [slave sketch](link), verify them (the v on the top left) and upload to the relevant Arduino (the arrow next to the verify button). The USB port to which the program is uploaded can be changed under tools -> port, and checked on the bottom right.
- Read out the master by opening the Serial monitor under tools, or press Ctrl + Shift + M (be sure you select the correct baud rate, which is given in the Arduino sketch)
- Feel free to change around the delay in the master sketch or the print message in the slave sketch 
- If you only have a single USB port, connect the 5V power output pin on your master Arduino with the Vin pin on the slave Arduino. Use the one USB port to first upload the slave sketch, and then connect the master to the USB port to power it, upload the master sketch and read out the master output.

**Multi-slave single-master set-up for receiving seperate text-based messages and sensor data**
- Connect the two Arduino's as in the previous subsection
- Using the breadboard, connect SDA, SCL, Vin and GND (ground) of the BME/BMP280 sensor to the SDA, SCL 5V and GND pins on the master Arduino
- Open the [master sketch](link) and the [slave sketch](link), verify them (the v on the top left) and upload to the relevant Arduino (the arrow next to the verify button). The USB port to which the program is uploaded can be changed under tools -> port, and checked on the bottom right.
- Read out the master by opening the Serial monitor under tools, or press Ctrl + Shift + M (be sure you select the correct baud rate, which is given in the Arduino sketch)
- Feel free to again change the master delay or the slave message, or to rub you hands and touch the sensor to see the temperature rise

**Single master-single slave text-based I2C communication via digital ports**