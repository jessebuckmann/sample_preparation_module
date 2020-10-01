# Report

### Goal of the project

*what we try to accomplish, this leads to the chosen project outline*

The goal of the power supply project is to construct a circuit that supplies stable power to all electronic devices (loads) of the science station in an off-grid fashion.
For that we chose power generation by solar panels, which makes us independet of wall outlets.
As the power coming from the panels is dependent on lighting, we need to interconnect a power storage that can supply stable power when charged up.
The loads of the science station can in principle run on DC or AC current and at different voltages. This affects the choice of batteries and additional components we need as described below.


### Project outline

The central unit of this setup will be the batteries that store and supply the science station.
In order to supply voltages that are widely used, a 12V lead-acid battery and a 5V litium-ion USB-powerbank are combined.
The 5V USB connection are the most convenient and widely used for small electronics like arduinos, which are the main controllers for the science stations.
Some other devices might need a higher voltage or even an alternating current.
This is easier to achieve with a 12V lead-acid battery, as it can suffice a higher output power.

The next step is a way to charge both the batteries independantly of the grid.
A solar panel can supply power anywhere it is, even some at cloudy days.
Each battery has its own pattern of charging.
Luckily, 12V lead-acid batteries are commonly combined with solar panels as off-grid or self-sustaining setups.
Therefore a solar charge controller is an easy tool to convert the variable output voltage of the solar panel into a useful one for the battery.
It also has deep-discharge and overcharging protection features, which come in handy. 
This charge controller provides a connection for the loads as well, as a 12V DC output.

With a DC/DC converter, this is converted into a 5V supply, that can charge the Lithium-ion battery as well.
A lead-acid battery is also used in cars and we used a tool for cars that can convert it to 230V AC power as additional power supply for devices that need regular wall-socket power.

To communicate with the rest of the science station, a connection with an arduino can be made.
This monitors the capacitance of the batteries and can shut down the experiment when the batteries are running out of power.
A load switch can disconnect the load, to avoid deep-discharging the batteries.

Below, A schemetic can be found of the setup.



![Circuit of project](./images/circuit.png)


### Important considerations

*all the stuff about conversion and all the connections*

- charge controller for battery
- voltage monitoring
- inverter

### Possible sources of noise

*which parts are sensitive to noise, which parts produce noise (noise = e.g. voltage fluctuations)*