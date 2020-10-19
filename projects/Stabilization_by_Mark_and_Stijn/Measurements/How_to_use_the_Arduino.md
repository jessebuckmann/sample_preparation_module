Because our feedback group apperently had never worked with an arduino before, we decided that we would write a small little manual on how to operate arduino.

To start, one should read the following internet page, where is explained what arduino is, how to use it and etc [Click here](https://www.arduino.cc/en/Guide). From this page, one can also download the arduino-software. 

Once you have donwloaded this software, you should also download the needed accelerometer-code [Click here](https://github.com/jrowberg/i2cdevlib). Once downloaded, you should look for your specific accelerometer in the arduino-folder (If you would have a accelerometer that doesn't work with arduino, you can also find code for those over here). In our case, we used the MPU6050. Once you found your accelerometer, you copy this entire folder in your "arduino-libraries"-folder, along with the I2Cdev (which is needed for the arduino to be able to find your accelerometer). In most cases, this "arduino-libraries"-folder can be found at "C:\Program Files (x86)\Arduino\libraries". However, this depends on where you saved your arduino-software, so you try to find this yourselves. 

Once you have done this, open your arduino-software. Once opened, click on the following: Files -> Examples -> MPU6050 -> MPU6050_DMP6. In this file, all the code that we used can be found. With this code, you are able to measure the yaw, pitch, role and accelerations in x,y and z.

