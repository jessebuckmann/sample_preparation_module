## intructions to use  the arduino to measure battery voltage

1. download the arduino IDE from their [website](https://www.arduino.cc/).
2. Under Tools > Boards > Board manager, download the correct package for the arduino you are using.
3. in the arduino code change the factor of 3.3 to the maximum voltage the model you are using can measure. (3.3 is for Due, for most others its 5.0)
4. Connect the voltage divider to the battery and the arduino as in the picture below. The tape on the voltage divider indicates to which pole it must be connected on the battery (red to red, black to black).
![Arduino_voltage_divider](./arduino_voltage_divider.png)
5. Verify the script and upload it to the arduino to run the code.
6. Open the serial window to read the results.