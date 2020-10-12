Hi honorable User!


If you haven't already, please first follow the [installation guide](projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Installation_guide.md). 

There are four options to use the program.
1. Measure using a real Arduino and Analog Discovery 2
2. Measure using a real Arduino and a simulated Analog Discovery 2
3. Only use a real Analog Discovery 2
4. Only use a simulated Analog Discovery 2

See below on how to set up each one of the four options.

Once you get the BIMBO up and running, you can navigate through the tabs and press the start/stop buttons to start measuring. When pressing scan on the Analog Discovery 2 tab, a window pops out which allows you to scan the data and save it over time. If you browse to save the file, it will save as a .nc. However, you can still change the extension before you save it to for example csv. Whatever extension is there, if you open it with notepad it will still be in the csv format. The is an example output file [here](projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Programs/Example_Measurements/exampleMeasurementAD2.csv). If you have ticked the Store config box it will also save a file with your config that looks like [this](projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Programs/Example_Measurements/exampleMeasurementAD2.yml). For scanning any data coming in via an arduino, e.g. temperature or pressure, press 'start scan' in the designated tab. This will start an invisible scan in the background. Pressing 'stop scan' will terminate the scanning procedure and create a .txt file in the source folder with the acquired data in the format: 

\[TemperatureArray]   
\[TimeArray]

For examples see [here](projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Programs/Example_Measurements/exampleMeasurementTemp.txt) and [here](projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Programs/Example_Measurements/exampleMeasurementPres.txt).

If you would like to use an Arduino. Please make sure it outputs the data in the format: time(in ms),temperature(as float),pressure(as float). If you have no way of getting actual data from an arduino, or don't know how, you can simply make it output simulated data in the correct format by uploading [simulation_for_arduino.ino](projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Programs/simulation_for_arduino.ino) to your arduino by using the [arduino IDE](https://www.arduino.cc/download_handler.php?f=/arduino-1.8.13-windows.exe)! In case you are using an Arduino Due, be sure to use the programming port on the arduino to upload any programs, it's the micro-usb port closest to the power input.

A list of known bugs can be found [here](/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Programs/Bugs.md).

In preparation of any of the four following options, open your preferred Python IDE and open the five .py files in experiment-design-2020-master\projects\SoftwareDesign_by_Nikita_Ravi_and_Jonno\Programs

**1. Arduino + real Analog Discovery 2**
- [ ] In the BIMBO_Interface.py uncomment the ArduinoWidget import in line 1.
- [ ] Uncomment the import from line 16 where the real controller is imported.
- [ ] Comment the import from line 17 where the simulated controller is imported.
- [ ] Uncomment lines 71 and 72 where the tabs for the Arduino are added .
- [ ] In order to start using the program, it is essential you plug in the Arduino measurement unit and make sure that it is outputting data in the required format.
- [ ] Once you have done this you have to check which COM-port is used to communicate with the device.
- [ ] This can be done (in Windows) by opening *Device Manager* and finding **Ports**. There it will say what COM-port is used.
- [ ] Now go to the ArduinoWidget.py file and change the 'COMX' in line 17 to whatever COM is used by your device.

You are all set to go, just run the BIMBO_Interface.py!

**2. Arduino + simulated Analog Discovery 2**
- [ ] In the BIMBO_Interface.py add the ArduinoWidget import to line 1 if it is not there.
- [ ] Comment the import from line 16 where the real controller is imported.
- [ ] Uncomment the import from line 17 where the simulated controller is imported.
- [ ] Uncomment lines 71 and 72 where the tabs for the Arduino are added.
- [ ] In order to start using the program, it is essential you plug in the Arduino measurement unit.
- [ ] Once you have done this you have to check which COM-port is used to communicate with the device.
- [ ] This can be done (in Windows) by opening *Device Manager* and finding **Ports**. There it will say what COM-port is used.
- [ ] Now go to the ArduinoWidget.py file and change the 'COMX' in line 17 to whatever COM is used by your device.

You are all set to go, just run the BIMBO_Interface.py!

**3. Only real Analog Discovery 2**
- [ ] In the BIMBO_Interface.py remove the ArduinoWidget import from line 1.
- [ ] Uncomment the import from line 16 where the real controller is imported.
- [ ] Comment the import from line 17 where the simulated controller is imported.
- [ ] Comment lines 71 and 72 where the tabs for the Arduino are added.


You are all set to go, just run the BIMBO_Interface.py!

**4. Only simulated Analog Discovery 2**
- [ ] In the BIMBO_Interface.py remove the ArduinoWidget import from line 1.
- [ ] Comment the import from line 16 where the real controller is imported.
- [ ] Uncomment the import from line 17 where the simulated controller is imported.
- [ ] Comment lines 71 and 72 where the tabs for the Arduino are added.

You are all set to go, just run the BIMBO_Interface.py!