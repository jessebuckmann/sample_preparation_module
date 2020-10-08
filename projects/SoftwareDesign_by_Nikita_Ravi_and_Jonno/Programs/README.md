Hi honorable User!

There are three options to use the program.
1. Measure using a real Arduino and Analog Discovery 2
2. Measure using a real Arduino and a simulated Analog Discovery 2
3. Only use a real Analog Discovery 2
4. Only use a simulated Analog Discovery 2


**1. Arduino + real Analog Discovery 2**
- [ ] In the BIMBO_Interface.py add the ArduinoWidget import to line 1 if it is not there
- [ ] Uncomment the import from line 16 where the real controller is imported
- [ ] Comment the import from line 17 where the simulated controller is imported
- [ ] Uncomment lines 70 and 71 where the tabs for the Arduino are added 
- [ ] In order to start using the program, it is essential you plug in the Arduino measurement unit.
- [ ] Once you have done this you have to check which COM-port is used to communicate with the device.
- [ ] This can be done (in Windows) by opening *Device Manager* and finding **Ports**. There it will say what COM-port is used.
- [ ] Now go to the ArduinoWidget.py file and change the 'COMX' in line 14 to whatever COM is used by your device.

You are all set to go, just run the BIMBO_Interface.py!

**2. Arduino + simulated Analog Discovery 2**
- [ ] In the BIMBO_Interface.py add the ArduinoWidget import to line 1 if it is not there
- [ ] Comment the import from line 16 where the real controller is imported
- [ ] Uncomment the import from line 17 where the simulated controller is imported
- [ ] Uncomment lines 70 and 71 where the tabs for the Arduino are added 
- [ ] In order to start using the program, it is essential you plug in the Arduino measurement unit.
- [ ] Once you have done this you have to check which COM-port is used to communicate with the device.
- [ ] This can be done (in Windows) by opening *Device Manager* and finding **Ports**. There it will say what COM-port is used.
- [ ] Now go to the ArduinoWidget.py file and change the 'COMX' in line 14 to whatever COM is used by your device.

You are all set to go, just run the BIMBO_Interface.py!

**3. Only real Analog Discovery 2**
- [ ] In the BIMBO_Interface.py remove the ArduinoWidget import from line 1
- [ ] Uncomment the import from line 16 where the real controller is imported
- [ ] Comment the import from line 17 where the simulated controller is imported
- [ ] Comment lines 70 and 71 where the tabs for the Arduino are added 


You are all set to go, just run the BIMBO_Interface.py!

**4. Only simulated Analog Discovery 2**
- [ ] In the BIMBO_Interface.py remove the ArduinoWidget import from line 1
- [ ] Comment the import from line 16 where the real controller is imported
- [ ] Uncomment the import from line 17 where the simulated controller is imported
- [ ] Comment lines 70 and 71 where the tabs for the Arduino are added 

You are all set to go, just run the BIMBO_Interface.py!


