<h1>Arduino Code</h1>
This folder contains the files to upload to the Arduinos in the smaller experiments.

<h2>digital_master and digital_slave<h2/>
Simple scripts for I2C communication between a master and slave Arduino via the digital pins.

<h2>master_reader and slve_reader<h2/>
Simple scripts for I2C communication between a master and slave Arduino via the analog pins.

<h2>BME</h2>
BME.ino can be uploaded to a master Arduino connected to a single (BME) sensor and possibly a slave Arduino. The master Arduino then reads the sensor output and, if present, the text-based message the slave sends directly. Should you want to use the second Arduino, the slave_reader.ino sketch should be uploaded to the slave device.

<h2>Hybrid<h2/>
The hybrid experiment assumes multiple Arduinos being able to send and recieve data. Hybrid_Master.ino can be uploaded to an Arduino, which then acts as the master Arduino requesting data from subscriber (slave) Arduinos and showing this data. Hybrid_Slave.ino can be uploaded to Arduinos connected to (BME) sensors. These subscribers then reads the sensors and gives the data to the master upon request.