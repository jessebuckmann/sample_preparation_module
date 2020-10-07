This document assumes the reader has read the [context and theory](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/CavendishTorsionBalance_by_Geert_and_Jillis/ContextAndTheory.md) file, and thus knows roughly the aim of the experiment and has some idea of the setup.

# Setup
The setup consists of 3 main parts; the torsion balance, the control mechanism and the detection suite.

## Torsion balance
***If it is necessary to interface with this part of the setup, please be careful.***  
During the measurement it should not be necessary to interface directly with the torsion balance. 
It is a quite delicate piece of equipment, mainly due to the wire on which the barbell is suspended.
This wire is necessarily thin and thus fragile, as a thick wire would have a too high torsion constant and thus move too little to measure effectively.   
The torsion balance consists of a baseplate, a turningtable with holders for the big balls, and the torsion balance-barbell setup.

### measurements
| part | measure |
| ------ | ------ |
| small balls | 6.33 g and 6.29 g |
| big balls | 1214.0 g and 1214.8 g |
| full barbell (including mirror, balls, rod, connector to wire, ...) | 31.7 g |
| barbell length | 12 cm? |
| diameter big balls | 5.09 cm |
| Thickness box | 3.75 cm |
| distance box - dectector | 17.2 cm |

## Control mechanism
The setup is controlled by a continuous servo attached to an Arduino Due.
The Arduino needs an external power source, as the servo needs a higher voltage than the USB can provide.
It is necessary to first connect the power source and only then connect the USB for the Arduino to use the correct power supply.
On the Arduino a program can be run to control the position of the turningtable with the big masses. 

<img src="./Images/schematicController.png"  width="750"> 

## Detection suite
The detection suite comprises a laser, a lightposition detector, a modulator and amplifier and the Digilent Analog Discovery 2. 
The laser and detector are connected to the modulator to isolate the signal from other light effects which might be picked up by the detector. 
The outputs of the modulator are connected to the oscilloscope channels on the Digilent Analog Discovery 2.
To read out the signal of the oscilloscope it is necessary to download either the [Waveforms package from Digilent](https://store.digilentinc.com/waveforms-download-only/) or the package that is being written by the [Software group](https://git.science.uu.nl/ued2020/experiment-design-2020/-/tree/master/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno).



<img src="./Images/schematicMeasurer.png"  width="750"> 


# Method
To find a value for G it is needed to measure 2 values of $`\phi_0`$,
 one where the balls are both clockwise close to the balance and one where the balls are counterclockwise close to the balance.
From the difference in these equilibrium positions the torque of the gravitational force can be inferred.

