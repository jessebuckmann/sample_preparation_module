# Reproducibility report

## Experiment/team: 
Hardware by Floris, Frank and Johanna

## Reviewers: 
Geert, Maria and Olaf

## Report 

### Documentation:

1.	Could you understand the purpose of the experiment? Explain.
The purpose of the experiment is to rebuild three set-ups connecting different arduinos and sensors. Within the larger project this is of importance since we want all the different components to be connected to each-other and to have communication between them. 

2.	Were the safety instructions clear?
Yes, since there were no safety instructions they were clear.

3.	How helpful is the documentation for reproducing the measurement?
The documentation was not quite complete. It is assumed that you have prior knowledge of arduino's and of the hardware. It would have been helpfull if the instructions would have included more detail on the placement of the wires (e.g. to which pins in the arduino the sensor had to be connected) in the arduino and or the sensors. It would have helpful as well if there would have been more instructions on what every element does and how it looks like (e.g. we did not know what the sensors look like and could not find them in the beginning).

4.	Did you get stuck at some point? What extra help did you need to proceed?
Yes, from the instructions alone it was not clear if we needed to use one arduino, or use them both at the same time. Luckily this was mentioned briefly in the readme so with that information we were able to figure out the set-up. Also, Maria and Geert had prior knowledge of working with arduinos and breadboard so we did not have to look up how they work in more detail to reproduce the set-ups

5.	Are you guided to reproduce previous measurements? How easily could you navigate through the project documentation?
The links to the necesarry sketches were placed in the instructions so this was quite convenient. We did miss clear goals by which we could check if our set-ups lead to the same results as the project group. We had no way of checking this. It was possible to deduce this for the first two set-ups from the code but not for the third set-up.

6.	What can be improved in the documentation?
The instructions could be improved by adding schematic drawings of each set-up. This would make the placing of all the components and wires clearer and easier to reproduce. Also provide a clear goal to the experiment, what should each set-up do exactly? How can we confirm if it is working properly?

### Measurements:

1.	Can you operate the setup with the provided instructions?
We answered this question in the previous part.


2.	How close were the results you obtain to the previously reported results?
We do not know precisely since we do not know the exact results the project group obtained. We did find however that the arduino's and sensors were communicating with the master arduino.

3.	Can you understand and explain the analysis procedure to a third person?
Not really since there is no analysis procedure. I think I have a general sense of how the code works but I could not explain it in detail.

4.	Is the setup robust and safe to operate? 
Yes it was safe

5.	Did you encounter any issues? Could you troubleshoot those without contacting the owners?
Yes, we did not know how the sensor looks like. We were able to troubleshoot this by googling for the name of the part we did not recognize.
We also had problems with how to connect the sensor to the arduino, but that was solved by trying a couple of variations.

6.	What part of the measurement procedure did you appreciate most?
It is nice that the Arduinos can communicate.


### Interactions:

1.	Could you relate to the stated goal of the project?
Yes, we also want to be able to control the different elements in the box from one central place.


2.	Which instructions did you need from the owners on top of the written files?
We could had asked them the results they had in order to know if ours were correct.

3.	Does the experiment accomplish its stated purpose?
It is not accomplished because the data from the sensor could not reach the second arduino. However, the owners of the project are already aware of this.

4.	What do you recommend to the project owners to improve their complete package?  
It seems that the problem in the Hybrid codes comes from the fact that a float-type has to be cast to a byte-type and this is not done explicitly.
It might be that [this](https://forum.arduino.cc/index.php?topic=577373.0) web-page can help with this.
The master arduino does send output when wiring incorrectly (SCL-A4 slave-A4 master, SDA-A5 slave-A5 master), maybe this helps in solving the problem, it did not send output when wiring correctly, as indicated by one of the owners of the project.
It would be nice to create a wiring diagram/pictures of the final setup.
It would be nice to include some documentation for people who did not yet work with an Arduino yet.

## Respone from project group: 
Thank you for the documentation.
It was indeed a bit vague how to connect the wires based purely on text. Wiring diagrams for the different set-ups are now included, as an overview diagram of an Arduino UNO board and the sensor. 
Hopefully this also solves probles regarding the recognision of the sensor component.
 
In our experience, the desired output was somewhat clear from the description of the set-up itself. 
However, since your experiences were different, a have added this more explicitly to the reproduction guide.
In addition, a mre detailed description on what the COM port output should read if the set-up is repeated.