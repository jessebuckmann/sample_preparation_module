This document assumes the reader has read the [context and theory](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/master/projects/CavendishTorsionBalance_by_Geert_and_Jillis/ContextAndTheory.md) file, and thus knows roughly the aim of the experiment and has some idea of the setup.

# Setup
The setup consists of 3 main parts; the torsion balance, the control mechanism and the detection suite.

## Torsion balance
The torsion balance consists of a round baseplate, a turningtable with holders for large balls, an insulated and grounded holder for the torsion balance and the torsion balance itself. The holder can be rotated at the base for finetuning. In the holder a Halter(or barbell) is suspended by a thin rectangular wire. This can be adjusted in height and angle at the top. **If it is necessary to adjust with this part of the setup, please be extremely careful.** It is a quite delicate piece of equipment, the wire is valuable and easily broken. During the measurement it should not be necessary to interface directly with any of these components torsion balance. 

## Control mechanism
The setup is controlled by a continuous servo attached to an Arduino Due.
The Arduino needs an external power source, as the servo needs a higher voltage than USB can provide. It is necessary to first connect the power source and **then** connect the USB to the Arduino. Otherwise the wrong power supply is used. On the Arduino a program can be run to control the position of the turningtable with the big masses. ADD LINK TO PROGRAM

<img src="./Images/schematicController.png"  width="750"> 

## Detection suite
The detection suite comprises a laser, a lightposition detector, a modulator and amplifier and the Digilent Analog Discovery 2. 
The laser and detector are connected to the modulator to isolate the signal from other light effects which might be picked up by the detector. 
The outputs of the modulator are connected to the oscilloscope channels on the Digilent Analog Discovery 2.
To read out the signal of the oscilloscope it is necessary to download either the [Waveforms package from Digilent](https://store.digilentinc.com/waveforms-download-only/) or the package that is being written by the [Software group](https://git.science.uu.nl/ued2020/experiment-design-2020/-/tree/master/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno).

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

<img src="./Images/schematicMeasurer.png"  width="750"> 


# Method
To find a value for G it is needed to measure 2 values of the rest angle $`\phi_0`$,
 one where the balls are both clockwise close to the balance and one where the balls are counterclockwise close to the balance.
From the difference in these equilibrium positions the torque of the gravitational force can be inferred. The torsion constant is determined by measuring the oscillation frequency of the halter.

