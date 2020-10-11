# Temperature measurement

In this section we discuss a small, quantitative experiment concerning the temperature inside the box we have performed. This test was performed to see whether our design ideas for The Box will lead to properly functioning box. Below we will give the intstructions for this temperature measurement if one would want to repeat this it. 

## Aim of the experiment

The experiment we chose to carry out is one that will test whether The Box needs additional (active) ventilation. We expect that especially the modules and power supply components will generate quite some heat, and we are worried that the heat cannot escape The Box, since it has to be sealed of properly to withstand rainy conditions. By carrying out two measurement-sets (one with The Box completely closed and taped off with dukttape to make it waterproof, and one with two panels opposite to each other slightly shifted down, so that airflow is possible (passive ventilation)). In both measurement-sets, the temperature will be monitored and plotted afterwards. Another important part of the project were the discussions with all other groups to see what their requirements for the box were and to meet all of their wishes. You will also see if the current design of the box meets all of their requirements.

## Safety Measurements and preperations

**Read this section carefully before starting on the experiment!**

During this experiment and in working with the box there are a couple of things you need to pay attention to:

- The edges of the panels of The Box are sharp, do not cut yourself when adding or removing these;
- Some of the panels of the box are attached to it using strong magnets. Be careful with your fingers when working with these plates and magnets.
- The Box is quite heavy. Do not let it run over your feet, for example;
- You will be working with boiling water. Do not burn yourself.
- During the experiment the box will contain boiling water and your laptop. Therefor make sure you do not move the box during the measurements!

Before you start with the experiment it is important that you learn how to assemble and disassemble the panels of the box, and that you understand how you can shift the panels. The panels of the box are attached to the sides and the top using either bolts or strong magnets. To give you a sense of direction: when standing **in front** of the box, the **back panel** and the **right-hand side** are attached using bolts. All other panels are attached using magnets (The top, the front and the left side panel). 

The magnetic side panels (left and front) are held in place by magnets and by in hight adjustable bolts in the beams. These bolts are placed below the panels to make sure the panels are placed at the correct hight. Take some time to try to remove these panels, reattach them and adjust the height of the panels.

The back and the right-hand side panel are attached using bolts. The back panel should be left as is, since its place during the experiment will not change. The height of the right hand side panel will be adjusted during the experiment. This will be done by removing the bolts at the top of the panel and loosening the bolt on the side of the panel. If all bolts are loosend you can shift the panel up and down (during the experiment with passive ventilation the panel will be shifted maximally upwards). Feel free to practice this in advance as well.

## Experimental setup

The experimental setup consists of the following equipment:

- The Box;
- Two glass beakers;
- A water cooker;
- Tools to unscrew the bolts;
- Dukttape;
- The Arduino-temperature setup from the Temperature Controle Group with a laptop supporting the Arduino software (The arduino software can be downloaded from the internet and the [code for the arduino](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/PrepTheBox_Olaf_and_Noor/Instructions/code.txt) is posted in this folder);
- Any other temperature measuring device that can save the data in 10 second intervals will do;

First make sure you have a working temperature measuremening device and that you have a way of plotting your data (e.g. Excel, python or mathematica).
If you feel comfortable working with the panels of the box, have a working temperature measurement device and all the equipment you can start the experiment following the instruction below. **First read through them beforme starting.**

## Step by step instructions for the experiment

The first thing you need to do is get an idea for the general design of the box. This can be done by reading [this document](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/PrepTheBox_Olaf_and_Noor/Roadmap-map/Context_and_Theory/BoxReport.docx) and by looking at the sketches provided in [this document](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/PrepTheBox_Olaf_and_Noor/Roadmap-map/Context_and_Theory/BoxSketch.pdf).

**No ventilation**

During the first measurement the box will be completely sealed off. First, all sides but one are taped off and thus made waterproof. Water is cooked, and put in the two beakers. The beakers are then placed in the box, in the lower compartment (because this one has the steadiest flooring, and we don't want water pouring over the laptop and/or Arduino). Once the initial steam cloud is gone, the laptop and the temperature sensor are placed inside, and the last panel is sealed off. The sensor writes to the Arduino IDE every ten seconds. After 25 minutes of measurement, the box is opened again, data is retrieved and put in Excel.

1. Make sure that all panels are placed at the correct height, sealing the box completely.
2. Remove the front panel.
3. Seal of the edges of the panels with dukttape, except for the bottom edges.
4. Start boiling 1.5 liters of water in the watercooker. While this is warming up start do step 5.
5. Place the two beakers on the bottom plate of the box and place the laptop and the temperature measurement device on the middle plate of the box. Make sure everything is stable since the middle plate has holes in it.
6. Once the water has cooked pour 750 mL of water in each beaker and start the temperature measurment.
7. After 30 seconds or so (to let most of the initial steam escape the box) put the front panel in place and seal its edges using the tape.
8. Let the setup stand for **25 minutes**. Do **NOT** move the box during the experiment.
9. While waiting go and talk to other project groups and ask what their requirements are in the functional off-grid measurement station. Consider if the current design of the box meets their requirements or if changes are necesarry. 
10. After the 25 minutes remove the tape from the front panel and remove the front panel itself. Take the laptop and the temperature measurement setup out of the box, stop the measurement and process the data.
11. Take out the beakers with water (**Caution, the beakers with water can still be very warm**)

**Passive Ventilation**

The second measurement has two opposite panels of The Box slightly ajar (The left and the right panel), and thus has a passive ventilation channel.

12. Remove the tape from the left and right hand side panels
13. Lower the **left** panel untill there is a gap of around 20 centimeters at the top of the panel.
14. Raise the right panel maximally. There will be a gap of around 15 centimeters at the bottom.
15. Seal the edges of the side panels.
16. Repeat step **4** up untill step **11**

Below, a few images can be seen. The first one shows the completely sealed off Box, the second one shows the passive ventilation setup, and the third one shows the insides of The Box. These can give some indication of what the set-up looks like

![The sealed off Box](./images/BoxSeal.jpeg)

![The passive ventilation setup](./images/PassiveVentilation.jpeg)

![The insides of the Box™](./images/BoxInsides.jpeg)


## Results

Create a plot of the results. Below the results of our experiment can be seen. What can you conclude based on your measurement? Also, does the design of the box meet the requirements of the other sub-project groups? What would you have done differently?

![tempplot](./images/tempplot.jpeg)

## Feedback form

Please provide feedback on our project. You can use [this template](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/Coordination/_Templates/peer_evaluation.md) to provide feedback and post it into the [feedback folder](https://git.science.uu.nl/ued2020/experiment-design-2020/-/tree/master/projects/PrepTheBox_Olaf_and_Noor/feedback). 

The best of luck with reproducing our experiment!

Cheers,

Noor and Olaf