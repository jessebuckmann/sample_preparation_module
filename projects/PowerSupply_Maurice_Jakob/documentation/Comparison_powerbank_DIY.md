# Comparison of a system based around power bank or fully DIY solar panel power station

## Power bank

### Advantages

+ Simple system, with internal charge controller
+ more [advanced powerbanks](https://www.coolblue.nl/product/834838/goal-zero-sherpa-100-ac-powerbank-met-power-delivery-25-600-mah.html#product-specifications) even have option for 220V AC output
+ 5V USB output used for the common Arduino

### disavantage

+ less control over output voltages. (Unless load has [USB-C commmunication option](https://www.allaboutcircuits.com/technical-articles/introduction-to-usb-type-c-which-pins-power-delivery-data-transfer/#:~:text=The%20default%20VBUS%20voltage%20is,maximum%20power%20of%20100%20W) to increase voltage up to 20V)
+ Not able to use solar panel as power source directly for the load, which results in low overal power consumtion ceiling
+ Can be slow to charge, due to power input limit

## [Full DIY solar panel power station](https://microcontrolere.wordpress.com/2016/12/16/mppt-solar-charger/)

### Advantages
+ Extremely versatile
+ Has option to use 12V battery, which usually have higher power output ceiling
+ Use solar cell and battery as power source in parallel

### disavantage
+ Requires 50+ parts 
+ Requires a lot of testing
+ Very fragile without expert knowledge on electronics

## Semi DIY
For example a [solar charge controller](https://www.conrad.nl/p/kemo-charging-controller-m149n-solar-laadregelaar-serie-12-v-10-a-110527) for a [large 12V battery](https://www.conrad.nl/p/conrad-energy-12-v-9-ah-loodaccu-12-v-9-ah-loodvlies-agm-b-x-h-x-d-151-x-94-x-65-mm-kabelschoen-635-mm-onderhoudsvr-250915).
Using a [dc/dc converter](https://www.conrad.nl/p/victron-energy-orion-tr-2412-5-dcdc-converter-60-w-1666864) to down convert to 12V from the solar panel.
For the ouput, voltage can be split using either a voltage divider or another down converter.
Conrad list for 12V and 5V DC converters is [here](https://www.conrad.nl/o/spanningsomvormers-dcdc-2110160?ATT_OUTPUT_VOLTAGES_any=12%20V,5%20V%2FDC&price_max=335&price_min=5.73).

### Advantages
+ We can create it how we like
+ High power output ceiling, with parallel solar panel and battery supply
+ 

### disavantage
+ [charge controllers](https://www.sparkfun.com/categories/421) seem to be only available for very low power solutions for 5V batteries
+ requires medium amount of testing
+ more complicated to set up output connections compared to powerbank
+ may be difficult to get 220V AC output

