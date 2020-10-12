**digital_master and digital_slave**

Simple scripts for I2C communication between a master and slave Arduino via the digital pins.

**master_reader and slave_reader**

Simple scripts for I2C communication between a master and slave Arduino via the analog pins.

**BME**

BME.ino can be uploaded to a master Arduino connected to a single (BME) sensor and possibly a slave Arduino. The master Arduino then reads the sensor output and, if present, the text-based message the slave sends directly. Should you want to use the second Arduino, the slave_reader.ino sketch should be uploaded to the slave device.

**Hybrid_Master and Hybrid_Slave**

The hybrid experiment has a network of multiple Arduinos being able to send data to a master Arduino. Hybrid_Master.ino can be uploaded to an Arduino, which then acts as the master Arduino requesting data from subscriber (slave) Arduinos and shows this data. Hybrid_Slave.ino can be uploaded to Arduinos connected to (BME) sensors. These subscribers then read the sensors and give the data to the master upon request.