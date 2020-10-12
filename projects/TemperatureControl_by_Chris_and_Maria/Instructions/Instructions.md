In this project you have to make a circuit which will measure the temperature of the box and using a peltier control it in a range you can define. Here are the steps you need to follow in order to achieve this:

### Part 1: Downloading and Installing Arduino

Go to [this site](https://www.arduino.cc/en/Main/software) and choose which suits for you depending on your operating system [here](https://git.science.uu.nl/m.lekou/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/Downloading_Arduino.jpg)

Then you can easily install the program.

As we will be using Arduino Due, you have to make an additional step:
Open the program
-> Go to tools -> Board “Arduino Yun” -> Board Manager-> Select:<< Arduino SAM Boards (32-bits ARM Cortex-M3) by Arduino>> as you can see [here](https://git.science.uu.nl/m.lekou/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/Installing_Arduino_Due.jpg)

Press Install and you are almost ready! (If you need more detailed description you can simply watch this [video](https://www.youtube.com/watch?v=ogXQIYnI8qE))

Re-open the Arduino, Go to tools -> Board “Arduino Yun” -> Arduino Due (Programming Port)

Now you are ready to copy-paste the [code](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/documantation/data/code.txt)!

### Part 2: Making the circuit

First, notice that you have all the required items:

1 Arduino Due

1 BreadBoard

1 sensor PTA 100

150 Ohm Resistor

4 Mosfets

1 Peltier with 1 heatsink 

The box

Extra Power Supply

Couple of Wires

During this part it will really help you to have open the [schematic](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/documantation/data/schematic.pdf). 
We can devide this part into 2 subparts:

1. Sensor subpart

Connect the PIN Ground of Arduino with the BreadBoard. 
The 150 Ohm Resistor must be connected with the ground and with the sensor.
The sensor has to be also connected with the PIN Ao and at 3.3V of Arduino.
[This](https://git.science.uu.nl/m.lekou/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/Sensor_Part.jpg) picture may help you.

2. Cooling/ Heating subpart

[This](https://git.science.uu.nl/m.lekou/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/Mosfet.png) picture will help you to understand when you see a MOSFET which side is the source, gate and drain.

**Mosfet 1**

Gate connected with:

- PIN 10 of Arduino

- Gate of Mosfet 3

Drain connected with 

- Gate of Mosfet 2

Source connected with 

- One side of Peltier(1)

- Drain of Mosfet 4

**Mosfet 2**

Source  connected with

- Other side of Peltier(2)

- Drain of Mosfet 3

Gate  connected with

- Gate of Mosfet 4

**Mosfet 3**

Source connected with

- Ground

**Mosfet 4**

Gate connected with

- PIN 2 of Arduino

Source connected with

- Ground

Also you will connect the two sides of Peltier with the Power Supply and you will turn it on to 12V

[This](https://git.science.uu.nl/m.lekou/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/CoolingHeating.jpg) picture will help you have a better understanding of the above part.

### Part 3: Connecting the code with the arduino

Connect the computer with the Arduino using a wire.
Open the program at your computer with the code and press upload.
It is ready!
If you want to see the value of Temperature just go to Tools and press Serial Monitor!
Also you can easily change the values of the range in the Temperature in this part of the code:
int T_L =15;
int T_H= 30;

Good luck :)




