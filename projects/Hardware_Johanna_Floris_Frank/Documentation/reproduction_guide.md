**General remarks**

- Since this projects is basically just connecting some Arduino's with some wires and running sketches on there, there are no special safety concerns inherent to the set-up
- Necesarry items are all found in our project box (along with a few redundant items you can leave in peace).

**Hardware required**

- Two Arduino UNO (other Arduino types would work, but the connection pins will be different than described here) with USB connecting cables
- 2 x Breadboard (For absolute certainty: to connect two wires, they must be placed in the same row of the breadboard)
- GybMep BME/BMP280 sensor
- Connecting wires
- PC with USB port (preferably 2, but one is also possible)
- Multimeter
- Two banana connector electric cables, two alligator connection clips

- If you do not receive a signal following the instructions, it is possible this is due to a non-function wire. This can be checked using a multimeter with two cables with alligator clip connections attached. With the multimeter in diode mode and the clips not in contact with each other, the multimeter should read a voltage of typically 2-3 V. Clamping each connecting end of the wire in one of the clips, the voltage difference should vanish (like what happens if you directly hold the clamps together). If the voltage doesn't drop, the wire is broken, which you can then throw in the bin.

**Setting up Arduino software**

- If you haven't already, download the Arduino [IDE](https://www.arduino.cc/en/Main/Software) software for your relevant operating system
- Open the Arduino program. Within the program, open the library manager **(sketch -> include library -> manage library, or press Ctrl+Shift+I)**, look for the **Adafruit_BME280 library**
- Install the Adafruit_BME280 library. The program should request to also install other libraries necessary for the Adafruit_BME280 library to function. Accept this request.
- Check if the **Wire, SoftwareSerial and Adafruit_Sensor libraries** are installed. The first two should be installed by default, the last one should be included if you have correctly followed the previous step. If any of them are, for some reason, not yet installed, do so.
- The links in this document link to Arduino sketches directly. In our experience, Arduino sketches need to be saved in a separate folder with the same name as the sketch itself (except for the .ino format denoter) for them to work.


**Experimental setup and instructions**

*Running the sketches*
- verify the code (the v on the top left) and upload to the relevant Arduino (the arrow next to the verify button). The USB port to which the program is uploaded can be changed under tools -> port, and checked on the bottom right.
- Read out the master/slave by opening the Serial monitor under tools, or **press Ctrl + Shift + M** (be sure you select the correct baud rate, which is given in the Arduino sketch as e.g. as an argument of the Serial.begin() functionality, typically set at 9600)
- **Take care** to upload the correct script with the correct COM

*Single master-single slave text-based I2C communication via analog ports, Arduino basics*
- Connect both Arduino's  to your PC (on seperarte USB ports) using the USB cables. Make sure you know the adress of the USB port each Arduino is connected to
- Pick one Arduino as the slave, the other as the master
- Connect the (analog) ground pins and the analog A4 and A5 pins on one Arduino to the same pins on the other Arduino
- Open the [master sketch](https://git.science.uu.nl/experiment-design-2020/-/tree/master/projects/projects/Hardware_Johanna_Floris_Frank/Arduino_code/master_reader.io.ino) and the [slave sketch](https://git.science.uu.nl/experiment-design-2020/-/tree/master/projects/Hardware_Johanna_Floris_Frank/Arduino_code/slave_reader.ino)
- Feel free to change around the delay in the master sketch or the print message in the slave sketch. After updating, the altered sketch (naturally) has to be verified and uploaded to the corresponding Arduino again.
- If you only have a single USB port, connect the 5V power output pin on your master Arduino with the Vin pin on the slave Arduino. Use the one USB port to first upload the slave sketch, and then connect the master to the USB port to power it, upload the master sketch and read out the master output.

*Read out the BME/BMP280 Sensor*
- Connect the *BME sensor* VIN and GND to the corresponding analog Arduino pins (5V, Ground)
- Connect the SCL and SDA from the sensor to the pins from the Aurduino
- Open the [BME sketch](https://git.science.uu.nl/experiment-design-2020/-/tree/master/projects/Hardware_Johanna_Floris_Frank/Arduino_code/BME.ino),

*Multi-slave single-master set-up for receiving seperate text-based messages and sensor data*
- Using the 1. breadboard: connect Vin and GND (ground) of the BME/BMP280 sensor directly to the 5V and GND pins on the slave Arduino.
- Using the 2. breadboard: connect the  SDA, SCL from the sensor with the slave and further with the master SDA, SCL in one line.
- Ground the slave to the master via the ground next to the SCL/SDA pins
- Open the [master sketch](https://git.science.uu.nl/experiment-design-2020/-/tree/master/projects/Hardware_Johanna_Floris_Frank/Arduino_code/Hybrid_Master.ino) and the [slave sketch](https://git.science.uu.nl/experiment-design-2020/-/blob/master/projects/Hardware_Johanna_Floris_Frank/Arduino_code/Hybrid_Slave.ino)


