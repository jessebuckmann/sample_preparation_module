In this project you have to make a circuit which will measure the temperature of the box and using a peltier control it in a range you can define. Here are the steps you need to follow in order to achieve this.

Notice: Don't expect the heating/cooling part to function normally yet. However, once you have completed the setup, the values of the temperature should be displayed on your screens. So, the aim until now is to reproduce the complete setup and to measure the temperature.

**Safety Instructions**: 

Although we are in a range of low voltage that it is not farmfull, attention must be taken when you are controlling the voltage of Power Supply. What we mean is be carefull to set it in the value we have indicated and not much more. If you do that there is nothing to worry about!

As you will see below, we use Peltier- an item that from its one side will be heated and on the other side cooled. (This is explained from the direction of the current, if you want to learn more about its operation see [context and theory](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/documantation/data/template_Article.pdf)). So, when it is activated it can be very hot so we strongly advise you to not touch it in that case!!!

### Part 1: Downloading and Installing Arduino

Go to [this site](https://www.arduino.cc/en/Main/software) and choose which suits for you depending on your operating system [here](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/Downloading_Arduino.jpg)

Then you can easily install the program.

Open the Arduino, Go to tools -> Board “Arduino Yun” -> Arduino Uno

Now you are ready to copy-paste the [code] (will be added)!

Notice: It is necessary to have Arduino Uno which provides us with 5V, in contrast to Arduino Due which can provides us only with 3.3V. So don't try to do this with Arduino Due!

### Part 2: Making the circuit

First, notice that you have all the required items:

1 Arduino Uno

1 BreadBoard

1 sensor PTA 100

150 Ohm Resistor

4 Mosfets

1 Peltier with 1 heatsink 

[The box](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/the_box.jpg) (the arrow shows where you can put the peltier)

Extra [Power Supply](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/power_supply.jpg)

Couple of Wires

During this part it will really help you to have open the [schematic](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/documantation/data/schematic.pdf). 
We can devide this part into 2 subparts:

1. Sensor subpart

Connect the PIN Ground of Arduino with the BreadBoard. 
The 150 Ohm Resistor must be connected with the ground and with the sensor.
The sensor has to be also connected with the PIN Ao and at 3.3V of Arduino.
[This](https://git.science.uu.nl/m.lekou/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/Sensor_Part.jpg) picture may help you.

2. Cooling/ Heating subpart

[This](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/Sensor_Part.jpg) picture will help you to understand when you see a MOSFET which side is the source, gate and drain.

Notice: The naming of the below Mosfets is just indicating, namely you will choose randomly which Mosfet will be the 1st. 2nd etc. 

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

Also you will connect the Power Supply with the drain of Mosfet 2 and Mosfet 3  and you will turn it on to 12V.

[This](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/TemperatureControl_by_Chris_and_Maria/Instructions/CoolingHeating.jpg) picture will help you have a better understanding of the above part.

### Part 3: Connecting the code with the arduino

Connect the computer with the Arduino using a wire.
Open the program at your computer with the code and press upload.
It is ready!
If you want to see the value of Temperature just go to Tools and press Serial Monitor!
Also you can easily change the values of the range in the Temperature in this part of the code:
int T_L =15;
int T_H= 30;

Good luck :)




