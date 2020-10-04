# Report

### Goal of the project

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
In our case, both the Charge Controller and the powerbank have internal load-switches that take care of this already.
However, additional protection and control can be obtained by adding these.

Below, A schemetic can be found of the setup.



![Circuit of project](./images/circuit.png)


### Important considerations

The lead battery has to be charged with a voltage close to its nominal voltage of 12V. 
Also it is sensitive to overcharging or deep discharge. 
This is taken care of by the charge controller, which also internally downconverts the input voltage from the solar panel.

As the charge controller will shut everything down in case of too high or low battery voltage and that can be troubling for some components there is a need for additional voltage monitoring.
This enables the user to disconnect the loads in time.

As described above, the lead battery is the most sensitive component of the setup.
It is needed because of AC loads in the science station.
The current from the solar pannel is DC and most loads use 5V DC which can be supplied via USB, which makes a power bank the convenient option.
However, an inverter that makes AC current out of DC input cannot connect to a power bank so the 12V lead battery is needed.

### Possible sources of noise

Not a source of noise but a nuisance is the weather dependent power supply of the solar panel
Other things: inverter uses standby power, the voltage measurement for the load switch is kind of inaccurate because of use of voltage divider.
Each of the DC sources will have a few percent variance. However, this is not an issue, since the tolerance of the devices used is fairly large.