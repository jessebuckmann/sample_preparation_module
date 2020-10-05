**15-9:**

We worked on trying to find out how a digilent would work and whether or not it would be compatible with our accelerometer. The first digilent that we tried was actually broken. It was not able to work without an external power source, something that a ordinary digilent should be able to do. We were able to get a second digilent to work. However, we noticed that our accelerometer would be much easier to work with, if we would use a Arduino instead, so we'll be doing that instead (we also asked the hard/software groupes if that wasn't a problem, which is wasn't).

**21-9:**

We solded (partially had sold) our accelerometer to a breadboard, so that we could connect it to a Arduino.

We then had a meeting with our Mentor (see Mentor_Meeting1_Notes.md).

We connected our Arduino Due to our accelerometer. However, we weren't able to generate any output. We later found out that Arduino Due and our accelerometer are not compatible. Because of this, we have asked Dante if we could get a Arduino Uno from him. If it can be found, we will be able to get this from him tomorrow (22-9-20), so that we can see if our accelerometer works.

We were however able to gain the measurements from the inner box (thus the minimal space needed for the Cavendish-Experiment). Hopefully tomorrow, we'll be able to gain the measurements from the outer box, so that we can calculate how much space we have for our spring-system.

Later this day, we gained the minimal dimensions needed in order to fit the experiments.
InnerBox - Width: 30, Length: 50, Hight: 35

**22-9:**
Mark did the Yaw, Pitch and Role measurements, in order to see if this part of the accelerometer was a viable option to measure the level of the final setup. Though the accelerometer produces decent values, we can't use this part of the accelerometer to calculate the level, because it calculates it's Yaw, Pitch and Role from the g's (gravitional vectors in x, y and z direction) and thus resets every time you start up a new measurement. This would mean that, in order to use the Yaw, Pitch and Role for the leveling system, we would need to always keep the accelerometer on and measuring, which isn't a viable option (since this would mean that our box would always have to give electricity to this part of our system).

**28-9:**
We did 




