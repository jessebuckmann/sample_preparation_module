# Power

| | |
| ------ | ------ |
| Operating Voltage | 230 V |
| Power Usage | We have to check (probably fairly low; small laser (1mW output) and a light sensor) |
| input type | AC |

The input voltage goes into a modulator to make the setup filter outside light. It directly controls the LASER and sensor. These use a much lower voltage. As such the modulator includes a transformer to transform back down to ±5V and ±8V. We feel it should be possible to cut out this transformer and directly feed the modulator, but the lab technician says otherwise for now.

# Size
| direction | size (cm) |
| ------ | ------ |
| width | 30 |
| depth | 50 |
| heigth | 35 |

# Vibration control
The experiment is vulnerable to low frequency vibrations. The natural frequency of the balance is 1 Hz. Therefore a low pass frequency dampening system with a thershold of 0.1 Hz would be desirable. 0.1-10 Hz couples strongly to our pendulum.

