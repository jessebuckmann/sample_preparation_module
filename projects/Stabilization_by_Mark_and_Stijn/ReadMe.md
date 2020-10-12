In this ReadMe-file, we will place the manual for our folders, as well as our experiments. 

The purpose of our experiment was to be able to both see/filter out vibrations, as well as get/keep the experiment level.

**Leveling:**
We firstly thought that, in order to get the experiment level, we could use to yaw, pitch and roll (which is something the acceleromotor is able to measure). In the end, you'll find that there is a big problem with trying to do it this way, which is that it resets everytime you restart the acceleromotor. However, it's a good experiment to do, because you will find that this part of the acceleromotor is very precize. 

To do the yaw pitch roll measurments, only the arduino uno, MPU6050 and connectors are needed in principle. With these components the MPU 6050 can be read out and that's all that’s needed. To do the calibration, a platform that can be rotated is needed. We used a machinist’s division table for this, but other platforms can be used. The machinist table is place in the upright position so (under the assumption that everything is straight) the z-axis of the chip is parallel to the gravitational vector. (again under the assumption we live on a flat earth with homogeneous gravity) When turning on the arduino it self calibrates to gravity so from that point everything is relative to that point. (this implies that for a reproducible result, the sensor needs to be booted in the exact same position)

When the sensor is setup and measuring the table can be rotated around the clock. This is done on increments of 1 degree from 0 < theta  < 10, than 5 degree intervals up to 90 degrees and from this point on only every 10 degrees to complete the circle. Whilst setting the angles it has to be taken in account that there is some mechanical give in the system. This could introduce a new error in the system when not dealt with correctly. To compensate for this give, the knob has to be put onder strain on the same side of each measurement point. This means either at the beginning or end of the give.  On each of the set angle points the yaw pitch and roll have to be manually read out. When all data is collected the points can be plotted in a program of your own choosing.

The Full Setup that we used can be found in the ["SetUp2"-folder](https://git.science.uu.nl/ued2020/experiment-design-2020/-/tree/master/projects/Stabilization_by_Mark_and_Stijn/TestRuns/YawPitchRole/SetUp).


**Vibrations:**
The main experiment that the "experiment-group" wanted to do, was the Cavendish-Experiment. This means that frequenties below 10 Hz will be "deadly" to the experiment. Our main objective thus became a little more specific than what we started with. However, we weren't to find a good way to "create" these low frequenties, in order to measure them and thus see if our system could filter them out. Because of this, we have only taken a look at frequenties between 20 and 100 Hz, because those we could create and thus see. 

In a vibration experiment, one needs 3 things:
- Something that creates the vibrations
- A mass that vibrates, on which you can stick your measuring device
- A device on which you can see the data measured.

In our case, that something that creates vibrations became a bass-speaker. This bass-speaker has been secured to a woaden board, which we put on some form of dampening substance. This way, the board will start to vibrate. On the other end of the board, we can then put our mass with our measuring device (the acceleromotor). Between the board and the mass, we can then prepare our system (this can be springs, a dampening substance, or in the easiest case: nothing). To see what has been measured, one has to take a look at what kind of acceleromotor one has. For our experiment, we used an acceleromotor that could directly be plugged into an oscilloscope, meaning that we could visualize the waves over there. However, one can also use the computer and the waveforms-programme of digilent, which is also able to visualize waves. The only thing that's left now, is to show how the system that you have taken a look at reacts to a certain frequency. This is done by making a bode plot, which can be done by a very good oscilloscope, but you can also do it by hand (which takes a lot longer).

The Full Setup that we used can be found in the ["SetUp2"-folder](https://git.science.uu.nl/ued2020/experiment-design-2020/-/tree/master/projects/Stabilization_by_Mark_and_Stijn/TestRuns/AccelerationTest/SetUp). We als made a ["MaterialsUsed"-file](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/Stabilization_by_Mark_and_Stijn/TestRuns/MaterialsUsed.md) where you can find all the materials that we used.