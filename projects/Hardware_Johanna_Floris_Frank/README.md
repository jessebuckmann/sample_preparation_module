**Welcome To The Hardware Project!** :raised_hands:

We, **Johanna**, **Frank** and **Floris** are the members of the Hardware-Group :v: .
The Hardware-Group aims to connect the techical parts of the box and to provide the experimentalists with a fast and save data transfer. 
Groups performing experiments and environment control give an Arduino-based text output.
The idea is now to connect these 'experiment Arduino's' as slaves to a central master Arduino, using which an I2C communication protocol may be established between them.
The master Arduino may then be read out by the computer running the data analysis and storage software.
The non-triviality lies in the fact that these slave Arduino's also serve as the master device within an experimental set-up by reading out the relevant sensor, which it must to upon request by the central master Arduino.
A more detailed report on context and theory, covering the I2C communication protocol and its main features (also compared to the frequently used SPI protocol), may be found [here](https://git.science.uu.nl/j.lomker/experiment-design-2020/-/blob/master/projects/Hardware_Johanna_Floris_Frank/Report_on_context_and_theory.md).

The first step is getting an I2C communication protocol running between two Arduino's, where a slave sends a simple text message to the master upon the master's request using the [Wire library](https://www.arduino.cc/en/Reference/Wire).
This message may then be printed by the master.
(link)

Secondly, a very simple set-up was designed in which a single master Arduino reads out a BME/BMP280 environmental dummy sensor using the [Adafruit sensor library](https://github.com/adafruit/Adafruit_Sensor).
(link)

The aformentioned two slaves, i.e. a sensor and a slave sending a text message, were combined into a single-master dual-slave set-up, so that the master receives both measurement values and the 
(link)

As a dummy circuit, it was attempted to connect a master Arduino to a slave
As of now, this set-up does not work yet because .
If this is 

Let's get this started :fire: !

**Cheerio !** :grin:
