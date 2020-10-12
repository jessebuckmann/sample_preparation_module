**Welcome To The Hardware Project!** :raised_hands:

We, **Johanna**, **Frank** and **Floris** are the members of the Hardware-Group :v: .
The Hardware-Group aims to connect the techical parts of the box and to provide the experimentalists with a fast and save data transfer. 
Groups performing experiments and environment control give an Arduino-based text output.
The idea is now to connect these 'experiment Arduino's' as slaves to a central master Arduino, using which an I2C communication protocol may be established between them.
The master Arduino may then be read out by the computer running the data analysis and storage software.
The non-triviality lies in the fact that these slave Arduino's also serve as the master device within an experimental set-up by reading out the relevant sensor, which it must to upon request by the central master Arduino.
A more detailed report on context and theory, covering the I2C communication protocol and its main features (also compared to the frequently used SPI protocol), may be found [here](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/Hardware_Johanna_Floris_Frank/Documentation/Report_on_context_and_theory.md).

**The Experiment(s)**

The first step is getting an I2C communication protocol running between two Arduino's, where a slave sends a simple text message to the master upon the master's request using the [Wire library](https://www.arduino.cc/en/Reference/Wire).
This message may then be printed by the master.

Secondly, a very simple set-up was designed in which a single master Arduino reads out a BME/BMP280 environmental dummy sensor using the [Adafruit sensor library](https://github.com/adafruit/Adafruit_Sensor).

The aformentioned two slaves, i.e. a sensor and a slave sending a text message, were combined into a single-master dual-slave set-up, so that the master receives both measurement values and the text message.

To simulate an experiment Arduino connected to the central master Arduino, a single slave reading out the BME/BMP280 was connected to the master.
It was attempted to have a text tranfser - a data request from the master to the slave, in order to get the measurement startet. Then the slave should read out the data fromthe sensor to send the data as answer to the master.
This set-up did not end up working properly, presumably because the connection of the analog pins somehow leads to the sensor being recognized by the master.

**The Next Steps**

Considering the failure of the previously mentioned set-up, communication between the two Arduino's via the digital port was attempted.
A simple text-based I2C communication protocol between two Arduino's via the digital pins using the [SofwareSerial library](https://www.arduino.cc/en/Reference/SoftwareSerial) was achieved, altough as of yet they are poorly synchronized since the reading and printing my the master is much slower compared to the slave sending the message. (link)
If this is fixed, it should be possible to transfer sensor data between sensor and master upon request of the master. After that, a generalization to a connection with multiple (two for a start) masters may be made.


Should you want to reproduce these circuits, have a look at the [manual](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/Hardware_Johanna_Floris_Frank/Documentation/reproduction_guide.md).

Let's get this started :fire: !

**Cheerio !** :grin:
