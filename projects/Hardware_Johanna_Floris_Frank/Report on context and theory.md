As per request of the software group, the experiments and sensor groups will provide a (text-based) Arduino output. 
The aim of this project is now to facilitate the transfer of this data output to the central CPU where data is analysed and displayed. 
This is done by connecting the Arduino devices these experiment and sensor groups use as slave devices to a central master Arduino device, which can be used to implement a serial data transfer protocol to ensure the data is transferred to the CPU in the required format. 
Another advantage is the possibility of easily connecting more slave devices if more experiment modules or sensor are to be added to the measurement box.

With this master Arduino, a uniform data transfer protocol may be implemented. We have opted for the I^2C protocol, which has several advantages over other serial protocols, including it requiring two connection wires (instead of four for e.g. SPI) and thus allowing more and more flexible connection of multiple slave devices.
Another advantage would be the ease with which it is implemented using pre-existing Arduino libraries such as the Wire library, especially considering the limited time available.
Finally, I^2C has the advantage of providing ACK/NACK (acknowledgment/ Not-acknowledgement) features that provide help in error handling.
Disadvantages such as relatively low data transfer speed (compared to SPI) and noise susceptibility (high compared to SSD, low compared to SPI) are supposed to be less of an issue.

Tests for the workings of the single master, multiple slave set-up are very straightforward: the slaves give an output (in the form of a string, byte or float) which have to be read by the master, which can be confirmed by simply checking the relevant COM output on a pc connected to the master.
To be useful for implementation, it also has to be established what the most efficient format of transferred data between the Arduinos is, i.e. as strings, floats or decomposed as bytes. After a working set-up is created (i.e. one or multiple 'talking' to a single master), factors like data transfer speed may be tested.

After familiarizing ourselves with the workings of Arduino, we gathered ideas about data transfer and worked on (1) a communication between two Arduinos in a master to slave relation, in which the slave sends a simple string upon being requested by the master.
From that we continued with an environmental measurement by setting up a circuit that included (2) a senor, connected to a single (master) Arduino and further to our computer.
The experiment was further expanded by coupling multiple slaves, a BME/BMP280 environmental sensor (providing measurement data) and another slave Arduino (providing the aforementioned string) to the master, which proved succesful.
Finally, an attempt was made to transfer sensor data to the master Arduino via a slave Arduino. 
This, however, has not worked yet (partially due to our still-limited understanding of working principles), and we will continue with that this coming week.
In the end we used the sensor to master (1) setup to provide the software group with an Arduino measurement to verify their code.
Here we had to adjust the Arduino code to transfer the data in the adequate file format/structure for the software group.