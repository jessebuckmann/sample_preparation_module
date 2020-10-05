The goal of our group is to provide a stable platform for the measurement setups. This goal was split up in 2 sub goals: Measurement of the level and oscillations and designing a level platform to isolate these oscillations. 
Looking into the methods used to measure the oscillations and level an accelerometer was found to be easiest to use. The first accelerometer used was a MPU6050 GY521, a sensor designed to be read out using an arduino. This sensor has a wide array of pre-written libraries online which makes using the sensor quite easy. 
The data gained from the sensor is dependant on the chosen library, the main differences here lay in the readout of the acceleration on x,y,z yaw, pitch, roll or the position in yaw, pitch and roll. Furthermore the sensor is able to measure temperature but this option was not used for this project. The sensor was first used in a measurement to check the accuracy of the yaw pitch roll position of the sensor. This was done by placing the sensor on a division table on a mill. Using this table the sensor can be turned accurately within 0.016 degrees. A photo of the setup can be seen here 

<img src = "TestRuns/YawPitchRole/SetUp/YawPitchRoleMeasurement_TotalView.jpeg" width="200" height= "200" >



The sensor was put as square to the table as possible but the measured signal proves this wasn’t completely true. The plots below show the measured yaw, pitch roll as a function of the set angle by the division table. Here the table is turned in the pitch direction. To display the roll accuracy in more detail the measured angle is subtracted from the set angle. 

INSERT FIG OF GRAPHS

As can be seen in the yaw and roll plots, the division table was not completely square to the mill table. When the setup was completely square the line should be all 0. However when looking at the pitch plot, it can be seen that the more the yaw and roll differ from 0, the more the pitch differs from the set angle. In theory the measured angles should be accurate up to 0.01 degree. This is however difficult to prove using the measurements done. Looking at the difference plot one conclusion can be that the angle can be measured within a 1.3 degree accuracy. However, because the yaw and roll there is a good argument that the accuracy is higher than the 1.3 degrees. However it is beyond the scope of the project to determine the effective accuracy.